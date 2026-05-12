# Design Brief — GR Comparison Page

## Overall Design Direction

**Feel:** Somewhere between editorial resource and branded landing page.
Think: NerdWallet article meets Global Rescue brand identity.

**NOT:** A sales-heavy marketing landing page with full-bleed hero sections and heavy animations.
**NOT:** A plain unstyled article with no brand presence.
**IS:** A polished, authoritative comparison resource that feels trustworthy and citable,
       with clear Global Rescue brand ownership at the top and bottom.

---

## Layout Structure

Use a **standard editorial article layout**:

```
┌─────────────────────────────────────┐
│  SITE HEADER (GR brand, nav, JOIN)  │
├─────────────────────────────────────┤
│  PAGE HERO (modest — title only,    │
│  subtitle, breadcrumb, maybe a      │
│  single background color or image)  │
├────────────────────┬────────────────┤
│                    │                │
│  MAIN CONTENT      │  STICKY        │
│  COLUMN            │  SIDEBAR       │
│  (max ~760px)      │  (TOC / CTA)   │
│                    │                │
│  • Methodology     │                │
│  • What's covered  │                │
│  • Provider cards  │                │
│  • Tables          │                │
│  • Reviews         │                │
│  • Credit cards    │                │
│  • How to choose   │                │
│  • FAQs            │                │
│                    │                │
├────────────────────┴────────────────┤
│  CTA BLOCK (full-width, branded)    │
├─────────────────────────────────────┤
│  FOOTER                             │
└─────────────────────────────────────┘
```

**Key layout specs:**
- Page max-width: 1200px
- Main content column: ~720–760px max
- Sidebar: ~260–280px, sticky, scrolls with page
- Content left-aligns with generous padding on mobile
- Sidebar collapses to below-hero on mobile (becomes inline TOC)

---

## Hero Section

Keep it, but make it **restrained**:
- Background: GR brand navy (exact hex from Figma)
- Content: H1 title, one-line subtitle, breadcrumb, last-updated date
- NO full-bleed photography
- NO trust counters, badge rows, or marketing copy in the hero
- A single "Jump to comparison table →" anchor link is fine
- Height: ~220–280px maximum (not a full-screen hero)

---

## Content Tone

Pull from the EA+ reference page approach:
- **Authoritative but fair** — acknowledge where competitors genuinely lead
- **Prose-first** — introduce each section with a clear paragraph before any table or list
- **Direct verdicts** — state clearly who wins each category and why, in one sentence
- **No hyperbole** — replace "best-in-class," "unparalleled," "exceptional" with specific facts
- **Cite specifics** — use dollar amounts, distances, response times, coverage limits where possible

Example of tone to AVOID:
> "Global Rescue delivers unparalleled, world-class rescue services with exceptional capabilities..."

Example of correct tone:
> "Global Rescue is the only provider in this comparison that deploys personnel to the point of injury — before a hospital is involved. That distinction matters most when you're injured in a remote area without reliable transport to a clinic."

---

## Provider Cards / Review Sections

Each provider should get a structured card or section with these elements — in this order:

1. **Provider name** (H3)
2. **Category badge** ("Best Overall", "Best for Seniors", etc.) — only if they win a category
3. **One-sentence verdict** — plain, specific, no fluff
4. **Essential Services score** — e.g. "3 of 5 essential services"
5. **Short prose review** — 2–4 sentences, editorial tone
6. **Feature mini-table or checklist** — Field Rescue, Medevac, Repatriation, Medical Advisory, Security Extraction
7. **"Best for:" line** — one sentence, specific traveler type
8. **Pricing note** — "Starting at ~$X" or "Annual from ~$X"

Keep Global Rescue's card at the top, expanded. All others can be collapsed or in a lighter treatment.

---

## Comparison Tables

- Use clean, simple HTML tables with minimal styling
- Sticky first column (provider name) on horizontal scroll
- Three visual states only: ✓ Full, ◐ Partial/Conditional, ✗ Not available
- Avoid emoji rating systems (🏅, 🟢, ⚠️) — use text + icon or simple symbols
- Mobile: allow horizontal scroll with a "scroll to see more →" hint

Preferred table style:
- Header row: GR brand navy background, white text
- Global Rescue row: light navy tint (#EBF3FF or similar), bold text
- Alternating row shading: white / very light gray
- Borders: subtle (1px #E2E8F0 or similar)

---

## Sticky Sidebar (Table of Contents)

- Appears on screens ≥1024px
- Sticky within the content area (not fixed to viewport)
- Contents: section links, current section highlighted
- Below TOC: a compact JOIN CTA box
  - "From $139/trip" pricing callout
  - "JOIN GLOBAL RESCUE" button (GR red, links to checkout)
  - 1–2 trust signals (no claims, no deductibles)

---

## Typography

**Source from Figma first.** If Figma extraction fails, use this fallback hierarchy:

```css
--font-heading: 'Barlow', sans-serif;   /* or whatever Figma specifies */
--font-body:    'Source Sans 3', sans-serif;
```

Sizes:
- H1: 36–42px, weight 700–800
- H2: 24–28px, weight 700
- H3: 18–20px, weight 600–700
- Body: 16–17px, weight 400, line-height 1.7
- Small/meta: 13–14px

---

## Color Usage

**Source exact values from Figma.** Expected GR palette (verify these):
- Primary navy: deep blue (~#0B2D5E range)
- CTA red: (~#C41230 range)
- Body text: near-black (~#1A2B45 range)
- Muted text: medium gray-blue (~#4A5B76 range)
- Page background: white
- Section alt background: very light blue-gray (~#F4F7FB range)
- Border: subtle (~rgba(0,0,0,0.08) range)

---

## Interactive Behavior

Keep these — they were working well:
- ✅ Accordion expand/collapse for provider reviews
- ✅ Table tab switcher (Essential 5 / Full 12-column)
- ✅ FAQ accordion
- ✅ Scroll-to-top button
- ✅ Active TOC highlighting via IntersectionObserver
- ✅ Smooth scroll offset for sticky header

Remove or simplify:
- ❌ Heavy CSS animations and transitions
- ❌ Complex hover effects
- ❌ The dot-pattern hero background
- ❌ Animated trust counters

---

## CTAs

**Primary CTA:** "JOIN GLOBAL RESCUE"
- Color: GR brand red
- URL: See `content/cta-links.md`
- Appears: In sidebar, at end of hero, in standalone CTA block before footer

**Secondary CTAs:** "Get a Quote" / "View Plans"
- Style: Outlined/ghost button in GR navy
- Used sparingly after provider review sections

---

## JSON-LD Structured Data

Must be included in `<head>`. See `content/structured-data.md` for all schemas:
- Organization
- Article
- FAQPage (10 Q&A pairs)
- ItemList (all 15 providers)
- BreadcrumbList

---

## Mobile Behavior

- Below 1024px: sidebar disappears, TOC becomes inline jump-links below hero
- Below 768px: provider cards stack vertically, comparison tables scroll horizontally
- Below 480px: hero H1 reduces to ~28px, padding tightens
- Touch targets: minimum 44×44px for all interactive elements

---

## Validation Checklist (before delivering)

- [ ] Opens in Chrome with no console errors
- [ ] All accordion expand/collapse works
- [ ] Table switcher works
- [ ] FAQs open/close
- [ ] JOIN button links to correct URL
- [ ] TOC links scroll to correct sections
- [ ] Page looks correct on 375px width (iPhone SE)
- [ ] Page looks correct on 1440px width (desktop)
- [ ] JSON-LD validates at schema.org/validator
- [ ] HTML validates (no unclosed tags)
