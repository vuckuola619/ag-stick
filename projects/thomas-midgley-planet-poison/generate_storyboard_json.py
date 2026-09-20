import json
import os

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison"
SCRIPT_DIR = os.path.join(PROJECT_DIR, "script")
os.makedirs(SCRIPT_DIR, exist_ok=True)

SUFFIX = (
    ', in the signature 2D cartoon illustration style of YouTube channel Neon Rush, '
    'featuring the iconic minimalist stickman character with a blank white circular head (#ffffff), '
    'simple expressive round cartoon eyes, thin black stick limbs, era-appropriate attire, '
    'bold crisp black ink outlines, clean cel-shading, vibrant high-contrast colors, '
    'punchy high CTR YouTube framing, perfectly centered cinematic composition, 16:9 widescreen composition, '
    'no text, no letters, no numbers, no words, no speech bubbles, no 3D CGI, no photorealism, no realistic human faces'
)

scenes_data = [
    # ACT 1: THE DEADLY KNOCK & THE ENGINE PUZZLE (Scenes 01–05)
    {
        "scene_id": "01",
        "act": 1,
        "act_title": "ACT 1: THE DEADLY KNOCK",
        "kinetic_hook_headline": "THE DEADLIEST ORGANISM",
        "voiceover_text": "In the entire history of planet Earth, no single organism—not the dinosaurs, not the black plague, not even any tyrant—has inflicted more destructive chemical damage upon our atmosphere and living bodies than one smiling, well-intentioned American engineer named Thomas Midgley Junior.",
        "word_count": 48,
        "visual_description": "Thomas Midgley stickman in 1920s suit and round spectacles standing cheerfully in center, holding a smoking glass chemical beaker with skull fumes, beside a giant cracked globe of planet Earth wrapped in yellow hazard caution ribbons.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1921, "location": "DAYTON, OHIO", "lead_blood": "0.5 ug/dL", "ozone": "350 DU", "status": "PRISTINE"},
        "codex_image_prompt": "Minimalist stickman engineer with a blank white circular head (#ffffff), cheerful expressive round cartoon eyes, black round spectacles, wearing a 1920s dark vest and bowtie, standing in center holding a glowing amber glass chemical flask emitting swirling toxic haze, beside a large stylized cartoon globe of Earth with cracked continents" + SUFFIX
    },
    {
        "scene_id": "02",
        "act": 1,
        "act_title": "ACT 1: THE DEADLY KNOCK",
        "kinetic_hook_headline": "THE ROARING ENGINES",
        "voiceover_text": "The year was 1916. The automotive revolution was sweeping across the world, but internal combustion engines faced an existential crisis. When drivers accelerated uphill or pushed their engines hard, a violent metallic pinging sound echoed from the hood. Engineers called it engine knocking.",
        "word_count": 49,
        "visual_description": "Vintage black Model-T automobile driving up a steep hill, steam hissing from front radiator, stickman driver panicking with sweat drops as glowing shockwaves radiate from the engine block.",
        "camera_shot": "wide",
        "camera_motion": "pan_right",
        "telemetry": {"year": 1916, "location": "DETROIT, MICHIGAN", "lead_blood": "0.5 ug/dL", "ozone": "350 DU", "status": "INDUSTRIAL BOOM"},
        "codex_image_prompt": "Minimalist stickman driver with a blank white circular head (#ffffff), wide panicked cartoon eyes, driving an antique black 1916 Model-T car struggling up a steep road hill, thick cartoon smoke and steam puffing from front hood with zigzag acoustic shockwave rings radiating from the vibrating engine compartment" + SUFFIX
    },
    {
        "scene_id": "03",
        "act": 1,
        "act_title": "ACT 1: THE DEADLY KNOCK",
        "kinetic_hook_headline": "SHATTERING PISTONS",
        "voiceover_text": "Engine knocking was not just annoying noise. It was premature, uneven detonation of gasoline vapors that literally cracked iron cylinder heads and smashed pistons to pieces. It capped engine compression ratios, severely choking power and threatening to stall the entire future of modern transportation.",
        "word_count": 47,
        "visual_description": "Cross-section schematic cutaway of an engine cylinder: piston rod snapping under violent fiery explosion, metal sparks flying, mechanical stress lines.",
        "camera_shot": "closeup",
        "camera_motion": "push_in",
        "telemetry": {"year": 1916, "location": "DELCO RESEARCH LAB", "lead_blood": "0.5 ug/dL", "ozone": "350 DU", "status": "KNOCK FAILURE"},
        "codex_image_prompt": "Dramatic cross-section cutaway of a vintage cast-iron automotive cylinder engine, showing a shattered cracked metallic piston rod snapping under intense fiery orange detonation sparks, glowing combustion flames inside the combustion chamber with flying iron shards and crack fissures" + SUFFIX
    },
    {
        "scene_id": "04",
        "act": 1,
        "act_title": "ACT 1: THE DEADLY KNOCK",
        "kinetic_hook_headline": "THE GM MANDATE",
        "voiceover_text": "Enter Charles Kettering, head of research at General Motors, and his brilliant mechanical protégé, Thomas Midgley Junior. Kettering handed Midgley a singular mission: find a chemical additive that could smooth out fuel combustion and eliminate engine knock forever. Midgley embarked on a relentless trial-and-error campaign.",
        "word_count": 50,
        "visual_description": "Executive stickman Kettering in fedora handing a blueprint roll to Midgley stickman in lab coat surrounded by hundreds of colorful glass chemical reagent bottles.",
        "camera_shot": "medium",
        "camera_motion": "static",
        "telemetry": {"year": 1919, "location": "GM RESEARCH LAB", "lead_blood": "0.5 ug/dL", "ozone": "350 DU", "status": "RESEARCH INITIATED"},
        "codex_image_prompt": "Two 1920s stickman figures in an antique laboratory: left figure wearing three-piece suit and fedora gesturing authoritatively, right figure wearing white lab coat and round spectacles holding an open clipboard, surrounded by wooden laboratory workbenches crammed with dozens of colorful glass retorts, test tubes, and chemical flasks" + SUFFIX
    },
    {
        "scene_id": "05",
        "act": 1,
        "act_title": "ACT 1: THE DEADLY KNOCK",
        "kinetic_hook_headline": "TETRAETHYL LEAD",
        "voiceover_text": "Midgley tested thousands of compounds: iodine, melted butter, camphor, and tellurium, which left him smelling like rotting garlic for months. Then, on December ninth, 1921, Midgley poured a tiny fraction of a drop of tetraethyl lead into a knocking test engine. The knocking stopped instantly.",
        "word_count": 48,
        "visual_description": "Midgley stickman using a glass eyedropper to drop a single glowing red liquid droplet into an open engine fuel tank, engine immediately humming smoothly with shiny golden sparkles.",
        "camera_shot": "closeup",
        "camera_motion": "push_in",
        "telemetry": {"year": 1921, "location": "DAYTON, OHIO", "lead_blood": "0.8 ug/dL", "ozone": "350 DU", "status": "TEL SYNTHESIZED"},
        "codex_image_prompt": "Minimalist stickman chemist with a blank white circular head (#ffffff), focused cartoon eyes, wearing white lab coat and round spectacles, using a slender glass pipette dropper to squeeze a single glowing crimson liquid drop into the open brass carburetor of a vintage stationary engine, laboratory background with glowing chemical glassware" + SUFFIX
    },

    # ACT 2: "LOONY GAS" & THE MAD REFINERY (Scenes 06–11)
    {
        "scene_id": "06",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "THE KNOWN POISON",
        "voiceover_text": "There was just one catastrophic problem. Humanity had known for over two thousand years that lead is a devastating neurotoxin. It accumulates silently in bones, destroys brain tissue, triggers hallucinations, and causes irreversible kidney failure. Yet General Motors smelled billions in patent profits.",
        "word_count": 46,
        "visual_description": "Ancient Roman skull stick figure silhouette beside a modern human skeleton x-ray illuminated in poisonous neon green, with heavy lead weights chained to the skull.",
        "camera_shot": "medium",
        "camera_motion": "pull_out",
        "telemetry": {"year": 1922, "location": "MEDICAL WARNING", "lead_blood": "2.5 ug/dL", "ozone": "350 DU", "status": "TOXIC HAZARD"},
        "codex_image_prompt": "An eerie anatomical human stick skeleton glowing with neon toxic green luminescence, with the skull and brain area highlighted in dark ominous purple radiation, surrounded by antique Roman lead water pipes and dark heavy metallic ingots, dark slate background with biohazard warning glow" + SUFFIX
    },
    {
        "scene_id": "07",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "THE \"ETHYL\" DECEPTION",
        "voiceover_text": "To hide the danger from the public, General Motors and Standard Oil formed the Ethyl Gasoline Corporation. They deliberately banned the word \"lead\" from all company letters, billboards, and gas station pumps. Leaded fuel was marketed purely under the friendly, harmless name: Ethyl.",
        "word_count": 48,
        "visual_description": "Vintage 1920s gas station with retro fuel pump dispenser, smiling stickman attendant in white cap holding hose, while boardroom executives count stacks of dollar bills behind dark glass.",
        "camera_shot": "wide",
        "camera_motion": "pan_left",
        "telemetry": {"year": 1923, "location": "NEW YORK CITY", "lead_blood": "4.2 ug/dL", "ozone": "350 DU", "status": "ETHYL CORP LAUNCHED"},
        "codex_image_prompt": "A sunny 1920s vintage American roadside filling station with an art-deco glass globe fuel pump dispenser, a friendly stickman gas attendant wearing uniform cap cheerfully holding a nozzle, while in the shadowed background boardroom silhouettes shake hands over stacks of gold coins" + SUFFIX
    },
    {
        "scene_id": "08",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "THE LOONY GAS BUILDING",
        "voiceover_text": "Production began in 1924 at a Standard Oil refinery in Bayway, New Jersey. Within days, disaster struck. Factory workers began acting erratically, twitching uncontrollably, and shouting at terrifying hallucinations of phantom insects crawling beneath their skin. Locals dubbed the chemical plant the Loony Gas Building.",
        "word_count": 51,
        "visual_description": "Gloomy industrial chemical refinery building with red brick chimneys puffing toxic yellow smoke, factory stickman worker outside clutching his head in terror, hallucinating giant shadowy insect silhouettes crawling all over.",
        "camera_shot": "wide",
        "camera_motion": "push_in",
        "telemetry": {"year": 1924, "location": "BAYWAY, NEW JERSEY", "lead_blood": "45.0 ug/dL", "ozone": "350 DU", "status": "WORKER PSYCHOSIS"},
        "codex_image_prompt": "Dark industrial 1924 oil refinery brick building with smoking iron chimneys and tangled steam pipes, in the foreground a stickman factory worker in overalls panicking with spiral cartoon eyes, clawing at his arms while ghostly shadowy cartoon insects and glowing phantom bugs swirl in the surrounding yellow chemical vapor" + SUFFIX
    },
    {
        "scene_id": "09",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "PSYCHOTIC BREAKDOWN",
        "voiceover_text": "Within a single week, five workers died in violent delirium, straitjacketed in hospital psych wards. Thirty-five more suffered permanent brain damage. New York and New Jersey immediately banned the sale of Ethyl, and the national press began questioning if this fuel was mass suicide.",
        "word_count": 47,
        "visual_description": "Gloomy 1920s hospital ward with barred windows, stickman in white hospital restraint coat thrashing on a cot as doctors in retro head mirrors take notes in horror.",
        "camera_shot": "medium",
        "camera_motion": "static",
        "telemetry": {"year": 1924, "location": "ELIZABETH GENERAL HOSPITAL", "lead_blood": "85.0 ug/dL", "ozone": "350 DU", "status": "5 FATALITIES"},
        "codex_image_prompt": "Somber 1920s hospital infirmary room with barred windows, a stickman patient in white restraint canvas jacket thrashing on an antique iron hospital bed with wild agitated cartoon eyes, while two stickman doctors in lab coats and head mirrors look on with grave shock, cold blue hospital lighting" + SUFFIX
    },
    {
        "scene_id": "10",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "THE 60-SECOND DEMO",
        "voiceover_text": "On October thirtieth, 1924, Midgley called an emergency press conference at the Hotel Pennsylvania. In front of stunned reporters, he poured pure tetraethyl lead over his bare hands, held a bottle beneath his nose, and deeply inhaled the concentrated vapor for sixty seconds, declaring it completely harmless.",
        "word_count": 53,
        "visual_description": "Thomas Midgley stickman standing at an ornate wooden lectern surrounded by vintage flashbulb cameras, washing his bare hands in a glass bowl of amber TEL fluid and deeply inhaling fumes from an uncapped flask with a confident smile.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1924, "location": "HOTEL PENNSYLVANIA, NYC", "lead_blood": "92.0 ug/dL", "ozone": "350 DU", "status": "PRESS DEMO (TEL)"},
        "codex_image_prompt": "Stickman chemist with round spectacles standing behind a wooden press conference podium, holding an amber glass bottle directly beneath his nose, inhaling rising white vapor trails with closed confident eyes, vintage 1920s camera tripods with exploding flash powder lamps in the background" + SUFFIX
    },
    {
        "scene_id": "11",
        "act": 2,
        "act_title": "ACT 2: LOONY GAS & THE MAD REFINERY",
        "kinetic_hook_headline": "SICK IN MIAMI",
        "voiceover_text": "What Midgley concealed from the cameras was that he was already severely poisoned himself. His lungs were damaged and his blood lead levels were dangerous. Immediately after the demonstration, he fled to Miami for months of secluded medical convalescence to flush the heavy metal from his body.",
        "word_count": 48,
        "visual_description": "Midgley stickman lying in a sunny Florida beach lounge chair under a palm tree, wrapped in a blanket, pale and shivering with thermometer in mouth, clutching an ice bag to his head.",
        "camera_shot": "medium",
        "camera_motion": "pull_out",
        "telemetry": {"year": 1925, "location": "MIAMI, FLORIDA", "lead_blood": "78.0 ug/dL", "ozone": "350 DU", "status": "LEAD CONVALESCENCE"},
        "codex_image_prompt": "Stickman in round spectacles lying weak and sickly on a wooden beach lounge chair under a drooping palm tree, wrapped in a thick wool blanket, with an antique glass thermometer in mouth and an ice compress bag on his head, warm tropical sun contrasting with his exhausted pale cartoon expression" + SUFFIX
    },

    # ACT 3: UNLEASHING LEAD ACROSS THE GLOBE (Scenes 12–16)
    {
        "scene_id": "12",
        "act": 3,
        "act_title": "ACT 3: GLOBAL LEAD POISONING",
        "kinetic_hook_headline": "68 MILLION TONS",
        "voiceover_text": "The federal government succumbed to corporate pressure, lifting the sales ban in 1926. For the next sixty years, virtually every automobile, truck, airplane, and tractor on Earth burned leaded gasoline. Over sixty-eight million tons of microscopic lead particles were spewed directly into the global atmosphere.",
        "word_count": 50,
        "visual_description": "Endless multi-lane highway crowded with 1950s cars, tailpipes blasting dark smoky gray plumes upward that merge into a massive planetary cloud engulfing the atmosphere.",
        "camera_shot": "wide",
        "camera_motion": "pan_right",
        "telemetry": {"year": 1955, "location": "GLOBAL HIGHWAYS", "lead_blood": "14.5 ug/dL", "ozone": "345 DU", "status": "68M TONS EMITTED"},
        "codex_image_prompt": "A sprawling multi-lane highway packed with bustling mid-century retro automobiles and cargo trucks, each exhaust pipe spewing thick billowing gray-black exhaust smoke trails that rise and merge into an ominous dark smog canopy covering the city skyline" + SUFFIX
    },
    {
        "scene_id": "13",
        "act": 3,
        "act_title": "ACT 3: GLOBAL LEAD POISONING",
        "kinetic_hook_headline": "IN EVERY BREATH",
        "voiceover_text": "Because lead particles are microscopic, they did not settle harmlessly on roads. They drifted on planetary wind currents into every lung, bloodstream, and glass of water. By the 1970s, the average American had blood lead levels six hundred times higher than pre-industrial human beings.",
        "word_count": 52,
        "visual_description": "Microscopic view of red blood cells flowing through an artery, surrounded by glowing sharp jagged gray lead atoms binding to hemoglobin and cell walls.",
        "camera_shot": "macro",
        "camera_motion": "push_in",
        "telemetry": {"year": 1970, "location": "GLOBAL POPULATION", "lead_blood": "22.0 ug/dL", "ozone": "340 DU", "status": "600X PRE-INDUSTRIAL"},
        "codex_image_prompt": "A stylized scientific cross-section inside a human blood vessel, showing smooth red disc-shaped red blood cells floating in crimson plasma, infiltrated by jagged, spiky metallic dark-gray lead dust particles attaching to the cells with toxic yellow corrosion halos" + SUFFIX
    },
    {
        "scene_id": "14",
        "act": 3,
        "act_title": "ACT 3: GLOBAL LEAD POISONING",
        "kinetic_hook_headline": "THE IQ DROP",
        "voiceover_text": "Lead attacks the developing brains of children, permanently lowering IQ, destroying impulse control, and inducing aggressive behavior. Epidemiologists estimate that leaded exhaust reduced the collective intelligence of entire generations by up to five full IQ points across the United States and Europe.",
        "word_count": 49,
        "visual_description": "Child stickman sitting at a school desk struggling with schoolwork, with a downward sloping red graph arrow pointing from a glowing brain illustration above.",
        "camera_shot": "medium",
        "camera_motion": "static",
        "telemetry": {"year": 1975, "location": "PEDIATRIC HEALTH", "lead_blood": "25.0 ug/dL", "ozone": "335 DU", "status": "COGNITIVE DEFICIT"},
        "codex_image_prompt": "A young stickman schoolchild sitting at a small wooden classroom desk, holding a pencil with confused dazed cartoon eyes, above their head is a stylized silhouette of a human brain fading from bright vibrant blue to dull gray, with a declining red stair-step graph line descending beside them" + SUFFIX
    },
    {
        "scene_id": "15",
        "act": 3,
        "act_title": "ACT 3: GLOBAL LEAD POISONING",
        "kinetic_hook_headline": "THE CRIME EXPLOSION",
        "voiceover_text": "Modern criminologists observed an uncanny pattern known as the Lead-Crime Hypothesis. Twenty years after atmospheric lead emissions peaked in any given country, violent crime skyrocketed precisely as poisoned children reached adulthood, and plummeted dramatically twenty years after leaded gas was finally phased out.",
        "word_count": 50,
        "visual_description": "Dramatic split screen comparison: on left, leaded gas exhaust emissions curve from 1950-1970; on right, violent city crime rates curving up identically twenty years later in 1970-1990.",
        "camera_shot": "wide",
        "camera_motion": "pan_left",
        "telemetry": {"year": 1990, "location": "CRIMINOLOGY AUDIT", "lead_blood": "18.0 ug/dL", "ozone": "320 DU", "status": "LEAD-CRIME CURVE"},
        "codex_image_prompt": "A gritty neon-lit city street alleyway under stormy rain, showing the silhouette of a menacing stickman figure fleeing past flashing police siren lights, framed against a towering glowing holographic comparison graph with two twin surging peaks glowing in amber and crimson" + SUFFIX
    },
    {
        "scene_id": "16",
        "act": 3,
        "act_title": "ACT 3: GLOBAL LEAD POISONING",
        "kinetic_hook_headline": "THE GREENLAND ICE",
        "voiceover_text": "The truth was uncovered by geochemist Clair Patterson. While measuring the true age of the Earth using lead isotopes, Patterson found lead contamination everywhere: in deep Antarctic snow, Greenland glaciers, and ancient ocean floor sediment. His fearless thirty-year crusade eventually forced the global ban on lead.",
        "word_count": 49,
        "visual_description": "Heroic stickman scientist Clair Patterson in red arctic parka and goggles, extracting an ice core sample drill cylinder glowing with dark lead dust layers on a windy polar glacier.",
        "camera_shot": "wide",
        "camera_motion": "push_in",
        "telemetry": {"year": 1965, "location": "GREENLAND ICE SHEET", "lead_blood": "15.0 ug/dL", "ozone": "330 DU", "status": "PATTERSON PROOF"},
        "codex_image_prompt": "Heroic stickman geochemist in bright red arctic polar parka, thick mittens, and snow goggles, kneeling on a wind-swept blue polar ice sheet, holding up a transparent cylindrical ice core drill sample showing distinct dark trapped pollution strata layers, polar research tents in background" + SUFFIX
    },

    # ACT 4: THE SECOND CATASTROPHE — REFRIGERATORS & FREON (Scenes 17–22)
    {
        "scene_id": "17",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "REFRIGERATOR BOMBS",
        "voiceover_text": "If Thomas Midgley had stopped with leaded gasoline, his tragic environmental legacy would already be etched into history. But in 1928, General Motors owned Frigidaire, and they had another multi-million dollar engineering crisis. Early household electric refrigerators were ticking chemical time bombs.",
        "word_count": 51,
        "visual_description": "Vintage 1920s rounded metal refrigerator in a domestic kitchen, with a glowing cartoon fuse burning on top and toxic yellow vapor hissing from rusted copper condenser coils on the back.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1928, "location": "FRIGIDAIRE LABS", "lead_blood": "12.0 ug/dL", "ozone": "350 DU", "status": "COOLANT CRISIS"},
        "codex_image_prompt": "A vintage 1928 rounded metal electric refrigerator standing in a domestic kitchen, with thick copper cooling tubes wrapped around the back leaking hissing jets of yellow vapor, stylized with subtle cartoon hazard warning lines radiating around the rattling appliance" + SUFFIX
    },
    {
        "scene_id": "18",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "LETHAL LEAKS",
        "voiceover_text": "Early cooling appliances used toxic, volatile compounds like ammonia, sulfur dioxide, and methyl chloride. A single cracked seal or severed pipe in the middle of the night would fill an apartment with suffocating poison, quietly wiping out entire sleeping families in their beds.",
        "word_count": 48,
        "visual_description": "Nighttime dark apartment bedroom, sleeping stick figures in bed while creeping sinister purple gas silently rolls across the floorboards from a cracked refrigerator door in the adjoining kitchen.",
        "camera_shot": "wide",
        "camera_motion": "pan_right",
        "telemetry": {"year": 1928, "location": "APARTMENT LEAK", "lead_blood": "12.0 ug/dL", "ozone": "350 DU", "status": "AMMONIA POISONING"},
        "codex_image_prompt": "A dimly lit 1920s apartment bedroom at midnight, showing two stickman figures asleep under bedcovers, while through an open hallway door a low, sinister blanket of heavy creeping violet-green chemical gas silently rolls across the wooden floorboards" + SUFFIX
    },
    {
        "scene_id": "19",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "SYNTHESIZING CFC-12",
        "voiceover_text": "Kettering once again summoned Midgley. He needed a non-flammable, non-toxic coolant with a low boiling point. Midgley analyzed the periodic table, and in just three days of frantic chemical synthesis, produced dichlorodifluoromethane—a revolutionary chlorofluorocarbon known as CFC-12, trademarked under the name Freon.",
        "word_count": 51,
        "visual_description": "Midgley stickman at laboratory chalkboard with periodic table, enthusiastically pointing chalk at Carbon, Chlorine, and Fluorine, surrounded by sparkling frosty blue ice crystal beakers.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1928, "location": "DAYTON, OHIO", "lead_blood": "12.0 ug/dL", "ozone": "350 DU", "status": "FREON-12 INVENTED"},
        "codex_image_prompt": "Thomas Midgley stickman wearing lab coat and round spectacles standing excitedly in front of a giant laboratory blackboard marked with chalk molecular diagrams, pointing enthusiastically at a glowing glass flask filled with crystal-clear bubbling liquid surrounded by sparkling blue frost crystals" + SUFFIX
    },
    {
        "scene_id": "20",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "INHALING FREON",
        "voiceover_text": "In April 1930, at the American Chemical Society meeting in Atlanta, Midgley pulled off another theatrical demonstration. He placed his mouth over a flask of pure Freon gas, took a deep breath, and exhaled smoothly over a lit candle, gently extinguishing the flame to thunderous scientific applause.",
        "word_count": 51,
        "visual_description": "Midgley stickman on stage in suit and spectacles, exhaling a gentle plume of white gas over a burning wax candle on a table, candle flame gently blowing out as cheering audience applauds.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1930, "location": "ACS MEETING, ATLANTA", "lead_blood": "12.5 ug/dL", "ozone": "350 DU", "status": "CANDLE STUNT (FREON)"},
        "codex_image_prompt": "Stickman chemist in a 1930s suit and spectacles standing on an auditorium stage, gently exhaling a soft puff of harmless-looking white mist from his mouth toward a small burning wax candle on a wooden table, instantly putting out the glowing flame without any explosion, theater backdrop" + SUFFIX
    },
    {
        "scene_id": "21",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "THE MIRACLE MOLECULE",
        "voiceover_text": "Freon was hailed as a triumphant humanitarian triumph. It unlocked safe domestic refrigerators, commercial air conditioning, skyscrapers in tropical deserts, grocery supermarket freezers, and convenient aerosol spray cans. For four decades, Midgley was showered with every prestigious chemistry award in existence.",
        "word_count": 49,
        "visual_description": "Montage of modern conveniences: gleaming 1950s supermarket freezer aisles, air-conditioned skyscraper windows, and hands pressing aerosol hairspray cans puffing white mist.",
        "camera_shot": "wide",
        "camera_motion": "pan_left",
        "telemetry": {"year": 1950, "location": "GLOBAL CONSUMER BOOM", "lead_blood": "13.0 ug/dL", "ozone": "348 DU", "status": "CFC GLOBAL BOOM"},
        "codex_image_prompt": "A vibrant 1950s montage scene featuring modern consumer marvels: an open grocery supermarket freezer aisle overflowing with frozen foods, gleaming glass skyscraper windows blowing cool air-conditioned breezes, and a vintage aerosol spray can spraying a clean cloud of propellant" + SUFFIX
    },
    {
        "scene_id": "22",
        "act": 4,
        "act_title": "ACT 4: THE REFRIGERATOR MIRACLE",
        "kinetic_hook_headline": "THE IMMORTAL COMPOUND",
        "voiceover_text": "What neither Midgley nor the world's greatest chemists realized was that Freon’s greatest commercial virtue was its deadliest planetary trap. Because CFC molecules were completely inert and unreactive, nothing in the lower atmosphere could break them down: no rain, no oxygen, and no living microbes.",
        "word_count": 49,
        "visual_description": "A shiny indestructible cartoon CFC molecule with a carbon center, two green chlorine spheres, and two purple fluorine spheres, bouncing off rain droplets and lightning bolts unharmed.",
        "camera_shot": "closeup",
        "camera_motion": "push_in",
        "telemetry": {"year": 1960, "location": "TROPOSPHERE", "lead_blood": "15.0 ug/dL", "ozone": "345 DU", "status": "INERT ACCUMULATION"},
        "codex_image_prompt": "A stylized 3D tetrahedral cartoon chemical molecule with glowing emerald chlorine atoms and purple fluorine atoms, floating completely untouched and immune through a stormy gray sky with rain droplets and electric lightning bolts bouncing off its indestructible crystal bonds" + SUFFIX
    },

    # ACT 5: THE SKY IS BREAKING — THE OZONE HOLE (Scenes 23–27)
    {
        "scene_id": "23",
        "act": 5,
        "act_title": "ACT 5: THE SKY IS BREAKING",
        "kinetic_hook_headline": "RISING TO SPACE",
        "voiceover_text": "Billions of tons of escaped Freon began a slow, thirty-year vertical ascent into the sky. Drifting past clouds and storms, the indestructible molecules crossed the tropopause and entered the upper stratosphere, home to Earth's fragile ultraviolet shield: the thin ozone layer.",
        "word_count": 49,
        "visual_description": "Earth atmospheric layers diagram: green aerosol spray plumes rising past fluffy white troposphere storm clouds, entering the deep indigo blue stratosphere where a glowing cyan ozone ribbon circles the globe.",
        "camera_shot": "wide",
        "camera_motion": "pan_up",
        "telemetry": {"year": 1972, "location": "STRATOSPHERE (25 KM)", "lead_blood": "16.0 ug/dL", "ozone": "330 DU", "status": "STRATOSPHERIC ASCENT"},
        "codex_image_prompt": "Panoramic view of Earth atmospheric layers curving over the blue ocean horizon, showing countless sparkling microscopic molecular dots rising upward past white cumulus clouds into the deep navy-blue stratosphere, toward a luminous thin cyan shield ring wrapping the planet" + SUFFIX
    },
    {
        "scene_id": "24",
        "act": 5,
        "act_title": "ACT 5: THE SKY IS BREAKING",
        "kinetic_hook_headline": "ATOMIC CHLORINE",
        "voiceover_text": "In 1974, chemists Mario Molina and F. Sherwood Rowland uncovered the horror. High in the stratosphere, fierce solar ultraviolet radiation finally blasted the CFC molecules apart, shearing off raw, reactive chlorine atoms. A lethal catalytic chain reaction was instantly ignited across the sky.",
        "word_count": 50,
        "visual_description": "Blinding solar ultraviolet beam striking a CFC molecule like a lightning strike, shattering off a sharp glowing green chlorine atom with crackling electrical energy.",
        "camera_shot": "closeup",
        "camera_motion": "push_in",
        "telemetry": {"year": 1974, "location": "UC IRVINE / STRATOSPHERE", "lead_blood": "17.0 ug/dL", "ozone": "310 DU", "status": "UV PHOTOLYSIS"},
        "codex_image_prompt": "A violent high-altitude cosmic scene where intense, blinding violet ultraviolet laser-like solar rays strike a floating CFC molecule in the deep dark sky, shattering the chemical bond with electric purple sparks and releasing a jagged, fiercely glowing neon green chlorine atom" + SUFFIX
    },
    {
        "scene_id": "25",
        "act": 5,
        "act_title": "ACT 5: THE SKY IS BREAKING",
        "kinetic_hook_headline": "CATALYTIC CHAIN",
        "voiceover_text": "A single detached chlorine atom acts as an atomic wrecking ball. It rips an oxygen atom from an ozone molecule, destroys it, regenerates itself, and repeats the cycle up to one hundred thousand times before leaving the atmosphere, systematically dissolving the planet's ultraviolet sunblock.",
        "word_count": 48,
        "visual_description": "Cartoon chlorine atom depicted as a spiked wrecking ball smashing through dozens of tri-atomic ozone O3 molecules, leaving shattered oxygen pairs behind.",
        "camera_shot": "macro",
        "camera_motion": "push_in",
        "telemetry": {"year": 1978, "location": "UPPER ATMOSPHERE", "lead_blood": "16.5 ug/dL", "ozone": "280 DU", "status": "1:100,000 CATALYST"},
        "codex_image_prompt": "Dynamic molecular action scene: an aggressive glowing neon green sphere acting like a wrecking ball smashing through a cluster of glowing three-sphere blue ozone molecules, shattering them into scattered pairs, leaving trails of dissipating cyan sparks in deep space" + SUFFIX
    },
    {
        "scene_id": "26",
        "act": 5,
        "act_title": "ACT 5: THE SKY IS BREAKING",
        "kinetic_hook_headline": "THE RIPPED SHIELD",
        "voiceover_text": "In May 1985, scientists at Halley Bay in Antarctica measured a terrifying sixty percent drop in stratospheric ozone. A continent-sized tear had opened directly over the South Pole. Unfiltered solar radiation was bombarding the planet, threatening catastrophic skin cancer rates, blindness, and collapsing phytoplankton ocean food chains.",
        "word_count": 51,
        "visual_description": "Satellite view of the Antarctic continent with a massive gaping dark violet and black void hole centered over the ice cap, piercing cosmic radiation rays pouring through.",
        "camera_shot": "wide",
        "camera_motion": "pull_out",
        "telemetry": {"year": 1985, "location": "HALLEY BAY, ANTARCTICA", "lead_blood": "12.0 ug/dL", "ozone": "120 DU", "status": "OZONE HOLE CONFIRMED"},
        "codex_image_prompt": "A dramatic satellite orbital view of Earth centered on the snowy white continent of Antarctica, where a giant ominous swirling deep purple and black atmospheric void hole is torn through the glowing blue atmosphere, with harsh solar radiation beams piercing straight down onto the ice" + SUFFIX
    },
    {
        "scene_id": "27",
        "act": 5,
        "act_title": "ACT 5: THE SKY IS BREAKING",
        "kinetic_hook_headline": "SAVING THE SKY",
        "voiceover_text": "Faced with global atmospheric collapse, world leaders signed the historic Montreal Protocol in 1987, universally banning CFCs. It was the most successful environmental treaty in human history, but the damage was so deep that the ozone layer will take until 2066 to fully heal.",
        "word_count": 48,
        "visual_description": "United Nations assembly hall with stickman diplomats standing together and signing a treaty parchment with golden pens, Earth in background slowly regenerating its cyan protective aura.",
        "camera_shot": "wide",
        "camera_motion": "static",
        "telemetry": {"year": 1987, "location": "MONTREAL, CANADA", "lead_blood": "9.0 ug/dL", "ozone": "160 DU", "status": "MONTREAL PROTOCOL"},
        "codex_image_prompt": "A grand international council hall where a row of diverse stickman world diplomats in sharp suits stand together behind a long wooden conference table signing a grand parchment treaty document, while in the panoramic window behind them the planet Earth glows with a rejuvenating cyan atmospheric shield" + SUFFIX
    },

    # ACT 6: THE ULTIMATE IRONY & ETERNAL LEGACY (Scenes 28–32)
    {
        "scene_id": "28",
        "act": 6,
        "act_title": "ACT 6: THE ULTIMATE IRONY",
        "kinetic_hook_headline": "PARALYZED AT 51",
        "voiceover_text": "Long before the world learned that his miracle Freon was destroying the heavens, Thomas Midgley met his own grim destiny. In the autumn of 1940, at the height of his fame, Midgley contracted polio at age fifty-one, leaving his legs permanently paralyzed.",
        "word_count": 47,
        "visual_description": "Older Thomas Midgley stickman with graying hair and spectacles sitting in an antique wooden wheelchair in his study, looking somberly at his inert legs wrapped in a blanket.",
        "camera_shot": "medium",
        "camera_motion": "push_in",
        "telemetry": {"year": 1940, "location": "WORTHINGTON, OHIO", "lead_blood": "14.0 ug/dL", "ozone": "350 DU", "status": "POLIO PARALYSIS"},
        "codex_image_prompt": "An older stickman with round spectacles and graying hair sitting quietly in an antique wooden spoked wheelchair beside a sunlit study window, wearing a 1940s knitted cardigan and a tartan blanket resting over paralyzed motionless legs, somber melancholic expression" + SUFFIX
    },
    {
        "scene_id": "29",
        "act": 6,
        "act_title": "ACT 6: THE ULTIMATE IRONY",
        "kinetic_hook_headline": "THE PULLEY HARNESS",
        "voiceover_text": "Being an obsessive mechanical inventor who could never leave a problem alone, Midgley refused to be trapped in bed. He designed an intricate overhead apparatus of motorized pulleys, cables, winches, and cloth harnesses suspended from his bedroom ceiling to lift himself into his wheelchair.",
        "word_count": 49,
        "visual_description": "Midgley's bedroom with an elaborate complex network of wooden ceiling beams, steel cables, brass pulleys, and canvas straps crisscrossing over an antique wooden bed.",
        "camera_shot": "wide",
        "camera_motion": "pan_up",
        "telemetry": {"year": 1942, "location": "HOME LABORATORY", "lead_blood": "14.0 ug/dL", "ozone": "350 DU", "status": "PULLEY RIG BUILT"},
        "codex_image_prompt": "A 1940s home bedroom dominated by an elaborate mechanical apparatus suspended from the ceiling beams, featuring dozens of brass pulleys, winding steel wire ropes, counterbalance weights, and canvas hoist harnesses hanging directly above a tidy wooden bed" + SUFFIX
    },
    {
        "scene_id": "30",
        "act": 6,
        "act_title": "ACT 6: THE ULTIMATE IRONY",
        "kinetic_hook_headline": "THE FATAL TANGLE",
        "voiceover_text": "On November second, 1944, at his home in Worthington, Ohio, the final tragic irony occurred. While operating the hoist alone, Midgley became hopelessly tangled in the ropes and cables. The motorized mechanism tightened around his neck, and he was strangled to death by his own invention.",
        "word_count": 48,
        "visual_description": "Shadowy, somber bedroom silhouette: the intricate pulley cables hanging taut and tangled, empty wheelchair beside the bed, morning light through lace curtains revealing the tragic mechanical accident.",
        "camera_shot": "medium",
        "camera_motion": "pull_out",
        "telemetry": {"year": 1944, "location": "WORTHINGTON, OHIO", "lead_blood": "14.0 ug/dL", "ozone": "350 DU", "status": "ACCIDENTAL STRANGULATION"},
        "codex_image_prompt": "A somber, respectful shadowy silhouette in a quiet 1944 bedroom at dawn, showing the tangled ropes and pulleys of the ceiling hoist mechanism hanging taut in the morning mist from lace curtains, with an empty wooden wheelchair resting abandoned beside the unmade bed" + SUFFIX
    },
    {
        "scene_id": "31",
        "act": 6,
        "act_title": "ACT 6: THE ULTIMATE IRONY",
        "kinetic_hook_headline": "THE HARSH VERDICT",
        "voiceover_text": "Environmental historian J. R. McNeill delivered the definitive verdict on Midgley's career, writing that he had more adverse impact on the global environment than any other single organism in Earth's history. Author Bill Bryson remarked that Midgley possessed an instinct for the regrettable that was almost uncanny.",
        "word_count": 52,
        "visual_description": "Thomas Midgley stickman standing between two halves of the planet: left side choked in black automotive lead smog, right side with a gaping hole in the purple ozone sky, while history books weigh down on both sides.",
        "camera_shot": "wide",
        "camera_motion": "push_in",
        "telemetry": {"year": 2000, "location": "HISTORICAL AUDIT", "lead_blood": "4.0 ug/dL", "ozone": "220 DU", "status": "MCNEILL VERDICT"},
        "codex_image_prompt": "A conceptual cinematic split composition: stickman inventor in 1920s suit and spectacles standing center-stage between two planetary disasters: to his left, city highways shrouded in gray toxic lead smog; to his right, Earth upper atmosphere with a violet ozone tear under blazing cosmic light" + SUFFIX
    },
    {
        "scene_id": "32",
        "act": 6,
        "act_title": "ACT 6: THE ULTIMATE IRONY",
        "kinetic_hook_headline": "THE LESSON OF MIDGLEY",
        "voiceover_text": "Thomas Midgley Junior was not an evil supervillain; he was an earnest engineer trying to solve immediate industrial problems. His tragedy stands as humanity's greatest cautionary tale: when we alter the chemistry of our planet for short-term convenience, the hidden bill always comes due.",
        "word_count": 51,
        "visual_description": "Planet Earth floating in deep space, slowly healing with a soft glowing emerald and blue atmosphere, surrounded by sparkling clean stars, reminding humanity of the fragility of our biosphere.",
        "camera_shot": "wide",
        "camera_motion": "pull_out",
        "telemetry": {"year": 2026, "location": "FUTURE PLANET EARTH", "lead_blood": "0.9 ug/dL", "ozone": "310 DU", "status": "HEALING BIOSPHERE"},
        "codex_image_prompt": "A breathtaking cinematic orbital view of planet Earth floating serenely in deep dark starlit space, surrounded by a delicate, glowing cyan and sapphire blue atmospheric shield that softly radiates life and healing, cinematic golden cosmic sun flare on horizon" + SUFFIX
    }
]

output_path = os.path.join(SCRIPT_DIR, "storyboard_32_scenes.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump({"title": "THE MAN WHO ACCIDENTALLY POISONED THE ENTIRE PLANET", "total_scenes": len(scenes_data), "scenes": scenes_data}, f, indent=2)

print(f"Successfully generated {len(scenes_data)} scenes to {output_path}")
