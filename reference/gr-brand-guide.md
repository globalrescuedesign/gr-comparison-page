# Global Rescue Brand Reference

Extracted from `Global Rescue Brand Guidlines.pdf` (15 pages, ©2024 Global Rescue LLC).

---

## Colors

| Role | Hex | RGB | Pantone | Notes |
|---|---|---|---|---|
| **Primary — GR Red** | `#d71635` | 215, 22, 53 | 199 C | Anchors the brand. Use for CTAs, accents, icons on white/grey. |
| Dark Red | `#910021` | 145, 0, 33 | 7427 C | Hover states, dark variants. |
| Storm Blue | `#406675` | 64, 102, 117 | 2180 C | Secondary. Use sparingly — graphs, contrast cells. |
| Arctic Blue | `#54c9fa` | 84, 201, 250 | 2985 C | Tertiary. Sparingly — only where contrast is needed. |
| Steel Grey | `#c2c7d1` | 194, 199, 209 | 538 C | Backgrounds, borders. |
| Almost Black | `#242126` | 36, 33, 38 | Neutral Black C | Body text, dark backgrounds. **Use this where you'd reach for navy.** |

**Proportions:** Red anchors; Almost Black + Steel Grey carry weight; Storm/Arctic Blue used sparsely.

**Audience tints:**
- Consumer: balanced, inspirational
- Channel partner: higher red + light grey for energizing feel
- Enterprise: more Almost Black + Storm Blue for serious/authoritative feel

---

## Typography

- **Roboto** — primary typeface for print and web
- **Roboto Condensed** — footers and accents only
- Print body: Roboto Light, 9pt / 13pt leading

Google Fonts:
- https://fonts.google.com/specimen/Roboto
- https://fonts.google.com/specimen/Roboto+Condensed

---

## Logo

- Logotype with plus icon in center
- Two-color preferred: GR Red + (Black or White), plus is filled white
- One-color variant: center of plus transparent
- **Never** place center of cross in red

**Don'ts (per pg 4):** off-brand colors, drop shadows/emboss, skew/stretch/rotate, unofficial graphics, encroaching text, two-color over colored background, low-contrast photo bg, bounding box on photo, red center.

---

## Voice & Style

- **Voice:** authoritative, well-researched, formal, straightforward. Conveys in-house expertise.
- **Tone:** shifts by audience (consumer vs. enterprise vs. channel partner), but voice is constant.
- **Style:** AP Style. Active voice. Concise. Short sentences.
- **Name:** "Global Rescue" — two words, both capitalized.

---

## Facts (for use in copy and JSON-LD)

- **Founded:** 2004
- **Headcount:** 250+ personnel
- **Operations centers:** 5 in 5 countries
- **Operations performed:** 20,000+ worldwide
- **Mission:** "the world's leading medical, security, evacuation, travel risk and crisis management services"
- **Medical partnership:** Exclusive relationship with **Johns Hopkins Department of Emergency Medicine Division of Special Operations**
- **Crises served:** Hezbollah/Israel war, Arab Spring, Haiti earthquake, Nepal earthquake, Hurricane Maria (Puerto Rico)
- **Operations staff include:** in-house paramedics, nurses, military special operations veterans
- **Trademarks:** Global Rescue, Travel Boldly, GRID, Signature Travel Insurance, TotalCare℠
- **Phone:** (800) 381-9754 · INTL +1 (617) 459-4200
- **Site:** www.globalrescue.com

---

## Photography direction

- Full color, candid feel
- Emotional connection — viewer feels part of the moment
- Should include "an element of risk or danger that the intended audience will connect with"
- **Avoid:** guns or dead animals in the foreground

---

## Reconciliation with current `global-rescue-landing.html` tokens

| Current variable | Current value | Brand-correct value | Action |
|---|---|---|---|
| `--red` | `#C8102E` | `#d71635` | Replace |
| `--red-dark` | `#A50C24` | `#910021` | Replace |
| `--navy` | `#0A2540` | `#242126` (Almost Black) | Replace; rename to `--ink-deep` |
| `--navy-deep` | `#061A30` | `#242126` | Consolidate |
| `--ink` | `#0F1E33` | `#242126` | Replace |
| `--text` | `#2A3447` | `#242126` (or rgba softer for body) | Replace |
| Font family (body) | Source Sans 3 | Roboto | Replace |
| Font family (display) | Source Serif 4 | Roboto / Roboto Condensed | Replace |

Add a `--storm` (`#406675`) and `--steel` (`#c2c7d1`) for secondary surfaces.
