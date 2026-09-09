# App Store Connect metadata kit

Drafted 8 Sep 2026 against the live listing (`id6747612321`, v1.2.5).
Everything here is paste-ready. Character counts verified against Apple's limits.

**Nothing in this file is live.** It has to be entered in App Store Connect by hand.

---

## 1. Keyword field (100 chars) — highest-leverage single change

Apple indexes the **app name**, **subtitle** and **keyword field**. It does *not*
index the description. So never spend keyword characters on a word already present
in the name or subtitle — it is already indexed and the repeat is wasted.

Words already covered by name + subtitle:
`notchnest, notch, dynamic, bar, ai, menu, tools`

**Proposed keyword field (96/100):**

```
menubar,widget,utility,dynamicisland,island,shelf,drop,airdrop,clipboard,pomodoro,timer,calendar
```

Rules applied: no spaces after commas (they cost characters), no plurals (Apple
stems automatically), no repeated words, no competitor brand names (rejection risk).

Didn't fit, in priority order if you free up room: `webcam, mirror, hub, macbook,
customize, productivity, dock`.

---

## 2. Subtitle (30 chars)

**Current:** `Clipboard, Music, Notes, Timer` (30/30)

It's fully used, but every term is one you can't win. Live App Store search:
`clipboard manager` → NotchNest not in top 39. `menu bar` → not in top 38.

**Recommended:**

| # | Subtitle | Chars | Adds to your indexed set |
|---|---|---|---|
| **A** | `AI Notch Bar & Menu Bar Tools` | 29 | **menu bar**, ai, tools |
| B | `Notch Widgets, AirDrop & Menu` | 29 | widgets, airdrop, menu |
| C | `Menu Bar Widget, AI Clipboard` | 29 | menu bar, widget, ai |
| D | `Notch Hub: Menu Bar & Widgets` | 29 | menu bar, hub, widgets |

Go with **A**. "Menu bar" is your largest uncovered cluster on both surfaces —
664 impressions in Search Console, and absent from the store's top 38.

If you pick B, C or D instead, drop the now-duplicated words from the keyword
field above and pull in replacements from the "didn't fit" list.

---

## 3. App name (30 chars)

**Current EN:** `NotchNest - Dynamic Notch Bar` (29/30) — keep it. Good keyword density.

Missing localizations (these storefronts currently serve English):

| Locale | Storefronts | Proposed name | Chars |
|---|---|---|---|
| Arabic | sa, ae, eg | `NotchNest - شريط النتش` | 22 |
| Chinese (Traditional) | tw, hk | `NotchNest - 瀏海效率工具列` | 19 |
| Portuguese (Portugal) | pt | `NotchNest - Notch Dinâmico` | 26 |

Arabic is the notable gap: v1.2.5 shipped Arabic RTL, the entire website is
translated into Arabic, and Egypt is a top-15 country in Search Console — but the
store listing is English in every Arabic storefront.

---

## 4. Description

**Current:** 1,705 / 4,000 characters. Three problems:

1. Opens with `"NotchNest is the #1 feature-rich notch enhancement app for Mac."`
   — an unverifiable superlative. App Review Guideline 2.3.7. You are ranked #2
   for `notch`, so it is also untrue.
2. `"Trusted by thousands of Mac users daily"` — with a rating count below Apple's
   display threshold, this invites scrutiny you don't need.
3. Never uses **menu bar**, **widget**, or **macOS Tahoe** — all terms with
   demonstrated demand.

The description does not affect ranking, only conversion. The first three lines
are what shows before "more" is tapped, so they carry the weight.

**Proposed replacement:**

```
Your Mac's notch does nothing. NotchNest gives it a job.

Hover the notch and it expands into a panel with your calendar, clipboard
history, notes, timer, music controls and a file shelf. Move away and it
collapses. No extra menu bar icon, no window to manage.

All AI runs on-device with Apple Intelligence — nothing you copy or write
is ever uploaded.

— WHAT'S IN THE NOTCH —

• AI Clipboard
Full clipboard history with search and pinning. Rephrase, summarize and refine
with on-device AI.

• File Tray + drag-to-AirDrop
Drop a file on the notch, grab it anywhere. Drop it on the AirDrop target and
the share sheet opens straight away.

• Calendar with AI briefings
Your Apple Calendar, with smart summaries of what's coming up.

• Music controls
Spotify, Apple Music and YouTube Music. Play, pause, skip, see what's playing.

• Quick Notes with AI
Capture an idea in two seconds, refine it with AI, synced across your devices.

• Pomodoro Timer
Sessions, breaks and daily streaks, running whether the panel is open or not.

• Camera Mirror
One-click webcam check before a call.

• Bookmarks Shelf
Pin the sites and apps you open every day.

• Infinity Run
A chicken runner in your notch. Because why not.

— MENU BAR, TOO —

A crowded menu bar hides icons behind the notch. NotchNest moves the things you
interact with — timer, clipboard, agenda — into the notch panel where they have
room, and frees the menu bar slots they used to occupy.

— WHY NOTCHNEST —

• Free to download — Premium lifts every limit, monthly or one-time Lifetime
• On-device Apple Intelligence — nothing uploaded, ever
• Mac App Store only: reviewed, notarized, sandboxed
• Native SwiftUI, built for macOS 26 and Liquid Glass
• Zero measurable idle cost on Apple Silicon
• Works on every Mac — notch or not, external displays included

Requires macOS 14 or later. AI features require Apple Intelligence.

Privacy: https://notchnest.app/privacy-policy.html
Terms: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Contact: 29satnam@gmail.com
```

### Free vs Premium

Confirmed from the in-app paywall. Worth stating plainly in the listing — vague
"free with in-app purchases" is what generates "everything is paid" reviews.

| | Free | Premium |
|---|---|---|
| Bookmarks | 1 | Unlimited |
| Notes | 1 | Unlimited |
| Clipboard items | 5 | Unlimited |
| File-Tray files | 2 | Unlimited |
| Calendar | Today only | All events |
| Camera mirror | 3 seconds | Unlimited |
| Pomodoro | Limited | Unlocked |
| Game | 2 plays / 24h | Fully unlocked |
| Upcoming features | — | Included |

Optional block to append to the description:

```
— FREE VS PREMIUM —

Everything is usable free, with limits: one bookmark, one note, five clipboard
items, two File-Tray files, today's calendar events, a three-second mirror.

NotchNest Premium lifts all of them — $2.99/month, or $14.99 once for Lifetime.
Every future feature is included.
```

---

## 5. Promotional text (170 chars, no review needed to change)

```
New in 1.2.5: Arabic, French, Spanish and Portuguese, a toggle for the battery
capsule, smoother open and close, and lower idle CPU.
```

Useful because it updates without a build submission. Rotate it for launches.

---

## 6. Pricing — one item to clean up in App Store Connect

The app itself now offers two tiers:

```
Monthly Subscription   $2.99 / month
NotchNest Lifetime    $14.99   pay once, use forever
```

**But Apple's product page still advertises a third**, checked live on 9 Sep 2026:

```
In-App Purchases: Yes
  Monthly Subscription   $2.99
  NotchNest Lifetime    $14.99
  Yearly Subscription   $14.99   <-- removed from the app, still listed
```

The yearly IAP is still in a saleable state in App Store Connect, so Apple keeps
showing it. Anyone reading the product page sees a $14.99/year subscription next
to a $14.99 pay-once Lifetime, which makes the pricing look broken.

Remove it: App Store Connect → Monetization → In-App Purchases → Yearly
Subscription → **Remove from Sale**. Existing subscribers, if any, keep their
entitlement; it just stops being offered and disappears from the listing.

## 7. Screenshots

9 of a possible 10, clear captions, real UI. Nothing to change.

## 8. Ratings

Apple's lookup API returns a rating count of 0 in all 47 storefronts, so no star
rating renders on your product page. You have 15 written US reviews averaging
exactly 4.0:

```
5★ ×7    4★ ×3    3★ ×4    1★ ×1
```

Add `SKStoreReviewController.requestReview(in:)` after a positive moment — a
completed Pomodoro session, or the tenth clipboard retrieval. Apple throttles it
to 3 prompts per year automatically.

Do the pricing-copy fix first. The 1★ is titled *"Everything is paid get
something else"* — prompting before expectations are aligned just harvests more
of those.
