import json
import os

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium"
SCRIPT_DIR = os.path.join(PROJECT_DIR, "script")
os.makedirs(SCRIPT_DIR, exist_ok=True)

# Visual Style Master Suffix (Dossier Zero 2D Stickman Noir - Anti AI Slop)
STICKMAN_NOIR_SUFFIX = (
    ', in the signature 2D stickman noir illustration style of The Dossier Zero, '
    'featuring a minimalist 2D cartoon stickman character with a blank solid white circular head (#ffffff), '
    'expressive cartoon eyes, thin black stick limbs, era-accurate clothing, '
    'set inside a gritty cinematic atmospheric environment with deep obsidian void (#0A0D14) background, '
    'dramatic chiaroscuro lighting, intense glowing electric cyan and Cherenkov blue (#00F0FF) radioluminescence, '
    'caution hazard yellow (#FFE600) accents, bold crisp vector outlines, clean cel-shading, '
    '16:9 widescreen composition, high-contrast YouTube framing, '
    'strictly zero text, no letters, no words, no numbers, no watermarks, no speech bubbles, no photorealism'
)

scenes_data = [
    # ==========================================
    # ACT 1: THE ABANDONED CLINIC & THE BREACH (Scenes 01–06)
    # ==========================================
    {
        "scene_id": "01",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "THE FORGOTTEN VAULT",
        "voiceover_text": "In the heart of central Brazil, on Avenida Paranaiba in Goiania, an abandoned private radiotherapy clinic stood in silent ruin. Following a bitter legal feud in 1985, the owners had walked away, leaving behind a heavily shielded subterranean treatment room containing an active teletherapy unit.",
        "word_count": 44,
        "visual_description": "Derelict abandoned radiotherapy clinic Instituto Goiano de Radioterapia at twilight, crumbling concrete walls, cracked windows, overgrown vines, stickman investigator holding a flashlight illuminating the shadowy entryway.",
        "camera_shot": "wide",
        "camera_motion": "slow_push_in",
        "telemetry": {"year": 1987, "location": "GOIANIA // IGR RUINS", "radiation_cpm": 35, "dose_rate": "0.12 uGy/h", "status": "ABANDONED CLINIC"},
        "codex_image_prompt": "Abandoned crumbling medical radiotherapy clinic building at night with broken windows and cracked concrete walls, overgrown wild weeds, illuminated by a single warm beam from a minimalist stickman investigator in trenchcoat holding a flashlight from the shadowy corner" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "02",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "SEPTEMBER 13: THE INTRUSION",
        "voiceover_text": "On Sunday, September 13, 1987, two local scavengers, Roberto dos Santos Alves and Wagner Mota Pereira, breached the unsecured clinic perimeter with a rusted wheelbarrow and basic hand tools, searching for scrap metal to sell to neighborhood junkyards for food money.",
        "word_count": 42,
        "visual_description": "Two minimalist 2D scavengers in ragged clothes creeping through a broken doorway into a dark basement vault pushing a squeaking metal wheelbarrow, dust motes in flashlight beams.",
        "camera_shot": "medium_low",
        "camera_motion": "tracking_right",
        "telemetry": {"year": 1987, "location": "AVENIDA PARANAIBA", "radiation_cpm": 85, "dose_rate": "0.35 uGy/h", "status": "PERIMETER BREACH"},
        "codex_image_prompt": "Two minimalist stickman scavengers in ragged clothes entering a dark dilapidated underground clinic basement pushing a squeaky metal wheelbarrow, holding rusted screwdrivers, flashlights casting dramatic chiaroscuro shadows across cracked tile floors" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "03",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "THE MASSIVE LEAD HEAD",
        "voiceover_text": "Deep inside the basement treatment bunker, they found an Italian-made Cesapan radiation therapy machine. Believing the massive lead shielding assembly was valuable scrap lead, they used wrenches, crowbars, and hammers to detach the heavy rotating cylindrical head from its mechanical mountings.",
        "word_count": 42,
        "visual_description": "Scavengers unbolting a massive vintage medical teletherapy gantry assembly, industrial mechanical gears, heavy lead cylinder being detached, metallic sparks and dust.",
        "camera_shot": "medium_closeup",
        "camera_motion": "pan_up",
        "telemetry": {"year": 1987, "location": "IGR TELETHERAPY ROOM", "radiation_cpm": 1250, "dose_rate": "4.5 mGy/h", "status": "MECHANICAL DISASSEMBLY"},
        "codex_image_prompt": "Minimalist stickman scavengers unbolting a massive industrial vintage teletherapy machine gantry, heavy metallic cylindrical lead treatment head suspended by iron chains, industrial mechanical gears, dramatic high contrast shadows" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "04",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "THE 100-KG DEATH HAUL",
        "voiceover_text": "Straining under the immense weight of the hundred-kilogram lead assembly, the two men loaded the heavy cylinder into their wheelbarrow and wheeled it across the sunbaked asphalt streets of Goiania, taking it directly to Roberto Alves' modest residential home on Rua 57.",
        "word_count": 42,
        "visual_description": "Scavengers pushing an overloaded wheelbarrow carrying the lead cylinder down a sunbaked Brazilian suburban street, houses in background, long dramatic shadows.",
        "camera_shot": "wide",
        "camera_motion": "tracking_left",
        "telemetry": {"year": 1987, "location": "RUA 57 // SUBURBAN TRANSIT", "radiation_cpm": 4500, "dose_rate": "15.0 mGy/h", "status": "TRANSIT THROUGH PUBLIC STREETS"},
        "codex_image_prompt": "Minimalist stickman scavengers pushing a heavy squeaking wheelbarrow containing a massive dull gray lead cylinder down a hot deserted urban asphalt street with telephone poles and modest brick houses, long dramatic sunset shadows" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "05",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "ACUTE RADIATION ONSET",
        "voiceover_text": "That very evening, both men began vomiting violently and suffered debilitating gastrointestinal cramps. Thinking they had eaten bad mangoes, they rested, unaware that invisible gamma rays were already destroying their cellular DNA and burning severe blisters into their hands.",
        "word_count": 39,
        "visual_description": "Stickman scavenger doubled over in agony on a backyard porch, clutching stomach, vomiting, hands glowing with painful red radiation burn marks, dark night void.",
        "camera_shot": "medium",
        "camera_motion": "slow_push_in",
        "telemetry": {"year": 1987, "location": "RESIDENCE RUA 57", "radiation_cpm": 18000, "dose_rate": "1.2 Gy/h", "status": "PRODROMAL RADIATION SICKNESS"},
        "codex_image_prompt": "Minimalist stickman clutching his stomach and doubled over in pain on the porch of a modest house at night, glowing red burn patches on hands and fingers, deep chiaroscuro lighting, dark gloomy midnight sky" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "06",
        "act": 1,
        "act_title": "ACT 1: THE ABANDONED CLINIC & THE BREACH",
        "kinetic_hook_headline": "PUNCTURING THE CAPSULE",
        "voiceover_text": "Over the next three days, Roberto continued hammering at the cylinder in his backyard. Finally, driving a sharp screwdriver into the protective aperture, he punctured the thin iridium window of the internal capsule—releasing the deadliest radioactive contaminant in South American history.",
        "word_count": 40,
        "visual_description": "Close up of stickman hands driving a sharp screwdriver into a lead capsule aperture, a thin needle-like beam of bright glowing electric cyan blue light piercing through the opening.",
        "camera_shot": "extreme_closeup",
        "camera_motion": "crash_zoom",
        "telemetry": {"year": 1987, "location": "RUA 57 // WORKBENCH", "radiation_cpm": 85000, "dose_rate": "8.5 Gy/h", "status": "CONTAINMENT BREACH"},
        "codex_image_prompt": "Dramatic macro closeup of a screwdriver puncturing the metallic window of a heavy lead cylinder, a sharp intense beam of radiant electric cyan blue light bursting out from the punctured hole into the dark room, metallic sparks" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 2: THE BLUE GLOW IN THE JUNKYARD (Scenes 07–12)
    # ==========================================
    {
        "scene_id": "07",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "RUA 26-A JUNKYARD",
        "voiceover_text": "On Friday, September 18, Roberto sold the punctured lead cylinder to Devair Alves Ferreira, the owner of a bustling scrap metal yard on Rua 26-A in the Aeroporto district. Devair paid for the scrap and hauled the heavy device into his garage.",
        "word_count": 42,
        "visual_description": "Stickman junkyard owner Devair Ferreira inspecting scrap metal in a cluttered junkyard with piles of rusted iron and discarded cars, exchanging paper cash with scavenger.",
        "camera_shot": "medium_wide",
        "camera_motion": "pan_right",
        "telemetry": {"year": 1987, "location": "RUA 26-A // JUNKYARD", "radiation_cpm": 95000, "dose_rate": "12.0 Gy/h", "status": "SCRAP METAL ACQUISITION"},
        "codex_image_prompt": "Cluttered junkyard on Rua 26-A with towering piles of rusted car engines and scrap metal, minimalist stickman junkyard owner handing cash to scavenger beside an open garage shed, industrial chiaroscuro atmosphere" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "08",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "THE MIRACLE IN THE DARK",
        "voiceover_text": "That night, stepping into the unlit garage, Devair stopped dead in his tracks. From inside the punctured lead cylinder, a mesmerizing, ethereal blue light was emanating into the darkness, glowing like a mystical gemstone from another realm.",
        "word_count": 38,
        "visual_description": "Dark garage interior, stickman junkyard owner standing awestruck in doorway, staring at a brilliant incandescent electric blue luminescence pouring out of a metal cylinder on the workbench.",
        "camera_shot": "wide",
        "camera_motion": "slow_push_in",
        "telemetry": {"year": 1987, "location": "DEVAIR GARAGE // MIDNIGHT", "radiation_cpm": 120000, "dose_rate": "18.5 Gy/h", "status": "RADIOLUMINESCENCE OBSERVED"},
        "codex_image_prompt": "Pitch dark garage room where a heavy metallic cylinder rests on a wooden workbench, casting a brilliant ethereal glowing electric cyan and deep blue light illuminating the room, minimalist stickman staring in absolute awe" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "09",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "50.9 TERABECQUERELS",
        "voiceover_text": "What Devair was witnessing was not magic. It was fifty point nine terabecquerels—one thousand three hundred and seventy-five Curies—of Caesium-137 chloride. The intense radiation was ionizing surrounding air molecules and atmospheric moisture, triggering brilliant Cherenkov luminescence and radioluminescence.",
        "word_count": 42,
        "visual_description": "Scientific anatomical cutaway of Caesium-137 chloride salt powder: crystal lattice emitting glowing beta particles and gamma rays, blue photon excitation shockwaves in air, dark void.",
        "camera_shot": "closeup_schematic",
        "camera_motion": "orbital",
        "telemetry": {"isotope": "CAESIUM-137", "activity": "50.9 TBq (1,375 Ci)", "radiation_cpm": 250000, "dose_rate": "35.0 Gy/h", "status": "ISOTOPIC IONIZATION"},
        "codex_image_prompt": "Scientific cinematic cross-section of glowing Caesium-137 chemical salt crystals, emitting intense pulsing electric blue Cherenkov radiation waves and ionizing gamma rays, deep obsidian void background" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "10",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "THE SACRED POWDER",
        "voiceover_text": "Convinced he had discovered a supernatural or holy substance with miraculous healing powers, Devair brought the cylinder into his living room. Over the next three days, he invited curious neighbors, relatives, and scrap dealers to marvel at the enchanted blue light.",
        "word_count": 42,
        "visual_description": "Devair's modest living room at night, family members and neighbors gathered around a small table gazing at the glowing blue powder, stickman children clapping, warm domestic atmosphere juxtaposed with lethal blue glow.",
        "camera_shot": "medium",
        "camera_motion": "slow_pan_left",
        "telemetry": {"year": 1987, "location": "DEVAIR RESIDENCE", "radiation_cpm": 310000, "dose_rate": "42.0 Gy/h", "status": "PUBLIC DISPLAY IN RESIDENCE"},
        "codex_image_prompt": "Crowded modest living room at night where several minimalist stickman adults and children gather around a wooden coffee table, gazing fascinated at a small bowl of intensely glowing blue powder, eerie cyan shadows on walls" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "11",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "THE SLEDGEHAMMER BLOW",
        "voiceover_text": "On September 21, eager to extract the valuable lead casing, Devair ordered his two junkyard employees, Israel Baptista dos Santos and Admilson Alves de Souza, to smash the remaining mechanism apart using heavy sledgehammers and cold chisels in the open yard.",
        "word_count": 42,
        "visual_description": "Two stickman junkyard workers swinging heavy iron sledgehammers down onto the lead cylinder, sparks and fine glowing dust spraying into the air, scrap yard piles around them.",
        "camera_shot": "medium_action",
        "camera_motion": "shake_impact",
        "telemetry": {"year": 1987, "location": "JUNKYARD YARD FLOOR", "radiation_cpm": 450000, "dose_rate": "65.0 Gy/h", "status": "MECHANICAL FRACTURE"},
        "codex_image_prompt": "Two minimalist stickman laborers swinging heavy iron sledgehammers down onto a cracked lead cylinder in a dusty scrapyard, explosive burst of glowing electric blue dust particles scattering into the air, high dynamic contrast" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "12",
        "act": 2,
        "act_title": "ACT 2: THE BLUE GLOW IN THE JUNKYARD",
        "kinetic_hook_headline": "THE INVISIBLE CLOUD",
        "voiceover_text": "The violent impacts pulverized the highly soluble caesium chloride salt into a fine microscopic dust. As the men swung their hammers, breathing heavily in the tropical heat, billions of radioactive particles coated their clothing, entered their lungs, and settled onto the soil.",
        "word_count": 42,
        "visual_description": "Microscopic view of glowing blue radioactive dust clouds drifting into stickman mouths and clothing, settling on dirt ground, glowing cyan mist filling the air.",
        "camera_shot": "wide_cinematic",
        "camera_motion": "slow_zoom_out",
        "telemetry": {"year": 1987, "location": "JUNKYARD OPEN AIR", "radiation_cpm": 600000, "dose_rate": "90.0 Gy/h", "status": "AIRBORNE AEROSOLIZATION"},
        "codex_image_prompt": "Cloud of glowing electric blue microscopic dust motes floating and dispersing through the humid night air around exhausted minimalist stickman workers, settling like glittering pollen across the dirt yard" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 3: THE CARNIVAL OF CONTAMINATION (Scenes 13–18)
    # ==========================================
    {
        "scene_id": "13",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "GIFTS OF DEATH",
        "voiceover_text": "Devair scooped fragments of the sparkling blue powder into small paper packets and distributed them to friends, neighbors, and relatives as lucky charms. Everyone wanted a pinch of the miracle dust that could shine without electricity or flame.",
        "word_count": 39,
        "visual_description": "Stickman hands wrapping glowing blue powder into small folded paper packets on a wooden counter, handing them to smiling neighbors, sinister irony.",
        "camera_shot": "closeup_hands",
        "camera_motion": "pan_down",
        "telemetry": {"year": 1987, "location": "RUA 26-A // DISTRIBUTION", "radiation_cpm": 550000, "dose_rate": "80.0 Gy/h", "status": "INTER-COMMUNAL DISTRIBUTION"},
        "codex_image_prompt": "Minimalist stickman hands scooping glowing electric blue crystal powder into small folded paper envelopes on a rustic wooden table, handing them to eager stickman neighbors, high contrast dark noir lighting" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "14",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "THE GLOWING CARNIVAL",
        "voiceover_text": "Across Rua 26-A, a festive carnival atmosphere unfolded. Young men rubbed the powder onto their arms and chests to show off in the dark. Women rubbed specks behind their ears and across their foreheads like shimmering party glitter.",
        "word_count": 39,
        "visual_description": "Group of stickman neighbors standing on dark street corner, glowing electric cyan marks painted on their arms, faces, and clothing, laughing and admiring their glowing bodies under the stars.",
        "camera_shot": "wide",
        "camera_motion": "slow_pan_right",
        "telemetry": {"year": 1987, "location": "RUA 26-A // STREET CORNER", "radiation_cpm": 420000, "dose_rate": "55.0 Gy/h", "status": "EPIDERMAL CONTAMINATION"},
        "codex_image_prompt": "Group of minimalist stickman figures gathered on a dark neighborhood street at night, their arms, cheeks, and shirts painted with intensely glowing electric blue powder like luminous body paint, festive yet haunting" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "15",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "IVO'S BAG OF DUST",
        "voiceover_text": "Devair's brother, Ivo Ferreira, lived just a few streets away. Enchanted by the glowing phenomenon, Ivo took a handful of the blue powder home in a plastic bag, placing it on his dining table to entertain his young family during dinner.",
        "word_count": 42,
        "visual_description": "Ivo stickman walking along suburban path at night carrying a glowing blue plastic bag, arriving at his family cottage doorway with warm light spilling out.",
        "camera_shot": "medium",
        "camera_motion": "tracking_forward",
        "telemetry": {"year": 1987, "location": "IVO FERREIRA RESIDENCE", "radiation_cpm": 380000, "dose_rate": "48.0 Gy/h", "status": "DOMESTIC TRANSPORTATION"},
        "codex_image_prompt": "Minimalist stickman walking along a dirt suburban footpath at night carrying a transparent plastic bag that glows with brilliant electric blue light, approaching the front door of a modest brick cottage" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "16",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "THE INNOCENT CURIOSITY",
        "voiceover_text": "Inside Ivo's home, his six-year-old daughter, Leide das Neves Ferreira, sat on the floor playing. Captivated by the magical blue sparkle, the little girl poured some of the powder onto the concrete floor, rubbing it across her hands and arms.",
        "word_count": 40,
        "visual_description": "Six-year-old stickman child sitting on a living room rug, happily playing with glowing blue powder on the floor, little stick hands coated in radiant cyan dust.",
        "camera_shot": "low_angle_closeup",
        "camera_motion": "slow_push_in",
        "telemetry": {"year": 1987, "location": "LIVING ROOM FLOOR", "radiation_cpm": 650000, "dose_rate": "95.0 Gy/h", "status": "PEDIATRIC EXPOSURE"},
        "codex_image_prompt": "Small minimalist stickman child sitting on the floor of a modest home playing innocently with glowing bright cyan powder scattered like glitter, small hands glowing brightly in the dim room, heartbreaking chiaroscuro" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "17",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "THE LETHAL SANDWICH",
        "voiceover_text": "While sitting on the floor surrounded by the glowing residue, Leide was handed a hard-boiled egg and a sandwich. Without washing her hands, she ate the food, inadvertently ingesting over one gigabecquerel of pure Caesium-137 directly into her gastrointestinal tract.",
        "word_count": 40,
        "visual_description": "Stickman child holding food in glowing blue hands, eating while sitting on the floor, glowing particles transferring from fingers onto the food, tragic intimate lighting.",
        "camera_shot": "closeup",
        "camera_motion": "freeze_slow_zoom",
        "telemetry": {"ingestion": "~1 GBq Cs-137", "organ": "GI TRACT // SYSTEMIC", "radiation_cpm": 800000, "dose_rate": "6.0 Gy WHOLE BODY", "status": "INTERNAL INGESTION"},
        "codex_image_prompt": "Dramatic closeup of a small minimalist stickman child eating a sandwich, with fingers and food glowing with bright electric cyan dust particles, sitting on a dark floor with soft warm background lamp light" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "18",
        "act": 3,
        "act_title": "ACT 3: THE CARNIVAL OF CONTAMINATION",
        "kinetic_hook_headline": "GLOWING IN THE DARK",
        "voiceover_text": "Hours later, when Leide's mother put her to bed and turned off the lights, she was horrified to see her daughter's face, hands, and chest radiating a visible ghostly blue luminescence in the pitch black bedroom. The lethal clock was already ticking.",
        "word_count": 42,
        "visual_description": "Pitch black child bedroom, mother stickman standing frozen in doorway, looking at child's bed where the little stickman silhouette glows with vivid ghost-blue Cherenkov luminescence.",
        "camera_shot": "wide_bedroom",
        "camera_motion": "slow_zoom_in",
        "telemetry": {"year": 1987, "location": "BEDROOM // MIDNIGHT", "radiation_cpm": 850000, "dose_rate": "6.0 Gy ESTIMATE", "status": "SYSTEMIC IRRADIATION"},
        "codex_image_prompt": "Chilling scene inside a dark bedroom at night, a terrified stickman mother standing in the doorway staring at her small child lying in bed glowing with an eerie, ghostly electric blue silhouette in the dark" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 4: THE SICKNESS & THE HEROIC COMMUTE (Scenes 19–24)
    # ==========================================
    {
        "scene_id": "19",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "THE SHADOW EPIDEMIC",
        "voiceover_text": "By September 25, the joyous curiosity collapsed into nightmare. Across the Aeroporto district, dozens of people fell violently ill with intractable vomiting, severe diarrhea, dizziness, and rapid hair loss. Dark, blackened burn lesions erupted across their hands and bodies.",
        "word_count": 39,
        "visual_description": "Montage of suffering residents: stickman figures lying in beds clutching heads, hair falling onto pillows, black necrotizing skin patches on hands, dark hospital silhouettes.",
        "camera_shot": "medium_montage",
        "camera_motion": "slow_pan_up",
        "telemetry": {"year": 1987, "location": "GOIANIA CLINICS", "radiation_cpm": 300000, "dose_rate": "ACUTE ARS", "status": "MASS CASUALTY EMERGENCE"},
        "codex_image_prompt": "Dark room where multiple sick minimalist stickman patients lie in beds clutching their heads and stomachs, clumps of hair fallen onto pillows, dark burn marks on skin, somber medical noir atmosphere" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "20",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "THE BLIND DIAGNOSIS",
        "voiceover_text": "Panicked families rushed to local clinics and emergency rooms. But local physicians, having never encountered acute radiation syndrome, misdiagnosed the victims with an aggressive tropical viral gastroenteritis, allergic reactions, or pemphigus foliaceus, sending them back into contaminated homes with antacids.",
        "word_count": 40,
        "visual_description": "Frantic clinic waiting room, stickman doctor in lab coat scratching head examining chart, bewildered patients in chairs, clinical fluorescent lighting in dark void.",
        "camera_shot": "wide",
        "camera_motion": "tracking_left",
        "telemetry": {"year": 1987, "location": "EMERGENCY CLINIC", "radiation_cpm": 180000, "dose_rate": "UNKNOWN ARS", "status": "MISDIAGNOSIS (GASTRITIS)"},
        "codex_image_prompt": "Crowded hospital clinic waiting room with minimalist stickman doctor in white coat holding medical clipboard looking confused, patients with glowing bandaged hands waiting on metal benches under cold fluorescent lights" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "21",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "MARIA GABRIELA'S EPIPHANY",
        "voiceover_text": "While doctors were baffled, one courageous woman saw the truth. Devair's thirty-seven-year-old wife, Maria Gabriela Ferreira, noticed that every single person who touched or stood near the glowing blue powder fell violently sick within hours. The powder was not holy; it was venomous.",
        "word_count": 43,
        "visual_description": "Maria Gabriela stickman standing in doorway of dark junkyard office, intense focused eyes, looking at the glowing cylinder on the workbench, realization dawning on her face.",
        "camera_shot": "medium_portrait",
        "camera_motion": "slow_push_in",
        "telemetry": {"year": 1987, "location": "DEVAIR RESIDENCE", "radiation_cpm": 750000, "dose_rate": "5.7 Gy ACCUMULATING", "status": "CORRELATION IDENTIFIED"},
        "codex_image_prompt": "Portrait of a brave minimalist stickman woman standing resolute in a dark doorway, looking with intense determined cartoon eyes at a glowing blue metallic capsule on a workbench, chiaroscuro golden and cyan lighting" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "22",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "THE DEADLIEST COMMUTE",
        "voiceover_text": "On the morning of Monday, September 28, Maria Gabriela acted. Placing the lead fragments and powder remnants into a thick plastic bag, she boarded a crowded public municipal bus and rode across the city center, shielding the deadly package between her legs.",
        "word_count": 41,
        "visual_description": "Maria Gabriela sitting inside a crowded municipal bus holding a plastic bag between her feet, passengers sitting beside her unaware, faint blue glow leaking from bag base.",
        "camera_shot": "medium_interior_bus",
        "camera_motion": "subtle_handheld",
        "telemetry": {"year": 1987, "location": "MUNICIPAL BUS // GOIANIA", "radiation_cpm": 850000, "dose_rate": "15.0 Gy/h NEAR FIELD", "status": "TRANSIT WITH UNSEALED SOURCE"},
        "codex_image_prompt": "Inside a crowded 1980s city bus, minimalist stickman passengers looking out windows while a determined stickman woman sits holding a heavy bag between her legs that emits a subtle faint cyan glow onto the metal bus floor" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "23",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "THE BAG ON THE DESK",
        "voiceover_text": "Arriving at the Vigilancia Sanitaria—the Goias State Health Surveillance Department on Avenida Goias—she carried the bag up the steps and marched into the office of Dr. Paulo Roberto Ferreira, setting the plastic bag directly onto his administrative desk.",
        "word_count": 40,
        "visual_description": "Maria Gabriela slamming the bag down onto a wooden office desk, Dr. Paulo Roberto looking up in shock from paperwork, office setting with Brazilian flag and filing cabinets.",
        "camera_shot": "medium",
        "camera_motion": "pan_down_to_desk",
        "telemetry": {"year": 1987, "location": "VIGILANCIA SANITARIA", "radiation_cpm": 920000, "dose_rate": "25.0 Gy/h", "status": "PUBLIC HEALTH DELIVERY"},
        "codex_image_prompt": "Minimalist stickman woman placing a heavy plastic bag on the wooden desk of a public health official in a government office, official looking up startled, dramatic office lighting with window blinds shadows" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "24",
        "act": 4,
        "act_title": "ACT 4: THE SICKNESS & THE HEROIC COMMUTE",
        "kinetic_hook_headline": "THE ULTIMATUM",
        "voiceover_text": "Looking the doctor in the eye, Maria Gabriela spoke the fateful words recorded in the IAEA archives: 'This is what is killing my family.' Her single act of defiance stopped city-wide contamination in its tracks—even as it sealed her own tragic fate.",
        "word_count": 43,
        "visual_description": "Close up profile of Maria Gabriela speaking with intense resolve, the glowing bag on the desk in the foreground, declassified stamp aesthetic in background.",
        "camera_shot": "closeup_dramatic",
        "camera_motion": "slow_zoom_in",
        "telemetry": {"year": 1987, "location": "AVENIDA GOIAS", "radiation_cpm": 950000, "dose_rate": "5.7 Gy LETHAL DOSE", "status": "HEROIC CONTAINMENT ALERT"},
        "codex_image_prompt": "Close-up cinematic shot of a courageous minimalist stickman woman speaking with resolute determination to a doctor, in the foreground on the desk sits a bag glowing with bright electric cyan light, high contrast noir shadows" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 5: THE GEIGER COUNTER SCREAMS (Scenes 25–30)
    # ==========================================
    {
        "scene_id": "25",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "THE PHYSICIST SUMMONED",
        "voiceover_text": "Sensing something profoundly dangerous, Dr. Paulo Roberto called Dr. Walter Mendes Ferreira, a visiting medical physicist from NUCLEBRAS. Walter borrowed a Nardeux scintillation radiation monitor and rushed to Avenida Goias on the morning of September 29.",
        "word_count": 37,
        "visual_description": "Dr. Walter Mendes Ferreira, stickman physicist in brown suit carrying a vintage yellow Nardeux scintillation detector with shoulder strap, stepping out of a car in front of the Health Department.",
        "camera_shot": "medium_exterior",
        "camera_motion": "tracking_forward",
        "telemetry": {"year": 1987, "location": "AVENIDA GOIAS // MORNING", "radiation_cpm": 150, "dose_rate": "0.5 uGy/h", "status": "SCINTILLATION MONITOR DEPLOYED"},
        "codex_image_prompt": "Minimalist stickman medical physicist in vintage 1980s suit stepping onto the sidewalk in front of a concrete government building, holding a portable yellow radiation survey meter with handheld probe, morning sunlight" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "26",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "THE PEGGED NEEDLE",
        "voiceover_text": "As Walter walked down the sidewalk toward the building, he switched on the detector. Decades later, he recalled his sheer horror: fifty meters before even reaching the entrance, the analog needle slammed violently past maximum scale, screaming with frantic audio clicks.",
        "word_count": 41,
        "visual_description": "Close up of vintage yellow analog radiation meter: needle pinned against the far right red danger peg, red alarm light flashing, physicist's hand shaking.",
        "camera_shot": "extreme_closeup_meter",
        "camera_motion": "macro_shake",
        "telemetry": {"detector": "NARDEUX SCINTILLATOR", "reading": "OFF SCALE (>100,000 CPM)", "radiation_cpm": 999999, "dose_rate": ">10 Gy/h", "status": "SATURATION DEFLECTION"},
        "codex_image_prompt": "Macro closeup of a vintage analog radiation survey meter face, the black needle violently pinned all the way past the red maximum danger zone, red warning lamp flashing, stickman hand holding meter with shock" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "27",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "CODE RED: EVACUATE",
        "voiceover_text": "Walter initially thought his instrument was malfunctioning. Borrowing a second detector, it also pinned at full deflection. Realizing an unshielded nuclear source was sitting inside a public office, Walter sprinted into the building, shouting for immediate, total evacuation.",
        "word_count": 39,
        "visual_description": "Physicist running up the steps into the government building waving his arms frantically, office workers streaming out in panic, yellow caution tape snapping in wind.",
        "camera_shot": "wide_action",
        "camera_motion": "pan_follow",
        "telemetry": {"year": 1987, "location": "HEALTH SURVEILLANCE BLDG", "radiation_cpm": 999999, "dose_rate": "CRITICAL EMERGENCY", "status": "TOTAL EVACUATION ORDERED"},
        "codex_image_prompt": "Minimalist stickman physicist running toward a government building waving arms in alarm, terrified office workers fleeing out through glass double doors onto the street, dramatic high contrast shadows" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "28",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "FEDERAL NUCLEAR ALERT",
        "voiceover_text": "By afternoon, an emergency alert flashed directly to the National Nuclear Energy Commission, CNEN, in Brasilia. Federal authorities recognized the nightmare: a major unshielded industrial radiation source was loose in the sixth largest metropolitan area in Brazil.",
        "word_count": 37,
        "visual_description": "Federal command war room in Brasilia: stickman military officers and nuclear commissioners gathered around a glowing map of Goiania with flashing red hazard beacons.",
        "camera_shot": "wide_command_room",
        "camera_motion": "slow_push_in",
        "telemetry": {"command": "CNEN BRASILIA", "alert_level": "LEVEL 5 INES", "radiation_cpm": 999999, "dose_rate": "MASSIVE ACCIDENT", "status": "FEDERAL INTERVENTION"},
        "codex_image_prompt": "Military command room at night with minimalist stickman officials in uniforms gathered around an illuminated digital map table showing the city of Goiania with pulsing red nuclear hazard markers, tension in the room" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "29",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "AERIAL GAMMA SWEEP",
        "voiceover_text": "Federal helicopters equipped with sensitive sodium iodide gamma-ray spectrometers were deployed over Goiania. Flying low over rooftops, their airborne sensors lit up like Christmas trees, detecting intense radiation plumes beaming up from multiple residential neighborhoods across the city.",
        "word_count": 38,
        "visual_description": "Military helicopter flying low over Goiania skyline at dusk, scanning beam of glowing cyan grid lines projecting down onto city blocks revealing glowing radioactive hot spots.",
        "camera_shot": "aerial_wide",
        "camera_motion": "flyover_tracking",
        "telemetry": {"platform": "HELICOPTER RECON", "sensor": "NaI(Tl) CRYSTAL", "radiation_cpm": 850000, "dose_rate": "AERIAL SPECTROMETRY", "status": "AIRBORNE RECONNAISSANCE"},
        "codex_image_prompt": "Military helicopter flying over a dark cityscape at dusk, sweeping a cone of glowing cyan radar grid lines down onto neighborhood houses below, revealing bright glowing blue radioactive hotspots among the rooftops" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "30",
        "act": 5,
        "act_title": "ACT 5: THE GEIGER COUNTER SCREAMS",
        "kinetic_hook_headline": "THE SEVEN GROUND ZEROS",
        "voiceover_text": "The aerial survey revealed seven primary foci of catastrophic contamination: the abandoned IGR clinic, Roberto's house on Rua 57, Devair's junkyard on Rua 26-A, Ivo's residence, a second junkyard, and multiple public transport routes where the dust had spread.",
        "word_count": 41,
        "visual_description": "Top-down tactical map of Goiania with seven glowing cyan radioactive epicenter rings radiating shockwaves, stickman investigator pointing red laser at the epicenters.",
        "camera_shot": "overhead_tactical_map",
        "camera_motion": "slow_zoom_in",
        "telemetry": {"epicenters": "7 MAJOR FOCI", "hotspots": "42 SECONDARY SITES", "radiation_cpm": 950000, "dose_rate": "SEVERE SPREAD", "status": "ISOLATION PERIMETERS DRAWN"},
        "codex_image_prompt": "Dark tactical dossier map of the city of Goiania, pinned with red and glowing cyan concentric circles marking seven contaminated ground zero zones, investigator stickman silhouette pointing at the map in shadow" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 6: THE STADIUM OF 100,000 (Scenes 31–36)
    # ==========================================
    {
        "scene_id": "31",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "THE OLYMPIC CITADEL",
        "voiceover_text": "To prevent nationwide panic and contain the fallout, authorities requisitioned the massive Estadio Olimpico Pedro Ludovico Teixeira in central Goiania, rapidly transforming the football stadium into the largest civil radiological triage and decontamination compound in human history.",
        "word_count": 39,
        "visual_description": "Giant Olympic football stadium converted into decontamination camp: field lined with medical tents, floodlights beaming down, hazmat technicians patrolling perimeter fences.",
        "camera_shot": "wide_stadium_overview",
        "camera_motion": "high_angle_pan",
        "telemetry": {"year": 1987, "location": "ESTADIO OLIMPICO", "screened_target": "100,000+ CITIZENS", "radiation_cpm": 12000, "dose_rate": "MASS SCREENING", "status": "TRIAGE CITADEL ESTABLISHED"},
        "codex_image_prompt": "Massive open-air football stadium at night illuminated by towering stadium floodlights, filled with rows of yellow decontamination tents, military hazmat personnel, and perimeter fences under a dark night sky" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "32",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "THE LINE OF 112,000",
        "voiceover_text": "Over the following days, more than one hundred and twelve thousand eight hundred terrified citizens—over ten percent of the city's entire population—queued for kilometers outside the stadium gates to be scanned one-by-one by technicians wielding Geiger-Muller probes.",
        "word_count": 39,
        "visual_description": "Endless line of thousands of stickman citizens queuing down boulevard outside stadium, technicians in white protective suits scanning individuals with yellow wand probes.",
        "camera_shot": "long_tracking_shot",
        "camera_motion": "slow_pan_along_line",
        "telemetry": {"citizens_screened": "112,800", "queue_length": "3.5 KM", "radiation_cpm": 15000, "dose_rate": "CIVILIAN TRIAGE", "status": "CONTINUOUS RADIATION SCREENING"},
        "codex_image_prompt": "Endless winding line of minimalist stickman citizens stretching for miles outside a massive concrete stadium, technicians in full white hazmat suits scanning people with handheld yellow radiation detector wands" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "33",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "STRIPPED & QUARANTINED",
        "voiceover_text": "Of those screened, two hundred and forty-nine people were flagged with significant radioactive contamination. Victims were immediately stripped of all clothing, which was incinerated as radioactive waste, and scrubbed repeatedly with acetic acid and chelating soaps in high-pressure showers.",
        "word_count": 39,
        "visual_description": "Decontamination shower corridor inside stadium: stickman victims being washed down with high-pressure water by hazmat workers in yellow suits and respirators, steam rising.",
        "camera_shot": "medium_corridor",
        "camera_motion": "tracking_forward",
        "telemetry": {"contaminated_detected": 249, "internal_contamination": 129, "radiation_cpm": 85000, "dose_rate": "CHEMICAL DECONTAMINATION", "status": "SCRUBBING & QUARANTINE"},
        "codex_image_prompt": "Industrial decontamination wash station inside a concrete stadium tunnel, hazmat technicians in bright yellow suits spraying high-pressure water hoses on minimalist stickman figures, heavy atmospheric mist and water puddles" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "34",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "THE PRUSSIAN BLUE REGIMEN",
        "voiceover_text": "One hundred and twenty-nine victims had ingested or inhaled Caesium-137. Doctors initiated an unprecedented medical intervention, administering massive oral doses of Prussian Blue—Radiogardase—an insoluble blue pigment that binds caesium ions in the intestines, preventing internal reabsorption.",
        "word_count": 38,
        "visual_description": "Medical counter with rows of dark Prussian Blue capsule bottles and blue powder cups, stickman doctor administering dark blue medicine to a bedridden patient.",
        "camera_shot": "closeup_medicine",
        "camera_motion": "rack_focus",
        "telemetry": {"antidote": "PRUSSIAN BLUE (RADIOGARDASE)", "dosage": "10g/day", "radiation_cpm": 150000, "dose_rate": "GASTROINTESTINAL BINDING", "status": "CHELATION THERAPY"},
        "codex_image_prompt": "Medical still life of dark navy blue Prussian Blue medicine bottles and capsules on a stainless steel medical tray, beside a minimalist stickman doctor attending to a bedridden patient in an isolation tent" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "35",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "AIRLIFT TO RIO",
        "voiceover_text": "The twenty most critically irradiated victims were rushed to Santa Maria Hospital, and the four worst cases were airlifted aboard Brazilian Air Force transport planes to the specialized Naval Hospital Marcilio Dias in Rio de Janeiro, placed into negative-pressure laminar flow isolation chambers.",
        "word_count": 42,
        "visual_description": "Military cargo plane tarmac at midnight: stickman patients on stretchers sealed in plastic isolation pods being loaded into the illuminated rear ramp of a transport aircraft.",
        "camera_shot": "wide_airfield",
        "camera_motion": "slow_push_in",
        "telemetry": {"transport": "C-130 HERCULES", "destination": "HOSPITAL MARCILIO DIAS, RIO", "radiation_cpm": 350000, "dose_rate": "AIR EVACUATION", "status": "CRITICAL WARD TRANSFER"},
        "codex_image_prompt": "Dark military airfield tarmac at night under rain, stickman patients on stretchers inside transparent sealed bio-hazard isolation pods being wheeled up the open cargo ramp of a massive military aircraft" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "36",
        "act": 6,
        "act_title": "ACT 6: THE STADIUM OF 100,000",
        "kinetic_hook_headline": "THE CELLULAR COLLAPSE",
        "voiceover_text": "Inside the isolation chambers, doctors fought a losing battle. The massive whole-body doses had completely obliterated the patients' bone marrow. White blood cell counts plummeted to zero, leaving them defenceless against systemic infections, internal hemorrhaging, and multi-organ failure.",
        "word_count": 39,
        "visual_description": "Intensive care isolation room: cardiac monitor graphs flatlining, stickman doctor in full sterile gown looking down solemnly at a bed surrounded by medical drip lines.",
        "camera_shot": "medium_icu",
        "camera_motion": "slow_zoom_in",
        "telemetry": {"leukocyte_count": "0 / mm3", "platelets": "CRITICAL DEFICIT", "radiation_cpm": 450000, "dose_rate": "TOTAL BONE MARROW APLASIA", "status": "TERMINAL ARS"},
        "codex_image_prompt": "Sterile high-tech hospital isolation chamber with glowing vital monitors showing declining cardiac lines, minimalist stickman doctors in full white protective suits standing solemnly beside a patient bed" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 7: THE STONE RIOTS & THE LEAD COFFINS (Scenes 37–42)
    # ==========================================
    {
        "scene_id": "37",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "THE FOUR VICTIMS",
        "voiceover_text": "In late October, the tragedy claimed its first lives. Admilson de Souza, eighteen, died on October 18. Maria Gabriela Ferreira, thirty-seven, and little Leide das Neves, six, both succumbed on October 23. Junkyard worker Israel dos Santos, twenty-two, died four days later.",
        "word_count": 43,
        "visual_description": "Memorial portrait composition: four minimalist stickman silhouettes with somber posture, candles flickering on black obsidian stone, names and dates carved into dark memorial slab.",
        "camera_shot": "wide_memorial",
        "camera_motion": "slow_pan_across",
        "telemetry": {"fatalities": 4, "leide_dose": "6.0 Gy", "maria_dose": "5.7 Gy", "israel_dose": "4.5 Gy", "admilson_dose": "5.3 Gy", "status": "FATALITIES RECORDED"},
        "codex_image_prompt": "Somber memorial space with four flickering memorial candles burning on black polished granite, casting golden light on four stickman silhouettes standing with bowed heads in deep obsidian void" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "38",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "THE 700-KG LEAD COFFINS",
        "voiceover_text": "Because the deceased bodies were still emitting hazardous gamma radiation, health authorities could not permit ordinary burials. Specialized coffins were constructed: thick lead sheeting encased inside reinforced waterproof concrete, each weighing nearly seven hundred kilograms.",
        "word_count": 37,
        "visual_description": "Close up of an industrial lead and concrete sarcophagus coffin: steel lifting rings, radiation hazard symbol embossed on lead, heavy industrial finish in a gloomy warehouse.",
        "camera_shot": "medium_closeup",
        "camera_motion": "orbital_pan",
        "telemetry": {"coffin_material": "LEAD + CONCRETE", "weight": "600–700 KG", "radiation_cpm": 25000, "dose_rate": "CONTAINED AT SURFACE", "status": "HERMETIC COFFIN ENCASEMENT"},
        "codex_image_prompt": "Massive monolithic rectangular lead coffin encased in thick rough industrial concrete with heavy steel hoist rings, resting on wooden blocks in a gloomy workshop, high-contrast chiaroscuro" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "39",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "THE CEMETERY MOB",
        "voiceover_text": "On October 24, when the hearse carrying Leide das Neves and Maria Gabriela arrived at Cemiterio Parque in Goiania, a violent mob of over two thousand terrified local residents blocked the gates with trucks, cars, and makeshift barricades, refusing to allow radioactive corpses into their soil.",
        "word_count": 46,
        "visual_description": "Angry mob of stickman civilians blocking the wrought iron cemetery gates, holding wooden planks and signs, burning tire smoke rising in background, hearse stopped on road.",
        "camera_shot": "wide_riot",
        "camera_motion": "handheld_tracking",
        "telemetry": {"year": 1987, "location": "CEMITERIO PARQUE // GATES", "mob_size": "2,000+ RIOTERS", "radiation_cpm": 1500, "status": "CIVIL UNREST & BARRICADES"},
        "codex_image_prompt": "Violent civil riot at the wrought-iron gates of Cemiterio Parque cemetery, angry mob of minimalist stickman figures throwing rocks and blocking the road with trucks and burning barricades, dramatic smoke and turmoil" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "40",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "HAIL OF STONES",
        "voiceover_text": "The protest turned into a ferocious riot. Hysterical citizens threw cobblestones, bricks, and bottles at the hearse and government workers. Believing the burial would poison the city's groundwater and property values forever, the mob attempted to overturn the funeral vehicles.",
        "word_count": 40,
        "visual_description": "Stones and bricks flying through air smashing windshield of funeral hearse, stickman government drivers ducking, chaos and smoke in cemetery street.",
        "camera_shot": "medium_action",
        "camera_motion": "shake_whip_pan",
        "telemetry": {"year": 1987, "location": "CEMITERIO PARQUE ROAD", "mob_actions": "BRICKS & STONES HURLED", "radiation_cpm": 1800, "status": "VIOLENT INTERFERENCE"},
        "codex_image_prompt": "Stones and bricks flying through the air hitting the windshield and roof of a black funeral hearse, stickman drivers ducking inside, rioting stickman silhouettes in background tossing cobblestones under smoky sky" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "41",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "THE CRANE BURIAL",
        "voiceover_text": "Military police deployed tear gas and riot batons to force open the cemetery gates. Under armed military escort, heavy construction cranes hoisted the seven-hundred-kilogram lead coffins high above the shouting crowd, lowering little Leide into a deep, reinforced concrete vault.",
        "word_count": 40,
        "visual_description": "Industrial crane lowering the massive lead-concrete coffin into a deep grave vault, surrounded by military police in riot gear with shields, tear gas smoke drifting in wind.",
        "camera_shot": "high_angle_crane",
        "camera_motion": "slow_crane_down",
        "telemetry": {"year": 1987, "location": "CEMITERIO PARQUE // VAULT", "security": "MILITARY POLICE BRIGADE", "vault_depth": "4.5 METERS", "status": "REINFORCED BURIAL COMPLETED"},
        "codex_image_prompt": "Dramatic high angle of a massive industrial construction crane hoisting a 700kg concrete lead coffin into a deep rectangular grave vault, surrounded by military police with riot shields amidst drifting tear gas smoke" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "42",
        "act": 7,
        "act_title": "ACT 7: THE STONE RIOTS & THE LEAD COFFINS",
        "kinetic_hook_headline": "THE LIVING SCARS",
        "voiceover_text": "The survivors carried permanent physical and emotional mutilation. Roberto Alves suffered severe radiation necrosis and had his right arm and fingers amputated. Devair Ferreira survived his seven-Gray exposure, but sank into severe depression and alcoholism, dying ostracized in 1994.",
        "word_count": 40,
        "visual_description": "Devair stickman sitting alone on a wooden bench at dusk with head in hands, Roberto stickman standing nearby with amputated arm sleeve pinned to shirt, desolate landscape.",
        "camera_shot": "wide_somber",
        "camera_motion": "slow_zoom_out",
        "telemetry": {"roberto_dose": "4.5 Gy (AMPUTATION)", "devair_dose": "7.0 Gy (SURVIVED)", "social_stigma": "TOTAL OSTRACIZATION", "status": "PERMANENT CHRONIC TRAUMA"},
        "codex_image_prompt": "Heartbreaking shot of two surviving minimalist stickman men at dusk: one sitting on a bench with head in hands, the other standing beside him with one empty sleeve pinned to his shirt, long shadows stretching across empty ground" + STICKMAN_NOIR_SUFFIX
    },

    # ==========================================
    # ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB (Scenes 43–48)
    # ==========================================
    {
        "scene_id": "43",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "SCORCHED EARTH PROTOCOL",
        "voiceover_text": "Following the burials, Brazil's nuclear forces launched a scorched-earth decontamination campaign. Entire residential blocks were cordoned off. Seven houses and three scrap metal yards were completely demolished down to the bedrock using heavy excavators and wrecking balls.",
        "word_count": 38,
        "visual_description": "Heavy yellow excavators demolishing brick houses on Rua 26-A, wrecking ball striking brick wall, hazmat workers spraying water hoses to suppress radioactive dust.",
        "camera_shot": "wide_demolition",
        "camera_motion": "tracking_right",
        "telemetry": {"houses_demolished": 7, "scrap_yards_razed": 3, "soil_scraped": "TOP 50 CM", "radiation_cpm": 45000, "status": "STRUCTURAL DEMOLITION"},
        "codex_image_prompt": "Heavy construction excavators tearing down brick houses in a deserted neighborhood, workers in white hazmat suits spraying water cannons to suppress dust clouds, desolate destruction scene" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "44",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "THE STRIPPED EARTH",
        "voiceover_text": "Heavy earthmovers scraped away the top half-meter of contaminated soil across entire streets. Thousands of household possessions—furniture, clothing, family photographs, automobiles, domestic pets, and ornamental trees—were seized and condemned to prevent any residual radiation.",
        "word_count": 37,
        "visual_description": "Bulldozer scraping barren red earth into piles, rows of confiscated cars and boxed household belongings tagged with yellow radioactive hazard triangles.",
        "camera_shot": "medium_wide",
        "camera_motion": "pan_left",
        "telemetry": {"personal_belongings": "CONCURRENT SEIZURE", "soil_removed": "1,200 TONS", "radiation_cpm": 18000, "status": "RADICAL SURFACE STRIPPING"},
        "codex_image_prompt": "Bulldozer scraping the top layer of earth off a barren street, leaving red scraped soil, in the foreground piles of tagged personal belongings, furniture, and cars labeled with yellow hazard triangles" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "45",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "3,500 CUBIC METERS",
        "voiceover_text": "The colossal cleanup produced three thousand five hundred cubic meters—over six thousand metric tons—of radioactive debris. The hazardous waste filled fourteen shipping containers, forty-two heavy concrete packaging boxes, and three thousand eight hundred sealed steel drums.",
        "word_count": 39,
        "visual_description": "Endless staging yard filled with thousands of sealed yellow 200-liter steel drums and massive blue shipping containers marked with black trefoil radiation symbols.",
        "camera_shot": "high_angle_staging_yard",
        "camera_motion": "slow_push_in",
        "telemetry": {"waste_volume": "3,500 m3", "waste_weight": "6,000 METRIC TONS", "steel_drums": 3800, "shipping_containers": 14, "status": "CONTAINMENT CONSOLIDATION"},
        "codex_image_prompt": "Vast industrial staging ground packed with thousands of sealed yellow radioactive steel drums and steel shipping containers bearing the black nuclear radiation trefoil symbol, gloomy overcast sky" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "46",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "ABADIA DE GOIAS REPOSITORY",
        "voiceover_text": "A permanent radioactive waste repository was constructed in the rolling hills of Abadia de Goias, twenty kilometers outside the city. The entire six thousand tons of debris were entombed within monolithic reinforced concrete subterranean chambers engineered to withstand earthquakes and erosion.",
        "word_count": 42,
        "visual_description": "Brutalist subterranean concrete bunker complex in rural hills of Abadia de Goiás, massive steel blast door closing, barbed wire security perimeter, ominous sunset.",
        "camera_shot": "wide_landscape",
        "camera_motion": "slow_pan_up",
        "telemetry": {"location": "ABADIA DE GOIAS // CRCN", "engineered_life": "300 YEARS", "seismic_rating": "GRADE 8", "status": "PERMANENT GEOLOGICAL REPOSITORY"},
        "codex_image_prompt": "Massive brutalist concrete bunker tomb constructed into the grassy rolling hills of Abadia de Goias, heavy steel blast doors, double security barbed wire fences, glowing orange sunset on horizon" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "47",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "THE 300-YEAR HALF-LIFE",
        "voiceover_text": "With a physical half-life of thirty point seventeen years, Caesium-137 decays slowly into Barium-137m, emitting penetrating gamma rays with each disintegration. It will take ten half-lives—three full centuries—until the blue powder beneath Abadia de Goias decays into harmless inert element.",
        "word_count": 42,
        "visual_description": "Scientific radioactive decay diagram: Caesium-137 decaying across 300-year timeline, atom releasing gamma ray photon, cross-section of deep concrete vaults underground.",
        "camera_shot": "split_schematic_vault",
        "camera_motion": "slow_pan_down",
        "telemetry": {"half_life": "30.17 YEARS", "decay_chain": "Cs-137 -> Ba-137m -> Ba-137", "quarantine_period": "300 YEARS (YEAR 2287)", "status": "RADIOACTIVE ENCAPSULATION"},
        "codex_image_prompt": "Cinematic split screen showing subterranean cross-section of massive concrete vaults deep underground storing yellow radioactive drums, juxtaposed with an atomic diagram of decaying Caesium-137 atoms emitting gamma rays" + STICKMAN_NOIR_SUFFIX
    },
    {
        "scene_id": "48",
        "act": 8,
        "act_title": "ACT 8: SCORCHED EARTH & THE 300-YEAR TOMB",
        "kinetic_hook_headline": "DOSSIER ZERO: CASE #05 VERDICT",
        "voiceover_text": "The Goiania catastrophe remains the definitive warning of forgotten industrial isotopes. It was not a reactor explosion or a weapon of war, but a simple broken capsule that unmasked human curiosity and tragedy. Case File zero five is officially classified.",
        "word_count": 42,
        "visual_description": "Investigator stickman in fedora and trenchcoat in underground archive vault, stamping 'CLASSIFIED' in crimson ink onto Manila dossier folder labeled 'CASE #05: GOIANIA 1987', filing it into a heavy steel cabinet drawer.",
        "camera_shot": "medium_closing",
        "camera_motion": "slow_push_in_to_drawer",
        "telemetry": {"dossier": "THE DOSSIER ZERO", "case_file": "#05 // CAESIUM-137", "status": "CLOSED & ARCHIVED", "final_record": "PERMANENT VAULT RECORD"},
        "codex_image_prompt": "Minimalist stickman investigator in dark trenchcoat and fedora in an underground archive vault, stamping a red rubber stamp onto a thick manila folder labeled Case File 05, sliding it into an iron filing drawer under a warm banker lamp" + STICKMAN_NOIR_SUFFIX
    }
]

def main():
    total_words = sum(s["word_count"] for s in scenes_data)
    total_scenes = len(scenes_data)
    est_audio_sec = (total_words / 160.0) * 60.0 + (total_scenes * 0.4)
    est_frames = int(est_audio_sec * 30)
    
    print(f"=== THE DOSSIER ZERO: CASE FILE #05 STORYBOARD ===")
    print(f"Total Scenes: {total_scenes} (8 Acts x 6 Scenes)")
    print(f"Total Words: {total_words} words")
    print(f"Estimated Speech + Pause Duration: {est_audio_sec:.1f}s ({est_audio_sec/60.0:.2f} mins)")
    print(f"Estimated Total Frames @ 30fps: {est_frames} frames")
    
    manifest = {
        "project": "the-dossier-zero",
        "series": "The Dossier Zero",
        "case_file": "Case File #05",
        "title": "THE BLUE POWDER OF DEATH: The Goiânia Radiological Catastrophe (1987)",
        "channel": "@TheDossierZero",
        "fps": 30,
        "width": 1920,
        "height": 1080,
        "total_scenes": total_scenes,
        "total_words": total_words,
        "scenes": scenes_data
    }
    
    json_path = os.path.join(SCRIPT_DIR, "storyboard_48_scenes.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"[OK] JSON Storyboard saved to: {json_path}")
    
    # Generate Markdown Script & Storyboard
    md_path = os.path.join(SCRIPT_DIR, "SCRIPT_AND_STORYBOARD.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# THE DOSSIER ZERO // CASE FILE #05\n")
        f.write("## THE BLUE POWDER OF DEATH: The Goiânia Radiological Catastrophe (1987)\n\n")
        f.write(f"- **Total Acts**: 8 Acts (Exactly 6 Scenes per Act = 48 Scenes)\n")
        f.write(f"- **Total Words**: {total_words} words\n")
        f.write(f"- **Target Duration**: ~{est_audio_sec/60.0:.2f} minutes ({est_frames} frames @ 30 FPS)\n")
        f.write(f"- **Compliance**: IAEA Official Report 1988 (\"The Radiological Accident in Goiânia\")\n\n---\n\n")
        
        current_act = 0
        for s in scenes_data:
            if s["act"] != current_act:
                current_act = s["act"]
                f.write(f"\n## {s['act_title']}\n\n")
            
            f.write(f"### [Scene {s['scene_id']}] {s['kinetic_hook_headline']}\n")
            f.write(f"**Voiceover Narration** ({s['word_count']} words):\n")
            f.write(f"> \"{s['voiceover_text']}\"\n\n")
            f.write(f"- **Telemetry**: `{s['telemetry']}`\n")
            f.write(f"- **Camera Shot**: `{s['camera_shot']}` | Motion: `{s['camera_motion']}`\n")
            f.write(f"- **Visual Prompt**: `{s['codex_image_prompt']}`\n\n---\n")
            
    print(f"[OK] Markdown Script saved to: {md_path}")

if __name__ == "__main__":
    main()
