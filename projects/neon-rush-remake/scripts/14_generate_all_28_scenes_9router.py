import urllib.request
import json
import base64
import os
import time

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

OUT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes_consistent'
PUBLIC_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\scenes_consistent'

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(PUBLIC_DIR, exist_ok=True)

# Master consistent style suffix applied to EVERY prompt
STYLE_SUFFIX = (
    ', cinematic dark editorial documentary concept art, graphic novel realism, '
    'deep titanium navy shadows (#070d1a), dramatic volumetric rim lighting, '
    'consistent stylized faceless figures with minimal features, sleek anatomy, '
    'vibrant molten chrome liquid silver and glowing ember accents, high contrast, clean bold lines, '
    '16:9 widescreen composition, no logos, no text watermarks, no photorealistic faces'
)

SCENE_PROMPTS = {
    1: 'Prehistoric stone age cavemen exploring deep inside a dark limestone cavern with glowing flaming wooden torches, discovering massive glistening veins of blood-red crystalline cinnabar mineral embedded in the rugged rock walls' + STYLE_SUFFIX,
    2: 'Close-up macro scientific study of raw unrefined crystalline cinnabar rock alpha-HgS on dark stone, sparkling crimson ruby gemstone crystal facets illuminated by warm lantern light' + STYLE_SUFFIX,
    3: 'Ancient stone age shaman grinding crimson cinnabar crystals with a heavy stone mortar and pestle into an ultra-fine brilliant vermilion red ritual powder inside a torchlit ceremonial cave' + STYLE_SUFFIX,
    4: 'Ancient Roman enslaved miners working inside the toxic subterranean cinnabar mines of Almaden Spain, dark limestone tunnels, glowing blood-red cinnabar veins, wooden ore carts, pickaxes, atmospheric dust' + STYLE_SUFFIX,
    5: 'A curious stone age hunter tossing a fist-sized lump of crimson red cinnabar directly into a roaring prehistoric campfire with burning red logs, dancing orange flames, and flying heat sparks' + STYLE_SUFFIX,
    6: 'Thermal decomposition reaction in a cave fire, mineral cinnabar cracking open in 500 degree heat, releasing glowing yellow sulfur dioxide gas and vaporized metallic fumes drifting toward ceiling' + STYLE_SUFFIX,
    7: 'Condensation of quicksilver: hot metallic mercury vapor touching cold cavern limestone rock, condensing instantly and bleeding bright gleaming droplets of living liquid silver chrome' + STYLE_SUFFIX,
    8: 'Silvery metallic beads of pure liquid mercury coalescing together on a dark flat stone floor, flawless specular mirror reflection, perfectly spherical non-wetting chrome liquid drops' + STYLE_SUFFIX,
    9: 'Anomalous physics density demonstration in laboratory: a heavy mechanical balance scale with 1 liter beaker of blue water (1 kg) on high left pan and 1 liter flask of dense liquid mercury (13.5 kg) heavily tilting the right pan downward' + STYLE_SUFFIX,
    10: 'Hydrostatic density demonstration: a heavy solid cast-iron cannonball floating effortlessly on the surface of a deep container of liquid metallic mercury, bobbing high with 41% volume above silver surface' + STYLE_SUFFIX,
    11: 'Physics capillary experiment: a vertical clear glass tube showing liquid mercury pushing upward into a proud convex dome meniscus with 140 degree contact angle, fiercely repelling the glass walls' + STYLE_SUFFIX,
    12: 'Metallic amalgamation reaction: a pure 24K solid gold ring touching liquid mercury, with silver fluid creeping upward and dissolving the gold crystal lattice into silvery amalgam paste' + STYLE_SUFFIX,
    13: 'Colonial silver extraction in 16th century Potosi Bolivia: massive open-air patio amalgamation yard beneath Cerro Rico mountain, indigenous workers mixing crushed ore and mercury pools' + STYLE_SUFFIX,
    14: 'Emperor Qin Shi Huang of ancient China seated on an ornate imperial bronze throne, wearing black and gold dragon robes, holding an alchemical jade cup containing toxic mercury elixir of immortality' + STYLE_SUFFIX,
    15: 'The colossal underground cosmic tomb of First Emperor Qin Shi Huang: miniature cosmos with 100 mechanical flowing rivers of pure shining liquid mercury tracing Chinese rivers under bronze star ceiling' + STYLE_SUFFIX,
    16: 'Ancient Chinese bamboo slip historical records and autopsy scrolls from Sima Qian Shiji detailing the imperial records of mercury poisoning, jade funerary vessels, and toxic vapor tests' + STYLE_SUFFIX,
    17: 'Medieval European alchemist laboratory: Paracelsus Tria Prima, glass alembics and retorts distilling boiling quicksilver over a glowing furnace, glowing mystical glassware and manuscripts' + STYLE_SUFFIX,
    18: 'Sir Isaac Newton in his dark Cambridge laboratory in 1693, surrounded by alchemical manuscripts on mercury transmutation, distillation retorts, and forensic hair spectrometry charts' + STYLE_SUFFIX,
    19: 'Historical Florence 1643 physics experiment by Evangelista Torricelli: a one-meter glass tube inverted in a mercury basin, showing the silver column standing at 760mm with a pure vacuum void at the top' + STYLE_SUFFIX,
    20: 'Daniel Gabriel Fahrenheit in 1714 crafting precision glass thermometer: fine glass capillary tube with bright liquid mercury column expanding linearly, brass degree measurement scale' + STYLE_SUFFIX,
    21: 'Venetian master craftsmen in 17th century Murano glass workshops spreading flat tin-mercury amalgam onto plate glass, creating the first distortion-free luxury specular mirrors' + STYLE_SUFFIX,
    22: 'Victorian felt hat manufacturing workshop in 19th century London: workers steaming rabbit fur with toxic mercuric nitrate, rising white fumes, workers suffering from erethism tremors' + STYLE_SUFFIX,
    23: 'Minamata Bay Japan 1956 marine tragedy: coastal fishing boats at twilight, stylized ocean cross-section showing toxic methylmercury bioaccumulating upward through fish and marine food chain' + STYLE_SUFFIX,
    24: 'United Nations UNEP diplomatic assembly hall in Kumamoto 2013: international delegates signing the global Minamata Convention treaty on mercury, world treaty ban map' + STYLE_SUFFIX,
    25: 'Dutch physicist Heike Kamerlingh Onnes in 1911 Leiden cryostat laboratory: cooling mercury with liquid helium to 4.2 Kelvin, discovering superconductivity with electrical resistance dropping to absolute zero' + STYLE_SUFFIX,
    26: 'NASA SERT-1 satellite in 1964 orbiting planet Earth in dark space: electrostatic mercury ion rocket thruster emitting a glowing electric cyan-blue exhaust beam at 30 km/s velocity' + STYLE_SUFFIX,
    27: 'Quantum electrodynamics physics visualization: relativistic Dirac electron atomic orbital model of element 80, showing contracted 6s2 valence shells moving near light speed, keeping mercury liquid' + STYLE_SUFFIX,
    28: 'Cosmic epilogue: glowing periodic table element card for Element 80 Hydrargyrum (Hg) suspended in starry deep space, connected by light beams from ancient cave fires to interstellar ion propulsion' + STYLE_SUFFIX
}

def generate_scene(s_id, prompt):
    filename = f"scene_{s_id:02d}.png"
    out_file = os.path.join(OUT_DIR, filename)
    public_file = os.path.join(PUBLIC_DIR, filename)

    if os.path.exists(out_file) and os.path.getsize(out_file) > 100000:
        print(f"[{s_id:02d}/28] {filename} already exists ({os.path.getsize(out_file)} bytes), skipping.")
        if not os.path.exists(public_file):
            import shutil
            shutil.copy2(out_file, public_file)
        return

    print(f"\n[{s_id:02d}/28] Generating {filename} via 9Router ({MODEL})...")
    payload = {
        'model': MODEL,
        'prompt': prompt,
        'n': 1,
        'size': '1024x1024'
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
    )

    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            b64 = data['data'][0]['b64_json']
            img_bytes = base64.b64decode(b64)
            with open(out_file, 'wb') as f:
                f.write(img_bytes)
            import shutil
            shutil.copy2(out_file, public_file)
            dur = time.time() - t0
            print(f"  [OK] Saved {filename} ({len(img_bytes)} bytes) in {dur:.1f}s")
    except Exception as e:
        print(f"  [ERROR] Scene {s_id} failed: {e}")
        if hasattr(e, 'read'):
            print("  Body:", e.read().decode('utf-8', errors='ignore'))
        # Wait 5s before next attempt
        time.sleep(5)

def main():
    print("=== GENERATING ALL 28 CONSISTENT SCENES VIA 9ROUTER CODEX ===")
    print(f"Model: {MODEL} | Target: {OUT_DIR}")
    
    # Check if scene 4 and scene 9 exist from test
    s4_test = os.path.join(OUT_DIR, 'scene_04_almaden_mine.png')
    s4_target = os.path.join(OUT_DIR, 'scene_04.png')
    if os.path.exists(s4_test) and not os.path.exists(s4_target):
        import shutil
        shutil.copy2(s4_test, s4_target)
        shutil.copy2(s4_test, os.path.join(PUBLIC_DIR, 'scene_04.png'))

    s9_test = os.path.join(OUT_DIR, 'scene_09_density_scale.png')
    s9_target = os.path.join(OUT_DIR, 'scene_09.png')
    if os.path.exists(s9_test) and not os.path.exists(s9_target):
        import shutil
        shutil.copy2(s9_test, s9_target)
        shutil.copy2(s9_test, os.path.join(PUBLIC_DIR, 'scene_09.png'))

    for s_id in range(1, 29):
        prompt = SCENE_PROMPTS[s_id]
        generate_scene(s_id, prompt)
        time.sleep(2)  # courteous gap between requests

    print("\n[COMPLETE] All 28 consistent scene images processed!")

if __name__ == '__main__':
    main()
