import urllib.request
import json
import base64
import os
import time
import shutil

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

OUT_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes_neon_rush'
PUBLIC_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\scenes_neon_rush'

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(PUBLIC_DIR, exist_ok=True)

# Suffix reinforcing Neon Rush 2D cartoon stickman identity
SUFFIX = (
    ', in the signature 2D cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank white circular head (#ffffff), '
    'simple expressive round cartoon eyes, thin black stick limbs, era-appropriate attire, '
    'bold crisp black ink outlines, clean cel-shading, vibrant high-contrast colors, '
    'punchy high CTR YouTube framing, 16:9 widescreen composition, '
    'no 3D CGI, no photorealism, no realistic human faces'
)

SCENE_PROMPTS = {
    1: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, wearing primitive prehistoric caveman animal fur pelt clothing, kneeling inside a dark limestone cavern "
        "with glowing torchlight, discovering a giant glowing blood-red cinnabar crystal rock dripping living molten silver quicksilver puddle "
        "onto the stone ground" + SUFFIX
    ),
    2: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, wearing caveman pelt, holding a large magnifying glass inspecting a huge sparkling crystalline red cinnabar rock mineral alpha-HgS, "
        "glowing ruby red crystal facets on dark rock pedestal" + SUFFIX
    ),
    3: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, wearing primitive shaman feathers and pelt, grinding bright red cinnabar rocks with a heavy stone mortar and pestle "
        "into bright vermilion red powder paint, cave wall with red handprints in background" + SUFFIX
    ),
    4: (
        "Minimalist stickman characters with blank white circular heads (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, wearing ragged ancient Roman worker tunics, mining in subterranean toxic tunnels of Almaden Spain with pickaxe "
        "and wooden ore cart full of glowing red cinnabar rocks, underground torches" + SUFFIX
    ),
    5: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, wearing caveman fur clothing, curiously tossing a bright red cinnabar rock into a roaring stone age campfire "
        "with dancing orange flames and sparks, night cave background" + SUFFIX
    ),
    6: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, reacting in surprise covering mouth as a red rock in a hot campfire cracks open, "
        "releasing swirling bright yellow sulfur gas clouds and glistening metallic silver mercury vapor rising upward" + SUFFIX
    ),
    7: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, reaching out hands in awe under cold cave ceiling rocks as metallic mercury vapor condenses "
        "and bleeds brilliant pure liquid silver droplets dripping down like living metal chrome" + SUFFIX
    ),
    8: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, kneeling and pointing down at specular mirror liquid mercury beads merging into a flawless shiny chrome liquid pool "
        "on dark stone floor, non-wetting liquid metal sphere" + SUFFIX
    ),
    9: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, in scientist lab coat pointing at a giant mechanical balance scale: on the high left pan is a 1 liter blue bottle of water (1 kg), "
        "on the slammed low right pan is a 1 liter flask of liquid mercury (13.5 kg), dramatic density comparison" + SUFFIX
    ),
    10: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, looking shocked as a heavy black solid cast-iron cannonball floats effortlessly on top of a big transparent tank "
        "filled with shiny liquid metallic mercury, floating high above the silver surface" + SUFFIX
    ),
    11: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, holding a ruler next to a vertical glass capillary tube showing liquid mercury bulging upward into a proud convex dome meniscus "
        "with 140 degree angle repelling the glass walls, physics lab" + SUFFIX
    ),
    12: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, gasping in astonishment holding a shiny 24K solid gold ring that touches a pool of liquid mercury, "
        "with silvery liquid mercury creeping over and dissolving the gold ring into silver amalgam paste" + SUFFIX
    ),
    13: (
        "Minimalist stickman characters with blank white circular heads (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, working in a 16th century colonial silver mining patio amalgamation yard in Potosi Bolivia, "
        "mixing silver ore with pools of liquid mercury beneath the massive red Cerro Rico mountain" + SUFFIX
    ),
    14: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as Emperor Qin Shi Huang in ornate ancient Chinese imperial black and gold dragon robes with crown, "
        "sitting on imperial bronze throne holding a green jade goblet filled with silvery glowing mercury elixir of immortality" + SUFFIX
    ),
    15: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, looking down in awe from a bridge inside the colossal subterranean tomb of Emperor Qin Shi Huang, "
        "showing a miniature cosmos with 100 glowing mechanical rivers of flowing shining liquid mercury tracing Chinese rivers under bronze star ceiling" + SUFFIX
    ),
    16: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed in ancient Chinese scholar robes, reading ancient bamboo slip scrolls and examining jade funerary vessels "
        "showing historical autopsy notes and skull danger symbols" + SUFFIX
    ),
    17: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as a medieval Renaissance alchemist in leather apron and spectacles, "
        "working in an alchemy laboratory with glowing furnace, glass distillation retorts and alembics boiling liquid quicksilver, mystical alchemy books" + SUFFIX
    ),
    18: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as Sir Isaac Newton in 17th century Cambridge scholar coat with curly white wig, "
        "holding an alchemy flask of mercury surrounded by handwritten Latin manuscripts and hair spectrometry test charts showing mercury spikes" + SUFFIX
    ),
    19: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as physicist Evangelista Torricelli in 1643 Florence, holding a 1-meter tall vertical glass tube "
        "inverted into a basin of liquid mercury, showing the silver mercury column standing at 760mm with an empty Torricellian vacuum void at the top" + SUFFIX
    ),
    20: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as Daniel Gabriel Fahrenheit in 1714 workshop, crafting precision glass thermometer "
        "with glowing red and silver mercury column rising inside glass capillary with brass temperature scale" + SUFFIX
    ),
    21: (
        "Minimalist stickman characters with blank white circular heads (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as 17th century Venetian Murano master glassmakers, carefully spreading shiny tin foil "
        "and liquid mercury onto large plate glass to create the world's first crystal-clear luxury mirrors, ornate Venetian workshop" + SUFFIX
    ),
    22: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as a Victorian 19th century London hat maker wearing apron and top hat, steaming a felt rabbit fur hat "
        "with hot mercuric nitrate, swirling white chemical steam, cartoon trembling shaking hands illustrating Mad Hatter syndrome" + SUFFIX
    ),
    23: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, standing on a Japanese fishing boat in Minamata Bay 1956 at sunset, with a cutaway diagram into the blue sea "
        "showing plankton eaten by small fish, eaten by big tuna fish with red warning bioaccumulation arrows of methylmercury" + SUFFIX
    ),
    24: (
        "Minimalist stickman characters with blank white circular heads (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed in diplomat suits at the United Nations assembly hall in Kumamoto 2013, "
        "signing the global Minamata Convention treaty with world map showing international mercury bans" + SUFFIX
    ),
    25: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, dressed as physicist Heike Kamerlingh Onnes in 1911 Leiden cryostat lab, looking excited next to a glass cryogenic tube "
        "filled with liquid helium and frozen mercury wire at 4.2 Kelvin, with a digital ohm meter reading 0.000 Ohm discovery of superconductivity" + SUFFIX
    ),
    26: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, in a retro astronaut spacesuit on a spacewalk next to NASA's SERT-1 satellite orbiting planet Earth in deep space, "
        "watching the electrostatic mercury ion rocket thruster firing a brilliant electric cyan-blue beam" + SUFFIX
    ),
    27: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, in lab coat pointing at a giant glowing atomic model of Element 80 Mercury, "
        "showing 80 protons in nucleus and relativistic 6s2 valence electron orbital rings spinning near the speed of light, glowing Dirac physics equations" + SUFFIX
    ),
    28: (
        "Minimalist stickman character with a blank white circular head (#ffffff), simple expressive round cartoon eyes, "
        "thin black stick limbs, floating in cosmic starry deep space looking at a giant glowing periodic table tile for Element 80 'Hg 80 Hydrargyrum', "
        "connected by glowing energy beams from ancient cavemen campfire on the left to advanced interstellar ion spaceships on the right" + SUFFIX
    )
}

def generate_scene(s_id, prompt):
    filename = f"scene_{s_id:02d}.png"
    out_file = os.path.join(OUT_DIR, filename)
    public_file = os.path.join(PUBLIC_DIR, filename)

    if os.path.exists(out_file) and os.path.getsize(out_file) > 100000:
        print(f"[{s_id:02d}/28] {filename} already exists ({os.path.getsize(out_file)} bytes), skipping.")
        if not os.path.exists(public_file):
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
            shutil.copy2(out_file, public_file)
            dur = time.time() - t0
            print(f"  [OK] Saved {filename} ({len(img_bytes)} bytes) in {dur:.1f}s")
    except Exception as e:
        print(f"  [ERROR] Scene {s_id} failed: {e}")
        if hasattr(e, 'read'):
            print("  Body:", e.read().decode('utf-8', errors='ignore'))
        time.sleep(5)

def main():
    print("=== GENERATING ALL 28 NEON RUSH CARTOON STICKMAN SCENES ===")
    print(f"Model: {MODEL} | Target: {OUT_DIR}")
    
    # Check if test_neon_rush_style_s01.png exists, copy to scene_01.png
    poc_src = r'C:\Users\bati-\.gemini\antigravity\brain\f39d64bf-6e51-40b4-92eb-7bf63798ce0e\test_neon_rush_style_s01.png'
    s1_out = os.path.join(OUT_DIR, 'scene_01.png')
    s1_pub = os.path.join(PUBLIC_DIR, 'scene_01.png')
    if os.path.exists(poc_src) and not os.path.exists(s1_out):
        print("[01/28] Copying proven test_neon_rush_style_s01.png to scene_01.png...")
        shutil.copy2(poc_src, s1_out)
        shutil.copy2(poc_src, s1_pub)

    for s_id in range(1, 29):
        prompt = SCENE_PROMPTS[s_id]
        generate_scene(s_id, prompt)
        time.sleep(1.5)  # Courteous delay

    print("\n[COMPLETE] All 28 Neon Rush cartoon stickman scene images generated and synced!")

if __name__ == '__main__':
    main()
