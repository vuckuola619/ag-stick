import urllib.request
import json
import base64
import os
import time
import shutil
import sys

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'
FALLBACK_MODEL = 'cx/gpt-5.6-luna-image'

LOCAL_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\demon-core-10min\assets\scenes_v2'
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\demon_core_v2\scenes'

os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

# Master standardized Neon Rush 2D cartoon stickman prompt suffix
SUFFIX = (
    ', in the signature 2D cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank white circular head (#ffffff), '
    'simple expressive round cartoon eyes, thin black stick limbs, era-appropriate attire, '
    'bold crisp 8-10px black ink outlines on every character, object, and environment, '
    'clean flat cel-shading, vibrant high-contrast colors, '
    'fully illustrated 2D cartoon background with hand-drawn comic line art, '
    'punchy high CTR YouTube framing, perfectly centered cinematic composition, 16:9 widescreen composition, '
    'strictly no 3D CGI, no photorealism, no realistic human faces, no chrome ray-tracing, '
    'no photographic textures, strictly no text, no letters, no labels, no watermark'
)

SCENE_PROMPTS = {
    1: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), "
        "simple expressive wide cartoon eyes, thin black stick limbs, wearing a 1940s white lab coat, "
        "standing centered looking down into an open heavy wooden crate holding a 2D cartoon gray plutonium metal sphere resting on a red velvet cushion, "
        "inside a 1945 secret Los Alamos wooden laboratory" + SUFFIX
    ),
    2: (
        "Minimalist 2D cartoon stickman military general with a blank white circular head (#ffffff), simple focused cartoon eyes, "
        "wearing 1940s olive-drab army uniform and tie, standing beside a large drafting map table showing Pacific theater islands, "
        "holding a stamped cancellation dossier, beside a 2D cartoon silhouette of a heavy B-29 bomber plane on an airfield tarmac" + SUFFIX
    ),
    3: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), simple curious cartoon eyes, "
        "wearing a white lab coat, standing centered outside a solitary rustic 1945 wooden research laboratory barrack nestled beneath towering red canyon cliffs "
        "of Pajarito Canyon New Mexico under a twilight dusky sky with glowing amber cabin windows" + SUFFIX
    ),
    4: (
        "Centered 2D cartoon diagram illustration of a gray plutonium metal sphere surrounded by orbiting cartoon neutron particles with bright electric cyan trajectory trails "
        "ricocheting between circular atomic nuclei, with bright comic fission bursts, beside a minimalist stickman scientist in white coat watching with a clipboard" + SUFFIX
    ),
    5: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), relaxed smiling cartoon eyes, "
        "wearing 1940s rolled-up collared shirt and tie, leaning casually against a wooden lab table while moving a 2D cartoon gray plutonium sphere with bare stick hands, "
        "analog vintage Geiger counter with a bouncing needle on the wooden table" + SUFFIX
    ),
    6: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), alarmed wide cartoon eyes, "
        "holding a long thin feather in his stick hands carefully reaching toward the curling tail of a gigantic sleeping fantasy dragon silhouette "
        "looming in the dark shadows of the wooden laboratory" + SUFFIX
    ),
    7: (
        "Centered 2D cartoon diagram illustration of a central metallic core encased inside a circular segmented shell barrier, "
        "bright glowing dashed projectile lines bouncing off the inner wall back toward the center, minimalist 2D cartoon stickman researcher inspecting with a magnifying glass" + SUFFIX
    ),
    8: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), focused cartoon eyes, "
        "wearing white lab coat and brown pants, holding a heavy rectangular dark gray tungsten carbide brick with both stick hands over a growing pyramid of gray bricks "
        "surrounding a 2D cartoon gray plutonium sphere on a sturdy wooden workbench" + SUFFIX
    ),
    9: (
        "Minimalist 2D cartoon stickman technician with a blank white circular head (#ffffff), tense sweating cartoon eyes, "
        "wearing retro horn-rimmed glasses and buttoned lab coat, staring intently at a vintage analog radiation meter with a bouncing indicator needle and glowing dial display, "
        "in a 1945 wooden laboratory at night" + SUFFIX
    ),
    10: (
        "Minimalist 2D cartoon science illustration of a dramatic exponential graph line soaring upward into a glowing warning red hazard zone, "
        "beside a centered minimalist stickman scientist with wide cartoon eyes gasping in shock with stick hands on his cheeks, "
        "laboratory blackboard with clean chalk grid in background" + SUFFIX
    ),
    11: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), wide-eyed cartoon wonder, "
        "wearing white lab coat, gently hovering a bare stick hand above a 2D cartoon gray metallic sphere that emits subtle shimmering warm heat ripple waves into the room air, "
        "on a wooden workbench in a 1945 research barrack" + SUFFIX
    ),
    12: (
        "Minimalist 2D cartoon stickman scientist working late at night at a wooden workbench under a single hanging vintage lamp, "
        "while in the background doorway a minimalist stickman soldier with a 1940s military helmet and slung rifle stands guard, "
        "rustic wooden wall laboratory interior" + SUFFIX
    ),
    13: (
        "Centered 2D cartoon composition showing a 2D gray plutonium sphere partially enclosed by heavy gray rectangular bricks on a wooden workbench, "
        "casting an ominous giant dragon claw shadow across the wooden laboratory wall behind it with warm amber desk lamp lighting" + SUFFIX
    ),
    14: (
        "Minimalist 2D cartoon young stickman scientist Harry Daghlian with a blank white circular head (#ffffff), focused cartoon eyes, "
        "wearing collared shirt and tie, walking late at night into an empty wooden research laboratory carrying a clipboard toward a central assembly workbench, "
        "illuminated by green-shaded overhead lamps" + SUFFIX
    ),
    15: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), terrified cartoon eyes with shock lines, "
        "losing grip as a heavy rectangular dark gray tungsten brick slips from his stick fingers mid-air directly downward toward an open assembly of bricks containing a gray metal core" + SUFFIX
    ),
    16: (
        "Minimalist 2D cartoon stickman scientist Harry Daghlian centered in dramatic silhouette, shielding his white circular head with an arm "
        "as a blinding brilliant explosion of electric cobalt-blue Cherenkov ionization light bursts from the central workbench, "
        "casting sharp cartoon shockwave rays across the wooden laboratory room" + SUFFIX
    ),
    17: (
        "Minimalist 2D cartoon stickman scientist with a blank white circular head (#ffffff), desperate wide cartoon eyes, "
        "lunging forward with bare stick arms to violently push over a tumbling wall of heavy rectangular bricks surrounding a glowing core, "
        "bricks scattering across the wooden floorboards with dynamic comic action dust" + SUFFIX
    ),
    18: (
        "Minimalist 2D cartoon medical diagram showing a stickman silhouette with right hand and chest glowing in intense hazard red and orange radiation crackle patterns, "
        "beside stylized floating cartoon DNA double helix strands breaking apart, dark chalkboard background" + SUFFIX
    ),
    19: (
        "Minimalist 2D cartoon stickman patient lying in a stark vintage 1945 hospital bed, beside a somber stickman doctor in a white coat bowing his head, "
        "somber vintage hospital room with a shaded window looking out at New Mexico desert mesa" + SUFFIX
    ),
    20: (
        "Minimalist 2D cartoon stickman scientist Louis Slotin with a blank white circular head (#ffffff), confident smiling cartoon eyes, "
        "wearing a vintage 1940s western denim shirt, necktie, and cowboy boots, standing proudly with arms folded beside a laboratory workbench with instruments" + SUFFIX
    ),
    21: (
        "Minimalist 2D cartoon scene showing eight distinct cartoon stickmen scientists with solid white circular heads gathered in a semi-circle around a central wooden workbench, "
        "wearing 1940s white lab coats, military uniforms, and office shirts, watching an experiment inside the wooden Omega Site laboratory" + SUFFIX
    ),
    22: (
        "Centered 2D cartoon cutaway illustration showing a gray plutonium sphere nestled inside a hollow bowl-shaped lower beryllium hemisphere, "
        "with a matching hollow upper beryllium dome hovering directly above it held by stickman hands, on a wooden workbench" + SUFFIX
    ),
    23: (
        "Close-up centered 2D cartoon illustration of two smooth gray beryllium dome halves separated by a narrow gap, "
        "with the flat steel blade of a yellow-handled flathead screwdriver wedged between the rims, held by a black stick cartoon hand, "
        "vintage wooden workbench in background" + SUFFIX
    ),
    24: (
        "High-tension 2D cartoon illustration: stickman scientist Louis Slotin with white circular head and wide horrified cartoon eyes, "
        "as the yellow flathead screwdriver slips diagonally downward and the two heavy gray beryllium dome halves slam shut flush together with a sharp metallic impact line" + SUFFIX
    ),
    25: (
        "Centered dramatic 2D cartoon explosion of brilliant electric cobalt-blue Cherenkov radiation light flooding the entire laboratory, "
        "illuminating the room and casting long sharp dynamic vector shadows from eight stickman scientists recoiling in sheer shock" + SUFFIX
    ),
    26: (
        "Minimalist 2D cartoon stickman scientist Louis Slotin with a white circular head (#ffffff) and courageous expression, "
        "bending over the workbench having just flung the upper beryllium dome clattering across the floorboards with bare stick hands, "
        "shielding seven recoiling stickmen behind him while clutching his burned stick hand" + SUFFIX
    ),
    27: (
        "Minimalist 2D cartoon stickman scientist Louis Slotin kneeling on the wooden floor holding a piece of white chalk, "
        "drawing circular chalk marks where various stickmen colleagues stand frozen in shock, overhead perspective of the 1945 wooden laboratory floor" + SUFFIX
    ),
    28: (
        "Minimalist 2D cartoon medical illustration: a somber 1946 hospital room silhouette with a centered hospital bed, "
        "beside a giant stylized cartoon hourglass with glowing radioactive sand grains trickling down into darkness" + SUFFIX
    ),
    29: (
        "Minimalist 2D cartoon illustration of three surviving stickman scientists in 1950s suits walking away from the wooden laboratory into the warm desert sun, "
        "casting long dark cartoon shadows across the dirt road toward the New Mexico desert mountains" + SUFFIX
    ),
    30: (
        "Minimalist 2D cartoon robotic steel mechanical claw arm operated by remote cables and pulleys, "
        "carefully lowering a beryllium dome onto a core from behind a thick lead-shielded concrete bunker wall, "
        "while a stickman technician observes safely through a periscope optical mirror" + SUFFIX
    ),
    31: (
        "Centered 2D cartoon vector graphic of a massive tropical atomic mushroom cloud column rising gracefully over a circular blue ocean atoll and silhouetted naval battleships, "
        "Operation Crossroads Bikini Atoll, vibrant fiery orange and yellow blast cap under a tropical sky" + SUFFIX
    ),
    32: (
        "Centered dramatic 2D cartoon composition: a single yellow flathead screwdriver lying quietly on an empty wooden workbench beside the silhouette of a resting gray metallic core, "
        "framed against a starry New Mexico night sky through an open wooden laboratory window" + SUFFIX
    ),
}

def generate_scene_image(scene_num: int, prompt: str, max_retries: int = 3) -> bool:
    s_id = f"{scene_num:02d}"
    out_file = os.path.join(LOCAL_DIR, f"scene_{s_id}.png")
    remotion_file = os.path.join(REMOTION_DIR, f"scene_{s_id}.png")

    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"[SKIP] Scene {s_id} already exists ({os.path.getsize(out_file)} bytes).", flush=True)
        if not os.path.exists(remotion_file):
            shutil.copyfile(out_file, remotion_file)
        return True

    # Special handling for Scene 01 if already perfected
    if scene_num == 1:
        prev_s1 = r'c:\Users\bati-\Documents\AG-Stick\projects\demon-core-10min\assets\scenes\scene_01.png'
        if os.path.exists(prev_s1) and os.path.getsize(prev_s1) > 1000000:
            print(f"[REUSE] Reusing perfected 2D Scene 01 ({os.path.getsize(prev_s1)} bytes)...", flush=True)
            shutil.copyfile(prev_s1, out_file)
            shutil.copyfile(prev_s1, remotion_file)
            return True

    payload = {
        'model': MODEL,
        'prompt': prompt,
        'size': '1672x941'
    }

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[GEN] Scene {s_id} | Attempt {attempt}/{max_retries} with {payload['model']}...", flush=True)
            t0 = time.time()
            req = urllib.request.Request(
                URL,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {API_KEY}'
                }
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                if 'data' in res and len(res['data']) > 0:
                    item = res['data'][0]
                    img_bytes = None
                    if 'b64_json' in item and item['b64_json']:
                        img_bytes = base64.b64decode(item['b64_json'])
                    elif 'url' in item and item['url']:
                        with urllib.request.urlopen(item['url'], timeout=60) as uresp:
                            img_bytes = uresp.read()

                    if img_bytes:
                        with open(out_file, 'wb') as f:
                            f.write(img_bytes)
                        shutil.copyfile(out_file, remotion_file)
                        dt = time.time() - t0
                        print(f"[SUCCESS] Scene {s_id} saved in {dt:.1f}s ({len(img_bytes)} bytes)", flush=True)
                        return True
                    else:
                        print(f"[WARN] Scene {s_id} returned empty image data.", flush=True)
        except Exception as e:
            print(f"[ERROR] Scene {s_id} attempt {attempt} failed: {e}", flush=True)
            if attempt == 2:
                payload['model'] = FALLBACK_MODEL
                print(f"[INFO] Switching to fallback model {FALLBACK_MODEL}", flush=True)
            time.sleep(3 * attempt)

    return False

def main():
    print("=======================================================================", flush=True)
    print("=== BATCH GENERATING THE DEMON CORE V2 (AUTHENTIC 2D NEON RUSH)     ===", flush=True)
    print("=== Model: cx/gpt-5.5-image via 9Router (port 20128)                ===", flush=True)
    print("=== Target: 32 Unified 2D Comic Scenes (Scenes 01 to 32)            ===", flush=True)
    print("=======================================================================\n", flush=True)

    total = len(SCENE_PROMPTS)
    success_count = 0

    for sc_num in range(1, total + 1):
        prompt = SCENE_PROMPTS[sc_num]
        print(f"\n--- Scene {sc_num:02d}/{total} ({(sc_num)/total*100:.1f}%) ---", flush=True)
        ok = generate_scene_image(sc_num, prompt)
        if ok:
            success_count += 1
        time.sleep(0.5)

    print(f"\n[FINISHED] The Demon Core v2 Batch Generation Complete: {success_count}/{total} scenes ready.", flush=True)

if __name__ == '__main__':
    main()
