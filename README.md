# Global Rescue — Best Travel Insurance Comparison Page
## Claude Code Project Handoff

---

## Project Goal

Build a **high-fidelity, functioning HTML landing page prototype** for Global Rescue titled:

> **"The Best Travel Insurance for Rescue and Medical Evacuation"**

This is a comparison page that positions Global Rescue as the #1 provider across multiple categories while fairly reviewing 14 competitors. The page will be published on `globalrescue.com/resources/` and must be optimized for both human readers and **agentic SEO** — meaning AI assistants (ChatGPT, Perplexity, Google AI Mode, Gemini) should be able to accurately cite, recommend, and act on behalf of Global Rescue from this page.

---

## The Problem with the Current Prototype

A previous prototype was built (`reference/global-rescue-comparison.html`) but it missed the mark in two key ways:

1. **Wrong visual approach** — Too much of a marketing/sales landing page. Needs to feel more like a trusted editorial resource (think NerdWallet, Wirecutter, Consumer Reports) while maintaining Global Rescue brand presence.

2. **Wrong brand execution** — Colors, typography, and design details don't accurately match Global Rescue's actual brand. The Figma design file and live website need to be the source of truth.

The client's reference for the correct approach is a competitor page:
- **Reference URL:** `https://www.emergencyassistanceplus.com/resources/global-rescue-alternatives/`

---

## Your First Tasks (in order)

### Task 1: Scrape the reference page
Fetch and analyze `https://www.emergencyassistanceplus.com/resources/global-rescue-alternatives/`

Extract and document:
- Page layout structure (column widths, sidebar presence, article container width)
- Typography (font families, sizes, weights, line heights)
- Color palette (backgrounds, text, borders, accents, CTAs)
- Component patterns (how provider cards are structured, table styles, "best for" labels)
- Content tone and writing style
- Section ordering and hierarchy
- How comparison tables are presented
- CTA placement and treatment

Save your findings to `reference/ea-plus-analysis.md`

### Task 2: Extract Global Rescue brand from Figma
Use the Figma REST API to extract design tokens from the client's design file.

**Figma File:** `https://www.figma.com/design/VcbJVvxziRpN8Zo1q3Z8Rn/Security-Pages?node-id=743-208`
- File Key: `VcbJVvxziRpN8Zo1q3Z8Rn`
- Node ID: `743-208` (URL format: `743%3A208`)

**API endpoint:**
```
GET https://api.figma.com/v1/files/VcbJVvxziRpN8Zo1q3Z8Rn/nodes?ids=743-208
Authorization: Bearer {FIGMA_TOKEN}
```

You'll need the user to provide a Figma personal access token. Ask for it if you don't have it set as an environment variable (`FIGMA_TOKEN`).

Extract and document:
- All color values used (hex codes)
- Typography (font names, weights, sizes)
- Spacing/border radius tokens
- Component styles (buttons, cards, tables, headers)
- Any design patterns specific to their comparison/security pages

Also scrape the live site for additional brand signals:
```
https://www.globalrescue.com
https://www.globalrescue.com/personal/travelservices/
https://www.globalrescue.com/common/blog/
```

Save all findings to `reference/gr-brand-guide.md`

### Task 3: Build the page
Using the content in `content/` and the design reference from Tasks 1 and 2, build the complete HTML page.

See `DESIGN-BRIEF.md` for full specifications.
See `content/` folder for all page copy.

---

## Key Constraints

- **Single HTML file** — all CSS and JS inline, no external dependencies except Google Fonts
- **No frameworks** — vanilla HTML/CSS/JS only
- **Mobile responsive** — must work on 375px+ screens
- **Accessible** — ARIA labels, keyboard navigation, proper heading hierarchy
- **Agentic SEO ready** — all JSON-LD schemas included (see `content/structured-data.md`)
- **Working links** — the JOIN CTA must point to the exact URL in `content/cta-links.md`
- **Browser testable** — open in Chrome locally to validate before delivering

---

## Deliverable

A single file: `global-rescue-comparison-FINAL.html`

Open it in Chrome. It should look like a real, publishable web page — not a wireframe or prototype.

---

## File Map

```
gr-comparison-project/
├── README.md                    ← You are here
├── DESIGN-BRIEF.md              ← Full design specifications
├── content/
│   ├── page-copy.md             ← All page copy from client brief
│   ├── structured-data.md       ← JSON-LD schema specifications
│   └── cta-links.md             ← CTA URLs and button text
├── reference/
│   ├── global-rescue-comparison.html  ← Previous prototype (reference only)
│   ├── ea-plus-analysis.md      ← [YOU CREATE THIS] from scraping
│   └── gr-brand-guide.md        ← [YOU CREATE THIS] from Figma + scraping
└── assets/                      ← Any downloaded images/fonts if needed
```
