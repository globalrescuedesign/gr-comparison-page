# Citation Plan — Per-Claim Source Attribution

Per Rebuilt-Priority-List Tier 1 #3: every comparative claim should carry an inline `<sup><a href="...">[n]</a></sup>` citation pointing to a primary source.

**Status:** proposed sources — placeholders where I'd otherwise be guessing URLs. Replace any `[verify URL]` entries with the canonical URL when convenient.

---

## Global Rescue (self-citations — high confidence)

| # | Claim | Proposed source |
|---|---|---|
| 1 | Founded 2004; mission language | GR Brand Guide pg 2 — internal, but mirrored on `https://www.globalrescue.com/about-us/` [verify URL] |
| 2 | 250+ personnel; 5 ops centers in 5 countries | GR Brand Guide pg 2 [verify URL — likely `https://www.globalrescue.com/about-us/`] |
| 3 | 20,000+ operations performed | GR Brand Guide pg 2 [verify — same URL or press kit] |
| 4 | Johns Hopkins Department of Emergency Medicine Division of Special Operations partnership | GR Brand Guide pg 12; JHU press release [verify URL] |
| 5 | Pricing — 7-day $139 / 45-day $349 / 90-day $455 | `https://www.globalrescue.com/personal/travelservices/` [verify URL] |
| 6 | High-Altitude Evacuation add-on | `https://www.globalrescue.com/lp/high-altitude-travel-evacuation/` |
| 7 | Student membership ($305–$805 / 45–365 days) | `https://www.globalrescue.com/personal/student/` [verify URL] |
| 8 | 2025 Skift IDEA Award — Industry Innovators: Business Travel | Skift announcement [verify URL] |
| 9 | 2024 Fast Company Most Innovative Company | Fast Company list [verify URL] |
| 10 | 2022 Inc. Best in Business | Inc. announcement [verify URL] |
| 11 | ISO 9001 certification | GR press release [verify URL] |

---

## Competitor capability claims (from Comparison Matrix)

| # | Claim | Proposed source |
|---|---|---|
| 12 | Medjet's 150-mile / hospital-of-choice / "bed-to-bed" rules | `https://medjetassist.com/Coverage/` [verify URL] |
| 13 | Medjet pricing $99 short-term, $315–$400 annual | Medjet pricing page [verify URL] |
| 14 | AirMed owned fleet of medically equipped aircraft | `https://www.airmed.com/about/` [verify URL] |
| 15 | EA+ — services begin after hospital admission | `https://www.emergencyassistanceplus.com/membership/how-it-works/` ✓ (URL surfaced in matrix) |
| 16 | EA+ pricing ~$229/year | EA+ membership page [verify URL] |
| 17 | DAN — global hyperbaric chamber network, dive-medicine specialists | `https://dan.org/travel-assist/` [verify URL] |
| 18 | GeoBlue Centers of Excellence; no search & rescue | `https://www.geobluetravelinsurance.com/` [verify URL] |
| 19 | International SOS — global medical/security; no technical SAR | `https://www.internationalsos.com/` [verify URL] |
| 20 | Seven Corners — adventure-sports rider required | Seven Corners plan docs [verify URL] |
| 21 | Travel Guard (AIG) — physician must certify evacuation | Travel Guard plan docs [verify URL] |
| 22 | Travelex — must reach a facility before evacuation authorized | Travelex plan docs [verify URL] |
| 23 | WorldTrips Atlas Travel — assistance center must approve | `https://www.worldtrips.com/atlas-travel-insurance` [verify URL] |
| 24 | Global Guardian — 150-mile / hospitalization required | Global Guardian product page [verify URL] |
| 25 | SkyMed — N. America/Caribbean regional focus | SkyMed coverage page [verify URL] |

---

## Credit card claims

| # | Claim | Proposed source |
|---|---|---|
| 26 | AMEX Platinum $695 annual fee; Premium Global Assist Hotline benefit | American Express Platinum benefits page [verify URL] |
| 27 | Chase Sapphire Reserve $550 annual fee; up to $100,000 evacuation | Chase benefits guide [verify URL] |
| 28 | Capital One Venture X $395 annual fee; reimbursement-based evacuation | Capital One benefits guide [verify URL] |

---

## Cost-of-evacuation claims

| # | Claim | Proposed source |
|---|---|---|
| 29 | Uninsured medevac costs $25,000–$300,000 | Industry reporting (e.g., HHS, Forbes, CNBC) [verify URL] |
| 30 | Helicopter medevac ~$60,000 | Industry reporting [verify URL] |
| 31 | Ground ambulance $5,000+ in remote regions | Industry reporting [verify URL] |

---

## Notes

- The matrix already surfaces one verified URL (EA+ how-it-works) — keep that as a model for the rest.
- For the `citation` array in the `Article` JSON-LD, every URL above becomes a `CreativeWork` entry, so AIs ingesting the schema see the full source list at once.
- When the user provides confirmed URLs, find/replace by reference number — every `[n]` superscript in the HTML maps to the table row of the same number.
