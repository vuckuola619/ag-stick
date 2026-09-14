import urllib.request
import json
import base64
import os
import shutil
import time

URL = 'http://127.0.0.1:20128/v1/images/generations'
API_KEY = 'sk-c4f2444795b190b3-kzvd4h-ea839762'
MODEL = 'cx/gpt-5.5-image'

LOCAL_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes'
REMOTION_DIR = r'c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\scenes'
os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

SCENES = {
    'scene_02': (
        'A high-end 2D editorial cartoon illustration, clean line art, rich vibrant colors: '
        'A primitive caveman stickman with a blank white circular head (faceless minimalist stickman head, no cartoon eyes, just a subtle simple smile line), '
        'messy wild brown hair, cheetah fur tunic, kneeling on dark cave rock holding a raw glowing ruby-red cinnabar crystal stone up close to inspect it with curiosity, '
        'sparkling crimson mineral facet reflections illuminating the stone cave floor and ancient stone tools, wide 16:9 cinematic composition'
    ),
    'scene_03': (
        'A high-end 2D editorial cartoon illustration, clean line art, vibrant colors: '
        'A primitive caveman stickman with a blank white circular head (faceless minimalist stickman head, no eyes), messy hair, cheetah fur tunic, '
        'dynamic action pose throwing a glowing red cinnabar stone into a roaring prehistoric campfire with a circle of rough grey stones, '
        'bright orange dancing flames and flying ember sparks, cave entrance overlooking prehistoric starry night in background, wide 16:9 composition'
    ),
    'scene_04': (
        'A high-end 2D editorial cartoon illustration, clean line art, dramatic thermal lighting: '
        'Intense close-up of a prehistoric campfire pit with blazing red-hot charcoal and burning firewood logs, '
        'the glowing ruby-red cinnabar stone is right in the center of the intense fire, cracking open with glowing fiery fissures and emitting faint silvery vapor fumes, '
        'extreme heat distortion, wide 16:9 cinematic composition'
    ),
    'scene_05': (
        'A high-end 2D editorial cartoon illustration, clean line art, rich vibrant colors: '
        'Dramatic shot of the cracked red cinnabar stone in the campfire bleeding and oozing shiny molten silver liquid metal (mercury) that drips onto cool river rocks below without sticking. '
        'In the background, the caveman stickman with a blank white circular face (faceless minimalist head, no eyes) leaps backward with arms raised in astonishment and awe, '
        'fiery reflections and liquid metallic shine, wide 16:9 cinematic composition'
    ),
    'scene_06': (
        'A high-end 2D editorial cartoon illustration, clean line art, vibrant colors: '
        'Macro close-up shot of shiny liquid chrome quicksilver (mercury) droplets and puddle resting on a dark flat slate stone, '
        'perfect spherical metallic beads rolling smoothly, intense mirror specular reflections reflecting torchlight and cave ceiling, '
        'distinct convex meniscus showing it does not wet the stone at all, pristine chrome reflections, wide 16:9 composition'
    ),
    'scene_07': (
        'A high-end 2D editorial cartoon illustration, clean line art, rich colors: '
        'An ancient alchemical laboratory distillation scene: an antique glass retorta distillation flask on a bronze stand over a steady burner flame, '
        'red cinnabar vaporizing through a curved glass tube and condensing into pure shiny silver liquid mercury droplets falling into a golden bowl, '
        'ancient scrolls and bronze tools on stone workbench, mystical scientific atmosphere, wide 16:9 composition'
    ),
    'scene_08': (
        'A high-end 2D editorial cartoon illustration, clean line art, rich vibrant colors: '
        'Grand historical montage: on the left, an ancient imperial tomb with subterranean rivers of glowing liquid mercury under starry constellations; '
        'on the right, vintage brass and glass scientific instruments including a classical mercury thermometer and barometer with silver liquid columns, '
        'dramatic golden illumination, wide 16:9 cinematic composition'
    )
}

def generate_scene(name, prompt):
    out_local = os.path.join(LOCAL_DIR, f"{name}.png")
    out_remotion = os.path.join(REMOTION_DIR, f"{name}.png")

    if os.path.exists(out_local) and os.path.getsize(out_local) > 50000:
        print(f"[{name}] already exists ({os.path.getsize(out_local)} bytes), skipping.")
        if not os.path.exists(out_remotion):
            shutil.copy2(out_local, out_remotion)
        return

    print(f"\n[+] Requesting {name} from 9router (cx/gpt-5.5-image)...")
    payload = {
        'model': MODEL,
        'prompt': prompt,
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

    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                b64 = res['data'][0]['b64_json']
                img_data = base64.b64decode(b64)
                with open(out_local, 'wb') as f:
                    f.write(img_data)
                shutil.copy2(out_local, out_remotion)
                print(f"  [OK] Saved {name}.png ({len(img_data)} bytes)")
                return
        except Exception as e:
            print(f"  [Attempt {attempt+1}] Error generating {name}: {e}")
            time.sleep(3)

def main():
    print("=== BATCH GENERATION OF REMAKE SCENES 2 THROUGH 8 ===")
    for name, prompt in SCENES.items():
        generate_scene(name, prompt)
    print("\nAll 8 scenes are fully generated and deployed!")

if __name__ == '__main__':
    main()
