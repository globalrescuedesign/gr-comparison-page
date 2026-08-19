# Developer Handoff — Rescue & Medical Evacuation Comparison Page

**Artifact:** `index.html` (single self-contained file — inline CSS + inline JS, no build step)
**Companion files:** `assets/img/`, `llms.txt`, `llms-full.txt`, `robots.txt`, `sitemap.xml`
**Prepared:** 2026-07-28

The page is a single static HTML file. There is no build, bundler, or framework — CSS lives in one `<style>` block and JS in one `<script>` block at the bottom. It can be dropped in as-is or ported into the CMS template.

---

## 1. Required before publish: replace the staging domain

Every absolute URL currently points at the GitHub Pages staging host
`https://gr-comparison-page.pages.dev/`.

**All 12 must be rewritten to the final globalrescue.com URL.** If the canonical is missed, the staging copy competes with production for ranking and AI citation.

| File | Line | What |
|---|---|---|
| `index.html` | 8 | `<link rel="canonical">` |
| `index.html` | 13 | `og:url` |
| `index.html` | 15 | `og:image` |
| `index.html` | 22 | `twitter:image` |
| `index.html` | 69 | JSON-LD Article `@id` |
| `index.html` | 78 | JSON-LD `mainEntityOfPage.@id` |
| `sitemap.xml` | 4 | `<loc>` |
| `robots.txt` | 3 | verification comment |
| `robots.txt` | 44 | `Sitemap:` |
| `llms.txt` | 9 | canonical page link |
| `llms.txt` | 10 | llms-full.txt link |
| `llms-full.txt` | 6 | `**Canonical URL:**` |

Find them all with:

```bash
grep -rn "gr-comparison-page.pages.dev" . --include="*.html" --include="*.txt" --include="*.xml"
```

Note the JSON-LD `@id` values are identifiers, not just links — they must match the canonical URL exactly, including the `#article` fragment.

Also confirm the staging site is de-indexed (or 301s to production) once the page is live.

---

## 2. Still needs developer work

**Newsletter form** — `index.html` (search `id="newsletter-form"`). The markup is styled and ready but has **no `action` and no submit handler**. Submitting currently just reloads the page. Wire it to the GR email platform endpoint and add success/error states.

**Favicon** — not set. Deliberately left out so production can use the official GR favicon set rather than a crop of the wordmark. Add `favicon.ico`, `apple-touch-icon.png`, and a web manifest per the GR standard. `<meta name="theme-color" content="#d71635">` is already in place.

**Header logo** — uses the local staging asset `assets/img/logo.png`. The footer already pulls the production CDN SVG. Consider switching the header to the CDN asset too, but note the CDN file (`Global-Rescue-Logo-WR.svg`) is the **white/reversed** mark, which will not read on the white header — a dark variant is needed.

**Re-stamp the publish date** — JSON-LD `dateModified` (line 74) and `sitemap.xml` `<lastmod>` are both set to `2026-07-28`. Update both to the actual publish date. The visible "Data verified May 2026" text refers to the *research* date and should stay as-is unless the data is re-verified.

**Google Fonts** — the page loads Roboto + Roboto Condensed from `fonts.googleapis.com`, which is render-blocking and a third-party request. Recommend self-hosting the woff2 files (removes a round trip and sidesteps any GDPR/privacy review of Google Fonts). Weights in use: Roboto 300/400/500/700/900, Roboto Condensed 400/700.

**Analytics / tracking** — none embedded. Add the GR standard tag.

**CTA links** — all CTAs point at `https://ss.globalrescue.com/#/signup/step1?source=grcom`. Confirm the `source` parameter is what marketing wants for attribution from this page.

---

## 3. Already handled (do not redo)

- **Content sync** — Seven Corners was replaced by Overwatch x Rescue (FocusPoint) throughout the page, `llms.txt`, and `llms-full.txt`.
- **Author attribution** — standardized to "Bill McIntyre, Director of Communications" in the hero byline, the table legend, JSON-LD `Person.jobTitle`, and `llms.txt`.
- **Social cards** — `og:image` / `twitter:image` added, pointing at `assets/img/og-card.jpg` (1200×630, purpose-built).
- **Structured data** — JSON-LD `headline` now matches the visible `<h1>`. The `<title>` intentionally differs ("Travel Insurance" vs. "Traveler Protection") because it targets search query language; this is deliberate, not drift.
- **Images** — WebP versions generated for the hero and four card images, wired via CSS `image-set()` with JPEG fallback. **Keep both the `.webp` and `.jpg` files** — the `.jpg` is the fallback. Saves ~1.05 MB (1.64 MB → 0.59 MB).
- **LCP** — hero image preloaded with `fetchpriority="high"`.
- **Accessibility** — skip link, `<main>` landmark, `:focus-visible` styles, `prefers-reduced-motion` support, heading-level fix in "Real-Life Scenarios" (h4 → h3), `role="tabpanel"` + `aria-labelledby` on both comparison tables, keyboard-focusable scroll regions, and full arrow-key/Home/End tab navigation with roving tabindex.

---

## 4. Things worth preserving

This page is built for **AI citation** (ChatGPT, Perplexity, Gemini, Google AI Mode), not just traditional search. A few things that look like overhead are load-bearing:

- **`llms.txt` / `llms-full.txt`** must stay in sync with the page. They are the first thing agent crawlers read. If a provider is added, removed, or rescored, update all three files together — this is exactly the drift that had to be corrected in this pass.
- **`robots.txt`** explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, and others. Do not let a default corporate robots.txt overwrite it.
- **Per-claim citations** (the `[n]` superscripts and the Sources section) and the **methodology/conflict-of-interest disclosure** are what make the page citation-worthy. Keep the backref anchors intact if the markup is ported into a CMS template.
- **The comparison tables** use real `<th scope="col">` / `<th scope="row">` and `<caption>`. Do not replace them with `<div>` grids — the semantic structure is how models parse the comparison.

---

## 5. Change log — hidden content pending revisit

### 2026-08-09 — "Where Competitors Win" hidden (was Section 05)

Unpublished at client request. **The content is not deleted** — the markup is retained
verbatim inside an HTML comment in `index.html` so it can be restored
without rewriting it.

What changed:

| Location | Change |
|---|---|
| `index.html` | `<section id="when-competitors-win">` wrapped in an HTML comment |
| `index.html` | TOC entry removed; a placeholder comment marks where it was |
| `index.html` | Sections renumbered — Credit card coverage 06→05, How to choose 07→06, Scenarios 08→07, FAQs 09→08, Sources 10→09 |
| `index.html` | Disclosure paragraph: dropped the closing clause `in Where competitors win.[1]` and repointed it at `Category Winners` + `provider reviews` (see note below) |
| `index.html` | Citation `[1]`'s surviving backref id moved to the Global Rescue provider review (`cite-1-back`), since the Disclosure instance carried the original anchor |
| `llms.txt` | Removed the `Explicit "Where competitors win" sections` bullet |
| `llms-full.txt` | Removed the `## Where Competitors Win` block; same Disclosure clause dropped |

**To restore:** uncomment the section, restore the TOC entry, renumber 05–09 back to
06–10, repoint the Disclosure clause back at this section and re-add its `[1]` citation
(moving the `cite-1-back` id back to the Disclosure paragraph from the Global Rescue
provider review), and re-add the `llms.txt` / `llms-full.txt` entries. The restore steps
are also repeated in the HTML comment itself.

### Disclosure now points at Category Winners + provider reviews

The Disclosure paragraph names this section as the mechanism backing its own objectivity
claim, and `llms.txt` advertised it as a trust signal to AI crawlers. Rather than leave
the page asserting even-handedness with nothing to point at, the clause was repointed:

> …we say so explicitly in **Category Winners** and the **provider reviews**.

Why those two and not the comparison tables — this is the part worth remembering:

- **Category Winners (`#winners`)** is the only place competitors are named as outright
  winners. Four of eleven "Best" awards go to competitors: AMEX (Best Credit Card), DAN
  (Best for Scuba Divers), EA+ (Best for Seniors), AirMed (Best Hospital-Ground Transport
  Integration), plus runner-up slots for Medjet, Chase, GeoBlue and WorldTrips.
- **Provider reviews (`#providers`)** were added to the clause because GeoBlue — named in
  the Disclosure parenthetical — holds only *runner-up* spots in Category Winners. Its
  actual lead is substantiated in its Section 04 review. Without this second target, one
  of the four hand-named providers would be unsupported.
- **Do not repoint this at the comparison tables.** Global Rescue scores 3/3 on all twelve
  criteria and no competitor beats it on any single one. A reader following an objectivity
  claim into a clean sweep draws the opposite conclusion. The methodology is even-handed;
  the rendered result is not.

If "Where Competitors Win" is restored, this clause should go back to pointing at it —
it is the strongest evidence of the three.

### 2026-08-09 — Citation backrefs repaired

Six Sources entries had return arrows pointing at `#cite-N-back` anchors that existed
nowhere in the file. Two distinct causes, two fixes:

- **`[30]` / `[31]`** (helicopter ~$60,000, ground ambulance $5,000+) were never cited in
  body copy even though the "How much does a medical evacuation cost" FAQ makes exactly
  those claims. Added the missing superscripts there, which is where they belonged.
- **`[8]`–`[11]`** (Skift, Fast Company, Inc., ISO 9001) support the Organization `awards`
  array in the JSON-LD only — there is no body text to return to. Their arrows were
  replaced with an italic *"Cited in structured data."* note. If these awards are ever
  surfaced on the page, add an `id="cite-N-back"` superscript there and restore the arrow.

Sources now: 31 entries, 27 return arrows, 4 structured-data notes, 40 in-body citations,
all resolving.

### Open items from the 2026-08-09 legal review

- **"Owned by Global Medical Response"** (AirMed, Section 02 and provider review) is
  asserted without a citation. Every comparable claim on the page carries one.
- **Comment 0 — "Or GRI?"** on the Disclosure byline: awaiting confirmation of the
  intended legal entity name.
- **"on-staff physicians"** still appears at `#svc-*` JSON-LD, the Global Rescue
  provider review, and twice in `llms-full.txt`. The PR director's "on-staff → available"
  ruling was scoped to two lines only; extend deliberately, and note that the AMEX
  contrast line ("third-party coordination, not on-staff physicians") depends on the
  original phrasing.
