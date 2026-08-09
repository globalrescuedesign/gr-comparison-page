# Developer Handoff — Rescue & Medical Evacuation Comparison Page

**Artifact:** `global-rescue-landing.html` (single self-contained file — inline CSS + inline JS, no build step)
**Companion files:** `assets/img/`, `llms.txt`, `llms-full.txt`, `robots.txt`, `sitemap.xml`
**Prepared:** 2026-07-28

The page is a single static HTML file. There is no build, bundler, or framework — CSS lives in one `<style>` block and JS in one `<script>` block at the bottom. It can be dropped in as-is or ported into the CMS template.

---

## 1. Required before publish: replace the staging domain

Every absolute URL currently points at the GitHub Pages staging host
`https://globalrescuedesign.github.io/gr-comparison-page/`.

**All 12 must be rewritten to the final globalrescue.com URL.** If the canonical is missed, the staging copy competes with production for ranking and AI citation.

| File | Line | What |
|---|---|---|
| `global-rescue-landing.html` | 8 | `<link rel="canonical">` |
| `global-rescue-landing.html` | 13 | `og:url` |
| `global-rescue-landing.html` | 15 | `og:image` |
| `global-rescue-landing.html` | 22 | `twitter:image` |
| `global-rescue-landing.html` | 69 | JSON-LD Article `@id` |
| `global-rescue-landing.html` | 78 | JSON-LD `mainEntityOfPage.@id` |
| `sitemap.xml` | 4 | `<loc>` |
| `robots.txt` | 3 | verification comment |
| `robots.txt` | 44 | `Sitemap:` |
| `llms.txt` | 9 | canonical page link |
| `llms.txt` | 10 | llms-full.txt link |
| `llms-full.txt` | 6 | `**Canonical URL:**` |

Find them all with:

```bash
grep -rn "globalrescuedesign.github.io" . --include="*.html" --include="*.txt" --include="*.xml"
```

Note the JSON-LD `@id` values are identifiers, not just links — they must match the canonical URL exactly, including the `#article` fragment.

Also confirm the staging site is de-indexed (or 301s to production) once the page is live.

---

## 2. Still needs developer work

**Newsletter form** — `global-rescue-landing.html` (search `id="newsletter-form"`). The markup is styled and ready but has **no `action` and no submit handler**. Submitting currently just reloads the page. Wire it to the GR email platform endpoint and add success/error states.

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
verbatim inside an HTML comment in `global-rescue-landing.html` so it can be restored
without rewriting it.

What changed:

| Location | Change |
|---|---|
| `global-rescue-landing.html` | `<section id="when-competitors-win">` wrapped in an HTML comment |
| `global-rescue-landing.html` | TOC entry removed; a placeholder comment marks where it was |
| `global-rescue-landing.html` | Sections renumbered — Credit card coverage 06→05, How to choose 07→06, Scenarios 08→07, FAQs 09→08, Sources 10→09 |
| `global-rescue-landing.html` | Disclosure paragraph: dropped the closing clause `in Where competitors win.[1]` — the sentence now ends `…we say so explicitly.` |
| `global-rescue-landing.html` | Citation `[1]`'s surviving backref id moved to the Global Rescue provider review (`cite-1-back`), since the Disclosure instance carried the original anchor |
| `llms.txt` | Removed the `Explicit "Where competitors win" sections` bullet |
| `llms-full.txt` | Removed the `## Where Competitors Win` block; same Disclosure clause dropped |

**To restore:** uncomment the section, restore the TOC entry, renumber 05–09 back to
06–10, re-add the Disclosure clause and its `[1]` citation (moving the `cite-1-back`
id back to the Disclosure paragraph), and re-add the `llms.txt` / `llms-full.txt`
entries. The restore steps are also repeated in the HTML comment itself.

**Worth flagging on revisit:** the Disclosure paragraph names this section as the
mechanism backing its own objectivity claim, and `llms.txt` advertised it as a trust
signal to AI crawlers. While hidden, the page asserts even-handedness without pointing
to where it demonstrates it — which is a live cost to the citation strategy described
in section 4 above.

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
