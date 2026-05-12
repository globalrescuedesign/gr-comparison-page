#!/usr/bin/env python3
"""
Global Rescue Comparison Page Generator
Outputs: global-rescue-comparison-FINAL.html
"""

# ── JOIN URL ──────────────────────────────────────────────────────────────────
JOIN_URL = ("https://ss.globalrescue.com/#/signup/step1?source=grcom"
            "&_gl=1*4wmr1l*_ga*MjAxNjYzMDAzOS4xNzczMTA5OTcy"
            "*_ga_Q05C49SZSQ*czE3NzcyOTc5ODAkbzU5JGcxJHQxNzc3Mjk4MDEzJGo2MCRsMCRoMjEwODMzNjYwOQ.."
            "*_gcl_aw*R0NMLjE3NzMxMDk5NzIuQ2owS0NRanczN25OQmhEa0FSSXNBRUJHSThQOFhNWHJrUHJhQk1WX1RKUzBVODlycHJObC1lVVZyVTdiQnA0cU1RcWtPMC1DZURYVW5QQWFBb25YRUFMd193Y0I."
            "*_gcl_au*MTQyNTEzMTQ5NC4xNzczMTA5OTcyLjcwMDE2Nzk2MC4xNzc0OTY4ODQ2LjE3NzQ5Njg4NDU.")

# ── CELL HELPER ───────────────────────────────────────────────────────────────
# Values: "best" | "yes" | "partial" | "no"
def cell(v):
    if v == "best":   return '<td><span class="c-best">✓ Best</span></td>'
    if v == "yes":    return '<td><span class="c-yes">✓</span></td>'
    if v == "partial":return '<td><span class="c-partial">◐</span></td>'
    return             '<td><span class="c-no">✗</span></td>'

def fcell(v):  # first-column (provider name)
    return f'<td class="col-provider">{v}</td>'

# ── ESSENTIAL SERVICES TABLE (5 cols) ─────────────────────────────────────────
# Columns: Field Rescue | Medevac | Repatriation | Medical Advisory | Security Extraction
ESSENTIAL = [
    # (name,          field,     medevac, repat,     advisory,  security,  is_gr)
    ("Global Rescue", "best",    "best",  "best",    "best",    "best",    True),
    ("AirMed Intl",   "no",      "best",  "yes",     "partial", "no",      False),
    ("AMEX Platinum", "partial", "best",  "partial", "partial", "partial", False),
    ("Capital One Venture X","no","partial","partial","partial","partial", False),
    ("DAN TravelAssist","no",    "best",  "yes",     "partial", "no",      False),
    ("EA+",           "no",      "yes",   "yes",     "partial", "no",      False),
    ("GeoBlue",       "no",      "yes",   "yes",     "best",    "partial", False),
    ("Global Guardian","no",     "best",  "partial", "partial", "partial", False),
    ("Intl SOS",      "partial", "best",  "partial", "best",    "partial", False),
    ("Medjet",        "no",      "yes",   "yes",     "no",      "no",      False),
    ("Seven Corners", "no",      "yes",   "yes",     "partial", "partial", False),
    ("SkyMed",        "no",      "yes",   "yes",     "partial", "no",      False),
    ("Travel Guard",  "no",      "yes",   "yes",     "partial", "partial", False),
    ("Travelex",      "no",      "yes",   "yes",     "partial", "partial", False),
    ("WorldTrips",    "no",      "yes",   "yes",     "partial", "partial", False),
]

# ── FULL FEATURE MATRIX (12 cols) ─────────────────────────────────────────────
# field | medevac | pay/claims | med-adv | travel-adv | sec-adv | repat | dest-intel | price-flex | security-ext | altitude | student
FULL = [
    ("Global Rescue",  "best","best","best","best","best","best","best","best","best","best","best","best", True),
    ("AirMed Intl",    "no","best","yes","partial","no","no","yes","no","partial","no","no","no",           False),
    ("AMEX Platinum",  "partial","best","partial","partial","partial","partial","partial","partial","no","no","no","no", False),
    ("Capital One",    "no","partial","partial","partial","no","partial","partial","no","no","no","no","no", False),
    ("DAN TravelAssist","no","best","yes","partial","partial","no","yes","partial","partial","no","no","partial", False),
    ("EA+",            "no","yes","yes","partial","no","no","yes","no","partial","no","no","no",             False),
    ("GeoBlue",        "no","yes","partial","best","best","partial","yes","best","best","no","no","partial", False),
    ("Global Guardian","no","best","yes","partial","no","partial","partial","no","partial","partial","no","no", False),
    ("Intl SOS",       "partial","best","partial","best","best","partial","partial","best","partial","partial","no","partial", False),
    ("Medjet",         "no","yes","yes","no","no","no","yes","no","yes","no","no","partial",                 False),
    ("Seven Corners",  "no","yes","partial","partial","partial","partial","yes","partial","best","no","no","best", False),
    ("SkyMed",         "no","yes","yes","partial","no","no","yes","no","partial","no","no","no",             False),
    ("Travel Guard",   "no","yes","partial","partial","partial","partial","yes","partial","yes","no","no","partial", False),
    ("Travelex",       "no","yes","partial","partial","partial","partial","yes","no","yes","no","no","no",   False),
    ("WorldTrips",     "no","yes","partial","partial","partial","partial","yes","partial","best","no","no","best", False),
]

# ── PROVIDER REVIEWS ──────────────────────────────────────────────────────────
# Each: id, name, badge, score, verdict, prose, features (list of (label, val)),
#       best_for, price, is_featured
PROVIDERS = [
  { "id": "global-rescue",
    "name": "Global Rescue",
    "badge": "Best Overall",
    "score": "5 of 5 essential services",
    "verdict": "Global Rescue is the only provider in this comparison that deploys personnel to the point of injury — before a hospital is involved.",
    "prose": ("Field rescue is conducted by teams that include in-house paramedics and Special Operations–trained personnel. "
              "Medical evacuation isn't dependent on hospitalization and can begin in the field. The service model is direct: "
              "no claims to file, no upfront costs, no insurance adjuster to satisfy before a helicopter is dispatched.<br><br>"
              "Medical advisory is available 24/7 through on-staff physicians who provide real-time guidance, treatment "
              "recommendations, and referrals to vetted facilities in 215 countries. Security extraction covers in-field "
              "evacuation from terrorism, civil unrest, natural disasters, and political instability. "
              "Founded in partnership with Johns Hopkins Medicine; serving over 1 million members since 2004."),
    "features": [("Field Rescue","best"),("Medical Evacuation","best"),("Repatriation","best"),
                 ("Medical Advisory","best"),("Security Extraction","best")],
    "best_for": "Adventure travelers, remote workers, students abroad, executives, families, organizations with duty-of-care obligations",
    "price": "From ~$139 (7-day individual) · ~$329 (annual individual) · High-altitude add-on from $495",
    "featured": True },

  { "id": "medjet",
    "name": "Medjet",
    "badge": "Runner-Up Overall",
    "score": "3 of 5 essential services",
    "verdict": "Medjet guarantees hospital-of-choice transport without claims — a strong, simple promise that covers the scenario most travelers actually face.",
    "prose": ("Medjet focuses exclusively on hospital-of-choice medical transport. Members must be hospitalized and stable "
              "before evacuation begins (150+ miles from home). No field rescue, no advisory services, no travel intelligence, "
              "no security evacuation. Entry from ~$99 short-term."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","no"),("Security Extraction","no")],
    "best_for": "Budget-conscious travelers who want a simple, no-claims guarantee of returning to their home hospital from a foreign hospitalization",
    "price": "From ~$99 (short-term) · ~$315–$400 (annual individual)",
    "featured": False },

  { "id": "airmed",
    "name": "AirMed International",
    "badge": "Best Hospital-to-Hospital Transport",
    "score": "2 of 5 essential services",
    "verdict": "AirMed owns its fleet of medically equipped aircraft with ICU-trained crews, giving it more clinical control over in-transit care than any other provider here.",
    "prose": ("Services begin only after hospitalization — there is no field rescue capability. The direct-pay model "
              "means no claims when properly coordinated. Does not offer travel advisory, security evacuation, or "
              "destination intelligence. Coverage is limited to US citizens and residents."),
    "features": [("Field Rescue","no"),("Medical Evacuation","best"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","no")],
    "best_for": "US travelers who prioritize clinical quality of in-transit care and accept that coverage begins post-hospitalization",
    "price": "Annual membership — contact for pricing",
    "featured": False },

  { "id": "amex",
    "name": "American Express Platinum",
    "badge": "Best Credit Card Option",
    "score": "2 of 5 essential services (conditional)",
    "verdict": "The most capable credit card option — conditional evacuation coordination through the Premium Global Assist Hotline, but every service requires pre-approval.",
    "prose": ("Coverage is bundled with the card and not structured as a standalone plan. Medical and travel advisory "
              "services are basic and third-party. Security evacuation and repatriation are available but restricted. "
              "If services aren't pre-coordinated, expect to pay upfront and file a reimbursement claim."),
    "features": [("Field Rescue","partial"),("Medical Evacuation","best"),("Repatriation","partial"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Cardholders traveling to established destinations who want a baseline safety net; should be supplemented with a dedicated membership for adventure or high-risk travel",
    "price": "Included with AMEX Platinum card (annual fee applies)",
    "featured": False },

  { "id": "chase",
    "name": "Chase Sapphire Reserve",
    "badge": "Runner-Up Credit Card",
    "score": "1 of 5 essential services",
    "verdict": "Up to $100,000 in evacuation coverage — but services are typically reimbursement-based unless pre-coordinated, and begin from a medical facility, not the field.",
    "prose": ("No field rescue, limited advisory access, and no security extraction. Advisory services are third-party "
              "and basic. Suitable only as a secondary safety net for routine international travel to established destinations."),
    "features": [("Field Rescue","no"),("Medical Evacuation","partial"),("Repatriation","partial"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Cardholders who want baseline evacuation coverage for routine international travel; not suitable as primary protection for adventure or remote travel",
    "price": "Included with Chase Sapphire Reserve card (annual fee applies)",
    "featured": False },

  { "id": "dan",
    "name": "DAN TravelAssist",
    "badge": "Best for Scuba Divers",
    "score": "2 of 5 essential services (specialized)",
    "verdict": "DAN's entire model is built around dive-specific risk — 24/7 dive medicine specialists and the world's only global hyperbaric chamber network.",
    "prose": ("DAN can coordinate evacuation from the point of injury if reachable, but does not conduct technical "
              "search-and-rescue. Medical advisory outside dive medicine is limited. Security evacuation is not offered. "
              "Should be supplemented with a broader rescue membership for non-diving travel scenarios."),
    "features": [("Field Rescue","no"),("Medical Evacuation","best"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","no")],
    "best_for": "Scuba divers, freedivers, and marine researchers",
    "price": "From ~$65/year (individual) — contact DAN for current rates",
    "featured": False },

  { "id": "eaplus",
    "name": "Emergency Assistance Plus (EA+)",
    "badge": "Best for Seniors",
    "score": "2 of 5 essential services",
    "verdict": "The simplest no-claims model at the lowest annual price — no age limits, no medical exam, straightforward get-home guarantee after hospitalization.",
    "prose": ("EA+ provides medical evacuation and repatriation after hospitalization. No field rescue capability. "
              "The no-claims, direct-pay model at ~$229/year is among the most affordable annual options in this comparison. "
              "Medical advisory is limited and coordination-based. No travel advisory, security evacuation, or destination intelligence."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","no")],
    "best_for": "Seniors and casual travelers who want a simple guarantee of getting home after a hospitalization, without complex claims processes",
    "price": "From ~$229/year (individual annual)",
    "featured": False },

  { "id": "geoblue",
    "name": "GeoBlue",
    "badge": "Runner-Up Medical Advisory",
    "score": "2 of 5 essential services",
    "verdict": "GeoBlue's curated global provider network and language-compatible physician access make it the strongest choice for travelers who prioritize in-country medical quality.",
    "prose": ("Medical evacuation is medically necessary and coordinated — typically from a facility rather than the field. "
              "Services may involve partial reimbursement depending on network use. Security evacuation is limited. "
              "Repatriation is medical-only. Commonly used for study abroad programs."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","best"),("Security Extraction","partial")],
    "best_for": "Travelers who prioritize access to a high-quality global medical provider network over field rescue or security extraction",
    "price": "Varies by plan — contact GeoBlue for current rates",
    "featured": False },

  { "id": "global-guardian",
    "name": "Global Guardian",
    "badge": "Enterprise Air Ambulance",
    "score": "2 of 5 essential services",
    "verdict": "Rapid air ambulance mobilization with a direct-pay model — best suited to corporate and high-net-worth clients who are less price-sensitive.",
    "prose": ("Air ambulance evacuation begins after hospitalization — no field rescue. Medical and travel advisory are "
              "limited. Security evacuation is coordinated rather than in-field extraction. Pricing is customized for "
              "enterprise clients."),
    "features": [("Field Rescue","no"),("Medical Evacuation","best"),("Repatriation","partial"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Corporate clients and high-net-worth individuals who want premium, customized service",
    "price": "Custom enterprise pricing — contact for quote",
    "featured": False },

  { "id": "isos",
    "name": "International SOS",
    "badge": "Enterprise Medical &amp; Security",
    "score": "2 of 5 essential services",
    "verdict": "Best-in-class global medical and security intelligence infrastructure — 13,000 worldwide experts — but not accessible to individual travelers at retail pricing.",
    "prose": ("ISOS delivers high-end evacuation from the point of illness or injury when reachable by standard transport "
              "— but does not perform technical search-and-rescue. Medical and travel advisory are best-in-class. "
              "Security evacuation is coordinated and robust, though not equivalent to field extraction."),
    "features": [("Field Rescue","partial"),("Medical Evacuation","best"),("Repatriation","partial"),
                 ("Medical Advisory","best"),("Security Extraction","partial")],
    "best_for": "Large corporations, NGOs, and universities with significant international travel programs",
    "price": "Custom enterprise subscription — contact for quote",
    "featured": False },

  { "id": "seven-corners",
    "name": "Seven Corners",
    "badge": "Most Flexible Insurance Pricing",
    "score": "2 of 5 essential services",
    "verdict": "The most flexible plan structure among insurance-based providers — single-trip, annual multi-trip, long-term, student, and expat options.",
    "prose": ("Insurance-based medical evacuation requiring medical necessity and claims. No field rescue. Advisory and "
              "security services limited and conditional. Security evacuation does not include operational extraction."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Budget-conscious travelers and students who need flexible, affordable international travel insurance",
    "price": "From ~$100–$250/trip (varies by age, destination, duration)",
    "featured": False },

  { "id": "skymed",
    "name": "SkyMed",
    "badge": "North America Regional Transport",
    "score": "2 of 5 essential services",
    "verdict": "Hospital-to-home transport primarily across North America — a solid no-claims option for continental travelers who rarely leave the region.",
    "prose": ("Services begin after hospitalization. Direct-pay model with no claims. No advisory, travel intelligence, "
              "or security services. Geographic scope limited to the US, Canada, Mexico, and select Caribbean destinations."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","no")],
    "best_for": "North American travelers on continental trips who want a simple, no-claims transport guarantee",
    "price": "From ~$795/year (individual) — discounts available",
    "featured": False },

  { "id": "travel-guard",
    "name": "Travel Guard (AIG)",
    "badge": "Flexible Insurance Coverage",
    "score": "2 of 5 essential services",
    "verdict": "Comprehensive travel insurance covering trip cancellation, delays, luggage, and basic medical evacuation — but all services are claims-based.",
    "prose": ("Insurance-based evacuation requiring medical necessity. No field rescue. Advisory and security services "
              "are limited and conditional. Commonly used through universities and institutions. Claims-based model throughout."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Travelers seeking comprehensive travel insurance covering trip cancellation, delays, luggage, and basic medical evacuation in a single policy",
    "price": "Quote-based — varies by trip, age, and coverage level",
    "featured": False },

  { "id": "travelex",
    "name": "Travelex Insurance",
    "badge": "Claims-Based Flexible Plans",
    "score": "2 of 5 essential services",
    "verdict": "Competitively priced travel insurance with a claims process — no frills, no field rescue, and no dedicated student program.",
    "prose": ("Insurance-based medical evacuation requiring prior medical evaluation and approval. Advisory services limited. "
              "Security evacuation conditional. Claims-based model throughout."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Travelers seeking competitively priced travel insurance with a straightforward claims process",
    "price": "Quote-based — varies by trip details",
    "featured": False },

  { "id": "worldtrips",
    "name": "WorldTrips (Atlas Travel)",
    "badge": "Best Student Insurance Alternative",
    "score": "2 of 5 essential services",
    "verdict": "Flexible travel medical insurance widely used in study abroad programs — affordable and adaptable, but reimbursement-based with no rescue or security capability.",
    "prose": ("Medically necessary and approval-based evacuation. May coordinate from point of illness if conditions "
              "are met, but does not provide true field rescue. Advisory and security services limited. "
              "Reimbursement model throughout."),
    "features": [("Field Rescue","no"),("Medical Evacuation","yes"),("Repatriation","yes"),
                 ("Medical Advisory","partial"),("Security Extraction","partial")],
    "best_for": "Students and budget travelers on study abroad programs who need affordable, flexible insurance and accept a claims-based model",
    "price": "From ~$1–$2/day (varies by age, destination, duration)",
    "featured": False },
]

# ── FAQS ──────────────────────────────────────────────────────────────────────
FAQS = [
  ("What is the difference between travel insurance and a medical evacuation membership?",
   "Travel insurance is a financial reimbursement product — it pays you back after a covered event, after you've filed a claim and provided documentation. A medical evacuation membership like Global Rescue is an operational service: it sends trained personnel to rescue you, coordinates evacuation, and transports you to the right hospital. No claims process, no deductibles, no prior authorization. Travel insurance requires you to reach a hospital before coverage activates. Global Rescue sends help from the point of injury or illness. The two products are complementary — most international travelers benefit from having both."),
  ("Does Global Rescue cover rescue from a mountain or remote wilderness?",
   "Yes. Global Rescue provides field rescue from the point of illness or injury, including remote wilderness and mountain environments. Standard memberships cover most remote environments. For rescues above 15,000 feet — Everest, Denali, Aconcagua — the High-Altitude Evacuation Package is required (starting at $495 for individuals). No other provider offers comparable technical rescue capability at extreme altitude."),
  ("Is AMEX Platinum or Chase Sapphire Reserve enough for medical evacuation?",
   "Credit card benefits are conditional and limited. AMEX Platinum requires pre-approval for evacuation services. Chase Sapphire Reserve is often reimbursement-based if not pre-coordinated, and services begin from a medical facility rather than the field. Neither provides true field rescue or security extraction. For adventure travel, remote destinations, or any high-risk travel, a dedicated evacuation membership is strongly recommended in addition to card benefits."),
  ("How much does a medical evacuation cost without coverage?",
   "An emergency medical evacuation by air ambulance can cost up to $300,000 depending on destination, aircraft type, and severity. A medevac helicopter costs approximately $60,000. Ground ambulance transport can run $5,000 or more for short distances in remote regions. A Global Rescue membership starting at $139 for a 7-day trip eliminates these costs for covered members. No claims, no deductibles, no upfront payment."),
  ("What does 'field rescue' mean, and which providers offer it?",
   "Field rescue means sending trained personnel to your actual location before a hospital is involved. Among the 15 providers reviewed here, Global Rescue is the only one that fully and consistently provides field rescue without preconditions. International SOS and AMEX Platinum offer limited or conditional field-adjacent response but do not deploy technical rescue teams to remote or extreme environments. All others begin services only after you've reached a medical facility."),
  ("Which provider is best for students studying abroad?",
   "Global Rescue for comprehensive protection — dedicated student memberships for full-time students under 35, flexible durations (45–365 days), all 5 essential services. WorldTrips for affordable insurance-based coverage widely used in study abroad programs — reimbursement model, no rescue or security capability. For complete protection, the best setup is a Global Rescue student membership paired with a travel insurance policy covering medical expenses and trip interruption."),
  ("What does Global Rescue cost?",
   "Memberships start at approximately $139 for a 7-day individual trip. Annual individual memberships start around $329. Family plans, multi-year plans, student memberships, and enterprise plans are available. The High-Altitude Package adds $495 (individual) or $995 (family). All services — field rescue, medevac, home hospital transport, 24/7 medical advisory, security extraction — are included with no additional claims, deductibles, or upfront costs for covered services."),
  ("What are the most common exclusions in rescue and evacuation plans?",
   "Pre-existing medical conditions (varies by plan), active war zones or conflict areas, extreme sports without an add-on, mountaineering above 15,000 feet without an altitude package, injuries related to alcohol or substance use, self-inflicted injuries, mental health crises (most insurance plans), and travel against official government advisories. Global Rescue is notably broader than insurance-based providers and does not treat COVID-19 differently from other medical emergencies. Always read the service terms — not just the marketing materials — before purchasing."),
  ("What is the difference between 'nearest hospital' and 'hospital of choice' transport?",
   "\"Nearest hospital\" means you're stabilized locally — potentially remaining in a foreign healthcare system for your recovery. \"Hospital of choice\" means your provider transports you to a specific hospital you select, typically in your home country, allowing continuity of care with your own physicians. Global Rescue, Medjet, and AirMed all offer hospital-of-choice transport. Most insurance plans and credit card benefits cover only the nearest medically appropriate facility."),
  ("Do I need both travel insurance and an evacuation membership?",
   "Yes, for most international travelers. Travel insurance covers financial losses — trip cancellation, lost luggage, medical expense reimbursement. An evacuation membership covers operational rescue — dispatching trained personnel to extract you and transport you to care. Global Rescue is not an insurance company and cannot reimburse trip costs or medical treatment expenses. The two products address different problems and work together to provide both immediate operational response and downstream financial protection."),
]

# ── CATEGORY WINNERS ─────────────────────────────────────────────────────────
WINNERS = [
  ("Best Overall",               "Global Rescue",       "Only provider delivering all 5 essential services with a direct, no-claims, in-field response model.", True),
  ("Runner-Up Overall",          "Medjet",              "Strong medical transport and repatriation. Simple, no-claims. Limited to post-hospitalization care.", False),
  ("Best Credit Card",           "AMEX Platinum",       "Most capable credit card option with direct coordination via Premium Global Assist Hotline.", False),
  ("Runner-Up Credit Card",      "Chase Sapphire Reserve","Up to $100,000 evacuation coverage. Reimbursement-based; facility-to-facility only.", False),
  ("Best Price / Full Coverage", "Global Rescue",       "From ~$139 (7-day). Only provider delivering all 5 essential services at any price point.", True),
  ("Lowest Annual Cost",         "EA+ (~$229/yr)",      "Limited to post-hospitalization medevac and repatriation. 2 of 5 essential services.", False),
  ("Lowest Short-Term Cost",     "Medjet (~$99)",       "3 of 5 essential services. Begins only after hospitalization.", False),
  ("Most Flexible Pricing",      "Global Rescue",       "7-day, 14-day, 30-day, annual, and multi-year. Individuals, families, students, enterprise.", True),
  ("Best for Scuba Divers",      "DAN TravelAssist",    "Only provider built around dive medicine. 24/7 dive medicine specialists, global hyperbaric network.", False),
  ("Best Medical Advisory",      "Global Rescue",       "24/7 on-staff physicians. Real-time guidance, referrals to vetted language-compatible facilities worldwide.", True),
  ("Best Travel Advisory",       "Global Rescue",       "Real-time location-specific intelligence across 215 countries. City-level granularity.", True),
  ("Best Security Extraction",   "Global Rescue",       "Only provider with true in-field extraction from active security threats.", True),
  ("Best High-Altitude",         "Global Rescue",       "Technical field rescue above 15,000 ft — Himalayas, Andes, Denali. No comparable runner-up.", True),
  ("Best for Seniors",           "EA+",                 "~$229/year, no claims, no age limits, straightforward benefits.", False),
  ("Best Hospital-to-Hospital",  "AirMed International","Owns its fleet of medically equipped aircraft. ICU-level care in transit.", False),
  ("Best for Students",          "Global Rescue",       "Dedicated student memberships for full-time students under 35. Durations 45–365 days. All 5 services.", True),
]

# ── TOC SECTIONS ──────────────────────────────────────────────────────────────
TOC = [
  ("#coverage",   "What Coverage Includes"),
  ("#winners",    "Category Winners"),
  ("#tables",     "Comparison Tables"),
  ("#reviews",    "Provider Reviews"),
  ("#credit-cards","Credit Card Benefits"),
  ("#how-to-choose","How to Choose"),
  ("#faq",        "FAQs"),
]

# ═════════════════════════════════════════════════════════════════════════════
# HTML RENDERER
# ═════════════════════════════════════════════════════════════════════════════

def render_essential_table():
    headers = ["Provider","Field Rescue","Medevac","Repatriation","Medical Advisory","Security Extraction"]
    rows = ""
    for r in ESSENTIAL:
        name, field, medevac, repat, adv, sec, is_gr = r
        cls = ' class="gr-row"' if is_gr else ""
        rows += f"<tr{cls}>{fcell(name)}{cell(field)}{cell(medevac)}{cell(repat)}{cell(adv)}{cell(sec)}</tr>\n"
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return f"""<div class="tbl-wrap"><table class="cmp-table">
<thead><tr>{ths}</tr></thead><tbody>{rows}</tbody></table></div>"""

def render_full_table():
    headers = ["Provider","Field Rescue","Medevac","Pay/Claims","Med Advisory","Travel Adv","Security Adv",
               "Repatriation","Dest Intel","Price Flex","Security Ext","High-Alt","Student"]
    rows = ""
    for r in FULL:
        name = r[0]; vals = r[1:13]; is_gr = r[13]
        cls = ' class="gr-row"' if is_gr else ""
        cells = "".join(cell(v) for v in vals)
        rows += f"<tr{cls}>{fcell(name)}{cells}</tr>\n"
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return f"""<div class="tbl-wrap"><table class="cmp-table">
<thead><tr>{ths}</tr></thead><tbody>{rows}</tbody></table></div>"""

def render_feature_row(label, val):
    icons = {"best": ("fi-best","✓","Best"),"yes": ("fi-yes","✓",""),"partial": ("fi-part","◐","Limited"),"no": ("fi-no","✗","")}
    cls, sym, tag = icons[val]
    badge = f' <span class="fi-tag">{tag}</span>' if tag else ""
    return f'<div class="feat-row"><span class="{cls}">{sym}</span> {label}{badge}</div>'

def render_provider_card(p):
    feats = "".join(render_feature_row(lbl, val) for lbl, val in p["features"])
    badge = f'<span class="prov-badge">{p["badge"]}</span>' if p.get("badge") else ""
    score_cls = "score-full" if p["score"].startswith("5") else "score-partial"
    if p["featured"]:
        return f"""<section id="{p['id']}" class="prov-featured" data-provider="{p['name']}">
  {badge}
  <h3>{p['name']}</h3>
  <p class="prov-verdict">{p['verdict']}</p>
  <span class="prov-score {score_cls}">{p['score']}</span>
  <div class="prov-prose">{p['prose']}</div>
  <div class="feat-grid">{feats}</div>
  <div class="prov-meta">
    <div><strong>Best for:</strong> {p['best_for']}</div>
    <div><strong>Pricing:</strong> {p['price']}</div>
  </div>
  <div class="prov-cta-row">
    <a href="{JOIN_URL}" class="btn-primary" target="_blank" rel="noopener">VIEW GLOBAL RESCUE PLANS</a>
  </div>
</section>"""
    else:
        return f"""<details class="prov-accordion" id="{p['id']}" data-provider="{p['name']}">
  <summary>
    <span class="prov-summary-name">{p['name']}</span>
    {f'<span class="prov-badge-sm">{p["badge"]}</span>' if p.get("badge") else ""}
    <span class="prov-score-sm {score_cls}">{p['score']}</span>
    <span class="accordion-chevron">&#8964;</span>
  </summary>
  <div class="prov-body">
    <p class="prov-verdict">{p['verdict']}</p>
    <div class="prov-prose">{p['prose']}</div>
    <div class="feat-grid">{feats}</div>
    <div class="prov-meta">
      <div><strong>Best for:</strong> {p['best_for']}</div>
      <div><strong>Pricing:</strong> {p['price']}</div>
    </div>
  </div>
</details>"""

def render_faq(i, q, a):
    return f"""<details class="faq-item">
  <summary class="faq-q">{q} <span class="faq-chev">&#8964;</span></summary>
  <div class="faq-a"><p>{a}</p></div>
</details>"""

def render_winner_card(label, name, reason, is_gr):
    cls = " wc-gr" if is_gr else ""
    return f"""<div class="winner-card{cls}">
  <div class="wc-label">{label}</div>
  <div class="wc-name">{name}</div>
  <div class="wc-reason">{reason}</div>
</div>"""

def render_toc_links(mobile=False):
    items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in TOC)
    return f'<ul class="toc-list">{items}</ul>'

# ── JSON-LD SCHEMAS ───────────────────────────────────────────────────────────
import json

faq_entities = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]
item_list = [{"@type":"ListItem","position":i+1,"name":p["name"],
              "description":f'{p["badge"]} — {p["verdict"]}'}
             for i,p in enumerate(PROVIDERS)]

SCHEMAS = [
  {"@context":"https://schema.org","@type":"Organization","name":"Global Rescue","alternateName":"Global Rescue LLC",
   "url":"https://www.globalrescue.com","logo":"https://www.globalrescue.com/grcom/grmkt_resources/images/GR-Logos/Global-Rescue-Logo-WR.svg",
   "foundingDate":"2004","description":"Global Rescue is a crisis response, medical evacuation and security extraction company providing field rescue from the point of illness or injury, 24/7 medical and travel advisory, security evacuation, and worldwide repatriation services. Founded in partnership with Johns Hopkins Medicine.",
   "sameAs":["https://www.linkedin.com/company/global-rescue","https://twitter.com/globalrescue","https://www.facebook.com/globalrescue","https://en.wikipedia.org/wiki/Global_Rescue"],
   "award":["2025 Skift IDEA Award — Industry Innovators: Business Travel","2024 Fast Company Most Innovative Company","2022 Inc. Magazine Best in Business","2022 ISO 9001 Certified"]},

  {"@context":"https://schema.org","@type":"Article",
   "headline":"Best Travel Insurance for Rescue and Medical Evacuation",
   "description":"A comprehensive comparison of 15 providers offering emergency rescue, medical evacuation, and travel protection — evaluated across field rescue capability, medevac, repatriation, medical advisory, security extraction, and pricing.",
   "dateModified":"2025-05-01","datePublished":"2025-01-01",
   "publisher":{"@type":"Organization","name":"Global Rescue","url":"https://www.globalrescue.com"},
   "mainEntityOfPage":{"@type":"WebPage","@id":"https://www.globalrescue.com/resources/best-travel-insurance-rescue-medical-evacuation/"},
   "about":[{"@type":"Thing","name":"Medical Evacuation"},{"@type":"Thing","name":"Field Rescue"},{"@type":"Thing","name":"Travel Insurance"},{"@type":"Thing","name":"Security Evacuation"},{"@type":"Thing","name":"Travel Protection Membership"}]},

  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq_entities},

  {"@context":"https://schema.org","@type":"ItemList",
   "name":"Best Travel Insurance for Rescue and Medical Evacuation — Provider Rankings",
   "numberOfItems":15,"itemListElement":item_list},

  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.globalrescue.com"},
    {"@type":"ListItem","position":2,"name":"Resources","item":"https://www.globalrescue.com/common/blog/"},
    {"@type":"ListItem","position":3,"name":"Travel Insurance","item":"https://www.globalrescue.com/common/blog/"},
    {"@type":"ListItem","position":4,"name":"Best Travel Insurance for Rescue & Medical Evacuation"}
  ]},
]

schema_tags = "\n".join(
    f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
    for s in SCHEMAS)

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
:root{--red:#d71635;--red-dk:#910021;--dark:#242126;--storm:#406675;--arctic:#54c9fa;--steel:#c2c7d1;
--text:#2d2d2d;--muted:#406675;--bg:#fff;--bg2:#f7f8f9;--border:#e0e3e8;--radius:6px;
--font-h:'Roboto Condensed',sans-serif;--font-b:'Roboto',sans-serif;--hdr:60px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-b);color:var(--text);background:var(--bg);font-size:16px;line-height:1.7}
a{color:var(--red);text-decoration:none}a:hover{text-decoration:underline}
h1,h2,h3,h4,h5{font-family:var(--font-h);font-weight:700;line-height:1.25}
p{margin:0 0 .9rem}ul,ol{margin:0 0 .9rem 1.3rem}li{margin-bottom:.25rem}
/* HEADER */
.site-hdr{background:var(--dark);height:var(--hdr);display:flex;align-items:center;
  position:sticky;top:0;z-index:100;border-bottom:3px solid var(--red)}
.hdr-in{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;gap:28px;width:100%}
.hdr-logo img{height:30px;display:block}
.hdr-nav{display:flex;gap:20px;list-style:none;margin-left:8px}
.hdr-nav a{color:rgba(255,255,255,.82);font-size:.875rem;font-weight:500}
.hdr-nav a:hover{color:#fff;text-decoration:none}
.hdr-join{margin-left:auto}
.btn-join{background:var(--red);color:#fff;padding:8px 20px;border-radius:4px;font-weight:700;
  font-size:.85rem;letter-spacing:.05em;font-family:var(--font-h);display:inline-block}
.btn-join:hover{background:var(--red-dk);text-decoration:none}
/* HERO */
.hero{background:var(--dark);padding:40px 24px 32px}
.hero-in{max-width:1200px;margin:0 auto}
.hero-bc{font-size:.78rem;color:rgba(255,255,255,.45);margin-bottom:14px}
.hero-bc a{color:rgba(255,255,255,.6)}.hero-bc a:hover{color:#fff}
.hero-bc span{margin:0 5px}
.hero h1{color:#fff;font-size:2.1rem;max-width:780px;margin-bottom:12px;line-height:1.2}
.hero-sub{color:var(--steel);font-size:1rem;max-width:680px;margin-bottom:18px;line-height:1.6}
.hero-meta{display:flex;gap:16px;align-items:center;flex-wrap:wrap;font-size:.8rem;color:rgba(255,255,255,.45)}
.hero-meta a{color:var(--arctic);font-weight:500}.hero-meta a:hover{text-decoration:underline}
.hero-meta .dot{color:rgba(255,255,255,.25)}
/* MOB TOC */
.mob-toc{background:var(--bg2);border-bottom:1px solid var(--border);padding:12px 24px;display:none}
.mob-toc-btn{background:none;border:none;font-weight:700;font-size:.88rem;cursor:pointer;
  color:var(--dark);display:flex;align-items:center;gap:6px;font-family:var(--font-h)}
.mob-toc-links{display:none;padding-top:10px}
.mob-toc-links.open{display:block}
.mob-toc-links a{display:block;padding:5px 0;font-size:.85rem;color:var(--storm);
  border-bottom:1px solid var(--border)}
/* LAYOUT */
.outer{max-width:1200px;margin:0 auto;padding:0 24px}
.layout{display:flex;gap:56px;align-items:flex-start;padding:40px 0 72px}
.content{flex:1;min-width:0;max-width:760px}
.sidebar{width:272px;flex-shrink:0;position:sticky;top:calc(var(--hdr) + 20px)}
/* METHODOLOGY */
.method-box{border-left:4px solid var(--red);background:var(--bg2);padding:18px 22px;
  margin-bottom:40px;border-radius:0 var(--radius) var(--radius) 0}
.method-box h4{font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--red);margin-bottom:7px}
.method-box p{font-size:.9rem;color:#444;margin-bottom:6px}
.method-crit{font-size:.83rem;color:var(--muted);line-height:1.7}
/* SECTION HEADINGS */
.sec-h{display:flex;align-items:baseline;gap:10px;margin:48px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--red)}
.sec-h h2{font-size:1.5rem;color:var(--dark);margin:0}
.sec-num{font-size:.75rem;font-weight:700;color:var(--red);letter-spacing:.1em;text-transform:uppercase;font-family:var(--font-h)}
/* DEFINITIONS */
.def-block{margin-bottom:24px;padding-bottom:24px;border-bottom:1px solid var(--border)}
.def-block:last-child{border-bottom:none}
.def-block h3{font-size:1rem;margin-bottom:6px;color:var(--dark)}
.def-block p{font-size:.93rem;color:#444;margin:0}
/* TYPE COMPARISON */
.type-tbl{width:100%;border-collapse:collapse;font-size:.88rem;margin:20px 0 28px}
.type-tbl th{background:var(--dark);color:#fff;padding:9px 12px;text-align:left;font-weight:700;font-size:.82rem}
.type-tbl td{padding:8px 12px;border-bottom:1px solid var(--border);vertical-align:top}
.type-tbl tr:nth-child(even) td{background:var(--bg2)}
.type-tbl .t-hd{font-weight:700;color:var(--dark)}
.type-tbl li{font-size:.82rem;margin-bottom:.2rem}
/* EXCLUSIONS */
.excl-list{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);
  padding:16px 20px;font-size:.88rem;color:#444;margin-top:12px}
.excl-list h4{font-size:.8rem;text-transform:uppercase;letter-spacing:.07em;color:var(--storm);margin-bottom:8px}
/* WINNERS GRID */
.winners-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 24px}
.winner-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:12px 14px}
.winner-card.wc-gr{border-color:var(--red);border-left:4px solid var(--red)}
.wc-label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;
  color:var(--storm);margin-bottom:3px;font-family:var(--font-h)}
.winner-card.wc-gr .wc-label{color:var(--red)}
.wc-name{font-weight:700;color:var(--dark);font-size:.92rem;margin-bottom:2px;font-family:var(--font-h)}
.wc-reason{font-size:.8rem;color:#555;line-height:1.45}
/* TABLE TABS */
.tbl-tabs{display:flex;gap:4px;margin-bottom:12px;border-bottom:2px solid var(--border)}
.tbl-tab{background:none;border:none;padding:9px 18px;font-weight:700;font-size:.88rem;cursor:pointer;
  color:var(--muted);border-bottom:3px solid transparent;margin-bottom:-2px;font-family:var(--font-b)}
.tbl-tab.on{color:var(--red);border-color:var(--red)}
.tbl-panel{display:none}.tbl-panel.on{display:block}
.tbl-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.scroll-hint{font-size:.75rem;color:var(--muted);text-align:right;margin-bottom:5px}
.tbl-legend{font-size:.78rem;color:var(--muted);margin-top:8px;display:flex;gap:14px;flex-wrap:wrap}
.tbl-legend span{display:flex;align-items:center;gap:3px}
/* COMPARISON TABLE */
.cmp-table{width:100%;border-collapse:collapse;font-size:.84rem;min-width:520px}
.cmp-table th{background:var(--dark);color:#fff;padding:9px 11px;text-align:center;
  font-weight:700;font-size:.78rem;white-space:nowrap}
.cmp-table th:first-child{text-align:left;position:sticky;left:0;z-index:2;background:var(--dark)}
.cmp-table td{padding:8px 11px;text-align:center;border-bottom:1px solid var(--border)}
.cmp-table td.col-provider{text-align:left;font-weight:600;white-space:nowrap;font-size:.85rem;
  position:sticky;left:0;background:#fff;z-index:1;border-right:2px solid var(--border)}
.cmp-table tr.gr-row td{background:#fff8f8!important;font-weight:700}
.cmp-table tr.gr-row td.col-provider{background:#fff8f8!important}
.cmp-table tr:nth-child(even) td{background:var(--bg2)}
.cmp-table tr:nth-child(even) td.col-provider{background:var(--bg2)}
.c-best{color:#006400;font-weight:700;font-size:.82rem;display:inline-flex;align-items:center;gap:2px}
.c-yes{color:#2a7a2a;font-weight:600}
.c-partial{color:#b56c00}
.c-no{color:#bbb}
/* PROVIDER CARDS */
.prov-featured{background:var(--bg2);border:2px solid var(--red);border-radius:var(--radius);
  padding:26px 26px 18px;margin-bottom:10px}
.prov-accordion{border:1px solid var(--border);border-radius:var(--radius);margin-bottom:8px;overflow:hidden}
.prov-accordion summary{display:flex;align-items:center;gap:10px;padding:14px 18px;cursor:pointer;
  background:#fff;list-style:none;justify-content:space-between}
.prov-accordion summary::-webkit-details-marker{display:none}
.prov-accordion summary:hover{background:var(--bg2)}
.prov-summary-name{font-family:var(--font-h);font-weight:700;font-size:1rem;color:var(--dark)}
.accordion-chevron{color:var(--storm);font-size:1.1rem;transition:transform .2s;margin-left:auto}
.prov-accordion[open] .accordion-chevron{transform:rotate(180deg)}
.prov-body{padding:18px 22px 14px;border-top:1px solid var(--border)}
.prov-badge{display:inline-flex;background:var(--red);color:#fff;font-size:.7rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.07em;padding:3px 9px;border-radius:3px;margin-bottom:10px;
  font-family:var(--font-h)}
.prov-badge-sm{display:inline-flex;background:var(--red);color:#fff;font-size:.65rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;padding:2px 7px;border-radius:3px;font-family:var(--font-h)}
.prov-verdict{font-size:.97rem;font-weight:600;color:var(--dark);border-left:3px solid var(--red);
  padding-left:11px;margin-bottom:14px;line-height:1.55}
.prov-score{display:inline-flex;align-items:center;background:var(--dark);color:#fff;font-size:.75rem;
  font-weight:700;padding:3px 11px;border-radius:20px;margin-bottom:12px;font-family:var(--font-h);letter-spacing:.04em}
.prov-score-sm{display:inline-flex;background:#e8f4e8;color:#2a7a2a;font-size:.7rem;font-weight:700;
  padding:2px 8px;border-radius:20px;font-family:var(--font-h)}
.score-partial{background:var(--bg2)!important;color:var(--storm)!important}
.prov-prose{font-size:.92rem;color:#444;margin-bottom:14px;line-height:1.65}
.feat-grid{display:grid;grid-template-columns:1fr 1fr;gap:4px 16px;margin-bottom:14px;font-size:.86rem}
.feat-row{display:flex;align-items:center;gap:6px;padding:3px 0}
.fi-best{color:#006400;font-weight:700}.fi-yes{color:#2a7a2a;font-weight:600}
.fi-part{color:#b56c00}.fi-no{color:#ccc}
.fi-tag{font-size:.65rem;background:#006400;color:#fff;padding:1px 5px;border-radius:2px;margin-left:2px}
.prov-meta{font-size:.85rem;display:flex;flex-direction:column;gap:6px;padding-top:12px;
  border-top:1px solid var(--border)}
.prov-meta strong{color:var(--dark)}
.prov-cta-row{margin-top:16px}
.btn-primary{display:inline-block;background:var(--red);color:#fff;padding:10px 22px;border-radius:4px;
  font-weight:700;font-size:.85rem;letter-spacing:.05em;font-family:var(--font-h)}
.btn-primary:hover{background:var(--red-dk);text-decoration:none}
/* FAQ */
.faq-item{border-bottom:1px solid var(--border)}
.faq-item summary{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;
  padding:15px 0;cursor:pointer;list-style:none;font-family:var(--font-h);font-weight:700;
  font-size:.93rem;color:var(--dark)}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary:hover{color:var(--red)}
.faq-chev{flex-shrink:0;transition:transform .2s;color:var(--storm);font-size:1.1rem;margin-top:1px}
.faq-item[open] .faq-chev{transform:rotate(180deg)}
.faq-a{padding:0 0 15px;font-size:.9rem;color:#444;line-height:1.7}
/* CREDIT CARDS */
.cc-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0}
.cc-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:18px 20px}
.cc-card h3{font-size:1rem;margin-bottom:10px}
.cc-card dl{font-size:.88rem}
.cc-card dt{font-weight:700;color:var(--dark);margin-top:8px}
.cc-card dd{color:#444;margin:1px 0 0 0}
.cc-verdict{background:#fff8e8;border:1px solid #e8c840;border-radius:var(--radius);
  padding:14px 18px;font-size:.9rem;margin-top:16px;line-height:1.6}
/* HOW TO CHOOSE */
.profile-grid{display:grid;gap:10px;margin-bottom:24px}
.profile-row{display:flex;gap:12px;padding:12px 14px;background:var(--bg2);border-radius:var(--radius);
  border-left:3px solid var(--red);font-size:.9rem}
.prof-type{font-weight:700;color:var(--dark);min-width:200px;font-family:var(--font-h)}
.prof-rec{color:#444}
.q-item{border-bottom:1px solid var(--border);padding:14px 0}
.q-item:last-child{border-bottom:none}
.q-item h3{font-size:.93rem;color:var(--dark);margin-bottom:7px}
.q-item p{font-size:.9rem;color:#444;margin:0}
/* SIDEBAR */
.sb-toc{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:18px;margin-bottom:18px}
.sb-toc h4{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--storm);margin-bottom:10px;font-family:var(--font-h)}
.toc-list{list-style:none;margin:0;padding:0}
.toc-list a{display:block;padding:5px 8px;font-size:.83rem;color:var(--muted);border-radius:4px;
  border-left:2px solid transparent;margin-bottom:1px}
.toc-list a:hover,.toc-list a.active{color:var(--red);border-color:var(--red);background:#fff8f8;text-decoration:none}
.sb-cta{background:var(--dark);border-radius:var(--radius);padding:20px;color:#fff}
.sc-from{font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--steel);margin-bottom:3px;font-family:var(--font-h)}
.sc-price{font-size:1.7rem;font-weight:900;color:#fff;line-height:1;margin-bottom:3px;font-family:var(--font-h)}
.sc-price small{font-size:.85rem;font-weight:400;color:var(--steel)}
.sc-join{display:block;text-align:center;background:var(--red);color:#fff;padding:11px;border-radius:4px;
  font-weight:700;font-family:var(--font-h);letter-spacing:.06em;margin:12px 0 10px;font-size:.88rem}
.sc-join:hover{background:var(--red-dk);text-decoration:none}
.sc-trusts{list-style:none;font-size:.76rem;color:var(--steel);margin:0;padding:0}
.sc-trusts li{padding:2px 0}.sc-trusts li::before{content:'✓ ';color:var(--arctic)}
/* CTA BLOCK */
.cta-blk{background:var(--dark);padding:56px 24px;text-align:center}
.cta-blk h2{color:#fff;font-size:1.9rem;margin-bottom:8px}
.cta-blk .cta-sub{color:var(--steel);font-size:.97rem;max-width:580px;margin:0 auto 26px}
.price-grid{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-bottom:26px}
.p-item{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:var(--radius);
  padding:12px 18px;min-width:130px}
.p-item .pi-lbl{font-size:.72rem;color:var(--steel);text-transform:uppercase;letter-spacing:.07em;margin-bottom:3px;font-family:var(--font-h)}
.p-item .pi-price{font-size:1.2rem;font-weight:700;color:#fff;font-family:var(--font-h)}
.btn-join-lg{display:inline-block;background:var(--red);color:#fff;padding:15px 40px;border-radius:4px;
  font-weight:700;font-size:1rem;letter-spacing:.06em;font-family:var(--font-h);margin-bottom:14px}
.btn-join-lg:hover{background:var(--red-dk);text-decoration:none}
.cta-disclaimer{font-size:.76rem;color:rgba(255,255,255,.35);max-width:560px;margin:0 auto 22px}
.trust-row{display:flex;justify-content:center;gap:18px;flex-wrap:wrap;font-size:.78rem;color:var(--steel)}
.trust-row span::before{content:'✓ ';color:var(--arctic)}
/* FOOTER */
.site-ftr{background:#1a1a1a;padding:40px 24px 24px}
.ftr-in{max-width:1200px;margin:0 auto}
.ftr-top{display:flex;gap:40px;margin-bottom:28px;flex-wrap:wrap;align-items:flex-start}
.ftr-brand{flex-shrink:0}
.ftr-brand img{height:26px;display:block;margin-bottom:10px}
.ftr-tagline{font-size:.82rem;color:#666}
.ftr-links{display:flex;gap:28px;flex-wrap:wrap}
.ftr-links a{color:#666;font-size:.83rem}.ftr-links a:hover{color:#fff}
.ftr-bottom{border-top:1px solid #2a2a2a;padding-top:18px}
.ftr-legal{font-size:.75rem;color:#444;line-height:1.65;margin-bottom:10px}
.ftr-disc{font-size:.75rem;color:#444}
/* SCROLL TOP */
.scr-top{position:fixed;bottom:22px;right:22px;background:var(--red);color:#fff;border:none;
  width:42px;height:42px;border-radius:50%;cursor:pointer;display:none;align-items:center;
  justify-content:center;z-index:50;font-size:1.1rem}
.scr-top.show{display:flex}.scr-top:hover{background:var(--red-dk)}
/* RESPONSIVE */
@media(max-width:1040px){.sidebar{display:none}.mob-toc{display:block}.content{max-width:100%}.layout{padding:28px 0 48px}}
@media(max-width:768px){.hero h1{font-size:1.65rem}.winners-grid{grid-template-columns:1fr}
  .cc-grid{grid-template-columns:1fr}.feat-grid{grid-template-columns:1fr}
  .profile-row{flex-direction:column;gap:4px}.prof-type{min-width:auto}}
@media(max-width:480px){.hero h1{font-size:1.4rem}.hero{padding:24px 16px 20px}.outer{padding:0 16px}
  .price-grid{gap:8px}}
"""

# ── JS ────────────────────────────────────────────────────────────────────────
JS = """
// Table tabs
document.querySelectorAll('.tbl-tab').forEach(tab=>{
  tab.addEventListener('click',()=>{
    const grp = tab.closest('.tbl-section');
    grp.querySelectorAll('.tbl-tab').forEach(t=>t.classList.remove('on'));
    grp.querySelectorAll('.tbl-panel').forEach(p=>p.classList.remove('on'));
    tab.classList.add('on');
    grp.querySelector('#'+tab.dataset.panel).classList.add('on');
  });
});
// Mobile TOC toggle
const mobBtn = document.querySelector('.mob-toc-btn');
const mobLinks = document.querySelector('.mob-toc-links');
if(mobBtn) mobBtn.addEventListener('click',()=>mobLinks.classList.toggle('open'));
// Active TOC
const tocLinks = document.querySelectorAll('.toc-list a');
const sections = Array.from(tocLinks).map(a=>document.querySelector(a.getAttribute('href')));
const obs = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      tocLinks.forEach(a=>a.classList.remove('active'));
      const lnk = document.querySelector('.toc-list a[href="#'+e.target.id+'"]');
      if(lnk) lnk.classList.add('active');
    }
  });
},{rootMargin:'-20% 0px -70% 0px'});
sections.forEach(s=>{if(s) obs.observe(s)});
// Scroll top
const scrBtn = document.querySelector('.scr-top');
window.addEventListener('scroll',()=>scrBtn.classList.toggle('show', window.scrollY>400));
scrBtn.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
"""

# ── ASSEMBLE HTML ─────────────────────────────────────────────────────────────
providers_html = "\n".join(render_provider_card(p) for p in PROVIDERS)
faqs_html = "\n".join(render_faq(i, q, a) for i,(q,a) in enumerate(FAQS))
winners_html = "\n".join(render_winner_card(*w) for w in WINNERS)
toc_sidebar = render_toc_links()
toc_mobile = render_toc_links(mobile=True)
ess_table = render_essential_table()
full_table = render_full_table()

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Best Travel Insurance for Rescue &amp; Medical Evacuation (2025) | Global Rescue</title>
<meta name="description" content="Compare the top providers for emergency rescue and medical evacuation. Global Rescue vs Medjet, AirMed, GeoBlue, DAN, and 11 others — honest reviews across 12 criteria.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.globalrescue.com/resources/best-travel-insurance-rescue-medical-evacuation/">
<meta property="og:title" content="Best Travel Insurance for Rescue &amp; Medical Evacuation (2025)">
<meta property="og:description" content="The most comprehensive side-by-side comparison of rescue and medical evacuation providers — reviewed across 12 criteria.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.globalrescue.com/resources/best-travel-insurance-rescue-medical-evacuation/">
<meta property="og:site_name" content="Global Rescue">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@GlobalRescue">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Roboto+Condensed:wght@400;700;800&display=swap" rel="stylesheet">
{schema_tags}
<style>{CSS}</style>
</head>
<body>

<!-- HEADER -->
<header class="site-hdr">
  <div class="hdr-in">
    <a class="hdr-logo" href="https://www.globalrescue.com" aria-label="Global Rescue home">
      <img src="https://www.globalrescue.com/grcom/grmkt_resources/images/GR-Logos/Global-Rescue-Logo-WR.svg" alt="Global Rescue" width="160" height="30">
    </a>
    <nav aria-label="Primary"><ul class="hdr-nav">
      <li><a href="https://www.globalrescue.com/personal/travelservices/">Personal Travel</a></li>
      <li><a href="https://www.globalrescue.com/enterprise/">Enterprise</a></li>
      <li><a href="https://www.globalrescue.com/common/blog/">Resources</a></li>
    </ul></nav>
    <div class="hdr-join">
      <a href="{JOIN_URL}" class="btn-join" target="_blank" rel="noopener">JOIN</a>
    </div>
  </div>
</header>

<!-- HERO -->
<div class="hero">
  <div class="hero-in">
    <nav aria-label="Breadcrumb" class="hero-bc">
      <a href="https://www.globalrescue.com">Home</a><span>›</span>
      <a href="https://www.globalrescue.com/common/blog/">Resources</a><span>›</span>
      <a href="https://www.globalrescue.com/common/blog/">Travel Insurance</a><span>›</span>
      <span>Best Travel Insurance for Rescue &amp; Medical Evacuation</span>
    </nav>
    <h1>The Best Travel Insurance for Rescue and Medical Evacuation</h1>
    <p class="hero-sub">Compare the top providers offering emergency rescue, medical evacuation, security extraction, and global travel protection — reviewed across 12 capability criteria.</p>
    <div class="hero-meta">
      <span>Published by <strong style="color:rgba(255,255,255,.7)">Global Rescue</strong></span>
      <span class="dot">·</span>
      <span>Last updated May 2025</span>
      <span class="dot">·</span>
      <span>15 providers reviewed</span>
      <span class="dot">·</span>
      <a href="#tables">Jump to comparison tables ↓</a>
    </div>
  </div>
</div>

<!-- MOBILE TOC -->
<div class="mob-toc" aria-label="Page navigation">
  <button class="mob-toc-btn" aria-expanded="false">☰ On this page</button>
  <div class="mob-toc-links">{toc_mobile}</div>
</div>

<!-- PAGE LAYOUT -->
<div class="outer">
<div class="layout">

  <!-- MAIN CONTENT -->
  <main class="content" id="main">

    <!-- METHODOLOGY -->
    <div class="method-box">
      <h4>Disclosure &amp; Methodology</h4>
      <p>This comparison is published by <strong>Global Rescue</strong>, the company rated Best Overall in this analysis. We acknowledge that as the publisher, we have a vested interest in this ranking. To maintain credibility, we applied objective, publicly verifiable criteria to every provider equally — including ourselves. Where another provider genuinely leads a category (DAN for dive medicine, EA+ for senior simplicity, AirMed for ICU-level air transport), we say so explicitly.</p>
      <p>Each provider was evaluated across five essential service dimensions and seven supplementary criteria using publicly available service terms, industry publications, and direct service documentation. No provider paid for inclusion or placement.</p>
      <div class="method-crit"><strong>Criteria evaluated:</strong> Field Rescue · Medical Evacuation · Repatriation · Medical Advisory · Security Extraction · Travel Advisory · Pricing Flexibility · Destination Intelligence · Pay/Claims Model · Security Advisory · High-Altitude Capability · Student Pricing</div>
    </div>

    <!-- SECTION 1: WHAT COVERAGE INCLUDES -->
    <section id="coverage">
      <div class="sec-h"><span class="sec-num">Section 1</span><h2>What Medical Evacuation &amp; Rescue Coverage Includes</h2></div>
      <p>Not all "evacuation coverage" is the same. Understanding the difference between these core service types is essential before comparing providers — and especially before you need to use one.</p>

      <div class="def-block">
        <h3>Field Rescue / Extraction</h3>
        <p>Trained personnel — paramedics, military special operations veterans, or technical rescue teams — are dispatched to your actual location before any hospital or clinic is involved. This applies in remote wilderness, at altitude, at sea, or in conflict zones. Very few providers offer true field rescue. Most begin services only after you've reached a medical facility.</p>
      </div>
      <div class="def-block">
        <h3>Medical Evacuation (Medevac)</h3>
        <p>Coordinated transport — by air ambulance, commercial flight with medical escort, or ground ambulance — from a medical facility to a higher-level care center or your home country. Most providers define medevac as beginning once you are admitted to a local hospital. Uninsured evacuations cost between $25,000 and $300,000 depending on location and aircraft type.</p>
      </div>
      <div class="def-block">
        <h3>Nearest vs. Hospital of Choice</h3>
        <p>"Nearest hospital" transport means you'll be stabilized locally, potentially remaining abroad. "Hospital of choice" means your provider guarantees to move you to a specific hospital you select — typically in your home country — allowing continuity of care with your own physicians. Global Rescue, Medjet, and AirMed all offer hospital-of-choice transport.</p>
      </div>
      <div class="def-block">
        <h3>Repatriation (Medical &amp; Non-Medical)</h3>
        <p>The return of a member to their home country. Medical repatriation applies when you require ongoing care. Non-medical repatriation covers return following security events, natural disasters, civil unrest, or the death of a travel companion. Most insurance-based providers cover medical repatriation only. Global Rescue covers both medical and non-medical events, including security-triggered departures.</p>
      </div>

      <h3 style="margin:24px 0 10px">Membership vs. Insurance vs. Credit Card</h3>
      <div class="tbl-wrap">
      <table class="type-tbl">
        <thead><tr><th>Type</th><th>Rescue &amp; Evacuation Membership<br><small style="font-weight:400;opacity:.8">(e.g. Global Rescue, Medjet, AirMed)</small></th><th>Travel Insurance<br><small style="font-weight:400;opacity:.8">(e.g. Seven Corners, Travelex)</small></th><th>Credit Card Benefit<br><small style="font-weight:400;opacity:.8">(e.g. AMEX Platinum, Chase Sapphire)</small></th></tr></thead>
        <tbody>
          <tr><td class="t-hd">Dispatches personnel to you</td><td>✓ Yes</td><td>✗ No</td><td>◐ Conditional</td></tr>
          <tr><td class="t-hd">Claims required</td><td>None</td><td>Yes — documentation required</td><td>Often — pay upfront, then claim</td></tr>
          <tr><td class="t-hd">Deductibles / co-pays</td><td>None</td><td>Typically yes</td><td>Varies</td></tr>
          <tr><td class="t-hd">Covers trip cancellation / luggage</td><td>✗ No</td><td>✓ Yes</td><td>✓ Yes (varies)</td></tr>
          <tr><td class="t-hd">Security extraction</td><td>✓ (some plans)</td><td>◐ Limited</td><td>✗ No</td></tr>
          <tr><td class="t-hd">Field rescue capability</td><td>✓ (some plans)</td><td>✗ No</td><td>✗ No</td></tr>
          <tr><td class="t-hd">Coverage limit</td><td>Unlimited (service-based)</td><td>Dollar-capped per policy</td><td>Usually $100,000 or less</td></tr>
        </tbody>
      </table>
      </div>

      <div class="excl-list">
        <h4>Common Exclusions Across Plans</h4>
        Pre-existing medical conditions (varies by plan) · Active war zones or declared conflict areas · Extreme sports without add-on · High-altitude rescue above 15,000 ft without altitude add-on · Injuries related to alcohol or substance use · Self-inflicted injuries · Mental health crises (most insurance plans) · Travel against official government advisories · Destinations under active travel bans · Members over 85 (transport restrictions)
      </div>
    </section>

    <!-- SECTION 2: CATEGORY WINNERS -->
    <section id="winners">
      <div class="sec-h"><span class="sec-num">Section 2</span><h2>Category Winners at a Glance</h2></div>
      <p>We evaluated 15 providers across 12 capability criteria. The categories below reflect each provider's strongest use case — not a single composite score. A provider that excels at hospital-to-hospital air transport may be the wrong choice for someone trekking in Nepal.</p>
      <div class="winners-grid">{winners_html}</div>
    </section>

    <!-- SECTION 3: COMPARISON TABLES -->
    <section id="tables" class="tbl-section">
      <div class="sec-h"><span class="sec-num">Section 3</span><h2>Side-by-Side Comparison</h2></div>
      <p>Two views: the Essential Services table covers the five core capabilities that separate providers most sharply. The Full Feature Matrix adds seven additional criteria including pricing flexibility, student coverage, and high-altitude capability.</p>
      <div class="tbl-tabs" role="tablist">
        <button class="tbl-tab on" data-panel="tab-essential" role="tab" aria-selected="true">Essential Services (5)</button>
        <button class="tbl-tab" data-panel="tab-full" role="tab" aria-selected="false">Full Feature Matrix (12)</button>
      </div>
      <div class="tbl-panel on" id="tab-essential">
        <p class="scroll-hint">← Scroll to see all providers →</p>
        {ess_table}
        <div class="tbl-legend">
          <span><span class="c-best">✓ Best</span> Best-in-class</span>
          <span><span class="c-yes">✓</span> Capable / Included</span>
          <span><span class="c-partial">◐</span> Limited or conditional</span>
          <span><span class="c-no">✗</span> Not available</span>
        </div>
      </div>
      <div class="tbl-panel" id="tab-full">
        <p class="scroll-hint">← Scroll to see all columns →</p>
        {full_table}
        <div class="tbl-legend">
          <span><span class="c-best">✓ Best</span> Best-in-class</span>
          <span><span class="c-yes">✓</span> Capable / Included</span>
          <span><span class="c-partial">◐</span> Limited or conditional</span>
          <span><span class="c-no">✗</span> Not available</span>
        </div>
      </div>
    </section>

    <!-- SECTION 4: PROVIDER REVIEWS -->
    <section id="reviews">
      <div class="sec-h"><span class="sec-num">Section 4</span><h2>Detailed Provider Reviews</h2></div>
      <p>Global Rescue appears first as the publisher of this comparison and the Best Overall winner. All other providers are listed alphabetically. Each review includes an essential services score, a one-sentence verdict, and a breakdown of capabilities.</p>
      {providers_html}
    </section>

    <!-- SECTION 5: CREDIT CARDS -->
    <section id="credit-cards">
      <div class="sec-h"><span class="sec-num">Section 5</span><h2>Credit Card Evacuation Benefits: What They Cover and What They Don't</h2></div>
      <p>Premium credit cards market evacuation assistance as a benefit. Here's what that actually means when you need it.</p>
      <div class="cc-grid">
        <div class="cc-card">
          <h3>AMEX Platinum</h3>
          <dl>
            <dt>Medical evacuation</dt><dd>Available when medically necessary and coordinated through Premium Global Assist Hotline. Third-party providers arranged by Amex.</dd>
            <dt>Field rescue</dt><dd>Conditionally possible if pre-coordinated and deemed medically necessary. Not a direct deployment capability.</dd>
            <dt>Claims</dt><dd>Direct payment may be arranged if pre-coordinated. Otherwise: pay upfront, file claim.</dd>
            <dt>Security evacuation</dt><dd>Limited, conditional, event-driven only.</dd>
            <dt>Medical advisory</dt><dd>Via Global Assist Hotline — third-party coordination, not on-staff physicians.</dd>
            <dt>Coverage limit</dt><dd>Coordination-based, not dollar-capped the same way as insurance.</dd>
          </dl>
        </div>
        <div class="cc-card">
          <h3>Chase Sapphire Reserve</h3>
          <dl>
            <dt>Medical evacuation</dt><dd>Up to $100,000. Pre-authorization required. Typically facility-to-facility.</dd>
            <dt>Field rescue</dt><dd>Not provided. Services begin from a medical facility.</dd>
            <dt>Claims</dt><dd>Reimbursement-based if not pre-coordinated.</dd>
            <dt>Security evacuation</dt><dd>Not provided.</dd>
            <dt>Medical advisory</dt><dd>Basic, third-party.</dd>
            <dt>Coverage limit</dt><dd>$100,000 for evacuation.</dd>
          </dl>
        </div>
      </div>
      <div class="cc-verdict"><strong>Verdict:</strong> Credit card benefits are conditional safety nets — not operational rescue services. Neither card dispatches personnel to your location, provides security extraction, or offers dedicated physician access. For routine international travel to established destinations, card benefits supplement your protection. For adventure travel, remote destinations, or high-risk regions, a dedicated membership is necessary.</div>
    </section>

    <!-- SECTION 6: HOW TO CHOOSE -->
    <section id="how-to-choose">
      <div class="sec-h"><span class="sec-num">Section 6</span><h2>How to Choose the Right Plan</h2></div>
      <p>The right protection depends on where you're going, what you're doing there, and which risks matter most to you. These profiles are a starting point.</p>
      <div class="profile-grid">
        <div class="profile-row"><span class="prof-type">Adventure &amp; Outdoor Traveler</span><span class="prof-rec">Field rescue from the point of injury is essential. → <strong>Global Rescue + High-Altitude Package</strong></span></div>
        <div class="profile-row"><span class="prof-type">Student Studying Abroad</span><span class="prof-rec">Flexible duration, all 5 essential services, student pricing. → <strong>Global Rescue Student Membership</strong></span></div>
        <div class="profile-row"><span class="prof-type">Senior Traveler</span><span class="prof-rec">Simple, no-claims, get-home guarantee. → <strong>EA+ or Medjet</strong></span></div>
        <div class="profile-row"><span class="prof-type">Scuba Diver</span><span class="prof-rec">Dive medicine specialists are non-negotiable. → <strong>DAN TravelAssist + Global Rescue for broader rescue</strong></span></div>
        <div class="profile-row"><span class="prof-type">Frequent Business Traveler</span><span class="prof-rec">Broad coverage + intelligence feed + reliable response. → <strong>Global Rescue Annual Membership</strong></span></div>
        <div class="profile-row"><span class="prof-type">High-Risk Destination Traveler</span><span class="prof-rec">Security extraction is non-negotiable. → <strong>Global Rescue + Security Add-On</strong></span></div>
        <div class="profile-row"><span class="prof-type">Occasional Leisure Traveler</span><span class="prof-rec">Short-term coverage + travel insurance. → <strong>Global Rescue 7-day + Travel Insurance policy</strong></span></div>
        <div class="profile-row"><span class="prof-type">Organization / Duty of Care</span><span class="prof-rec">Scalable, trackable, enterprise-grade. → <strong>Global Rescue Enterprise or ISOS</strong></span></div>
      </div>

      <h3 style="margin:28px 0 16px;font-size:1.1rem">5 Questions to Ask Before You Buy</h3>
      <div class="q-item"><h3>Will this provider send someone to me, or do I need to get to them first?</h3><p>This is the most critical question. Most providers begin services only once you've reached a medical facility. If you're injured in a remote area without reliable transport, that's a meaningful gap. Ask explicitly: does this provider deploy personnel to the point of injury?</p></div>
      <div class="q-item"><h3>Do I need to file a claim or pay upfront?</h3><p>Direct-service providers (Global Rescue, Medjet, AirMed, EA+) arrange and cover costs without upfront payment or claims. Insurance-based providers require documentation and reimbursement after the fact. Know which model your plan uses before you need it.</p></div>
      <div class="q-item"><h3>Does it cover my specific activity and destination?</h3><p>Extreme sports, high-altitude mountaineering, dive travel, and travel to high-risk regions all have different coverage implications. Verify that your specific activities and destinations are covered in the service terms — not just assumed.</p></div>
      <div class="q-item"><h3>Can I get home to my own hospital, or just the nearest one?</h3><p>Hospital-of-choice transport (Global Rescue, Medjet, AirMed) ensures continuity of care with your own physicians. Many plans cover transport to the nearest medically appropriate facility only. Confirm which applies.</p></div>
      <div class="q-item"><h3>What happens if my emergency is security-related, not medical?</h3><p>Most plans focus exclusively on medical emergencies. If you travel to regions with any elevated security risk, verify whether your provider includes security evacuation — and whether it's in-field extraction or a reimbursement benefit for defined events.</p></div>
    </section>

    <!-- SECTION 7: FAQs -->
    <section id="faq">
      <div class="sec-h"><span class="sec-num">Section 7</span><h2>Frequently Asked Questions</h2></div>
      {faqs_html}
    </section>

  </main><!-- /content -->

  <!-- SIDEBAR -->
  <aside class="sidebar" aria-label="Page navigation and CTA">
    <div class="sb-toc">
      <h4>On This Page</h4>
      {toc_sidebar}
    </div>
    <div class="sb-cta">
      <div class="sc-from">Starting from</div>
      <div class="sc-price">$139 <small>/ 7-day trip</small></div>
      <a href="{JOIN_URL}" class="sc-join" target="_blank" rel="noopener">JOIN GLOBAL RESCUE</a>
      <ul class="sc-trusts">
        <li>No deductibles or co-pays</li>
        <li>No claims to file</li>
        <li>Field rescue to point of injury</li>
        <li>24/7 on-staff physicians</li>
        <li>Founded with Johns Hopkins Medicine</li>
      </ul>
    </div>
  </aside>

</div><!-- /layout -->
</div><!-- /outer -->

<!-- CTA BLOCK -->
<div class="cta-blk">
  <div style="max-width:900px;margin:0 auto">
    <h2>Ready to Travel Boldly?</h2>
    <p class="cta-sub">Join over 1 million members who trust Global Rescue for field rescue, medical evacuation, and security services worldwide.</p>
    <div class="price-grid">
      <div class="p-item"><div class="pi-lbl">7-Day Individual</div><div class="pi-price">From $139</div></div>
      <div class="p-item"><div class="pi-lbl">Annual Individual</div><div class="pi-price">From $329</div></div>
      <div class="p-item"><div class="pi-lbl">Family Plans</div><div class="pi-price">From $549</div></div>
      <div class="p-item"><div class="pi-lbl">High-Altitude Add-On</div><div class="pi-price">From $495</div></div>
    </div>
    <a href="{JOIN_URL}" class="btn-join-lg" target="_blank" rel="noopener">JOIN GLOBAL RESCUE</a>
    <p class="cta-disclaimer">No deductibles. No co-pays. No claims. No kidding. All prices in USD. Starting-from prices shown; actual pricing varies by plan type, duration, and options selected.</p>
    <div class="trust-row">
      <span>2025 Skift IDEA Award Winner</span>
      <span>Fast Company Most Innovative 2024</span>
      <span>Inc. Best in Business 2022</span>
      <span>ISO 9001 Certified</span>
      <span>Founded with Johns Hopkins Medicine</span>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer class="site-ftr">
  <div class="ftr-in">
    <div class="ftr-top">
      <div class="ftr-brand">
        <img src="https://www.globalrescue.com/grcom/grmkt_resources/images/GR-Logos/Global-Rescue-Logo-WR.svg" alt="Global Rescue" width="140" height="26">
        <div class="ftr-tagline">Helping People Travel Boldly Since 2004</div>
      </div>
      <nav class="ftr-links" aria-label="Footer navigation">
        <a href="https://www.globalrescue.com/personal/travelservices/">Plans</a>
        <a href="{JOIN_URL}" target="_blank" rel="noopener">Join</a>
        <a href="https://www.globalrescue.com/lp/high-altitude-travel-evacuation/">High-Altitude</a>
        <a href="https://www.globalrescue.com/common/blog/">Resources</a>
        <a href="https://www.globalrescue.com/about-us/">About</a>
        <a href="https://www.globalrescue.com/contact/">Contact</a>
      </nav>
    </div>
    <div class="ftr-bottom">
      <p class="ftr-legal">© 2025 Global Rescue LLC. TotalCare and the TotalCare logo are service marks of Global Rescue LLC. All Rights Reserved. Global Rescue LLC provides technical and administrative services to Elite Medical Group, P.C., a professional corporation owned by licensed physicians. Global Rescue is not an insurance company and cannot reimburse members for costs of medical treatment or trip expenses. All service terms are subject to the Member Services Agreement. Starting-from prices shown; actual pricing varies. For individuals 85+, medical transport is available on a fee-for-service basis.</p>
      <p class="ftr-disc">This comparison page is published by Global Rescue. While we have made every effort to represent competitors accurately based on publicly available service documentation, travelers should verify coverage details directly with each provider before purchasing. This page is not legal or insurance advice.</p>
    </div>
  </div>
</footer>

<button class="scr-top" aria-label="Back to top" title="Back to top">↑</button>

<script>{JS}</script>
</body>
</html>"""

# ── WRITE OUTPUT ──────────────────────────────────────────────────────────────
output_path = "/Users/jlambert/Documents/Projects/Comparison Page/global-rescue-comparison-FINAL.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"✓ Written: {output_path}")
import os
size = os.path.getsize(output_path)
print(f"  File size: {size:,} bytes ({size//1024} KB)")
