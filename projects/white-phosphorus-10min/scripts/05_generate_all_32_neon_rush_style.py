import urllib.request
import json
import base64
import time
import os
import shutil
from PIL import Image

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

LOCAL_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\assets\scenes'
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\white_phosphorus\scenes'
TEST_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\white-phosphorus-10min\assets\test_scenes'

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

# Master standardized Neon Rush 2D cartoon stickman prompt suffix
SUFFIX = (
    ', in the signature 2D cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank white circular head (#ffffff), '
    'simple expressive round cartoon eyes, thin black stick limbs, era-appropriate attire, '
    'bold crisp black ink outlines, clean cel-shading, vibrant high-contrast colors, '
    'punchy high CTR YouTube framing, perfectly centered cinematic composition, 16:9 widescreen composition, '
    'no 3D CGI, no photorealism, no realistic human faces'
)

SCENE_PROMPTS = {
    1: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), simple expressive wide cartoon eyes, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center holding a glowing brass lantern '
        'in front of a towering pyramid of wooden oak barrels leaking amber fluid in a dark German stone cellar, '
        'bold high-CTR comic callout text 1,500 GALLONS?!' + SUFFIX
    ),
    2: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), simple expressive scheming cartoon eyes, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center holding a glowing alchemical parchment '
        'inscribed with golden transmutation circles and a glowing yellow urine droplet turning into shiny gold coins, '
        'surrounded by antique alchemical retorts and amber flasks with bold comic callout text PEE INTO GOLD?' + SUFFIX
    ),
    3: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), funny cartoon dizzy spiral eyes, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center pinching his nose with one stick hand '
        'while holding a wooden paddle stirring a gigantic bubbling wooden vat of murky fermented urine with bright toxic green bubbles '
        'and swirling neon green stink fume clouds rising, dark cellar background with cobwebs and skull bottles, '
        'bold high-CTR comic callout text STINK INTENSE!' + SUFFIX
    ),
    4: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), simple expressive wide cartoon eyes, '
        'thin black stick limbs, wearing 17th century alchemist leather apron, standing in center holding an iron ladle, '
        'boiling thick gooey pitch-black tar syrup in a giant black iron cauldron over a roaring stone hearth campfire with bright dancing orange flames '
        'and flying heat embers, dark alchemical workshop background, bold high-CTR comic callout text BOILING TO TAR!' + SUFFIX
    ),
    5: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), intense focused cartoon eyes, '
        'thin black stick limbs, wearing 17th century alchemist leather apron, standing in center vigorously pumping giant dual leather bellows '
        'into a glowing white-hot blast furnace with a sealed clay retort reaching 1,200 degrees Celsius, intense orange heat sparks flying, '
        'workshop background with bold high-CTR comic callout text 1,200°C INFERNO!' + SUFFIX
    ),
    6: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), wide jaw-dropped cartoon shock eyes, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center leaning over a long curved glass alembic tube '
        'submerged in a cold water trough, watching mysterious ghost-like luminous green vapor creeping through the glass tubing, '
        'dark cellar workshop with bold high-CTR comic callout text GHOSTLY VAPOR!' + SUFFIX
    ),
    7: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), amazed sparkling cartoon eyes, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center gently cupping in his hands a waxy pale lump '
        'that radiates an intense, soft alien emerald-green glow illuminating his stick face in a dark cellar, '
        'bold high-CTR comic callout text COLD GREEN FIRE!' + SUFFIX
    ),
    8: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), triumphant cheerful cartoon grin, '
        'thin black stick limbs, wearing 17th century alchemist scholar coat, standing in center holding high a glowing glass jar containing white phosphorus, '
        'beside a giant glowing periodic table card for Element 15 Phosphorus with symbol P, '
        'dark slate background with bold high-CTR comic callout text ELEMENT 15 UNLOCKED!' + SUFFIX
    ),
    9: (
        'Minimalist stickman alchemist with a blank white circular head (#ffffff), showman cartoon grin, '
        'thin black stick limbs, standing in center holding a glowing green quill pen writing glowing words on dark velvet royal curtains, '
        'while a funny stickman king wearing golden crown watches with popping wide cartoon eyes in royal palace hall, '
        'bold high-CTR comic callout text ROYAL GLOW SHOW!' + SUFFIX
    ),
    10: (
        'Minimalist stickman scientist with a blank white circular head (#ffffff), smart expressive cartoon eyes, '
        'thin black stick limbs, wearing modern white lab coat and black gloves, standing in center pointing at a giant glowing 3D tetrahedral P4 molecule model '
        'with 60-degree bent bonds and floating O2 oxygen molecules shedding bright green photon light bursts, '
        'science laboratory background with bold high-CTR comic callout text P4 MOLECULAR TRAP!' + SUFFIX
    ),
    11: (
        'Minimalist stickman scientist with a blank white circular head (#ffffff), panicked wide cartoon eyes leaping backward, '
        'thin black stick limbs, wearing white lab coat, reacting as a waxy white phosphorus lump on a lab table next to a thermometer reading 30°C (86°F) '
        'violently detonates into a roaring spontaneous orange fireball with thick white billowing smoke clouds, '
        'lab background with bold high-CTR comic callout text INSTANT FIRE: 30°C!' + SUFFIX
    ),
    12: (
        'Minimalist stickman scientist with a blank white circular head (#ffffff), astonished wide cartoon eyes, '
        'thin black stick limbs, wearing white lab coat, standing in center pointing at a clear glass beaker filled with water, '
        'where a submerged chunk of white phosphorus continues vigorously burning, bubbling, and sparkling beneath the water line, '
        'physics lab background with bold high-CTR comic callout text BURNS UNDERWATER?!' + SUFFIX
    ),
    13: (
        'Minimalist stickman natural philosopher Robert Boyle with a blank white circular head (#ffffff), focused cartoon eyes, '
        'thin black stick limbs, wearing late-17th-century scholar attire and white cravat, standing in center using brass tongs to place glowing cylindrical '
        'phosphorus sticks safely into glass apothecary bottles filled with water, workshop background with bold high-CTR comic callout text STORED IN WATER!' + SUFFIX
    ),
    14: (
        'Minimalist stickman inventor with a blank white circular head (#ffffff), joyful cartoon eyes, '
        'thin black stick limbs, wearing 1830s European waistcoat, standing in center striking a wooden friction match against a rough striker strip, '
        'producing an explosive burst of yellow sparks and a dancing bright match flame, '
        'dark studio background with bold high-CTR comic callout text THE FRICTION MATCH!' + SUFFIX
    ),
    15: (
        'Minimalist stickman with a blank white circular head (#ffffff), cheerful cartoon eyes, '
        'thin black stick limbs, wearing Victorian bowler hat, standing in center surrounded by towering colorful geometric stacks of vintage matchboxes '
        'labeled LUCIFERS and thousands of scattered wooden matchsticks forming an industrial wonder, '
        'retro factory background with bold high-CTR comic callout text MILLIONS OF MATCHES!' + SUFFIX
    ),
    16: (
        'Minimalist stickman Victorian factory tycoon with a blank white circular head (#ffffff), greedy cartoon grin, '
        'thin black stick limbs, wearing tall black top hat and holding bags of gold pounds, standing in center before a looming dark brick factory '
        'with tall smoking chimneys, as sinister toxic green vapor seeps from cracked basement windows, '
        'dark London industrial background with bold high-CTR comic callout text THE DEADLY SECRET!' + SUFFIX
    ),
    17: (
        'Minimalist stickman teenage Matchgirls with blank white circular heads (#ffffff), exhausted droopy cartoon eyes, '
        'thin black stick limbs, wearing ragged Victorian work aprons, standing at a long wooden dipping table dipping bundles of matchsticks '
        'into steaming vats of hot white phosphorus paste, London factory room with bold high-CTR comic callout text 14 HOURS A DAY!' + SUFFIX
    ),
    18: (
        'Minimalist stickman factory girl with a blank white circular head (#ffffff), sorrowful cartoon eyes, '
        'thin black stick limbs, wearing Victorian worker dress, standing in center holding a piece of bread with glowing green toxic dust caked on her fingers, '
        'surrounded by thick swirling phosphorus garlic vapor clouds, dark factory corner with bold high-CTR comic callout text POISON ON THE BREAD!' + SUFFIX
    ),
    19: (
        'Minimalist stickman factory worker with a blank white circular head (#ffffff), crying cartoon pain eyes, '
        'thin black stick limbs, wearing Victorian dress, standing in center clutching her swollen jaw with both hands as comic agony lightning bolts '
        'radiate from the throbbing tooth socket, Victorian dental room with bold high-CTR comic callout text THE ROT BEGINS!' + SUFFIX
    ),
    20: (
        'Minimalist stickman medical doctor in vintage physician coat standing in center pointing at a giant anatomical cartoon skull cross-section diagram, '
        'highlighting the lower jawbone decaying in necrotic green lattice with blood vessels strangled by bisphosphonates and warning crossbones, '
        'medical clinic background with bold high-CTR comic callout text PHOSSY JAW HORROR!' + SUFFIX
    ),
    21: (
        'Minimalist stickman girl with a blank white circular head (#ffffff), shocked terrified cartoon eyes, '
        'thin black stick limbs, sitting in center on a simple wooden bed in a completely dark Victorian tenement bedroom at night, '
        'where her lower jaw and mouth area glow with an intense, eerie radioactive-green phosphorescence in pitch darkness, '
        'tenement room with bold high-CTR comic callout text GLOWING JAWBONES!' + SUFFIX
    ),
    22: (
        'Minimalist stickman Victorian surgeon with a blank white circular head (#ffffff), somber cartoon eyes, '
        'thin black stick limbs, wearing vintage surgeon apron, standing in center holding a stainless steel surgical bone amputation saw '
        'next to an antique medical tray and anatomical diagram of complete lower jaw removal, '
        'operating theater background with bold high-CTR comic callout text SURGICAL BONE SAW!' + SUFFIX
    ),
    23: (
        'Group of minimalist stickman female match workers with blank white circular heads (#ffffff), determined fiery angry cartoon eyes, '
        'thin black stick arms thrusting bold protest banners reading STOP THE POISON and FAIR WAGES into the air, '
        'marching united in center down a cobblestone London street past Parliament, bold high-CTR comic callout text 1,400 GIRLS REVOLT!' + SUFFIX
    ),
    24: (
        'Minimalist stickman with a blank white circular head (#ffffff), triumphant cartoon eyes, '
        'thin black stick limbs, standing in center holding a giant 1906 Bern Convention international treaty scroll stamped with a huge red BANNED mark, '
        'next to a modern safe red matchbox labeled RED PHOSPHORUS SAFETY MATCH, '
        'government hall with bold high-CTR comic callout text WHITE PHOSPHORUS BANNED!' + SUFFIX
    ),
    25: (
        'Minimalist stickman soldier with a blank white circular head (#ffffff), alert focused cartoon eyes, '
        'wearing a simple 2D steel combat helmet, crouching in center in a battlefield trench behind sandbags, '
        'as military artillery shells marked WP detonate in fiery orange explosions in the background, '
        'battlefield with bold high-CTR comic callout text WILLIE PETE WARFARE!' + SUFFIX
    ),
    26: (
        'Minimalist stickman observer with a blank white circular head (#ffffff), wide shocked cartoon eyes, '
        'thin black stick limbs, standing in center watching a massive towering wall of blinding impenetrable white chemical smoke '
        'streaked with blazing yellow phosphorus incendiary sparks erupting across the night horizon, '
        'tactical battlefield with bold high-CTR comic callout text WHITE SMOKE SCREEN!' + SUFFIX
    ),
    27: (
        'Minimalist stickman scientist with a blank white circular head (#ffffff), wondrous sparkling cartoon eyes, '
        'thin black stick limbs, wearing lab coat, standing in center looking up in awe at a gigantic luminous DNA double helix '
        'where glowing phosphate nodes labeled P connect the entire spiral genetic ladder of life, '
        'cosmic science background with bold high-CTR comic callout text THE CODE OF LIFE!' + SUFFIX
    ),
    28: (
        'Minimalist stickman farmer with a blank white circular head (#ffffff), cheerful smiling cartoon eyes, '
        'thin black stick limbs, wearing straw hat and blue overalls, standing in center carrying a big sack of fertilizer marked P - PHOSPHATE, '
        'in the middle of a vast, golden sunlit wheat field with rich green sprouts, '
        'countryside sunrise background with bold high-CTR comic callout text FEEDING THE PLANET!' + SUFFIX
    ),
    29: (
        'Minimalist stickman analyst with a blank white circular head (#ffffff), smart expressive cartoon eyes, '
        'thin black stick limbs, standing in center beside a giant split globe diagram: left side showing golden wheat and green crops with a digital counter '
        'reading 4,000,000,000 FED, right side showing a steep upward economic bar graph, '
        'data center background with bold high-CTR comic callout text 4 BILLION FED!' + SUFFIX
    ),
    30: (
        'Minimalist stickman geologist with a blank white circular head (#ffffff), serious alarmed cartoon eyes, '
        'thin black stick limbs, wearing khaki explorer vest, standing in center pointing a red laser pointer at a world map highlighting Morocco '
        'with a flashing warning gauge reading 70% OF WORLD RESERVES and warning hazard sirens, '
        'command room with bold high-CTR comic callout text PEAK PHOSPHORUS!' + SUFFIX
    ),
    31: (
        'Minimalist stickman environmental engineer with a blank white circular head (#ffffff), proud cartoon smile, '
        'thin black stick limbs, wearing white hard hat and green safety vest, standing in center beside a high-tech modern wastewater bioreactor '
        'turning municipal liquid sewage into sparkling white crystalline struvite fertilizer pellets, '
        'clean modern eco-facility with bold high-CTR comic callout text PEE TO FERTILIZER!' + SUFFIX
    ),
    32: (
        'Grand climactic finale: Minimalist stickman with a blank white circular head (#ffffff), epic determined cartoon eyes, '
        'thin black stick limbs, standing boldly in the exact center of the frame, split down the middle: left side engulfed in roaring orange and green flames '
        'representing fire and war, right side blooming with electric cyan DNA helices and vibrant green wheat stalks representing life and food, '
        'holding high a glowing glass flask of Element 15, bold high-CTR comic callout text THE DEVIL’S ELEMENT!' + SUFFIX
    ),
}

def sync_existing_test_scenes():
    # Copy verified test scenes 1-4 if they exist
    for s_id in range(1, 5):
        test_file = os.path.join(TEST_DIR, f"test_scene_{s_id:02d}.png")
        local_file = os.path.join(LOCAL_DIR, f"scene_{s_id:02d}.png")
        remotion_file = os.path.join(REMOTION_DIR, f"scene_{s_id:02d}.png")
        if os.path.exists(test_file):
            print(f"[SYNC] Copying verified test_scene_{s_id:02d}.png to production assets...")
            shutil.copy2(test_file, local_file)
            shutil.copy2(test_file, remotion_file)

def generate_scene(s_id: int, prompt: str, max_retries: int = 3) -> bool:
    filename = f"scene_{s_id:02d}.png"
    out_file = os.path.join(LOCAL_DIR, filename)
    remotion_file = os.path.join(REMOTION_DIR, filename)

    # Check if already generated in 16:9 widescreen (width > 1600 and height > 900)
    if os.path.exists(out_file) and os.path.getsize(out_file) > 100000:
        try:
            with Image.open(out_file) as im:
                w, h = im.size
                if w >= 1600 and h >= 900 and (w / h) > 1.6:
                    print(f"[{s_id:02d}/32] {filename} is already 16:9 widescreen ({w}x{h}), skipping.")
                    if not os.path.exists(remotion_file):
                        shutil.copy2(out_file, remotion_file)
                    return True
        except Exception:
            pass

    print(f"\n[{s_id:02d}/32] Generating {filename} in Neon Rush 2D Style via 9Router...")
    payload = {
        'model': MODEL,
        'prompt': prompt,
        'n': 1,
        'size': '1024x1024'
    }

    for attempt in range(1, max_retries + 1):
        t0 = time.time()
        try:
            req = urllib.request.Request(
                URL,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {API_KEY}'
                }
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            b64 = data['data'][0]['b64_json']
            img_bytes = base64.b64decode(b64)

            with open(out_file, 'wb') as f:
                f.write(img_bytes)
            shutil.copy2(out_file, remotion_file)

            with Image.open(out_file) as im:
                res = im.size

            dur = time.time() - t0
            print(f"  [OK] Scene {s_id:02d} saved ({len(img_bytes)} bytes | {res[0]}x{res[1]}) in {dur:.1f}s")
            return True
        except Exception as e:
            print(f"  [WARN] Scene {s_id:02d} attempt {attempt} failed: {e}")
            time.sleep(3 * attempt)

    return False

def main():
    print("=======================================================================")
    print("=== BATCH GENERATING 32 NEON RUSH SCENES FOR WHITE PHOSPHORUS       ===")
    print("=== Model: cx/gpt-5.5-image | 16:9 Widescreen | Center Composition  ===")
    print("=======================================================================\n")

    sync_existing_test_scenes()

    success = 0
    for s_id in range(1, 33):
        prompt = SCENE_PROMPTS[s_id]
        ok = generate_scene(s_id, prompt)
        if ok:
            success += 1
        time.sleep(1.0)

    print(f"\n[COMPLETE] Batch Generation Finished: {success}/32 scenes ready in 16:9 widescreen!")

if __name__ == '__main__':
    main()
