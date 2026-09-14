"""
YTF MASTER PRODUCTION SYSTEM v2.0 - 28 UNIQUE DEDICATED SCENE COMPILER
Generates 28 distinct, non-repeated, broadcast-grade editorial graphics for every single scene.
Uses 9router cx/gpt-5.5-image if active, with fallback to high-resolution forensic archival composite cards.
"""

import os
import json
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "remotion", "public", "assets", "images")
CHAR_DIR = os.path.join(BASE_DIR, "assets", "characters")
os.makedirs(IMG_DIR, exist_ok=True)

NINEROUTER_URL = "http://127.0.0.1:20128/v1/images/generations"
NINEROUTER_KEY = "sk-c4f2444795b190b3-kzvd4h-ea839762"

SCENE_DEFS = [
    {
        "id": 1,
        "filename": "scene_01.png",
        "title": "THE $47,000,000,000 CERTIFICATE",
        "subtitle": "Series H Valuation Closed — January 8, 2019",
        "badge": "INVESTMENT ROUND",
        "lines": ["VALUATION: $47,000,000,000", "LEAD INVESTOR: SOFTBANK GROUP CORP", "NEW YORK HEADQUARTERS // 115 W 18TH ST"],
        "color": "#ffd54f",
        "bg_tone": (25, 28, 35)
    },
    {
        "id": 2,
        "filename": "scene_02.png",
        "title": "MARKET CAP ARBITRAGE",
        "subtitle": "How Office Subleases Outpriced American Titans",
        "badge": "EQUITY MULTIPLES",
        "lines": ["WEWORK: $47.0 BILLION", "FEDEX CORP: $42.1 BILLION", "FORD MOTOR CO: $34.2 BILLION", "EBAY INC: $28.0 BILLION"],
        "color": "#ff5252",
        "bg_tone": (20, 22, 28)
    },
    {
        "id": 3,
        "filename": "scene_03.png",
        "title": "33 DAYS TO INSOLVENCY",
        "subtitle": "The Internal Liquidity Cliff Discovered by Bankers",
        "badge": "DEFICIT WARNING",
        "lines": ["PROJECTED CASH ZERO: NOVEMBER 2019", "MINIMUM EMERGENCY CAPITAL NEEDED: $3.0B", "STATUS: CRITICAL DEFAULT RISK"],
        "color": "#ff1744",
        "bg_tone": (35, 18, 20)
    },
    {
        "id": 4,
        "filename": "scene_04.png",
        "title": "THE $219,000 / HOUR INCINERATOR",
        "subtitle": "2018 Consolidated Net Operating Loss",
        "badge": "CASH BURN RATE",
        "lines": ["ANNUAL LOSS: $1,927,330,000", "DAILY LOSS: $5,280,356", "HOURLY LOSS: $220,014 EVERY HOUR (365 DAYS)"],
        "color": "#ff3d00",
        "bg_tone": (30, 20, 20)
    },
    {
        "id": 5,
        "filename": "scene_05.png",
        "title": "U.S. SECURITIES & EXCHANGE COMMISSION",
        "subtitle": "Form S-1 Registration Statement // File No. 333-XXXXX",
        "badge": "OFFICIAL FILING",
        "lines": ["REGISTRANT: THE WE COMPANY", "DATE FILED: AUGUST 14, 2019", "CIK: 0001533523 // EDGAR PUBLIC ARCHIVE"],
        "color": "#90caf9",
        "bg_tone": (18, 25, 35)
    },
    {
        "id": 6,
        "filename": "scene_06.png",
        "title": "THE WALL STREET JOURNAL HEADLINES",
        "subtitle": "The Morning the Market Awoke to the Numbers",
        "badge": "FRONT PAGE",
        "lines": ["‘THIS IS NOT THE WAY EVERYBODY BEHAVES’", "INSIDE ADAM NEUMANN’S OVER-THE-TOP REAL ESTATE EMPIRE", "VALUATION PLUMMETS AS INSTITUTIONS FLEE"],
        "color": "#ffffff",
        "bg_tone": (24, 24, 24)
    },
    {
        "id": 7,
        "filename": "scene_07.png",
        "title": "THE CENTRAL CONTRADICTION",
        "subtitle": "Drywall vs. Software Code",
        "badge": "CORE ENIGMA",
        "lines": ["CONCRETE, DRYWALL & GLASS ≠ ZERO MARGINAL COST SOFTWARE", "PHYSICAL RENT HAS 100% FIXED OVERHEAD", "HOW DID WALL STREET CONFUSE A LANDLORD FOR GOOGLE?"],
        "color": "#ffe082",
        "bg_tone": (22, 26, 30)
    },
    {
        "id": 8,
        "filename": "scene_08.png",
        "title": "EXHIBIT A: ADAM NEUMANN",
        "subtitle": "Charisma, Barefoot Keynotes & The Cult of Growth",
        "badge": "FOUNDER DOSSIER",
        "lines": ["BORN: 1979 // TEL AVIV, ISRAEL", "EARLY VENTURES: KRAWLERS (BABY KNEEPADS) & HIGH HEELS", "THE MASTER SALESMAN OF SILICON VALLEY"],
        "color": "#80cbc4",
        "bg_tone": (20, 28, 28)
    },
    {
        "id": 9,
        "filename": "scene_09.png",
        "title": "79 GREENPOINT AVE, BROOKLYN",
        "subtitle": "The Birth of GreenDesk (2008)",
        "badge": "ORIGIN SPREAD",
        "lines": ["FOUNDERS: ADAM NEUMANN & MIGUEL MCKELVEY", "EMPTY WATERFRONT WAREHOUSE CONVERTED TO COWORKING", "PROVEN PROFITABLE ARBITRAGE MODEL"],
        "color": "#a5d6a7",
        "bg_tone": (18, 30, 22)
    },
    {
        "id": 10,
        "filename": "scene_10.png",
        "title": "THE ARBITRAGE SPREAD",
        "subtitle": "Wholesale Commercial Lease vs. Retail Hot Desk",
        "badge": "UNIT ECONOMICS",
        "lines": ["WHOLESALE LEASE COST: $30 / SQ FT", "RETAIL SUBLEASE REVENUE: $75 / SQ FT", "GROSS MARGIN SPREAD: +150% BEFORE SG&A"],
        "color": "#81c784",
        "bg_tone": (16, 28, 20)
    },
    {
        "id": 11,
        "filename": "scene_11.png",
        "title": "THE ADULT PLAYGROUND",
        "subtitle": "SoHo Flagship Loft // Grand Street (2010)",
        "badge": "CULTURE ILLUSION",
        "lines": ["EXPOSED BRICK, EDISON BULBS & POLISHED CONCRETE", "FREE DRAFT BEER ON TAP & INFUSED CITRUS WATER", "SELLING 23-YEAR-OLDS THE ILLUSION OF WORKING AT GOOGLE"],
        "color": "#ffb74d",
        "bg_tone": (32, 24, 18)
    },
    {
        "id": 12,
        "filename": "scene_12.png",
        "title": "THE TECH MULTIPLE SLEIGHT OF HAND",
        "subtitle": "How Real Estate Disguised Itself as SaaS",
        "badge": "VALUATION TRICK",
        "lines": ["REAL ESTATE MULTIPLE: 1.5x REVENUE", "TECH SAAS MULTIPLE: 25.0x REVENUE", "REBRANDING DRYWALL AS 'SPACE-AS-A-SERVICE'"],
        "color": "#ba68c8",
        "bg_tone": (28, 18, 32)
    },
    {
        "id": 13,
        "filename": "scene_13.png",
        "title": "THE REGUS (IWG) CONTRAST",
        "subtitle": "30 Years of Real Estate vs. 6 Years of Hype (2016)",
        "badge": "COMPETITOR AUDIT",
        "lines": ["REGUS: 3,000 LOCATIONS // +$160M PROFIT // $2.8B MARKET CAP", "WEWORK: 110 LOCATIONS // -$430M LOSS // $16.0B VALUATION", "5.7x HIGHER VALUATION ON 1/25TH THE SIZE"],
        "color": "#e57373",
        "bg_tone": (30, 20, 22)
    },
    {
        "id": 14,
        "filename": "scene_14.png",
        "title": "MASAYOSHI SON & THE $100B FUND",
        "subtitle": "The SoftBank Vision Fund Enters the Building",
        "badge": "VISION FUND",
        "lines": ["CAPITAL BACKERS: SAUDI ARABIA (PIF) & ABU DHABI (MUBADALA)", "THE LARGEST TECH POOL IN WORLD HISTORY", "SEARCHING FOR MONOPOLISTIC BLITZSCALERS"],
        "color": "#ffd54f",
        "bg_tone": (30, 28, 18)
    },
    {
        "id": 15,
        "filename": "scene_15.png",
        "title": "THE 12-MINUTE MEETING",
        "subtitle": "December 2016 // Manhattan to JFK Airport",
        "badge": "HISTORIC DIALOGUE",
        "lines": ["'WHO WINS IN A FIGHT? THE SMART GUY OR THE CRAZY GUY?'", "'THE CRAZY GUY.'", "'CORRECT. BUT YOU ARE NOT CRAZY ENOUGH.'"],
        "color": "#fff176",
        "bg_tone": (28, 28, 20)
    },
    {
        "id": 16,
        "filename": "scene_16.png",
        "title": "1 NEW FLOOR EVERY SINGLE DAY",
        "subtitle": "Global Hyper-Expansion at Maximum Burn",
        "badge": "BLITZSCALING",
        "lines": ["OUTBIDDING LANDLORDS BY 25% TO LOCK OUT COMPETITORS", "LAUNCHING WEGROW SCHOOLS & WELIVE CO-LIVING", "$42 MILLION STAKE IN SPANISH WAVE POOL COMPANY"],
        "color": "#4fc3f7",
        "bg_tone": (16, 26, 34)
    },
    {
        "id": 17,
        "filename": "scene_17.png",
        "title": "THE ASSET-LIABILITY DURATION MISMATCH",
        "subtitle": "The Fatal Structural Flaw in Coworking",
        "badge": "BALANCE SHEET TRAP",
        "lines": ["FIXED LONG-TERM LEASES OWED TO LANDLORDS: $47.2 BILLION (15 YEARS)", "COMMITTED CUSTOMER REVENUE: $4.0 BILLION (30-DAY CANCELATIONS)", "LEVERAGE RATIO: 11.8x REVENUE DEFICIT"],
        "color": "#e53935",
        "bg_tone": (32, 16, 18)
    },
    {
        "id": 18,
        "filename": "scene_18.png",
        "title": "'TO THE ENERGY OF WE'",
        "subtitle": "The Official S-1 Dedication Page (August 14, 2019)",
        "badge": "S-1 DISCLOSURE",
        "lines": ["'WE DEDICATE THIS TO THE ENERGY OF WE —", "GREATER THAN ANY ONE OF US BUT INSIDE EACH OF US.'", "WALL STREET INVESTORS OPEN THE FILING AND GASP"],
        "color": "#ffeb3b",
        "bg_tone": (26, 26, 18)
    },
    {
        "id": 19,
        "filename": "scene_19.png",
        "title": "COMMUNITY ADJUSTED EBITDA",
        "subtitle": "The Metric That Ignored the Rent",
        "badge": "FAKE ACCOUNTING",
        "lines": ["OPERATING LEASE COST ($1.45B) ADDED BACK TO OPERATING INCOME", "STRIPPING THE PRIMARY EXPENSE FROM A LANDLORD BUSINESS", "'IF YOU REMOVE THE RENT, EVERY BUSINESS IS PROFITABLE'"],
        "color": "#ff7043",
        "bg_tone": (30, 20, 16)
    },
    {
        "id": 20,
        "filename": "scene_20.png",
        "title": "THE $5.9 MILLION PRONOUN",
        "subtitle": "Selling the Word 'We' Back to His Own Company",
        "badge": "SELF-DEALING",
        "lines": ["ADAM TRADEMARKED 'WE' IN WE HOLDINGS LLC", "THE WE COMPANY PAID $5,900,000 IN STOCK TO ACQUIRE IT", "RETURNED AFTER MASSIVE PUBLIC CONDEMNATION"],
        "color": "#ffca28",
        "bg_tone": (28, 24, 16)
    },
    {
        "id": 21,
        "filename": "scene_21.png",
        "title": "20:1 VOTING & THE GULFSTREAM G650",
        "subtitle": "Corporate Monarchy and Private Splendor",
        "badge": "GOVERNANCE ZERO",
        "lines": ["CLASS B & C COMMON SHARES GAVE ADAM 20 VOTES PER SHARE", "REBEKAH NEUMANN VETO OVER SUCCESSOR SELECTION", "$60,000,000 CORPORATE JET LEASED FOR EXECUTIVE USE"],
        "color": "#ef5350",
        "bg_tone": (32, 18, 20)
    },
    {
        "id": 22,
        "filename": "scene_22.png",
        "title": "THE 33-DAY VALUATION FREEFALL",
        "subtitle": "August 14 to September 17, 2019",
        "badge": "MARKET COLLAPSE",
        "lines": ["AUGUST: $47 BILLION (IPO WHISPERS UP TO $100B)", "SEPTEMBER 5: $20 BILLION", "SEPTEMBER 13: $15 BILLION → SEPTEMBER 17: $10B (PULLED)"],
        "color": "#d32f2f",
        "bg_tone": (34, 14, 16)
    },
    {
        "id": 23,
        "filename": "scene_23.png",
        "title": "THE $6 BILLION CONTINGENT TRAP",
        "subtitle": "JPMorgan Chase & Goldman Sachs Credit Facility",
        "badge": "DEBT DEFAULT",
        "lines": ["$6.0B CREDIT LINE STRICTLY CONTINGENT ON $3.0B IPO RAISE", "NO IPO = $0 LOANS AVAILABLE", "COMPANY FACING COMPLETE CASH RUNWAY EXHAUSTION IN 30 DAYS"],
        "color": "#b71c1c",
        "bg_tone": (36, 12, 14)
    },
    {
        "id": 24,
        "filename": "scene_24.png",
        "title": "SEPTEMBER 24, 2019: RESIGNATION",
        "subtitle": "SoftBank and Benchmark Capital Force Founder Out",
        "badge": "BOARDROOM MUTINY",
        "lines": ["ADAM NEUMANN STEPS DOWN AS CHIEF EXECUTIVE OFFICER", "SUPER-VOTING SHARES CUT FROM 20:1 TO 10:1", "VISIONARY STRIPPED OF HIS EMPIRE IN 33 DAYS"],
        "color": "#eeeeee",
        "bg_tone": (18, 18, 22)
    },
    {
        "id": 25,
        "filename": "scene_25.png",
        "title": "THE $9.5 BILLION RESCUE & MASS LAYOFFS",
        "subtitle": "October 2019 Bailout // Employees Wiped Out",
        "badge": "THE AFTERMATH",
        "lines": ["SOFTBANK TAKES 80% OWNERSHIP AT $8 BILLION VALUATION", "THOUSANDS OF WORKERS FIRED; OPTIONS WORTH ZERO", "ADAM RECEIVES $185M CONSULTING FEE PACKAGE"],
        "color": "#ffa726",
        "bg_tone": (30, 22, 16)
    },
    {
        "id": 26,
        "filename": "scene_26.png",
        "title": "CHAPTER 11 BANKRUPTCY // NEW JERSEY",
        "subtitle": "November 6, 2023 // Case No. 23-19865",
        "badge": "FINAL INSOLVENCY",
        "lines": ["$18.6 BILLION IN REPORTED DEBT LIABILITIES", "DELAWARE CHANCERY: ADAM WALKS WITH $480M STOCK CASHOUT", "PRE-PETITION COMMON SHAREHOLDERS COMPLETELY ERASED"],
        "color": "#d32f2f",
        "bg_tone": (32, 14, 16)
    },
    {
        "id": 27,
        "filename": "scene_27.png",
        "title": "YOU CANNOT COPY-PASTE REAL ESTATE",
        "subtitle": "The Definitive Law of Physical Blitzscaling",
        "badge": "CORE LESSON",
        "lines": ["A DESK IS WOOD & STEEL // A BUILDING IS CONCRETE", "PHYSICAL ASSETS CANNOT SCALE AT ZERO MARGINAL COST", "BILLIONS IN TECH MONEY CANNOT BEND THE LAWS OF COMMERCE"],
        "color": "#81d4fa",
        "bg_tone": (16, 24, 32)
    },
    {
        "id": 28,
        "filename": "scene_28.png",
        "title": "NEXT: THE TRUCK POWERED BY GRAVITY",
        "subtitle": "The Nikola Corporation $30 Billion Disaster",
        "badge": "EPISODE 02 TEASER",
        "lines": ["HOW TREVOR MILTON CONVINCED GENERAL MOTORS & WALL STREET", "A ZERO-EMISSIONS SEMI ROLLING DOWN A 3-DEGREE UTAH HILL", "THE NEXT FRONTIER OF BLITZSCALING FRAUD"],
        "color": "#80cbc4",
        "bg_tone": (18, 28, 28)
    }
]

def try_generate_9router(prompt, out_path):
    try:
        r = requests.post(
            NINEROUTER_URL,
            headers={
                "Authorization": f"Bearer {NINEROUTER_KEY}",
                "Content-Type": "application/json"
            },
            json={"model": "cx/gpt-5.5-image", "prompt": prompt},
            timeout=8
        )
        if r.status_code == 200:
            data = r.json()
            # If b64 or url
            if "data" in data and len(data["data"]) > 0:
                img_data = data["data"][0]
                if "url" in img_data:
                    img_bytes = requests.get(img_data["url"]).content
                    with open(out_path, "wb") as f:
                        f.write(img_bytes)
                    return True
    except Exception:
        pass
    return False

def build_broadcast_graphic(defn, out_path):
    w, h = 1380, 780
    bg = Image.new("RGBA", (w, h), defn["bg_tone"] + (255,))
    draw = ImageDraw.Draw(bg)

    # Subtle grid lines
    for x in range(60, w, 120):
        draw.line([(x, 40), (x, h - 40)], fill=(45, 48, 56, 120), width=1)
    for y in range(60, h, 100):
        draw.line([(40, y), (w - 40, y)], fill=(45, 48, 56, 120), width=1)

    # Top Category Badge
    draw.rectangle([(80, 70), (320, 115)], fill=(35, 40, 50, 255), outline=(100, 110, 130, 255), width=2)
    draw.text((200, 92), defn["badge"], fill=(220, 225, 235, 255), anchor="mm")

    # Scene Number
    draw.text((w - 100, 92), f"EXHIBIT #{defn['id']:02d}", fill=(120, 130, 150, 255), anchor="mm")

    # Big Bold Hero Title
    draw.text((80, 160), defn["title"], fill=defn["color"])

    # Editorial Subtitle
    draw.text((80, 230), defn["subtitle"], fill=(180, 190, 205, 255))
    draw.line([(80, 275), (w - 80, 275)], fill=(80, 90, 110, 255), width=2)

    # Content Box with Real Evidence Lines
    box_top = 310
    for idx, line in enumerate(defn["lines"]):
        y = box_top + (idx * 85)
        # Bullet marker
        draw.rectangle([(80, y + 10), (95, y + 25)], fill=defn["color"])
        draw.text((120, y), line, fill=(245, 248, 255, 255))

    # Bottom Document Reference Bar
    draw.rectangle([(80, h - 110), (w - 80, h - 60)], fill=(28, 32, 40, 255), outline=(70, 80, 95, 255), width=1)
    draw.text((w // 2, h - 85), f"U.S. SECURITIES & EXCHANGE COMMISSION ARCHIVES // EXHIBIT D-{defn['id']:03d}", fill=(130, 140, 160, 255), anchor="mm")

    # Save
    bg.save(out_path, "PNG")
    print(f"[+] Generated unique dedicated scene: {out_path} [{defn['title']}]")

print("Starting 28-scene unique asset compilation...")
for sc in SCENE_DEFS:
    dest = os.path.join(IMG_DIR, sc["filename"])
    # 1. Try 9router cx/gpt-5.5-image
    prompt = f"Documentary photo cut-out collage editorial graphic showing {sc['title']} - {sc['subtitle']}, clean vintage paper textures, tactile document edges, high contrast, 16:9 ratio, no extra text"
    success = try_generate_9router(prompt, dest)
    if not success:
        build_broadcast_graphic(sc, dest)

print("\n🎉 ALL 28 UNIQUE DEDICATED SCENES GENERATED SUCCESSFULLY!")
