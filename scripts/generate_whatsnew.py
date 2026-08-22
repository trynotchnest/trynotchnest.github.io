#!/usr/bin/env python3
"""Regenerate the static, crawlable changelog in whats-new.html from appcast.xml.

The release cards live between the <!-- RELEASES:START --> and
<!-- RELEASES:END --> markers so this can run unattended in CI (see
.github/workflows/generate-appcast.yml). appcast.xml is the source of truth and
is itself auto-refreshed from App Store data, so rendering from it keeps the
changelog fresh without a client-side fetch.
"""
import html
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPCAST = ROOT / "appcast.xml"
PAGE = ROOT / "whats-new.html"

START = "<!-- RELEASES:START -->"
END = "<!-- RELEASES:END -->"


def parse_items(xml: str):
    items = re.findall(r"<item>(.*?)</item>", xml, re.S)
    out = []
    for it in items:
        title = re.search(r"<title>(.*?)</title>", it, re.S)
        pub = re.search(r"<pubDate>(.*?)</pubDate>", it)
        desc = re.search(r"<description>(.*?)</description>", it, re.S)
        title_txt = html.unescape(title.group(1)).strip() if title else ""
        ver_m = re.search(r"Version\s+([0-9][0-9.]*)", title_txt)
        version = ver_m.group(1) if ver_m else (title_txt or "Latest")
        # description is CDATA-wrapped, entity-escaped HTML
        body = ""
        if desc:
            # description is entity-escaped HTML that itself wraps an (also
            # escaped) CDATA section, so unescape first, then strip the markers.
            body = html.unescape(desc.group(1)).strip()
            body = re.sub(r"<!\[CDATA\[|\]\]>", "", body).strip()
        out.append({"version": version, "pub": pub.group(1).strip() if pub else "", "body": body})
    return out


def fmt_date(rfc822: str) -> str:
    for f in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
        try:
            return datetime.strptime(rfc822, f).strftime("%B %-d, %Y")
        except ValueError:
            continue
    return rfc822


def body_to_html(body: str) -> str:
    """appcast notes are loose <h3>/<li>/<p> without a wrapping <ul>. Group the
    <li> runs into proper lists so the markup is valid and readable."""
    if not body:
        return "<p>No release notes available.</p>"
    parts = re.split(r"(?i)(<h3>.*?</h3>|<li>.*?</li>|<p>.*?</p>)", body, flags=re.S)
    tokens = [p.strip() for p in parts if p and p.strip()]
    out, buf = [], []
    for t in tokens:
        if re.match(r"(?i)^<li>", t):
            buf.append(t)
            continue
        if buf:
            out.append("<ul>" + "".join(buf) + "</ul>")
            buf = []
        if re.match(r"(?i)^<h3>", t):
            out.append("<strong>" + re.sub(r"(?is)</?h3>", "", t).strip() + "</strong>")
        elif re.match(r"(?i)^<p>", t):
            out.append(t)
        else:
            out.append("<p>" + t + "</p>")
    if buf:
        out.append("<ul>" + "".join(buf) + "</ul>")
    return "\n                        ".join(out)


def card(item) -> str:
    return f"""                <article class="release-card">
                    <div class="release-header">
                        <div>
                            <h2 class="release-version">Version {html.escape(item['version'])}</h2>
                            <p class="release-date">{html.escape(fmt_date(item['pub']))}</p>
                        </div>
                    </div>
                    <div class="release-content">
                        {body_to_html(item['body'])}
                    </div>
                </article>"""


def main():
    items = parse_items(APPCAST.read_text())
    if not items:
        raise SystemExit("no <item> entries found in appcast.xml")
    cards = "\n".join(card(i) for i in items)
    block = f"{START}\n{cards}\n                {END}"

    page = PAGE.read_text()
    if START in page and END in page:
        page = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, page, flags=re.S)
    else:
        raise SystemExit("markers not found in whats-new.html")

    # keep SoftwareApplication softwareVersion in sync with newest release
    page = re.sub(r'("softwareVersion":\s*")[^"]*(")', rf'\g<1>{items[0]["version"]}\g<2>', page)

    PAGE.write_text(page)
    print(f"whats-new.html: wrote {len(items)} releases (latest {items[0]['version']})")


if __name__ == "__main__":
    main()
