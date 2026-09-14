import json, urllib.request, uuid, base64, os, time, sys

with open(r'C:\Users\bati-\.codex\auth.json', 'r') as f:
    codex_auth = json.load(f)

tokens = codex_auth.get('tokens', {})
acc_tok = tokens.get('access_token')
account_id = tokens.get('account_id')

IMG_DIR = os.path.join("remotion", "public", "assets", "images")
os.makedirs(IMG_DIR, exist_ok=True)

# 28 Scene prompts tailored for editorial photo-cutout collage documentary
SCENE_PROMPTS = {
    1: (
        "Vintage editorial photo-collage cut-out style: a glowing golden corporate trophy valuation certificate displaying '$47,000,000,000' "
        "dissolving into smoke and fluttering paper confetti above a modern glass skyscraper. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic rim lighting, isolated on solid dark charcoal background, no extra text"
    ),
    2: (
        "Vintage editorial photo-collage cut-out style: a giant antique brass hourglass filled with crisp 100-dollar bills rapidly draining into a fiery pit below. "
        "A calendar page showing '33 DAYS' with bold red tally marks. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic high contrast lighting, isolated on solid dark charcoal background, no extra text"
    ),
    3: (
        "Vintage editorial photo-collage cut-out style: an old weathered brick-and-mortar Manhattan commercial building clumsily disguised with fake glowing blue fiber optic cables, "
        "giant computer server racks, and silicon circuit boards peeling off the brick facade. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    4: (
        "Vintage editorial photo-collage cut-out style: an antique brass balance scale. On one side, a heavy cluster of 3,000 boring gray corporate office towers firmly grounded. "
        "On the other side, a small cluster of trendy glass offices floating high in the sky attached to giant inflated valuation balloons. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    5: (
        "Vintage editorial photo-collage cut-out style: an odd nostalgic still-life collage featuring a pair of padded baby crawler knee pads, "
        "a foaming glass beer mug next to an office beer keg tap, and a wooden ping pong paddle with ball. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    6: (
        "Vintage editorial photo-collage cut-out style: an industrial 2008 Brooklyn warehouse interior converted into makeshift office cubicles made of recycled cardboard, "
        "wooden pallets, and potted ferns, with an old receipt stamped 'PAID $3,000,000'. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    7: (
        "Vintage editorial photo-collage cut-out style: a bustling 2010 New York SoHo loft office with exposed brick, warm glowing Edison bulbs, "
        "a vibrant neon sign on the wall, and silhouettes of young tech founders working at communal wooden tables. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    8: (
        "Vintage editorial photo-collage cut-out style: an antique alchemist's glass beaker transforming dusty commercial real estate lease contracts into shimmering gold tech stock certificates "
        "with mathematical formulas and '20x MULTIPLE' diagrams floating around it. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    9: (
        "Vintage editorial photo-collage cut-out style: a massive futuristic military bazooka cannon marked 'VISION FUND $100B' firing huge bundles of hundred-dollar bills into the sky like fireworks. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    10: (
        "Vintage editorial photo-collage cut-out style: the interior backseat of a classic black Tokyo luxury taxi cab at night. Rain on the windows, neon Tokyo lights outside, "
        "and two hands sketching a bold contract on a glowing tablet screen with a golden handshake. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    11: (
        "Vintage editorial photo-collage cut-out style: a paper cutout puppet of a charismatic tech visionary with flowing hair standing atop a mountain of glowing neon unicorn horns "
        "surrounded by electric lightning bolts and torn newspaper headlines. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    12: (
        "Vintage editorial photo-collage cut-out style: a towering geyser of venture capital cash and gold coins blasting through the roof of a corporate glass office building into the stratosphere. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    13: (
        "Vintage editorial photo-collage cut-out style: a global world map with giant yellow industrial construction cranes rapidly stacking glass office floors higher and higher into the clouds at breakneck speed. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    14: (
        "Vintage editorial photo-collage cut-out style: a high-fashion luxury editorial collage featuring a golden megaphone, mystical healing crystals, "
        "and glossy magazine typography fragments about spiritual corporate wellness. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    15: (
        "Vintage editorial photo-collage cut-out style: a wild summer music festival in the woods with glamping tents, flying confetti, champagne bottles popping, "
        "a surfboard, and an electric guitar, blending wild festival hedonism with corporate lanyard badges. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    16: (
        "Vintage editorial photo-collage cut-out style: an old vintage commercial cash register smoking and overheating, spitting out an endless red receipt stamped with massive negative financial figures and red balance sheet charts. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    17: None, # Already generated as a masterpiece!
    18: (
        "Vintage editorial photo-collage cut-out style: an official SEC S-1 legal prospectus booklet opened to a mystical dedication page radiating strange golden spiritual light, "
        "surrounded by skeptical Wall Street analyst magnifying glasses. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    19: (
        "Vintage editorial photo-collage cut-out style: a corporate financial income statement where a giant pair of vintage golden scissors is physically cutting out and removing the word 'RENT' from the expense column. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    20: (
        "Vintage editorial photo-collage cut-out style: a giant metallic corporate sculpture of the two-letter word 'WE', with a retail barcode price tag hanging from it reading '$5,900,000' next to a signed buyout agreement. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    21: (
        "Vintage editorial photo-collage cut-out style: a sleek private luxury jet (Gulfstream G650) flying through the clouds, accompanied by a golden monarch's crown and a gavel symbolizing absolute 20:1 super-voting power. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    22: (
        "Vintage editorial photo-collage cut-out style: a chaotic Wall Street stock exchange trading floor with plummeting red stock line charts, "
        "torn stock tickers falling like autumn leaves, and stunned corporate investors holding their heads. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    23: (
        "Vintage editorial photo-collage cut-out style: a massive heavy steel bank vault door slamming shut with heavy chains and padlocks, "
        "trapping an empty cash briefcase with an emergency countdown timer at zero. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    24: (
        "Vintage editorial photo-collage cut-out style: a wooden puppet of a corporate CEO with all its strings cleanly severed by shears, "
        "packing a cardboard office moving box in an empty penthouse office with the skyline behind him. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    25: (
        "Vintage editorial photo-collage cut-out style: a giant financial rescue lifeboat labeled SoftBank pulling the founder onboard with a golden parachute, "
        "while thousands of office chairs and employee stock option certificates sink beneath the ocean waves. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    26: (
        "Vintage editorial photo-collage cut-out style: a dark abandoned modern coworking reception desk with flickering shattered neon lights, "
        "dusty neglected plants, and an official legal petition stamped 'CHAPTER 11 BANKRUPTCY' pinned to the desk. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    27: (
        "Vintage editorial photo-collage cut-out style: heavy concrete building blocks and wooden furniture refusing to be copied, "
        "with a giant digital computer mouse cursor arrow trying and failing to drag-and-drop a skyscraper across a physical landscape. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    ),
    28: (
        "Vintage editorial photo-collage cut-out style: a sleek futuristic electric semi truck perched atop a steep barren mountain road in the Utah desert, "
        "with its engine compartment open and visibly empty, rolling downward purely by gravity under a dramatic sunset sky. "
        "Deckle torn paper edges, tactile archival paper texture, dramatic lighting, isolated on solid dark charcoal background, no extra text"
    )
}

def refresh_token_if_needed():
    global acc_tok
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': tokens.get('refresh_token'),
        'client_id': 'app_EMoamEEZ73f0CkXaXp7hrann'
    }
    req = urllib.request.Request(
        'https://auth.openai.com/oauth/token',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req, timeout=10) as res:
        data = json.loads(res.read().decode('utf-8'))
        acc_tok = data['access_token']
        tokens['access_token'] = acc_tok
        tokens['refresh_token'] = data.get('refresh_token', tokens.get('refresh_token'))
        codex_auth['tokens'] = tokens
        with open(r'C:\Users\bati-\.codex\auth.json', 'w') as f:
            json.dump(codex_auth, f, indent=2)
        print("[*] Token refreshed successfully.")

def generate_scene(scene_id, prompt):
    filename = f"scene_{scene_id:02d}.png"
    out_path = os.path.join(IMG_DIR, filename)

    if scene_id == 17:
        print(f"[SKIP] Scene 17 already exists as master sprite.")
        return True

    print(f"\n[+] Requesting Scene {scene_id:02d} image generation...")
    headers = {
        "Authorization": f"Bearer {acc_tok}",
        "Content-Type": "application/json",
        "chatgpt-account-id": account_id,
        "originator": "codex_cli_rs",
        "User-Agent": "codex_cli_rs/0.136.0",
        "session_id": str(uuid.uuid4()),
        "x-client-request-id": str(uuid.uuid4()),
        "Accept": "text/event-stream, application/json"
    }

    tool_def = {
        "type": "image_generation",
        "output_format": "png",
        "size": "1024x1024"
    }

    body = {
        "model": "gpt-5.5",
        "instructions": "",
        "input": [
            {
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": prompt}]
            }
        ],
        "tools": [tool_def],
        "tool_choice": "auto",
        "parallel_tool_calls": False,
        "prompt_cache_key": str(uuid.uuid4()),
        "stream": True,
        "store": False,
        "reasoning": None
    }

    req = urllib.request.Request(
        "https://chatgpt.com/backend-api/codex/responses",
        data=json.dumps(body).encode('utf-8'),
        headers=headers
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as res:
            found = False
            while True:
                line = res.readline()
                if not line:
                    break
                line_str = line.decode('utf-8', errors='ignore').strip()
                if line_str.startswith('data:') and 'image_generation_call' in line_str:
                    try:
                        d = json.loads(line_str[5:].strip())
                        item = d.get('item', {})
                        if item.get('type') == 'image_generation_call' and item.get('result'):
                            b64 = item['result']
                            with open(out_path, "wb") as img_f:
                                img_f.write(base64.b64decode(b64))
                            print(f"[OK] Saved Scene {scene_id:02d} -> {out_path} ({len(b64)} bytes)")
                            found = True
                    except Exception as e:
                        print("Parse error:", repr(e))
            return found
    except urllib.error.HTTPError as e:
        print(f"[-] HTTPError on scene {scene_id}: {e.code}")
        if e.code in [401, 403]:
            print("[!] Refreshing token...")
            refresh_token_if_needed()
        return False
    except Exception as e:
        print(f"[-] Error on scene {scene_id}: {e}")
        return False

# Parse CLI args for targeted generation
target_scenes = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(1, 29))

print(f"Starting batch generation for scenes: {target_scenes}")
for sid in target_scenes:
    prompt = SCENE_PROMPTS.get(sid)
    if not prompt:
        continue
    success = False
    for attempt in range(3):
        success = generate_scene(sid, prompt)
        if success:
            break
        print(f"[!] Retry {attempt+1} for scene {sid} in 5s...")
        time.sleep(5)
    time.sleep(2)

print("\nBatch generation pass complete!")
