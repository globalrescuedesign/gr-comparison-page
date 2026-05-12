# Structured Data (JSON-LD) Specifications

All schemas below must be included in the `<head>` of the HTML page.

---

## 1. Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Global Rescue",
  "alternateName": "Global Rescue LLC",
  "url": "https://www.globalrescue.com",
  "logo": "https://www.globalrescue.com/grcom/grmkt_resources/images/GR-Logos/Global-Rescue-Logo-WR.svg",
  "foundingDate": "2004",
  "description": "Global Rescue is a crisis response, medical evacuation and security extraction company providing field rescue from the point of illness or injury, 24/7 medical and travel advisory, security evacuation, and worldwide repatriation services. Founded in partnership with Johns Hopkins Medicine.",
  "sameAs": [
    "https://www.linkedin.com/company/global-rescue",
    "https://twitter.com/globalrescue",
    "https://www.facebook.com/globalrescue",
    "https://en.wikipedia.org/wiki/Global_Rescue"
  ],
  "award": [
    "2025 Skift IDEA Award — Industry Innovators: Business Travel",
    "2024 Fast Company Most Innovative Company",
    "2022 Inc. Magazine Best in Business",
    "2022 ISO 9001 Certified"
  ]
}
```

---

## 2. Article

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Best Travel Insurance for Rescue and Medical Evacuation",
  "description": "A comprehensive comparison of 15 providers offering emergency rescue, medical evacuation, and travel protection — evaluated across field rescue capability, medevac, repatriation, medical advisory, security extraction, and pricing.",
  "dateModified": "2025-05-01",
  "datePublished": "2025-01-01",
  "publisher": {
    "@type": "Organization",
    "name": "Global Rescue",
    "url": "https://www.globalrescue.com"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.globalrescue.com/resources/best-travel-insurance-rescue-medical-evacuation/"
  },
  "about": [
    {"@type": "Thing", "name": "Medical Evacuation"},
    {"@type": "Thing", "name": "Field Rescue"},
    {"@type": "Thing", "name": "Travel Insurance"},
    {"@type": "Thing", "name": "Security Evacuation"},
    {"@type": "Thing", "name": "Travel Protection Membership"}
  ]
}
```

---

## 3. FAQPage

Include all 10 Q&A pairs from content/page-copy.md Section 7.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between travel insurance and a medical evacuation membership?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Full answer text from page-copy.md Q1]"
      }
    }
    // ... repeat for all 10 questions
  ]
}
```

---

## 4. ItemList (Provider Rankings)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Best Travel Insurance for Rescue and Medical Evacuation — Provider Rankings",
  "numberOfItems": 15,
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Global Rescue", "description": "Best Overall — Only provider delivering all 5 essential services with direct, no-claims, in-field response."},
    {"@type": "ListItem", "position": 2, "name": "Medjet", "description": "Runner-Up Overall — Strong medical transport with hospital-of-choice guarantee and no-claims model."},
    {"@type": "ListItem", "position": 3, "name": "AirMed International", "description": "Best Hospital-to-Hospital Transport — Own fleet, ICU-level care in transit."},
    {"@type": "ListItem", "position": 4, "name": "GeoBlue", "description": "Runner-Up Medical Advisory — Strong curated global provider network."},
    {"@type": "ListItem", "position": 5, "name": "International SOS", "description": "Enterprise-grade global medical and security assistance."},
    {"@type": "ListItem", "position": 6, "name": "DAN TravelAssist", "description": "Best for Scuba Divers — Dive-specific medical expertise and global hyperbaric network."},
    {"@type": "ListItem", "position": 7, "name": "American Express Platinum", "description": "Best Credit Card Option — Most capable credit card with conditional evacuation coordination."},
    {"@type": "ListItem", "position": 8, "name": "Chase Sapphire Reserve", "description": "Runner-Up Credit Card — Up to $100,000 evacuation coverage."},
    {"@type": "ListItem", "position": 9, "name": "Emergency Assistance Plus (EA+)", "description": "Best for Seniors — Simple, affordable, no-claims model at ~$229/year."},
    {"@type": "ListItem", "position": 10, "name": "Seven Corners", "description": "Most Flexible Insurance Pricing — Widest range of plan types and durations."},
    {"@type": "ListItem", "position": 11, "name": "WorldTrips (Atlas Travel)", "description": "Best Student Insurance Alternative — Affordable and flexible for study abroad."},
    {"@type": "ListItem", "position": 12, "name": "Travel Guard (AIG)", "description": "Flexible insurance-based evacuation and travel protection."},
    {"@type": "ListItem", "position": 13, "name": "Global Guardian", "description": "Enterprise air ambulance with rapid mobilization."},
    {"@type": "ListItem", "position": 14, "name": "SkyMed", "description": "Regional hospital-to-home transport for North America."},
    {"@type": "ListItem", "position": 15, "name": "Travelex Insurance", "description": "Flexible insurance-based medical evacuation."}
  ]
}
```

---

## 5. BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.globalrescue.com"},
    {"@type": "ListItem", "position": 2, "name": "Resources", "item": "https://www.globalrescue.com/common/blog/"},
    {"@type": "ListItem", "position": 3, "name": "Travel Insurance", "item": "https://www.globalrescue.com/common/blog/"},
    {"@type": "ListItem", "position": 4, "name": "Best Travel Insurance for Rescue & Medical Evacuation"}
  ]
}
```
