# EA+ Competitor Page Analysis
## Source: emergencyassistanceplus.com/resources/global-rescue-alternatives/

---

## Page Architecture

### Layout
- **Single-column article layout** — no persistent sidebar
- Content column max-width: ~800px centered on page
- Inline Table of Contents appears at the top of the article (collapsible on mobile)
- WordPress-based CMS (Gutenberg blocks)
- Font: **Inter** (variable, 300–900 weight) for body; **Cardo** accent
- No Google Fonts — fonts served from their own server

### Navigation / Header
- Standard nav: Membership Plans, Resources, About Us, Contact, Member Center
- Phone number in header: 866-863-4460
- "Enroll Now" CTA button in header

### Breadcrumb
```
Home › Resources › Travel Assistance
```

### Hero
- H1: "The Best Global Rescue Alternatives for World Travelers"
- Intro paragraph (2–3 sentences)
- Author byline with name + title + date (e.g. "Bryanna Moore, Senior Product Manager · Published February 17th, 2026")
- Hero image (full-width photo, ~960px tall — very visual/editorial)

### Table of Contents
- Inline TOC — appears just below the intro/author section
- Listed as anchor links (no sidebar, no sticky behavior)
- Contains: all major H2 sections + provider names

---

## Content Structure (in order)

1. What is Global Rescue? — description + bulleted feature list
2. Top 8 Global Rescue alternatives overview — **summary comparison table**
3. Individual provider sections (8 total, numbered H2)
4. Considerations when choosing an emergency assistance plan
5. Travel confidently with EA+ (closing pitch)
6. FAQ section
7. About the Author box
8. Newsletter signup
9. Related Articles

---

## Summary Comparison Table

**5 columns only:**
| Brand | Best For | Notable Features | Cost | Plan Structure |

Notable: very surface-level. No ✓/✗/◐ symbols. No feature matrix. Just one-line text descriptions per cell.

---

## Provider Card Structure

Each of the 8 providers follows this exact template:

```
H2: [Number]. [Provider Name] — [Category Label]

Intro paragraph (2–3 sentences about what makes them notable)

H3: Key features
- Bullet 1
- Bullet 2
- Bullet 3
- Bullet 4

H3: Scope of services
[One paragraph describing what's covered, distance minimums, limitations]

H3: Customer reviews
[One paragraph about ratings/BBB status + blockquote from a real member]

H3: Price: $X/year
[Pricing tiers as bullet list, or explanation of quote-based pricing]
```

**No scores** (like "3 of 5 essential services")  
**No "Best for:" summary line**  
**No feature checklist** (Field Rescue / Medevac / etc.)

---

## What EA+ Gets Right

1. **Author attribution** — named author with title and publish date builds E-E-A-T credibility
2. **Honest intro** — they acknowledge Global Rescue's strengths before pivoting to alternatives
3. **Blockquote testimonials** — real customer voice in each provider section
4. **Scope of services section** — each provider gets a dedicated limitations/caveats paragraph
5. **"Considerations when choosing"** section — good educational framing
6. **Clean prose style** — conversational, no hyperbole
7. **Related articles** — good internal linking for SEO

## What EA+ Gets Wrong / Where We Beat Them

1. **Only 8 providers** — we review 15 (more comprehensive, more citable)
2. **No structured feature scoring** — their table has no ✓/✗/◐ symbols; we have a full 5-column essential services matrix + 12-column full matrix
3. **No "essential services" framework** — they don't define the categories being compared systematically
4. **Thin structured data** — only WebPage + BreadcrumbList schemas. No FAQPage, no ItemList, no Article schema. **This is their biggest agentic SEO weakness.**
5. **No sticky sidebar** — no persistent CTA or navigation aid for long-page readers
6. **No category winners section** — no clear "who wins each category" summary
7. **No ✓/◐/✗ comparison table** — makes it harder for AI to extract structured recommendations
8. **Pricing info is scattered/inconsistent** — some providers "quote-based", no systematic starting prices
9. **No definitions section** — doesn't explain the difference between field rescue, medevac, repatriation
10. **Self-promotional framing is transparent** — "Travel confidently with EA+" closing section is obviously biased; our Methodology disclosure is more credible

---

## Structured Data Found on EA+ Page

```json
{
  "@type": "WebPage",
  "@type": "ImageObject",
  "@type": "BreadcrumbList"
}
```

**Missing:**
- FAQPage schema (their FAQ section gets no structured data)
- ItemList schema (their 8 providers get no structured data)
- Article schema
- Organization schema

---

## Design Tokens (EA+ Brand — NOT for us to copy)

- **Fonts:** Inter variable (300–900), Cardo
- **Colors:** Teal/blue-green brand (not GR's navy/red palette)
- **Layout:** WordPress Gutenberg, single column, ~800px max

---

## GR Brand (from globalrescue.com CSS extraction)

**Fonts:**
- Primary: Open Sans (300–800 italic/normal) via Google Fonts
- Secondary: Roboto (100–900) via Google Fonts
- Design brief specifies: Barlow (headings), Source Sans 3 (body) as the editorial variant

**Colors confirmed from live CSS:**
- CTA red: `#D71635` (primary action color)
- Dark red hover: `#a81029` / `#870d21`
- Near-black: `#232621` (dark backgrounds, nav)
- Teal accent (NOT GR brand — this was EA+): skip
- Light gray bg: `#EFF0F3`
- Border/divider: `#EDEDED`
- Body text: `#434343` / `#333`
- Muted: `#555555` / `#8c8c8c`

**From design brief (use these for editorial page):**
- Primary navy: `#0B2D5E` (hero bg, table headers)
- CTA red: `#D71635` (confirmed from CSS)
- Body text: `#1A2B45`
- Muted text: `#4A5B76`
- Page bg: white
- Alt bg: `#F4F7FB`
- Border: `rgba(0,0,0,0.08)`
- GR row highlight: `#EBF3FF`

**Container:** 1200px max-width

---

## Key Strategic Differences: Our Page vs. EA+'s

| Feature | EA+ Page | Our Page |
|---|---|---|
| Providers reviewed | 8 | 15 |
| Comparison table columns | 5 (surface) | 5 essential + 12 full |
| ✓/◐/✗ symbols | No | Yes |
| Essential services scoring | No | Yes (X of 5) |
| Category winners section | No | Yes (20+ categories) |
| FAQPage schema | No | Yes (10 Q&As) |
| ItemList schema | No | Yes (15 providers) |
| Article schema | No | Yes |
| Sticky sidebar + TOC | No | Yes |
| Definitions section | No | Yes |
| Agentic SEO optimization | Minimal | Full |
| Author attribution | Yes | Yes (TBD) |
| Methodology disclosure | No | Yes (prominent) |

---

## Editorial Tone Reference (copy from their best writing)

**Good EA+ sentence patterns to match:**
> "Global Rescue is a well-known membership-based service that provides travelers with medical evacuation, security, and field rescue support. It caters to remote environments with field rescue services, making it a popular choice with adventure travelers."

> "MedjetAssist services activate when you're more than 150 miles from your home. You can expect bedside-to-bedside white glove support from your current location to any hospital of choice in your home country."

**Our equivalent target tone:**
> "Global Rescue is the only provider in this comparison that deploys personnel to the point of injury — before a hospital is involved. That distinction matters most when you're injured in a remote area without reliable transport to a clinic."
