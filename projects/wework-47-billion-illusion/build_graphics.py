"""
YTF MASTER PRODUCTION SYSTEM v2.0 - ASSET COMPILER
Generates high-fidelity real document scans, animated charts, and physical collage backgrounds.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.join(BASE_DIR, "assets", "documents")
CHART_DIR = os.path.join(BASE_DIR, "assets", "charts")
BG_DIR = os.path.join(BASE_DIR, "assets", "backgrounds")

os.makedirs(DOC_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(BG_DIR, exist_ok=True)

# 1. Real SEC Form S-1 Dedication Page Document
doc_s1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1600" width="1200" height="1600">
  <defs>
    <filter id="paper-texture" x="0%" y="0%" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="5" result="noise" />
      <feDiffuseLighting in="noise" lighting-color="#fdfbf7" surfaceScale="2" result="light">
        <feDistantLight azimuth="60" elevation="50" />
      </feDiffuseLighting>
      <feBlend mode="multiply" in="SourceGraphic" in2="light" />
    </filter>
    <filter id="drop-shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="12" dy="18" stdDeviation="15" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Desk Background Context -->
  <rect width="1200" height="1600" fill="#1e222a"/>

  <!-- Paper Sheet -->
  <g filter="url(#drop-shadow)">
    <rect x="100" y="80" width="1000" height="1440" rx="4" fill="#faf6ee" filter="url(#paper-texture)"/>
    
    <!-- SEC Header Bar -->
    <text x="600" y="180" font-family="'Courier New', monospace" font-size="20" font-weight="bold" fill="#333" text-anchor="middle" letter-spacing="3">UNITED STATES SECURITIES AND EXCHANGE COMMISSION</text>
    <text x="600" y="215" font-family="'Courier New', monospace" font-size="16" fill="#666" text-anchor="middle">WASHINGTON, D.C. 20549</text>
    <line x1="200" y1="240" x2="1000" y2="240" stroke="#444" stroke-width="2"/>
    <text x="600" y="290" font-family="'Courier New', monospace" font-size="28" font-weight="900" fill="#111" text-anchor="middle">FORM S-1</text>
    <text x="600" y="325" font-family="'Courier New', monospace" font-size="16" fill="#444" text-anchor="middle">REGISTRATION STATEMENT UNDER THE SECURITIES ACT OF 1933</text>
    <line x1="200" y1="350" x2="1000" y2="350" stroke="#444" stroke-width="1"/>

    <!-- Company Name -->
    <text x="600" y="440" font-family="'Georgia', serif" font-size="38" font-weight="bold" fill="#000" text-anchor="middle">The We Company</text>
    <text x="600" y="475" font-family="'Courier New', monospace" font-size="15" fill="#666" text-anchor="middle">(Exact name of registrant as specified in its charter)</text>

    <!-- Dedication Section with Torn Box & Yellow Highlighter -->
    <rect x="220" y="580" width="760" height="420" fill="#f4efe1" stroke="#d0c7b0" stroke-width="2" stroke-dasharray="6,4"/>
    
    <!-- Yellow Highlighter under dedication text -->
    <rect x="260" y="740" width="680" height="45" fill="#ffeb3b" opacity="0.85" rx="3" transform="rotate(-0.5 600 760)"/>
    <rect x="310" y="805" width="580" height="45" fill="#ffeb3b" opacity="0.85" rx="3" transform="rotate(0.3 600 825)"/>

    <text x="600" y="700" font-family="'Georgia', serif" font-style="italic" font-size="24" fill="#555" text-anchor="middle">Page 1 — Dedication</text>
    <text x="600" y="775" font-family="'Georgia', serif" font-size="30" font-weight="bold" fill="#000" text-anchor="middle">"We dedicate this to the energy of we —</text>
    <text x="600" y="840" font-family="'Georgia', serif" font-size="30" font-weight="bold" fill="#000" text-anchor="middle">greater than any one of us but inside each of us."</text>

    <!-- Forensic Red Annotation Stamp -->
    <g transform="translate(680, 1050) rotate(-12)">
      <rect x="-10" y="-10" width="360" height="90" fill="none" stroke="#d32f2f" stroke-width="6" rx="8" opacity="0.9"/>
      <text x="170" y="32" font-family="'Arial Black', sans-serif" font-size="24" font-weight="900" fill="#d32f2f" text-anchor="middle" letter-spacing="2">EVIDENCE EXHIBIT</text>
      <text x="170" y="65" font-family="'Courier New', monospace" font-size="18" font-weight="bold" fill="#d32f2f" text-anchor="middle">SEC CIK: 0001533523</text>
    </g>

    <!-- Red Arrow pointing to highlighter -->
    <path d="M 180 880 Q 240 850 260 780" fill="none" stroke="#d32f2f" stroke-width="5" marker-end="url(#arrow)"/>
    <text x="160" y="920" font-family="'Comic Sans MS', cursive, sans-serif" font-size="22" font-weight="bold" fill="#d32f2f">NOT A JOKE.</text>
  </g>
</svg>
"""

# 2. Community Adjusted EBITDA Accounting Ledger Document
doc_ebitda_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="1200" height="900">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="8" dy="12" stdDeviation="10" flood-color="#000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect width="1200" height="900" fill="#16181d"/>
  
  <g filter="url(#shadow)">
    <rect x="80" y="60" width="1040" height="780" rx="6" fill="#fdfbf5"/>
    <text x="600" y="130" font-family="'Courier New', monospace" font-size="26" font-weight="bold" fill="#222" text-anchor="middle">THE WE COMPANY // NON-GAAP RECONCILIATION</text>
    <text x="600" y="165" font-family="'Courier New', monospace" font-size="18" fill="#777" text-anchor="middle">Fiscal Year Ended December 31, 2018 (in thousands)</text>
    <line x1="120" y1="190" x2="1080" y2="190" stroke="#333" stroke-width="2"/>

    <!-- Line Items -->
    <text x="140" y="250" font-family="'Courier New', monospace" font-size="22" fill="#222">Net Loss Attributable to WeWork</text>
    <text x="1040" y="250" font-family="'Courier New', monospace" font-size="22" font-weight="bold" fill="#d32f2f" text-anchor="end">$(1,927,330)</text>

    <text x="140" y="310" font-family="'Courier New', monospace" font-size="22" fill="#444">Add: Depreciation &amp; Amortization</text>
    <text x="1040" y="310" font-family="'Courier New', monospace" font-size="22" fill="#2e7d32" text-anchor="end">+$458,200</text>

    <text x="140" y="370" font-family="'Courier New', monospace" font-size="22" fill="#444">Add: Stock-Based Compensation</text>
    <text x="1040" y="370" font-family="'Courier New', monospace" font-size="22" fill="#2e7d32" text-anchor="end">+$124,500</text>

    <text x="140" y="430" font-family="'Courier New', monospace" font-size="22" fill="#444">Add: General &amp; Administrative</text>
    <text x="1040" y="430" font-family="'Courier New', monospace" font-size="22" fill="#2e7d32" text-anchor="end">+$357,000</text>

    <!-- The Scandalous Red Strike-out Line: RENT -->
    <g>
      <rect x="130" y="465" width="930" height="60" fill="#ffebee" rx="4"/>
      <text x="140" y="505" font-family="'Courier New', monospace" font-size="24" font-weight="bold" fill="#b71c1c">Add: Building Lease &amp; Rent Costs (REMOVED!)</text>
      <text x="1040" y="505" font-family="'Courier New', monospace" font-size="24" font-weight="bold" fill="#2e7d32" text-anchor="end">+$1,454,600</text>
      <line x1="135" y1="500" x2="750" y2="500" stroke="#d32f2f" stroke-width="4"/>
    </g>

    <line x1="120" y1="560" x2="1080" y2="560" stroke="#000" stroke-width="3"/>

    <!-- Magic Result -->
    <rect x="130" y="600" width="930" height="85" fill="#fff9c4" rx="4" stroke="#fbc02d" stroke-width="3"/>
    <text x="150" y="655" font-family="'Arial Black', sans-serif" font-size="28" fill="#111">"COMMUNITY ADJUSTED EBITDA"</text>
    <text x="1040" y="655" font-family="'Arial Black', sans-serif" font-size="34" fill="#2e7d32" text-anchor="end">+$467,000</text>

    <!-- Handwritten stamp note -->
    <text x="600" y="780" font-family="'Comic Sans MS', cursive" font-size="24" font-weight="bold" fill="#d32f2f" text-anchor="middle">"If you ignore the rent, a landlord is wildly profitable."</text>
  </g>
</svg>
"""

# 3. Chart: $47.2B Lease Liabilities vs $4.0B Committed Backlog
chart_debt_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <rect width="1200" height="800" fill="#1b1e24"/>
  
  <!-- Title -->
  <text x="600" y="90" font-family="'Arial Black', sans-serif" font-size="32" font-weight="bold" fill="#ffffff" text-anchor="middle">THE ASSET-LIABILITY DURATION MISMATCH</text>
  <text x="600" y="130" font-family="'Helvetica Neue', sans-serif" font-size="20" fill="#9e9e9e" text-anchor="middle">WeWork Contractual Obligations vs Committed Customer Revenue (June 2019)</text>

  <!-- Bars Area -->
  <g transform="translate(150, 200)">
    <!-- Owed to Landlords Bar (Giant) -->
    <rect x="100" y="40" width="320" height="460" fill="#d32f2f" rx="6"/>
    <text x="260" y="140" font-family="'Arial Black', sans-serif" font-size="44" fill="#ffffff" text-anchor="middle">$47.2B</text>
    <text x="260" y="190" font-family="'Helvetica Neue', sans-serif" font-size="22" font-weight="bold" fill="#ffebee" text-anchor="middle">15-Year Fixed Leases</text>
    <text x="260" y="230" font-family="'Helvetica Neue', sans-serif" font-size="18" fill="#ffcdd2" text-anchor="middle">Owed to Landlords</text>
    <text x="260" y="270" font-family="'Helvetica Neue', sans-serif" font-size="16" fill="#ffffff" text-anchor="middle">(Legally Binding / No Exit)</text>

    <!-- Customer Commitments Bar (Tiny) -->
    <rect x="520" y="420" width="320" height="80" fill="#388e3c" rx="6"/>
    <text x="680" y="385" font-family="'Arial Black', sans-serif" font-size="44" fill="#81c784" text-anchor="middle">$4.0B</text>
    <text x="680" y="460" font-family="'Helvetica Neue', sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">Customer Backlog</text>
    <text x="680" y="540" font-family="'Helvetica Neue', sans-serif" font-size="18" fill="#a5d6a7" text-anchor="middle">(30-Day Hot Desk Cancelations)</text>

    <!-- Base Line -->
    <line x1="40" y1="500" x2="880" y2="500" stroke="#ffffff" stroke-width="4"/>
  </g>

  <!-- Forensic Callout -->
  <rect x="250" y="710" width="700" height="50" rx="8" fill="#263238" stroke="#ffb300" stroke-width="2"/>
  <text x="600" y="743" font-family="'Courier New', monospace" font-size="20" font-weight="bold" fill="#ffb300" text-anchor="middle">SOURCE: FORM S-1 // LIABILITIES EXCEED REVENUE BACKLOG BY 11.8x</text>
</svg>
"""

# 4. Chart: The 33-Day Valuation Crash ($47B -> $8B)
chart_crash_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <rect width="1200" height="800" fill="#14171d"/>
  
  <text x="600" y="80" font-family="'Arial Black', sans-serif" font-size="34" fill="#ffffff" text-anchor="middle">THE 33-DAY COLLAPSE</text>
  <text x="600" y="120" font-family="'Helvetica Neue', sans-serif" font-size="20" fill="#b0bec5" text-anchor="middle">Implied Equity Valuation Freefall (Jan 2019 – Oct 2019)</text>

  <!-- Step Chart -->
  <g transform="translate(100, 180)">
    <!-- Grid lines -->
    <line x1="80" y1="60" x2="980" y2="60" stroke="#37474f" stroke-width="1" stroke-dasharray="4,4"/>
    <text x="60" y="65" font-family="'Courier New', monospace" font-size="16" fill="#78909c" text-anchor="end">$50B</text>

    <line x1="80" y1="200" x2="980" y2="200" stroke="#37474f" stroke-width="1" stroke-dasharray="4,4"/>
    <text x="60" y="205" font-family="'Courier New', monospace" font-size="16" fill="#78909c" text-anchor="end">$30B</text>

    <line x1="80" y1="340" x2="980" y2="340" stroke="#37474f" stroke-width="1" stroke-dasharray="4,4"/>
    <text x="60" y="345" font-family="'Courier New', monospace" font-size="16" fill="#78909c" text-anchor="end">$10B</text>

    <line x1="80" y1="420" x2="980" y2="420" stroke="#ffffff" stroke-width="3"/>
    <text x="60" y="425" font-family="'Courier New', monospace" font-size="16" fill="#ffffff" text-anchor="end">$0</text>

    <!-- Path Line -->
    <path d="M 120 80 L 360 80 L 460 270 L 580 320 L 700 360 L 860 380" fill="none" stroke="#ff1744" stroke-width="8" stroke-linejoin="round"/>

    <!-- Step Dots & Annotations -->
    <!-- Jan 2019: $47B -->
    <circle cx="120" cy="80" r="12" fill="#ffd600"/>
    <text x="120" y="40" font-family="'Arial Black', sans-serif" font-size="22" fill="#ffd600" text-anchor="middle">$47 BILLION</text>
    <text x="120" y="460" font-family="'Courier New', monospace" font-size="16" fill="#cfd8dc" text-anchor="middle">Jan 2019</text>

    <!-- Aug 14: S-1 Filed -->
    <circle cx="360" cy="80" r="10" fill="#ffffff"/>
    <text x="360" y="40" font-family="'Arial Black', sans-serif" font-size="18" fill="#ffffff" text-anchor="middle">S-1 Filed</text>
    <text x="360" y="460" font-family="'Courier New', monospace" font-size="16" fill="#cfd8dc" text-anchor="middle">Aug 14</text>

    <!-- Sep 05: $20B -->
    <circle cx="460" cy="270" r="10" fill="#ff1744"/>
    <text x="460" y="240" font-family="'Arial Black', sans-serif" font-size="20" fill="#ff5252" text-anchor="middle">$20B</text>
    <text x="460" y="460" font-family="'Courier New', monospace" font-size="16" fill="#cfd8dc" text-anchor="middle">Sep 05</text>

    <!-- Sep 17: $10B / IPO Pulled -->
    <circle cx="700" cy="360" r="12" fill="#ff1744"/>
    <text x="700" y="325" font-family="'Arial Black', sans-serif" font-size="20" fill="#ff5252" text-anchor="middle">$10B (Pulled)</text>
    <text x="700" y="460" font-family="'Courier New', monospace" font-size="16" fill="#cfd8dc" text-anchor="middle">Sep 17</text>

    <!-- Oct 22: $8B Bailout -->
    <circle cx="860" cy="380" r="14" fill="#d50000"/>
    <text x="860" y="340" font-family="'Arial Black', sans-serif" font-size="22" font-weight="bold" fill="#ff1744" text-anchor="middle">$8B Rescue</text>
    <text x="860" y="460" font-family="'Courier New', monospace" font-size="16" fill="#cfd8dc" text-anchor="middle">Oct 22</text>
  </g>
</svg>
"""

# Write files
with open(os.path.join(DOC_DIR, "doc_s1_dedication.svg"), "w", encoding="utf-8") as f:
    f.write(doc_s1_svg)

with open(os.path.join(DOC_DIR, "doc_community_ebitda.svg"), "w", encoding="utf-8") as f:
    f.write(doc_ebitda_svg)

with open(os.path.join(CHART_DIR, "chart_lease_vs_backlog.svg"), "w", encoding="utf-8") as f:
    f.write(chart_debt_svg)

with open(os.path.join(CHART_DIR, "chart_valuation_crash.svg"), "w", encoding="utf-8") as f:
    f.write(chart_crash_svg)

print(" All SVG document and chart assets compiled successfully!")
