# Claude Code Task Instructions

## Environment Setup

```bash
# Check Node.js is available (for running a local preview server)
node --version

# Check Python is available (for scraping)
python3 --version

# Install scraping dependencies if needed
pip3 install requests beautifulsoup4 cssutils
# or
npm install puppeteer  # if you need JavaScript-rendered pages
```

---

## Task 1: Scrape the EA+ Reference Page

The client's reference page is:
`https://www.emergencyassistanceplus.com/resources/global-rescue-alternatives/`

This is a competitor comparison page. We want to match its editorial approach, NOT its brand or content.

### What to extract:

```python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}
response = requests.get(
    'https://www.emergencyassistanceplus.com/resources/global-rescue-alternatives/',
    headers=headers
)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract:
# 1. Page layout structure (main content wrapper width, sidebar presence)
# 2. Font families from inline styles or <style> tags
# 3. Color values from CSS
# 4. Provider card/section HTML structure
# 5. Table HTML structure
# 6. "Best for" label treatment
# 7. CTA button styles
# 8. Section heading hierarchy
```

If the page returns a 403 (blocks basic requests), try with Puppeteer/playwright:
```bash
npx puppeteer-core  # or install chromium
```

Or use the cached Google version:
```
https://webcache.googleusercontent.com/search?q=cache:https://www.emergencyassistanceplus.com/resources/global-rescue-alternatives/
```

Also scrape these EA+ pages for additional layout reference:
- `https://www.emergencyassistanceplus.com/resources/medjet-alternatives/`
- `https://www.emergencyassistanceplus.com/resources/emergency-assistance-plus-vs-global-rescue/`

**Save findings to:** `reference/ea-plus-analysis.md`

---

## Task 2: Extract Global Rescue Brand from Figma

### Option A: Figma REST API

```bash
# Set your Figma token (ask user if not available as env var)
export FIGMA_TOKEN="your_token_here"

# Fetch the specific node
curl -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/VcbJVvxziRpN8Zo1q3Z8Rn/nodes?ids=743-208" \
  > reference/figma-node-743-208.json

# Also fetch the full file for styles
curl -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/VcbJVvxziRpN8Zo1q3Z8Rn" \
  > reference/figma-full-file.json

# Parse colors from the response
python3 -c "
import json

with open('reference/figma-full-file.json') as f:
    data = json.load(f)

# Extract color styles
styles = data.get('styles', {})
for key, style in styles.items():
    print(f'{style[\"name\"]}: {key}')
"
```

### Option B: Scrape the Live GR Website for CSS

```python
import requests
from bs4 import BeautifulSoup
import re

# Fetch homepage
r = requests.get('https://www.globalrescue.com', 
    headers={'User-Agent': 'Mozilla/5.0 (compatible)'})
soup = BeautifulSoup(r.content, 'html.parser')

# Find all linked stylesheets
stylesheets = soup.find_all('link', rel='stylesheet')
for sheet in stylesheets:
    href = sheet.get('href', '')
    if href:
        # Fetch each stylesheet
        if href.startswith('/'):
            href = 'https://www.globalrescue.com' + href
        css_r = requests.get(href)
        # Extract color values
        colors = re.findall(r'#[0-9a-fA-F]{3,6}', css_r.text)
        # Extract font-family declarations
        fonts = re.findall(r"font-family:\s*([^;]+)", css_r.text)
        print(f"Stylesheet: {href}")
        print(f"Colors found: {set(colors)}")
        print(f"Fonts found: {set(fonts)}")
```

Also check:
- `https://www.globalrescue.com/personal/travelservices/` (their main product page)
- `https://www.globalrescue.com/common/blog/detail/medical-emergency-evacuation-travel/` (a blog post — see their article layout)

**Save findings to:** `reference/gr-brand-guide.md`

---

## Task 3: Build the Page

Once you have the brand data and EA+ layout analysis, build `global-rescue-comparison-FINAL.html`.

### Critical requirements:

1. **Two-column layout on desktop** — main content (~760px) + sticky sidebar (~280px)
2. **Sidebar contains:** Table of Contents + compact JOIN CTA box
3. **Hero:** Restrained — background color only (no images), H1 + subtitle, max 280px tall
4. **Provider cards:** Structured consistently with: name, badge, verdict, score, prose, feature list, best-for, price
5. **Tables:** Clean, minimal — ✓/◐/✗ symbols, no emoji
6. **All 10 FAQs** as accordion with JSON-LD schema
7. **All JSON-LD schemas** from `content/structured-data.md` in `<head>`
8. **JOIN button URL** exactly as specified in `content/cta-links.md`
9. **Exact brand colors** from Figma/website scrape

### File structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Meta tags -->
  <!-- JSON-LD schemas (all 5) -->
  <!-- Google Fonts -->
  <style>
    /* All CSS inline — no external stylesheets */
  </style>
</head>
<body>
  <!-- Site Header -->
  <!-- Hero -->
  <!-- TOC Bar (mobile) -->
  <div class="page-layout">
    <main class="content-column">
      <!-- Breadcrumb -->
      <!-- Methodology box -->
      <!-- Section 1: What's Covered -->
      <!-- Section 2: Providers Overview -->
      <!-- Section 3: Comparison Tables -->
      <!-- Section 4: Provider Reviews -->
      <!-- Section 5: Credit Cards -->
      <!-- Section 6: How to Choose -->
      <!-- Section 7: FAQs -->
    </main>
    <aside class="sidebar">
      <!-- Sticky TOC -->
      <!-- JOIN CTA box -->
    </aside>
  </div>
  <!-- CTA Block -->
  <!-- Footer -->
  <script>
    /* All JS inline */
  </script>
</body>
</html>
```

---

## Task 4: Test the Page

```bash
# Start a local server
python3 -m http.server 8080
# or
npx serve .

# Open in browser
open http://localhost:8080/global-rescue-comparison-FINAL.html
```

Test checklist:
- [ ] Renders correctly at 1440px width
- [ ] Renders correctly at 768px width  
- [ ] Renders correctly at 375px width
- [ ] Sidebar is sticky and scrolls with content
- [ ] All accordions open/close
- [ ] Table switcher works
- [ ] FAQ accordions work
- [ ] JOIN button clicks through to correct URL
- [ ] TOC links scroll to correct sections
- [ ] No console errors

---

## Task 5: Validate Structured Data

```bash
# Copy the JSON-LD from the page and validate at:
# https://validator.schema.org/
# or use the CLI tool:
npx schema-dts-gen  # if available
```

---

## Questions for the User

If you hit these blockers, ask:

1. **Figma token not available** → "I need your Figma personal access token to pull brand colors from the design file. You can create one at figma.com/settings under 'Personal access tokens'."

2. **EA+ page returns 403 with all approaches** → "The EA+ page is blocking all automated access. Can you paste the HTML source of the page, or share a screenshot of the layout you want me to match?"

3. **GR website blocks CSS access** → "I'll work from the colors I can extract from page inspections. Please confirm if the primary navy is approximately #0B2D5E and the CTA red is approximately #C41230."
