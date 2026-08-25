#!/usr/bin/env python3
"""Generate localized NotchNest pages (landing + learn hub + articles) and keep
hreflang consistent across the whole site.

Locales: en (root, hand-authored), de, zh (hand-authored), and the generated set
ar, fr, pt-br, pt-pt, es-mx. English/German/Chinese pages are only *patched*
here (unified hreflang cluster + language switcher + correct rating); the five
generated locales are written in full from the templates + translation tables
below.

Run:  python3 scripts/build_i18n.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://notchnest.app/"

# ── locale registry ────────────────────────────────────────────────────────
# order matters: drives hreflang + footer language list
ORDER = ["en", "de", "zh", "ar", "fr", "pt-BR", "pt-PT", "es-MX"]
DIRS = {"en": "", "de": "de/", "zh": "zh/", "ar": "ar/", "fr": "fr/",
        "pt-BR": "pt-br/", "pt-PT": "pt-pt/", "es-MX": "es-mx/"}
EXTRA = {"en": ["en-us", "en-gb", "en-in"], "zh": ["zh-cn"], "es-MX": ["es-419"]}
SWITCH = {"en": "English", "de": "Deutsch", "zh": "中文", "ar": "العربية",
          "fr": "Français", "pt-BR": "Português (BR)", "pt-PT": "Português (PT)",
          "es-MX": "Español (MX)"}
# locales generated from scratch (landing/learn); de+zh are hand-authored but
# their for/ + compare/ + remaining articles are generated here too (backfill)
GEN = ["ar", "fr", "pt-BR", "pt-PT", "es-MX"]
FULL = ["de", "zh", "ar", "fr", "pt-BR", "pt-PT", "es-MX"]  # every non-English locale
LANG_ATTR = {"de": "de", "zh": "zh-Hans", "ar": "ar", "fr": "fr",
             "pt-BR": "pt-BR", "pt-PT": "pt-PT", "es-MX": "es-MX"}
HTML_DIR = {"ar": "rtl"}  # else ltr
OG_LOCALE = {"de": "de_DE", "zh": "zh_CN", "ar": "ar_SA", "fr": "fr_FR",
             "pt-BR": "pt_BR", "pt-PT": "pt_PT", "es-MX": "es_MX"}
STORE_CC = {"de": "de", "zh": "cn", "ar": "sa", "fr": "fr",
            "pt-BR": "br", "pt-PT": "pt", "es-MX": "mx"}
CURRENCY = {"de": "EUR", "zh": "CNY", "ar": "SAR", "fr": "EUR",
            "pt-BR": "BRL", "pt-PT": "EUR", "es-MX": "MXN"}
RATING = {"de": "4,0", "zh": "4.0", "ar": "4.0", "fr": "4,0",
          "pt-BR": "4,0", "pt-PT": "4,0", "es-MX": "4.0"}


def store_url(loc):
    return f"https://apps.apple.com/{STORE_CC[loc]}/app/notchnest-power-your-notch/id6747612321"


def hreflang(suffix, indent=""):
    """Unified alternate cluster for a page that exists in every locale."""
    lines = []
    for code in ORDER:
        url = BASE + DIRS[code] + suffix
        lines.append(f'<link rel="alternate" hreflang="{code}" href="{url}" />')
        for e in EXTRA.get(code, []):
            lines.append(f'<link rel="alternate" hreflang="{e}" href="{url}" />')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE + suffix}" />')
    return "\n".join(indent + l for l in lines)


HREFLANG_RE = re.compile(
    r'(?:[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/>\s*\n)+')


def patch_hreflang(html, suffix, indent="    "):
    """Replace the first contiguous run of alternate links with the unified block;
    if the page has none, insert the block right after the canonical link."""
    block = hreflang(suffix, indent) + "\n"
    if HREFLANG_RE.search(html):
        return HREFLANG_RE.sub(lambda _: block, html, count=1)
    m = re.search(r'([ \t]*<link rel="canonical"[^>]*>\s*\n)', html)
    if m:
        return html[:m.end()] + block + html[m.end():]
    return html


# ── footer language column (all 8 locales) ─────────────────────────────────
def footer_lang_inline(current, suffix=""):
    """Compact one-line language switcher for learn hub + article footers."""
    out = []
    for code in ORDER:
        href = "/" + DIRS[code] + suffix
        cur = ' aria-current="page"' if code == current else ""
        out.append(f'<a href="{href}" hreflang="{code}"{cur}>{SWITCH[code]}</a>')
    return '<div class="footer-lang">' + "".join(out) + "</div>"


def footer_lang_links(current, suffix=""):
    out = []
    for code in ORDER:
        href = "/" + DIRS[code] + suffix
        label = SWITCH[code]
        if code == current:
            out.append(f'<li><a href="{href}" aria-current="page">{label}</a></li>')
        else:
            out.append(f'<li><a href="{href}">{label}</a></li>')
    return "\n      ".join(out)


# translation tables live in build_i18n_data.py to keep this file readable
from build_i18n_data import LANDING, LEARN_INDEX, ARTICLES, UI  # noqa: E402


def rtl_attrs(loc):
    d = HTML_DIR.get(loc)
    return f' dir="{d}"' if d else ""


def rtl_style(loc):
    if loc != "ar":
        return ""
    return ("\n<style>body{direction:rtl}.hero-grid,.cases-grid,.faq-grid,"
            ".footer-grid,.hero-meta,.stats{direction:rtl}.crumbs,.article-meta"
            "{direction:rtl}</style>")


# ── landing page ───────────────────────────────────────────────────────────
def build_landing(loc):
    t = LANDING[loc]
    d = DIRS[loc]
    su = store_url(loc)
    faq = t["faq"]
    faq_json = ",\n      ".join(
        '{ "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
        % (jstr(q), jstr(a)) for q, a in faq)
    cards = "\n    ".join(
        f'<div class="case"><span class="case-tag">{tag}</span><h3>{h}</h3><p>{p}</p></div>'
        for tag, h, p in t["cards"])
    faq_cards = "\n    ".join(
        f'<details class="faq-card"><summary class="faq-question">{q}<span class="faq-toggle"></span></summary>\n      <div class="faq-answer">{a}</div>\n    </details>'
        for q, a in faq)
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<meta name="keywords" content="{t['keywords']}" />
<link rel="canonical" href="{BASE}{d}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang('')}
<meta property="og:title" content="{t['title']}" />
<meta property="og:description" content="{t['og_desc']}" />
<meta property="og:url" content="{BASE}{d}" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="{BASE}1200x630-banner.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="manifest" href="/site.webmanifest" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": {jstr(t['title'])},
    "url": "{BASE}{d}",
    "inLanguage": "{LANG_ATTR[loc]}",
    "description": {jstr(t['wp_desc'])},
    "isPartOf": {{ "@type": "WebSite", "name": "NotchNest", "url": "{BASE}" }}
  }},
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "NotchNest",
    "operatingSystem": "macOS 14.0+",
    "applicationCategory": "ProductivityApplication",
    "inLanguage": "{LANG_ATTR[loc]}",
    "description": {jstr(t['sa_desc'])},
    "url": "{BASE}{d}",
    "downloadUrl": "{su}",
    "image": "{BASE}assets/notchnest-icon.png",
    "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.0", "ratingCount": "15", "bestRating": "5", "worstRating": "1" }},
    "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "{CURRENCY[loc]}", "availability": "https://schema.org/InStock", "url": "{su}" }}
  }},
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "inLanguage": "{LANG_ATTR[loc]}",
    "mainEntity": [
      {faq_json}
    ]
  }}
]
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav" aria-label="{t['nav_aria']}"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="NotchNest" width="28" height="28" /><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/">EN</a>
    <a href="/{d}learn/" class="nn-nav-keep">{t['nav_learn']}</a>
  </div>
</div></nav>

<main class="main-container">
<div class="content-wrapper">

<section class="hero" aria-label="NotchNest">
  <div class="hero-grid">
    <div class="hero-copy">
      <span class="eyebrow"><span class="eyebrow-dot" aria-hidden="true"></span>{t['eyebrow']}</span>
      <h1 class="hero-h1">{t['h1']}</h1>
      <p class="hero-lede">{t['lede']}</p>
      <div class="hero-ctas">
        <a class="mas-badge" href="{su}" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="{t['badge_alt']}" /></a>
        <a class="btn-ghost" href="/{d}learn/">{t['ghost']}</a>
      </div>
      <div class="hero-meta">
        <span><strong>★ {RATING[loc]}</strong> · {t['meta_ratings']}</span>
        <span class="dot" aria-hidden="true"></span>
        <span><strong>{t['free']}</strong> {t['meta_store']}</span>
        <span class="dot" aria-hidden="true"></span>
        <span><strong>macOS 14+</strong> · Apple Silicon</span>
      </div>
    </div>
    <div class="hero-stage">
      <video class="hero-video" width="1920" height="1200" autoplay muted loop playsinline preload="metadata" poster="/assets/notchnest-poster.webp" aria-label="NotchNest demo">
        <source src="/assets/notchnest-demo.webm" type="video/webm" />
        <source src="/assets/notchnest-demo.mp4" type="video/mp4" />
      </video>
    </div>
  </div>
  <div class="stats">
    <div><div class="stat-num">★ {RATING[loc]}</div><div class="stat-label">{t['stat_rating']}</div></div>
    <div><div class="stat-num">15</div><div class="stat-label">{t['stat_reviews']}</div></div>
    <div><div class="stat-num">macOS 14+</div><div class="stat-label">{t['stat_os']}</div></div>
    <div><div class="stat-num">{t['free']}</div><div class="stat-label">{t['stat_store']}</div></div>
  </div>
</section>

<section class="cases-section" aria-label="{t['feat_kicker']}">
  <header class="section-head">
    <span class="section-kicker">{t['feat_kicker']}</span>
    <h2 class="section-title">{t['feat_title']}</h2>
    <p class="section-lede">{t['feat_lede']}</p>
  </header>
  <div class="cases-grid">
    {cards}
  </div>
</section>

<section class="faq-section">
  <header class="section-head"><span class="section-kicker">FAQ</span><h2 class="section-title">{t['faq_title']}</h2></header>
  <div class="faq-grid">
    {faq_cards}
  </div>
</section>

<section class="cta-band">
  <div class="cta-inner">
    <h2 class="cta-title">{t['cta_title']}</h2>
    <p class="cta-lede">{t['cta_lede']}</p>
    <a class="mas-badge mas-badge-on-dark" href="{su}" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="{t['badge_alt']}" /></a>
  </div>
</section>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand"><a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="NotchNest" width="28" height="28" /><span>NotchNest</span></a><p class="footer-tag">{t['footer_tag']}</p></div>
    <div class="footer-col"><h4>{t['col_app']}</h4><ul>
      <li><a href="{su}" target="_blank" rel="noopener">Mac App Store</a></li>
      <li><a href="/whats-new.html">{t['whats_new']}</a></li>
    </ul></div>
    <div class="footer-col"><h4>{t['col_lang']}</h4><ul>
      {footer_lang_links(loc)}
    </ul></div>
    <div class="footer-col"><h4>{t['col_legal']}</h4><ul>
      <li><a href="/privacy-policy.html">{t['privacy']}</a></li>
      <li><a href="mailto:29satnam@gmail.com">{t['support']}</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom"><span>© <span id="yr"></span> {t['copyright']}</span></div>
</footer>

</div>
</main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body>
</html>
"""


ARTICLE_SLUGS = ["how-to-use-the-macbook-notch", "best-macos-notch-apps"]
FOR_SLUGS = ["developers", "designers", "students"]


def build_for(loc, slug):
    from build_i18n_for import FOR, FOR_UI
    t = FOR[slug][loc]
    u = FOR_UI[loc]
    d = DIRS[loc]
    su = store_url(loc)
    url = f"{BASE}{d}for/{slug}/"
    cases = "\n      ".join(
        f'<div class="case"><span class="case-tag">{e}</span><h3>{h}</h3><p>{p}</p></div>'
        for e, h, p in t["cases"])
    faq_cards = "\n      ".join(
        f'<details class="faq-card"><summary class="faq-question">{q}<span class="faq-toggle"></span></summary><div class="faq-answer">{a}</div></details>'
        for q, a in t["faq"])
    faq_json = ",\n      ".join(
        '{ "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
        % (jstr(q), jstr(a)) for q, a in t["faq"])
    role_links = " &middot; ".join(
        f'<a href="/{d}for/{s}/" style="color:var(--muted)">{u["roles"][s]}</a>' for s in FOR_SLUGS)
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang(f'for/{slug}/')}
<meta property="og:title" content="{t['title']}" />
<meta property="og:description" content="{t['description']}" />
<meta property="og:url" content="{url}" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="{BASE}1200x630-banner.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@codetard" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org", "@type": "WebPage",
    "name": {jstr(t['title'])}, "url": "{url}", "inLanguage": "{LANG_ATTR[loc]}",
    "description": {jstr(t['description'])},
    "isPartOf": {{ "@type": "WebSite", "name": "NotchNest", "url": "{BASE}" }},
    "primaryImageOfPage": {{ "@type": "ImageObject", "url": "{BASE}1200x630-banner.jpg" }}
  }},
  {{
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": {jstr(u['home'])}, "item": "{BASE}{d}" }},
      {{ "@type": "ListItem", "position": 2, "name": {jstr(t['crumb'])}, "item": "{url}" }}
    ]
  }},
  {{
    "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "{LANG_ATTR[loc]}",
    "mainEntity": [
      {faq_json}
    ]
  }}
]
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav" aria-label="{u['nav_aria']}"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="NotchNest" width="28" height="28" /><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/{d}#features">{u['features']}</a><a href="/{d}compare/">{u['compare']}</a><a href="/{d}learn/" class="nn-nav-keep">{u['learn']}</a>
  </div>
</div></nav>
<main class="main-container"><div class="content-wrapper">
  <div class="crumbs"><a href="/{d}">{u['home']}</a><span class="sep">/</span><span>{t['crumb']}</span></div>
  <section class="hero" aria-label="{t['crumb']}">
    <div class="hero-grid">
      <div class="hero-copy">
        <span class="eyebrow"><span class="eyebrow-dot"></span> {u['eyebrow']}</span>
        <h1 class="hero-h1">{t['h1']}</h1>
        <p class="hero-lede">{t['lede']}</p>
        <div class="hero-ctas">
          <a class="mas-badge" href="{su}" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="{u['badge_alt']}" /></a>
          <a class="btn-ghost" href="/{d}#features">{u['playground']}</a>
        </div>
      </div>
      <div class="hero-stage">
        <video class="hero-video" width="1920" height="1200" autoplay muted loop playsinline preload="metadata" poster="/assets/notchnest-poster.webp" aria-label="NotchNest demo">
          <source src="/assets/notchnest-demo.webm" type="video/webm" />
          <source src="/assets/notchnest-demo.mp4" type="video/mp4" />
        </video>
      </div>
    </div>
  </section>
  <section class="cases-section" aria-label="{t['crumb']}">
    <header class="section-head"><span class="section-kicker">{t['crumb']}</span><h2 class="section-title">{u['section_title']}</h2></header>
    <div class="cases-grid">
      {cases}
    </div>
  </section>
  <section class="faq-section">
    <header class="section-head"><span class="section-kicker">FAQ</span><h2 class="section-title">{u['faq_title']}</h2></header>
    <div class="faq-grid">
      {faq_cards}
    </div>
  </section>
  <section class="cta-band"><div class="cta-inner">
    <h2 class="cta-title">{u['cta_title']}</h2>
    <p class="cta-lede">{t['cta_lede']}</p>
    <a class="mas-badge mas-badge-on-dark" href="{su}" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="{u['badge_alt']}" /></a>
  </div></section>
  <footer class="site-footer">
    <div class="footer-bottom"><span>&copy; <span id="yr"></span> NotchNest &middot; Satnam Singh</span><span>{role_links}</span></div>
  </footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body></html>
"""


def build_learn_index(loc):
    t = LEARN_INDEX[loc]
    d = DIRS[loc]
    cards = "\n    ".join(
        f'<a class="learn-card" href="{c[0]}"><span class="learn-card-tag">{c[1]}</span><h2>{c[2]}</h2><p>{c[3]}</p><span class="arrow">{c[4]}</span></a>'
        for c in t["cards"])
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<link rel="canonical" href="{BASE}{d}learn/" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang('learn/')}
<meta property="og:title" content="{t['title']}" />
<meta property="og:description" content="{t['og_desc']}" />
<meta property="og:url" content="{BASE}{d}learn/" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:image" content="{BASE}assets/og/learn-index.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": {jstr(t['title'])},
  "url": "{BASE}{d}learn/",
  "inLanguage": "{LANG_ATTR[loc]}",
  "breadcrumb": {{
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": {jstr(t['crumb_home'])}, "item": "{BASE}{d}" }},
      {{ "@type": "ListItem", "position": 2, "name": {jstr(t['crumb_learn'])}, "item": "{BASE}{d}learn/" }}
    ]
  }}
}}
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="" width="28" height="28"/><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/learn/">EN</a><a href="/{d}learn/" class="nn-nav-keep">{t['nav_learn']}</a>
  </div>
</div></nav>

<main class="main-container"><div class="content-wrapper">
  <div class="crumbs"><a href="/{d}">{t['crumb_home']}</a><span class="sep">/</span><span>{t['crumb_learn']}</span></div>
  <header class="learn-hero">
    <h1>{t['hero_h1']}</h1>
    <p>{t['hero_p']}</p>
  </header>
  <div class="learn-grid">
    {cards}
  </div>
  <footer class="site-footer">
    <div class="footer-bottom"><span>© <span id="yr"></span> NotchNest · Satnam Singh</span>{footer_lang_inline(loc, 'learn/')}</div>
  </footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body></html>
"""


def build_article(loc, slug):
    t = ARTICLES[slug][loc]
    d = DIRS[loc]
    su = store_url(loc)
    url = f"{BASE}{d}learn/{slug}/"
    faq_json = ",\n      ".join(
        '{ "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
        % (jstr(q), jstr(a)) for q, a in t["faq"])
    # optional HowTo block (only slug 1 has it)
    howto = ""
    if t.get("howto"):
        steps = ",\n      ".join(
            '{ "@type": "HowToStep", "position": %d, "name": %s, "text": %s }'
            % (i + 1, jstr(n), jstr(x)) for i, (n, x) in enumerate(t["howto"]["steps"]))
        howto = """,
  {
    "@context": "https://schema.org", "@type": "HowTo",
    "name": %s, "totalTime": "PT3M", "inLanguage": "%s",
    "step": [
      %s
    ]
  }""" % (jstr(t["howto"]["name"]), LANG_ATTR[loc], steps)
    related = "\n        ".join(
        f'<a class="related-card" href="{r[0]}"><h3>{r[1]}</h3><p>{r[2]}</p></a>'
        for r in t["related"])
    body = t["body"].replace("%STORE%", su)
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang(f'learn/{slug}/')}
<meta property="og:title" content="{t['og_title']}" />
<meta property="og:description" content="{t['og_desc']}" />
<meta property="og:url" content="{url}" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:type" content="article" />
<meta property="og:image" content="{BASE}assets/og/{slug}.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@codetard" />
<meta name="twitter:creator" content="@codetard" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org", "@type": "Article",
    "headline": {jstr(t['jsonld_headline'])},
    "description": {jstr(t['jsonld_desc'])},
    "image": "{BASE}assets/og/{slug}.png",
    "datePublished": "2026-06-10T00:00:00+00:00", "dateModified": "2026-06-13T00:00:00+00:00",
    "inLanguage": "{LANG_ATTR[loc]}",
    "author": {{ "@type": "Person", "name": "Satnam Singh", "url": "https://silverseahog.com/", "jobTitle": "Swift Developer",
      "sameAs": ["https://silverseahog.com/","https://twitter.com/codetard","https://github.com/29satnam","https://www.linkedin.com/in/satnam-singh-948348aa/","https://instagram.com/codetard"] }},
    "publisher": {{ "@type": "Organization", "name": "NotchNest", "logo": {{ "@type": "ImageObject", "url": "{BASE}assets/notchnest-icon.png" }} }},
    "mainEntityOfPage": "{url}"
  }},
  {{
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": {jstr(t['crumb_home'])}, "item": "{BASE}{d}" }},
      {{ "@type": "ListItem", "position": 2, "name": {jstr(t['crumb_learn'])}, "item": "{BASE}{d}learn/" }},
      {{ "@type": "ListItem", "position": 3, "name": {jstr(t['crumb_this'])}, "item": "{url}" }}
    ]
  }},
  {{
    "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "{LANG_ATTR[loc]}",
    "mainEntity": [
      {faq_json}
    ]
  }}{howto}
]
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="" width="28" height="28"/><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/learn/{slug}/">EN</a>
    <a href="/{d}learn/" class="nn-nav-keep">{t['nav_learn']}</a>
  </div>
</div></nav>

<main class="main-container"><div class="learn-wrap">
  <div class="crumbs"><a href="/{d}">{t['crumb_home']}</a><span class="sep">/</span><a href="/{d}learn/">{t['crumb_learn']}</a><span class="sep">/</span><span>{t['crumb_this']}</span></div>

  <header class="article-head">
    <span class="article-kicker">{t['kicker']}</span>
    <h1 class="article-h1">{t['h1']}</h1>
    <p class="article-lede">{t['lede']}</p>
    <div class="article-meta"><span>{t['updated']}</span><span class="dot"></span><span>{t['readtime']}</span><span class="dot"></span><span>{t['byline']}</span></div>
  </header>

  <article class="article-body">
    {body}

    <aside class="author-bio">
      <img class="author-avatar" src="https://github.com/29satnam.png" alt="Satnam Singh" width="56" height="56" loading="lazy" />
      <div>
        <h3>{t['author_h3']}</h3>
        <p>{t['author_bio']}</p>
      </div>
    </aside>

    <section class="related-section">
      <h2>{t['related_h2']}</h2>
      <div class="related-grid">
        {related}
      </div>
    </section>
  </article>

  <footer class="site-footer">
    <div class="footer-bottom"><span>© <span id="yr"></span> NotchNest · Satnam Singh</span>{footer_lang_inline(loc, f'learn/{slug}/')}</div>
  </footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body></html>
"""


COMPARE_SLUGS = ["notchnest-vs-notchnook", "notchnest-vs-alcove", "notchnest-vs-boring-notch"]


def build_compare(loc, slug):
    from build_i18n_compare import CMP, CMP_UI, TOK, ROWS, FEATURES
    t = CMP[slug][loc]
    u = CMP_UI[loc]
    tok = TOK[loc]
    d = DIRS[loc]
    su = store_url(loc)
    url = f"{BASE}{d}compare/{slug}/"
    comp = CMP[slug]["competitor"]
    feats = FEATURES[slug][loc]
    rows = ""
    for i, (nc, nt, cc, ct) in enumerate(ROWS[slug]):
        rows += (f'        <tr><td>{feats[i]}</td>'
                 f'<td class="{nc}">{tok.get(nt, nt)}</td>'
                 f'<td class="{cc}">{tok.get(ct, ct)}</td></tr>\n')
    faq_cards = "\n    ".join(
        f'<details class="faq-card"><summary class="faq-question">{q}<span class="faq-toggle"></span></summary><div class="faq-answer">{a}</div></details>'
        for q, a in t["faq"])
    faq_json = ",".join(
        '{ "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
        % (jstr(q), jstr(a)) for q, a in t["faq"])
    others = [s for s in COMPARE_SLUGS if s != slug]
    rel = []
    for os_ in others:
        rel.append((f"/{d}compare/{os_}/", f"NotchNest vs {CMP[os_]['competitor']}", u["related_blurb"]))
    rel.append((f"/{d}learn/best-macos-notch-apps/", u["bestapps_h3"], u["bestapps_blurb"]))
    related = "\n        ".join(
        f'<a class="related-card" href="{r[0]}"><h3>{r[1]}</h3><p>{r[2]}</p></a>' for r in rel)
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang(f'compare/{slug}/')}
<meta property="og:title" content="{t['title']}" />
<meta property="og:description" content="{t['description']}" />
<meta property="og:url" content="{url}" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:type" content="article" />
<meta property="og:image" content="{BASE}assets/og/best-macos-notch-apps.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@codetard" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<script type="application/ld+json">
[
  {{
    "@context": "https://schema.org", "@type": "SoftwareApplication",
    "name": "NotchNest", "operatingSystem": "macOS 14.0+", "applicationCategory": "ProductivityApplication",
    "applicationSubCategory": "Mac notch utility", "softwareVersion": "1.2.5", "inLanguage": "{LANG_ATTR[loc]}",
    "url": "{BASE}", "downloadUrl": "{su}", "image": "{BASE}assets/notchnest-icon.png",
    "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.0", "ratingCount": "15", "bestRating": "5", "worstRating": "1" }},
    "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "{CURRENCY[loc]}", "availability": "https://schema.org/InStock", "url": "{su}" }}
  }},
  {{
    "@context": "https://schema.org", "@type": "Article",
    "headline": {jstr(t['title'].split(' — ')[0])}, "description": {jstr(t['description'])},
    "image": "{BASE}assets/og/best-macos-notch-apps.png",
    "datePublished": "2026-06-11T00:00:00+00:00", "dateModified": "2026-06-13T00:00:00+00:00", "inLanguage": "{LANG_ATTR[loc]}",
    "author": {{ "@type": "Person", "name": "Satnam Singh", "url": "https://silverseahog.com/", "jobTitle": "Swift Developer",
      "sameAs": ["https://silverseahog.com/","https://twitter.com/codetard","https://github.com/29satnam","https://www.linkedin.com/in/satnam-singh-948348aa/","https://instagram.com/codetard"] }},
    "publisher": {{ "@type": "Organization", "name": "NotchNest", "logo": {{ "@type": "ImageObject", "url": "{BASE}assets/notchnest-icon.png" }} }},
    "mainEntityOfPage": "{url}"
  }},
  {{
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": {jstr(u['home'])}, "item": "{BASE}{d}" }},
      {{ "@type": "ListItem", "position": 2, "name": {jstr(u['compare'])}, "item": "{BASE}{d}compare/" }},
      {{ "@type": "ListItem", "position": 3, "name": "NotchNest vs {comp}", "item": "{url}" }}
    ]
  }},
  {{
    "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "{LANG_ATTR[loc]}",
    "mainEntity": [{faq_json}]
  }}
]
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav" aria-label="{u['nav_aria']}"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="NotchNest" width="28" height="28" /><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/{d}#features">{u['features']}</a><a href="/{d}compare/">{u['compare']}</a><a href="/{d}learn/" class="nn-nav-keep">{u['learn']}</a>
  </div>
</div></nav>
<main class="main-container"><div class="learn-wrap">
  <div class="crumbs"><a href="/{d}">{u['home']}</a><span class="sep">/</span><a href="/{d}compare/">{u['compare']}</a><span class="sep">/</span><span>NotchNest vs {comp}</span></div>
  <header class="article-head">
    <span class="article-kicker">{u['kicker']}</span>
    <h1 class="article-h1">NotchNest vs {comp}</h1>
    <p class="article-lede">{t['lede']}</p>
    <div class="article-meta"><span>{u['updated']}</span><span class="dot"></span><span>{u['readtime']}</span><span class="dot"></span><span>{u['byline']}</span></div>
  </header>
  <article class="article-body">
    <p>{t['intro']}</p>
    <h2>{u['th_feature']}</h2>
    <table class="cmp-table">
      <thead><tr><th>{u['th_feature']}</th><th>NotchNest</th><th>{comp}</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>{u['cta_h3']}</h3>
        <p>{u['cta_p']}</p>
      </div>
      <a href="{su}" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="{u['badge_alt']}" /></a>
    </div>
    <h2>{u['verdict_h2']}</h2>
    <p>{t['verdict']}</p>
    <h2>{u['faq_h2']}</h2>
    {faq_cards}
    <aside class="author-bio">
      <img class="author-avatar" src="https://github.com/29satnam.png" alt="Satnam Singh" width="56" height="56" loading="lazy" />
      <div>
        <h3>{u['author_h3']}</h3>
        <p>{u['author_bio']}</p>
      </div>
    </aside>
    <section class="related-section">
      <h2>{u['related_h2']}</h2>
      <div class="related-grid">
        {related}
      </div>
    </section>
  </article>
  <footer class="site-footer">
    <div class="footer-bottom"><span>&copy; <span id="yr"></span> NotchNest &middot; Satnam Singh</span>{footer_lang_inline(loc, f'compare/{slug}/')}</div>
  </footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body></html>
"""


def build_compare_index(loc):
    from build_i18n_compare import CMP, CMP_UI
    u = CMP_UI[loc]
    d = DIRS[loc]
    blurb = {"notchnest-vs-notchnook": u["hub_p"], "notchnest-vs-alcove": u["hub_p"], "notchnest-vs-boring-notch": u["hub_p"]}
    cards = "\n    ".join(
        f'<a class="learn-card" href="/{d}compare/{s}/"><span class="learn-card-tag">{u["kicker"]}</span><h2>NotchNest vs {CMP[s]["competitor"]}</h2><p>{CMP[s][loc]["lede"][:90]}…</p><span class="arrow">{u["compare_arrow"]}</span></a>'
        for s in COMPARE_SLUGS)
    cards += (f'\n    <a class="learn-card" href="/{d}learn/best-macos-notch-apps/"><span class="learn-card-tag">{u["kicker"]}</span>'
              f'<h2>{u["bestapps_h3"]}</h2><p>{u["bestapps_blurb"]}</p><span class="arrow">{u["read_arrow"]}</span></a>')
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<title>{u['hub_title']}</title>
<meta name="description" content="{u['hub_desc']}" />
<link rel="canonical" href="{BASE}{d}compare/" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang('compare/')}
<meta property="og:title" content="{u['hub_title']}" />
<meta property="og:description" content="{u['hub_desc']}" />
<meta property="og:url" content="{BASE}{d}compare/" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:image" content="{BASE}assets/og/best-macos-notch-apps.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org", "@type": "CollectionPage",
  "name": {jstr(u['hub_title'])}, "url": "{BASE}{d}compare/", "inLanguage": "{LANG_ATTR[loc]}",
  "breadcrumb": {{ "@type": "BreadcrumbList", "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": {jstr(u['home'])}, "item": "{BASE}{d}" }},
    {{ "@type": "ListItem", "position": 2, "name": {jstr(u['compare'])}, "item": "{BASE}{d}compare/" }}
  ] }}
}}
</script>{rtl_style(loc)}
</head>
<body>
<nav class="nn-nav" aria-label="{u['nav_aria']}"><div class="nn-nav-inner">
  <a class="nn-brand" href="/{d}"><img class="nn-brand-mark" src="/assets/notchnest-icon.png" alt="NotchNest" width="28" height="28" /><span>NotchNest</span></a>
  <div class="nn-nav-links">
    <a href="/{d}#features">{u['features']}</a><a href="/{d}compare/" class="nn-nav-keep">{u['compare']}</a><a href="/{d}learn/">{u['learn']}</a>
  </div>
</div></nav>
<main class="main-container"><div class="content-wrapper">
  <div class="crumbs"><a href="/{d}">{u['home']}</a><span class="sep">/</span><span>{u['compare']}</span></div>
  <header class="learn-hero">
    <h1>{u['hub_h1']}</h1>
    <p>{u['hub_p']}</p>
  </header>
  <div class="learn-grid">
    {cards}
  </div>
  <footer class="site-footer">
    <div class="footer-bottom"><span>&copy; <span id="yr"></span> NotchNest &middot; Satnam Singh</span>{footer_lang_inline(loc, 'compare/')}</div>
  </footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body></html>
"""


def build_privacy(loc):
    from build_i18n_privacy import PRIVACY
    t = PRIVACY[loc]
    d = DIRS[loc]
    url = f"{BASE}{d}privacy-policy.html"
    sections = "\n        ".join(
        f'<div class="privacy-section"><h3 class="privacy-heading">{h}</h3>{c}</div>'
        for h, c in t["sections"])
    return f"""<!DOCTYPE html>
<html lang="{LANG_ATTR[loc]}"{rtl_attrs(loc)}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{t['title']}</title>
<meta name="description" content="{t['description']}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
{hreflang('privacy-policy.html')}
<meta property="og:title" content="{t['title']}" />
<meta property="og:description" content="{t['description']}" />
<meta property="og:url" content="{url}" />
<meta property="og:locale" content="{OG_LOCALE[loc]}" />
<meta property="og:type" content="website" />
<meta property="og:image" content="{BASE}1200x630-banner.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="stylesheet" href="/styles.css" />
<link rel="apple-touch-icon" href="/assets/notchnest-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<link rel="shortcut icon" href="/favicon.ico" />
<meta name="theme-color" content="#000000" />
<meta name="color-scheme" content="dark" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<script type="application/ld+json">
{{
  "@context": "https://schema.org", "@type": "PrivacyPolicy",
  "name": {jstr(t['title'])}, "url": "{url}", "inLanguage": "{LANG_ATTR[loc]}",
  "isPartOf": {{ "@type": "WebSite", "name": "NotchNest", "url": "{BASE}" }}
}}
</script>{rtl_style(loc)}
</head>
<body class="notchnest-body">
<div class="background-gradient"></div>
<main class="main-container"><div class="content-wrapper">
  <nav class="nav-section"><a class="back-button" href="/{d}">← {t['back']}</a></nav>
  <section class="privacy-header-section">
    <div class="app-info"><div class="app-header">
      <h1 class="privacy-title">{t['h1']}</h1>
      <p class="app-description">{t['description']}</p>
    </div></div>
  </section>
  <section class="privacy-content-section"><div class="privacy-card">
    <div class="privacy-intro">
      <h2 class="privacy-section-title">{t['policy_title']}</h2>
      <p class="privacy-intro-text">{t['effective']}</p>
      <p class="privacy-intro-text">{t['intro']}</p>
    </div>
    <div class="privacy-section" style="border:1px solid rgba(255,255,255,0.14);border-radius:14px;padding:16px 18px;margin:8px 0 20px;background:rgba(255,255,255,0.04)">
      <p class="privacy-text" style="margin:0">⚠️ {t['disclaimer']} <a class="faq-link" href="/privacy-policy.html">{t['read_en']}</a></p>
    </div>
    <div class="privacy-sections">
        {sections}
    </div>
  </div></section>
  <footer class="site-footer"><div class="footer-bottom"><span>© <span id="yr"></span> NotchNest · Satnam Singh</span></div></footer>
</div></main>
<script>var yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def jstr(s):
    """JSON string literal (escape quotes/backslashes)."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("  wrote", path.relative_to(ROOT))


def footer_lang_span(current):
    """<a> list for the root footer-lang span."""
    out = []
    for code in ORDER:
        href = "/" + DIRS[code]
        cur = ' aria-current="page"' if code == current else ""
        out.append(f'                        <a href="{href}" hreflang="{code}"{cur}>{SWITCH[code]}</a>')
    return "\n".join(out)


def patch_existing():
    print("patching en/de/zh:")
    # root English homepage
    p = ROOT / "index.html"
    h = p.read_text(encoding="utf-8")
    h = patch_hreflang(h, "")
    h = re.sub(r'"inLanguage":\s*\[[^\]]*\]',
               '"inLanguage": ["en", "de", "zh", "ar", "fr", "pt-BR", "pt-PT", "es-MX"]', h, count=1)
    h = re.sub(r'<span class="footer-lang">.*?</span>',
               '<span class="footer-lang">\n' + footer_lang_span("en") + '\n                    </span>',
               h, count=1, flags=re.S)
    p.write_text(h, encoding="utf-8")
    print("  patched index.html")

    # German + Chinese homepages
    for loc, h4 in (("de", "Sprache"), ("zh", "语言")):
        p = ROOT / DIRS[loc] / "index.html"
        h = p.read_text(encoding="utf-8")
        h = patch_hreflang(h, "", indent="")
        # stale rating → real 4.0 / 15
        h = h.replace('"ratingValue": "4.7", "ratingCount": "1008"',
                      '"ratingValue": "4.0", "ratingCount": "15"')
        h = h.replace('"priceCurrency": "EUR"',
                      '"priceCurrency": "%s"' % ({"de": "EUR", "zh": "CNY"}[loc]))
        # expand footer language list to all 8
        li = "\n      ".join(
            f'<li><a href="/{DIRS[c]}"%s>{SWITCH[c]}</a></li>' % (' aria-current="page"' if c == loc else "")
            for c in ORDER)
        h = re.sub(r'(<h4>' + h4 + r'</h4><ul>).*?(</ul>)',
                   lambda m: m.group(1) + "\n      " + li + "\n    " + m.group(2), h, count=1, flags=re.S)
        p.write_text(h, encoding="utf-8")
        print(f"  patched {DIRS[loc]}index.html")


def patch_learn_hreflang():
    """Bring en/de/zh learn hub + the two translated articles up to the 8-locale cluster."""
    targets = [("learn/", "learn/")]
    for slug in ARTICLE_SLUGS:
        targets.append((f"learn/{slug}/", f"learn/{slug}/"))
    for loc in ("en", "de", "zh"):
        d = DIRS[loc]
        for suffix, _ in targets:
            p = ROOT / d / suffix / "index.html"
            if not p.exists():
                continue
            h = p.read_text(encoding="utf-8")
            ind = "" if loc in ("de", "zh") else "    "
            h = patch_hreflang(h, suffix, indent=ind)
            p.write_text(h, encoding="utf-8")
    print("  patched en/de/zh learn hreflang")


def xhtml_alts(suffix):
    lines = []
    for code in ORDER:
        url = BASE + DIRS[code] + suffix
        lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{url}"/>')
        for e in EXTRA.get(code, []):
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{e}" href="{url}"/>')
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + suffix}"/>')
    return "\n".join(lines)


def update_sitemap():
    p = ROOT / "sitemap.xml"
    xml = p.read_text(encoding="utf-8")
    # refresh the (shared) homepage alternate cluster to the full 8-locale set
    old = "\n".join([
        '    <xhtml:link rel="alternate" hreflang="en" href="https://notchnest.app/"/>',
        '    <xhtml:link rel="alternate" hreflang="en-us" href="https://notchnest.app/"/>',
        '    <xhtml:link rel="alternate" hreflang="en-gb" href="https://notchnest.app/"/>',
        '    <xhtml:link rel="alternate" hreflang="en-in" href="https://notchnest.app/"/>',
        '    <xhtml:link rel="alternate" hreflang="de" href="https://notchnest.app/de/"/>',
        '    <xhtml:link rel="alternate" hreflang="zh" href="https://notchnest.app/zh/"/>',
        '    <xhtml:link rel="alternate" hreflang="zh-cn" href="https://notchnest.app/zh/"/>',
        '    <xhtml:link rel="alternate" hreflang="x-default" href="https://notchnest.app/"/>',
    ])
    if old in xml:
        xml = xml.replace(old, xhtml_alts(""))
    # append the new locale pages if not already present
    entries = []
    for loc in FULL:
        d = DIRS[loc]
        pages = [("", "weekly", "0.9"), ("learn/", "monthly", "0.7")]
        for slug in ARTICLE_SLUGS:
            pages.append((f"learn/{slug}/", "monthly", "0.7"))
        for slug in FOR_SLUGS:
            pages.append((f"for/{slug}/", "monthly", "0.6"))
        pages.append(("compare/", "monthly", "0.7"))
        for slug in COMPARE_SLUGS:
            pages.append((f"compare/{slug}/", "monthly", "0.7"))
        for slug in ARTICLES:
            if slug not in ARTICLE_SLUGS and loc in ARTICLES[slug]:
                pages.append((f"learn/{slug}/", "monthly", "0.7"))
        pages.append(("privacy-policy.html", "yearly", "0.3"))
        for suffix, cf, pr in pages:
            url = BASE + d + suffix
            if f"<loc>{url}</loc>" in xml:
                continue
            entries.append(
                f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-08-24T00:00:00+00:00</lastmod>\n"
                f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n"
                f"{xhtml_alts(suffix)}\n  </url>")
    if entries:
        xml = xml.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    p.write_text(xml, encoding="utf-8")
    print(f"  sitemap: refreshed home alternates, added {len(entries)} URLs")


def build_llms(loc):
    la = LANDING[loc]
    li = LEARN_INDEX[loc]
    d = DIRS[loc]
    home = BASE + d
    art = ARTICLES
    lines = [
        "# NotchNest",
        "",
        "> " + la["sa_desc"],
        "",
        f"- {la['title'].split('—')[0].strip()}: {home}",
        f"- {li['nav_learn']}: {home}learn/",
        f"- {art['how-to-use-the-macbook-notch'][loc]['h1']}: {home}learn/how-to-use-the-macbook-notch/",
        f"- {art['best-macos-notch-apps'][loc]['h1']}: {home}learn/best-macos-notch-apps/",
        f"- Mac App Store: {store_url(loc)}",
        "",
    ]
    return "\n".join(lines)


def update_llms():
    for loc in GEN:
        (ROOT / DIRS[loc] / "llms.txt").write_text(build_llms(loc), encoding="utf-8")
    # add a Languages section to the root llms.txt (idempotent)
    for fn in ("llms.txt", "llms-full.txt"):
        p = ROOT / fn
        h = p.read_text(encoding="utf-8")
        if "## Languages" in h:
            h = re.sub(r"\n## Languages\n.*?(?=\n## |\Z)", "", h, flags=re.S)
        block = ["", "## Languages", ""]
        for code in ORDER:
            url = BASE + DIRS[code]
            block.append(f"- {SWITCH[code]}: {url}" + ("" if code in ("en",) else f" ({url}llms.txt)" if code in [c for c in GEN] else ""))
        section = "\n".join(block) + "\n"
        h = h.rstrip() + "\n" + section
        p.write_text(h, encoding="utf-8")
    print(f"  llms: wrote {len(GEN)} localized llms.txt + root Languages section")


def patch_en_compare():
    """English compare pages: fix stale rating and the outdated language row."""
    for slug in COMPARE_SLUGS:
        p = ROOT / "compare" / slug / "index.html"
        if not p.exists():
            continue
        h = p.read_text(encoding="utf-8")
        h = h.replace('"ratingValue": "4.7", "ratingCount": "1008"',
                      '"ratingValue": "4.0", "ratingCount": "15"')
        h = h.replace('<td>Localised (EN/DE/ZH)</td>', '<td>Localized (8 languages)</td>')
        p.write_text(h, encoding="utf-8")
    print("  patched en compare rating + language row")


def patch_simple_hreflang(suffixes):
    """Patch the English original of pages that now exist in every locale."""
    for suffix in suffixes:
        p = ROOT / suffix if suffix.endswith(".html") else ROOT / suffix / "index.html"
        if not p.exists():
            continue
        h = p.read_text(encoding="utf-8")
        h = patch_hreflang(h, suffix, indent="")
        p.write_text(h, encoding="utf-8")
    print(f"  patched en hreflang for {len(suffixes)} page(s)")


def main():
    print("landing pages:")
    for loc in GEN:
        write(ROOT / DIRS[loc] / "index.html", build_landing(loc))
    print("learn hubs + articles:")
    for loc in GEN:
        write(ROOT / DIRS[loc] / "learn" / "index.html", build_learn_index(loc))
        for slug in ARTICLE_SLUGS:
            write(ROOT / DIRS[loc] / "learn" / slug / "index.html", build_article(loc, slug))
    # extra learn articles translated into every non-English locale (backfills de/zh too)
    extra = [s for s in ARTICLES if s not in ARTICLE_SLUGS]
    if extra:
        print("extra learn articles:")
        for loc in FULL:
            for slug in extra:
                if loc in ARTICLES[slug]:
                    write(ROOT / DIRS[loc] / "learn" / slug / "index.html", build_article(loc, slug))
    print("for/ pages:")
    for loc in FULL:
        for slug in FOR_SLUGS:
            write(ROOT / DIRS[loc] / "for" / slug / "index.html", build_for(loc, slug))
    print("compare/ pages:")
    for loc in FULL:
        write(ROOT / DIRS[loc] / "compare" / "index.html", build_compare_index(loc))
        for slug in COMPARE_SLUGS:
            write(ROOT / DIRS[loc] / "compare" / slug / "index.html", build_compare(loc, slug))
    print("privacy pages:")
    for loc in FULL:
        write(ROOT / DIRS[loc] / "privacy-policy.html", build_privacy(loc))
    patch_existing()
    patch_learn_hreflang()
    extra_learn = [f"learn/{s}/" for s in ARTICLES if s not in ARTICLE_SLUGS]
    patch_simple_hreflang([f"for/{s}/" for s in FOR_SLUGS]
                          + ["compare/"] + [f"compare/{s}/" for s in COMPARE_SLUGS]
                          + extra_learn + ["privacy-policy.html"])
    patch_en_compare()
    print("sitemap:")
    update_sitemap()
    print("llms:")
    update_llms()


if __name__ == "__main__":
    main()
