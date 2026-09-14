import urllib.request
import json
import base64
import os
import shutil
import time

URL = "http://127.0.0.1:20128/v1/images/generations"
API_KEY = "sk-c4f2444795b190b3-kzvd4h-ea839762"
MODEL = "cx/gpt-5.5-image"

LOCAL_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scenes_8min"
REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\scenes_8min"
os.makedirs(LOCAL_DIR, exist_ok=True)
os.makedirs(REMOTION_DIR, exist_ok=True)

# 32 Scenes (4 scenes per Act, 8 Acts total)
# Core character rule: faceless minimalist stickman head (smooth blank white circular head, no cartoon eyes, subtle simple smile or nose curve line only)
# Ultra-rich environment, cinematic 16:9 editorial cartoon illustration, crisp clean linework, volumetric lighting

SCENES = {
    # ACT 1: Prehistoric Discovery & Cinnabar (7000 BC)
    "scene_01": (
        "A high-end 2D editorial graphic novel illustration, clean linework, rich atmospheric lighting: "
        "A primitive stickman caveman with a blank white circular head (faceless minimalist stickman head, no eyes, subtle smile line), "
        "messy wild prehistoric hair, cheetah fur pelt, holding a burning wooden torch while exploring a deep limestone cavern, "
        "discovering glistening veins of bright ruby-red crystalline cinnabar mineral embedded in the dark rugged rock wall, "
        "atmospheric cave dust particles in torchlight beam, wide 16:9 cinematic framing"
    ),
    "scene_02": (
        "A high-end 2D editorial graphic novel illustration, clean linework, vibrant crimson illumination: "
        "Close-up of a primitive stickman caveman with a blank white circular head (faceless minimalist stickman head, no eyes, slight curious expression), "
        "kneeling on dark cave stone holding a raw glowing crimson cinnabar crystal stone close to inspect it, "
        "geometric crystal facets reflecting glowing torchlight, scattered flint stones and prehistoric tools on ground, wide 16:9 framing"
    ),
    "scene_03": (
        "A high-end 2D editorial graphic novel illustration, clean linework, rich colors: "
        "Two primitive stickmen with blank white circular heads (faceless minimalist stickman heads, no eyes), "
        "using a large rough stone mortar and pestle to grind deep red cinnabar chunks into fine vibrant vermilion red cosmetic powder, "
        "crimson dust clouds rising gently, ancient cave dwelling with drying hides and woven baskets, wide 16:9 framing"
    ),
    "scene_04": (
        "A high-end 2D editorial graphic novel illustration, clean linework, ritual atmosphere: "
        "Ancient cave wall ceremonial painting scene: stickman shaman with blank white circular head (faceless minimalist head, feather in hair), "
        "using red cinnabar vermilion paint to press glowing crimson handprints and paint running mammoths and bison on a vast rough cave wall, "
        "dramatic firelight casting deep warm shadows, wide 16:9 framing"
    ),

    # ACT 2: The Campfire Accident & Living Silver
    "scene_05": (
        "A high-end 2D editorial graphic novel illustration, clean linework, dynamic comic action: "
        "Primitive stickman with a blank white circular head (faceless minimalist stickman head, no eyes, cheeky grin curve), "
        "playfully tossing a fist-sized glowing ruby-red cinnabar stone directly into a roaring prehistoric campfire built of rough river stones, "
        "bright orange flames, flying sparks and embers, starry prehistoric night visible through cave mouth, wide 16:9 framing"
    ),
    "scene_06": (
        "A high-end 2D editorial graphic novel illustration, clean linework, thermal intensity: "
        "Intense close-up inside the roaring prehistoric campfire: firewood logs glowing orange-white hot (>500°C), "
        "the red cinnabar rock in the center cracking apart with fiery glowing fissures, billowing thick pale yellow sulfur dioxide smoke fumes, "
        "heat waves and violent thermal distortion, wide 16:9 cinematic framing"
    ),
    "scene_07": (
        "A high-end 2D editorial graphic novel illustration, clean linework, magical transformation: "
        "Dramatic shot of the cracked red cinnabar stone bleeding and sweating droplets of bright molten liquid chrome silver (mercury), "
        "silvery beads dripping down onto cold flat river rocks below without sticking, cooling into liquid metallic pools, "
        "sparkling reflections of orange embers against liquid chrome, wide 16:9 framing"
    ),
    "scene_08": (
        "A high-end 2D editorial graphic novel illustration, clean linework, hilarious comic reaction: "
        "Stickman caveman with a blank white circular head (faceless minimalist stickman head, no eyes, mouth open in comic astonishment), "
        "leaping backward with arms flung up in sheer awe and shock as perfectly round shiny silver mercury beads roll and bounce across the dark rock floor, "
        "glowing embers and cave shadows, wide 16:9 framing"
    ),

    # ACT 3: The Impossible Physics of Quicksilver
    "scene_09": (
        "A high-end 2D editorial graphic novel illustration, clean linework, macro photography aesthetic: "
        "Macro close-up shot of pristine liquid mercury (quicksilver) droplets and puddles resting on dark polished black obsidian stone, "
        "perfect spherical metallic beads reflecting the surrounding room with mirror-chrome clarity, "
        "smooth fluid surface tension, dramatic studio spotlight reflections, wide 16:9 framing"
    ),
    "scene_10": (
        "A high-end 2D editorial graphic novel illustration, clean linework, scientific visual: "
        "Extreme density demonstration: a heavy solid black cast-iron cannonball floating effortlessly on the surface of a deep glass basin filled with liquid silver mercury, "
        "the iron ball sits high on the silvery liquid without sinking at all, clean minimalist laboratory setting, precise scientific aesthetic, wide 16:9 framing"
    ),
    "scene_11": (
        "A high-end 2D editorial graphic novel illustration, clean linework, physics diagram aesthetic: "
        "Extreme surface tension comparison: inside a transparent glass laboratory cylinder, liquid mercury pushes upward into a distinct convex rounded dome (convex meniscus), "
        "firmly repelling and refusing to wet the clear glass walls, next to a water cylinder showing concave meniscus for contrast, clean technical lighting, wide 16:9 framing"
    ),
    "scene_12": (
        "A high-end 2D editorial graphic novel illustration, clean linework, dramatic chemical reaction: "
        "Amalgamation visual: a solid shiny yellow gold wedding ring placed into a shallow pool of liquid mercury, "
        "the quicksilver liquid greedily creeping up and dissolving the solid gold ring, turning the golden surface into a silvery amalgamated slush, "
        "dramatic metallurgical reaction, wide 16:9 framing"
    ),

    # ACT 4: Imperial China & Qin Shi Huang (210 BC)
    "scene_13": (
        "A high-end 2D editorial graphic novel illustration, clean linework, grand imperial setting: "
        "Ancient Chinese palace throne room: Emperor Qin Shi Huang as a stickman with a blank white circular head wearing an elaborate imperial black and gold Hanfu crown and silk robes, "
        "seated on a dragon throne, Taoist alchemists with white circular heads bowing and presenting ornate jade boxes containing red cinnabar pills and crystal vials of silver mercury, wide 16:9 framing"
    ),
    "scene_14": (
        "A high-end 2D editorial graphic novel illustration, clean linework, awe-inspiring scale: "
        "The underground Terracotta Army of Qin Shi Huang: vast subterranean stone corridors filled with thousands of life-sized terracotta soldiers standing in strict formation, "
        "hanging bronze oil lamps casting long atmospheric shadows along the vaulted ancient ceilings, wide 16:9 cinematic framing"
    ),
    "scene_15": (
        "A high-end 2D editorial graphic novel illustration, clean linework, mythical engineering: "
        "The secret tomb chamber of Emperor Qin Shi Huang: a colossal underground cavern where the ceiling is studded with luminous glowing pearls forming astronomical constellations, "
        "and the floor features a detailed topographical relief map of China with 100 mechanically pumped flowing rivers and lakes of glowing liquid quicksilver, wide 16:9 framing"
    ),
    "scene_16": (
        "A high-end 2D editorial graphic novel illustration, clean linework, dramatic historical tragedy: "
        "Emperor Qin Shi Huang stickman collapsing onto his golden dragon couch, clutching his chest in agony, "
        "an ornate golden goblet knocked over on the floor spilling red wine mixed with silver mercury drops, shadowy palace curtains fluttering, tragic royal atmosphere, wide 16:9 framing"
    ),

    # ACT 5: Western Alchemy & Isaac Newton
    "scene_17": (
        "A high-end 2D editorial graphic novel illustration, clean linework, moody European alchemy: "
        "16th-century medieval alchemist laboratory: cluttered wooden workbench filled with blown-glass alembics, retorts, brass celestial globes, skull, stacks of leather grimoires, "
        "and bubbling glass flasks under warm glowing candlelight and moonbeams streaming through gothic arched windows, wide 16:9 framing"
    ),
    "scene_18": (
        "A high-end 2D editorial graphic novel illustration, clean linework, scientific alchemy: "
        "Distillation apparatus: red cinnabar mineral heating in a glass retort flask over a bronze charcoal furnace, "
        "ruby vapors condensing through a long curved glass neck and dripping pure sparkling liquid mercury drops into a crystal beaker, labeled with ancient alchemical symbols for Sulfur and Mercury, wide 16:9 framing"
    ),
    "scene_19": (
        "A high-end 2D editorial graphic novel illustration, clean linework, historical scholar: "
        "Sir Isaac Newton as a stickman with a blank white circular head and long powdered wig, seated in his Cambridge study at midnight, "
        "surrounded by optic prisms splitting rainbow light, handwritten calculus scrolls, and a smoking crucible on a small furnace emitting silver vapors, wide 16:9 framing"
    ),
    "scene_20": (
        "A high-end 2D editorial graphic novel illustration, clean linework, eerie paranoia: "
        "Close-up of Newton stickman with trembling hands holding an ink quill, furiously scribbling cryptic alchemical transmutation formulas in a massive journal, "
        "shadows dancing on bookshelf walls, a vial of silvery quicksilver reflecting the guttering candle flame, wide 16:9 framing"
    ),

    # ACT 6: The Scientific Revolution (Torricelli & Fahrenheit)
    "scene_21": (
        "A high-end 2D editorial graphic novel illustration, clean linework, Renaissance science: "
        "Evangelista Torricelli in Florence (1643) as a scholar stickman with blank white circular head and 17th-century Italian doublet, "
        "holding a tall one-meter clear glass tube filled with heavy liquid mercury, carefully inverting it into a stone basin of mercury, courtyard of Tuscan villa in background, wide 16:9 framing"
    ),
    "scene_22": (
        "A high-end 2D editorial graphic novel illustration, clean linework, eureka physics moment: "
        "The Torricellian vacuum experiment: the mercury column in the inverted glass tube drops and stabilizes at exactly 76 centimeters (760 mmHg), "
        "leaving a sparkling clear empty vacuum void at the sealed top tip, Torricelli stickman gesturing in scientific triumph, blueprint annotations overlaid, wide 16:9 framing"
    ),
    "scene_23": (
        "A high-end 2D editorial graphic novel illustration, clean linework, 18th-century precision: "
        "Daniel Gabriel Fahrenheit in 1714 workshop as a craftsman stickman with blank white circular head, "
        "calibrating the first precision mercury glass thermometer against ice water and boiling water, fine graduated measurement lines etched onto the glass tube, brass calipers and tools on table, wide 16:9 framing"
    ),
    "scene_24": (
        "A high-end 2D editorial graphic novel illustration, clean linework, Venetian craftsmanship: "
        "Venetian artisan workshop in the 17th century: craftsmen stickmen spreading shiny tin-mercury amalgam paste over large smooth sheets of flat crystal glass, "
        "peeling back the cloth to reveal a flawless, dazzling mirror reflection of the grand Venetian canal outside the workshop window, wide 16:9 framing"
    ),

    # ACT 7: The Poisonous Legacy (Mad Hatter & Minamata)
    "scene_25": (
        "A high-end 2D editorial graphic novel illustration, clean linework, Victorian industrial grit: "
        "19th-century felt hat factory: Victorian workers stickmen with blank white circular heads working in a gloomy, poorly ventilated brick warehouse, "
        "soaking raw beaver and rabbit fur in steaming vats of acidic mercury nitrate, thick toxic steam filling the rafters, wide 16:9 framing"
    ),
    "scene_26": (
        "A high-end 2D editorial graphic novel illustration, clean linework, expressive surrealism: "
        "The Mad Hatter character: an eccentric Victorian gentleman stickman with a blank white circular head wearing an oversized green top hat (marked 10/6), "
        "sitting at a chaotic tea party table with flying teacups, trembling jittery hands, and spinning whimsical clock gears representing neurological mercury madness, wide 16:9 framing"
    ),
    "scene_27": (
        "A high-end 2D editorial graphic novel illustration, clean linework, somber industrial tragedy: "
        "Minamata Bay in Kyushu, Japan (1950s): a sprawling industrial chemical factory on the shoreline discharging dark chemical effluent containing methylmercury into the serene coastal ocean water, "
        "wooden fishing boats docked nearby under an overcast grey sky, wide 16:9 cinematic framing"
    ),
    "scene_28": (
        "A high-end 2D editorial graphic novel illustration, clean linework, global milestone: "
        "Diplomatic assembly hall in Geneva/Kumamoto: international delegates stickmen with blank white circular heads at the United Nations signing ceremony for the Minamata Convention on Mercury, "
        "a golden quill signing the formal environmental treaty, world map on large display behind podium, wide 16:9 framing"
    ),

    # ACT 8: Space Age & Quantum Future
    "scene_29": (
        "A high-end 2D editorial graphic novel illustration, clean linework, cryogenic physics: "
        "Heike Kamerlingh Onnes in Leiden laboratory (1911) as a scientist stickman with blank white circular head, "
        "operating a brass liquid helium cryostat cooling a capillary of liquid mercury down to 4.2 Kelvin (-269°C), "
        "galvanometer needle suddenly dropping to zero showing the discovery of quantum superconductivity, wide 16:9 framing"
    ),
    "scene_30": (
        "A high-end 2D editorial graphic novel illustration, clean linework, aerospace engineering: "
        "NASA SERT-1 spacecraft in deep outer space orbiting the glowing blue curved Earth, "
        "firing its pioneering electrostatic ion thruster engine which emits a brilliant glowing cyan-blue plume of ionized mercury vapor propelling the satellite forward, wide 16:9 framing"
    ),
    "scene_31": (
        "A high-end 2D editorial graphic novel illustration, clean linework, futuristic quantum tech: "
        "Modern cutting-edge quantum physics laboratory: high-vacuum stainless steel chamber with magnetic levitation tracks, "
        "liquid metal mercury-gallium microfluidic circuit traces glowing softly on silicon wafers, clean room aesthetic with glass partitions, wide 16:9 framing"
    ),
    "scene_32": (
        "A high-end 2D editorial graphic novel illustration, clean linework, epic grand finale: "
        "Grand split-screen allegorical composition: on the left half, the primitive caveman stickman sitting by the glowing red campfire under a dark rocky cave; "
        "on the right half, a modern astronaut in a sleek spacesuit looking out at distant nebulae and stars; "
        "connecting both halves is a dynamic flowing spiral of liquid chrome mercury droplets and glowing atomic orbital rings (Hg 80), wide 16:9 cinematic framing"
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
        "model": MODEL,
        "prompt": prompt,
        "size": "1024x1024"
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                b64 = res["data"][0]["b64_json"]
                img_data = base64.b64decode(b64)
                with open(out_local, "wb") as f:
                    f.write(img_data)
                shutil.copy2(out_local, out_remotion)
                print(f"  [OK] Saved {name}.png ({len(img_data)} bytes)")
                return
        except Exception as e:
            print(f"  [Attempt {attempt+1}] Error generating {name}: {e}")
            time.sleep(4)

def main():
    print(f"=== BATCH GENERATION FOR 32 SCENES ({len(SCENES)} total) ===")
    for name, prompt in SCENES.items():
        generate_scene(name, prompt)
    print("\nAll 32 scenes generation loop complete!")

if __name__ == "__main__":
    main()
