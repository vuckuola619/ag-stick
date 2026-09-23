import json
import os

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium"
SCRIPT_FILE = os.path.join(PROJECT_DIR, "script", "storyboard_48_scenes.json")
MD_FILE = os.path.join(PROJECT_DIR, "script", "SCRIPT_AND_STORYBOARD.md")

with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Expanded texts ensuring deep investigative narration hitting 2,050 - 2,150 words total (~43-46 words per scene)
expansions = {
    "01": "In the central Brazilian state of Goias, on Avenida Paranaiba in the heart of Goiania, the abandoned Instituto Goiano de Radioterapia stood in decaying silence. Following an acrimonious legal battle in 1985, the clinic owners had vacated the building, abandoning an unsecured subterranean treatment vault that still housed an active, lethal teletherapy unit.",
    "02": "On the morning of Sunday, September 13, 1987, two impoverished local scavengers, twenty-two-year-old Roberto dos Santos Alves and nineteen-year-old Wagner Mota Pereira, slipped through the unguarded perimeter. Armed with rusted screwdrivers and a squeaking wheelbarrow, they hunted for scrap metal to sell to local junkyards for pocket money.",
    "03": "Deep inside the ruined bunker, they discovered an Italian-made Cesapan radiation therapy machine. Believing the massive protective lead housing could be sold for valuable scrap lead, they used hammers, wrenches, and crowbars to forcibly detach the heavy rotating cylindrical head from its mechanical gantry mountings.",
    "04": "Straining under the immense weight of the hundred-kilogram lead assembly, the two scavengers loaded the heavy cylinder into their wheelbarrow. Under the blazing tropical sun, they wheeled the lethal cargo directly through the busy public streets of Goiania, taking it to Roberto's modest residential home on Rua 57.",
    "05": "That very evening, both men began vomiting violently, accompanied by severe dizziness and acute gastrointestinal cramps. Assuming they had suffered food poisoning from spoiled tropical fruit, they rested in bed, entirely unaware that invisible gamma rays were already destroying their cellular DNA and burning deep erythema blisters into their hands.",
    "06": "Over the next three days, Roberto continued hammering relentlessly at the cylinder in his backyard. Finally, driving a hardened screwdriver into the aperture, he punctured the one-millimeter iridium window of the internal containment capsule—breaching the deadliest radioactive source ever unleashed across the entire Western Hemisphere.",
    "07": "On Friday, September 18, Roberto sold the punctured lead cylinder to Devair Alves Ferreira, the owner of a bustling neighborhood scrap metal yard on Rua 26-A in the Aeroporto district. Devair paid eighteen dollars for the scrap and hauled the mysterious heavy device into his dark garage.",
    "08": "That night, stepping into the unlit garage shed, Devair stopped dead in his tracks. From inside the punctured lead cylinder, a mesmerizing, incandescent electric blue luminescence was pouring out into the darkness, casting eerie dancing shadows across the concrete walls like a mystical gemstone from another realm.",
    "09": "What Devair was witnessing was not magic. It was fifty point nine terabecquerels—one thousand three hundred and seventy-five Curies—of Caesium-137 chloride salt. The intense ionizing radiation was bombarding surrounding atmospheric nitrogen and humidity, exciting electrons and producing an ethereal, glowing Cherenkov luminescence and radioluminescent blue aura.",
    "10": "Convinced he had discovered a miraculous supernatural relic possessing divine healing energy, Devair carried the glowing cylinder into his family living room. Over the next three days, he proudly invited curious neighbors, relatives, and local scrap dealers to marvel at the enchanted blue light in the dark.",
    "11": "On September 21, eager to extract the valuable lead casing, Devair ordered his two young junkyard employees, Israel Baptista dos Santos and Admilson Alves de Souza, to smash the stubborn mechanism apart. In the open yard, they attacked the cylinder with heavy steel sledgehammers and cold chisels.",
    "12": "The violent sledgehammer impacts pulverized the highly soluble caesium chloride salt into a fine microscopic powder. As the workers swung their hammers, breathing heavily in the humid air, billions of invisible radioactive particles coated their skin and clothing, entered their lungs, and settled permanently into the yard soil.",
    "13": "Fascinated by the blue sparkle, Devair scooped fragments of the powder into small folded paper packets, distributing them as good-luck charms to friends, neighbors, and visiting relatives. Word spread rapidly across the neighborhood that Devair Ferreira possessed miraculous dust that glowed brightly without electricity or flame.",
    "14": "Across Rua 26-A, an eerie carnival atmosphere erupted. Excited young men rubbed the luminous powder onto their forearms and chests to show off in dark alleys. Neighborhood women dabbed sparkling specks behind their ears and across their foreheads like shimmering, exotic party glitter.",
    "15": "Devair's brother, Ivo Ferreira, lived just a few blocks away. Enchanted by the glowing phenomenon, Ivo took a handful of the blue powder home in a plastic bag, placing it onto his family kitchen table to show off as an astonishing scientific curiosity during the evening family dinner.",
    "16": "Inside Ivo's home, his beloved six-year-old daughter, Leide das Neves Ferreira, was sitting on the concrete floor playing. Captivated by the radiant blue sparkle, the little girl poured some of the powder onto the floor, rubbing it across her hands, face, and arms in innocent delight.",
    "17": "While sitting on the contaminated floor surrounded by the glowing residue, Leide was handed a hard-boiled egg and a sandwich. Without washing her hands, she ate the food, inadvertently ingesting over one gigabecquerel of pure Caesium-137 directly into her digestive tract—a massive internal dose of six Gray.",
    "18": "Hours later, when Leide's mother put her to bed and turned off the bedroom lights, she screamed in sheer horror. In the pitch-black room, her little daughter's face, hands, and nightgown were radiating a visible, ghostly blue luminescence. The lethal biological countdown was now irreversibly underway.",
    "19": "By September 25, the festive curiosity collapsed into a waking medical nightmare. Across the Aeroporto district, dozens of residents collapsed with intractable projectile vomiting, severe diarrhea, extreme vertigo, and massive hair loss. Agonizing black radiation burns and necrotizing ulcers erupted across their hands and bodies.",
    "20": "Frantic families rushed their loved ones to local clinics and emergency rooms. But local doctors, having never encountered acute radiation syndrome in their careers, misdiagnosed the outbreak as an aggressive tropical gastroenteritis or allergic food poisoning, sending dying victims back to their contaminated bedrooms with antacids.",
    "21": "While physicians remained completely baffled, one courageous woman recognized the terrifying pattern. Devair's thirty-seven-year-old wife, Maria Gabriela Ferreira, noticed that every single person who touched or stood near the glowing blue powder fell catastrophically ill within hours. The powder was not holy; it was deadly poison.",
    "22": "On the morning of Monday, September 28, Maria Gabriela decided to act alone. Packing the remaining lead fragments and glowing powder into a thick plastic bag, she boarded a crowded public municipal bus and rode across the city center, shielding the deadly radioactive package between her legs.",
    "23": "Arriving at the Goias State Health Surveillance Department—the Vigilancia Sanitaria on Avenida Goias—she carried the bag up the concrete steps and marched into the office of Dr. Paulo Roberto Ferreira, setting the plastic bag directly onto the doctor's wooden administrative desk.",
    "24": "Looking the stunned physician dead in the eye, Maria Gabriela spoke the historic words preserved in the IAEA archives: 'This is what is killing my entire family.' Her single act of decisive bravery stopped city-wide contamination in its tracks—even as it sealed her own tragic death.",
    "25": "Sensing that the mysterious heavy bag contained something profoundly hazardous, Dr. Paulo Roberto summoned Dr. Walter Mendes Ferreira, a visiting medical physicist from NUCLEBRAS. Walter borrowed a portable Nardeux scintillation radiation monitor and rushed to Avenida Goias on the morning of September 29.",
    "26": "As Walter walked down the sidewalk toward the health department building, he switched on the scintillation detector. Decades later, he recalled his visceral shock: fifty meters before even reaching the entrance doorway, the analog needle slammed violently past maximum scale, screaming with frantic, saturated audio clicks.",
    "27": "Believing his detector was broken, Walter tested a second radiation survey meter, which instantly pinned at full deflection. Realizing that a massive, unshielded radiological source was sitting inside a crowded government office, Walter sprinted up the stairs, shouting for the immediate, total evacuation of the building.",
    "28": "By that afternoon, an urgent red alert flashed directly to the National Nuclear Energy Commission, CNEN, in Brasilia. Federal authorities recognized an unprecedented national crisis: an unsealed, major industrial teletherapy source was contaminating the sixth largest metropolitan area in Brazil, triggering an INES Level 5 radiological emergency.",
    "29": "Brazilian military helicopters equipped with high-sensitivity sodium iodide gamma-ray spectrometers were deployed over Goiania. Flying low over residential rooftops at dusk, their airborne sensors lit up like Christmas trees, detecting intense radiation plumes beaming up from multiple suburban neighborhoods across the city.",
    "30": "The aerial and ground surveys mapped seven primary epicenters of severe contamination: the abandoned clinic, Roberto's house on Rua 57, Devair's junkyard on Rua 26-A, Ivo's residence, a second scrap yard, and several bus routes where invisible radioactive dust had been tracked.",
    "31": "To prevent widespread civil panic and contain the contamination, federal authorities requisitioned the massive Estadio Olimpico Pedro Ludovico Teixeira in central Goiania. The football stadium was rapidly transformed into the largest civilian radiological triage and decontamination compound ever operated in human history.",
    "32": "Over the following two weeks, more than one hundred and twelve thousand eight hundred terrified citizens—over ten percent of Goiania's entire population—queued for kilometers outside the stadium gates to be scanned one-by-one by hazmat technicians wielding yellow Geiger-Muller survey wands.",
    "33": "Of those screened, two hundred and forty-nine individuals showed significant radioactive contamination. Victims were immediately stripped of all their clothing, which was incinerated as high-level waste, and scrubbed repeatedly with warm water, acetic acid, and chelating soaps in high-pressure chemical decontamination showers.",
    "34": "One hundred and twenty-nine victims suffered dangerous internal contamination. Doctors initiated an unprecedented emergency protocol, administering massive oral doses of Prussian Blue—Radiogardase—an insoluble blue pigment that chemically binds caesium ions in the digestive tract to interrupt enterohepatic cycling and accelerate fecal excretion.",
    "35": "The twenty most critically irradiated patients were admitted to Santa Maria Hospital, while the four worst cases were airlifted aboard Brazilian Air Force transport planes to the specialized Naval Hospital Marcilio Dias in Rio de Janeiro, placed into strict negative-pressure, sterile laminar-flow isolation chambers.",
    "36": "Inside the Rio isolation ward, physicians fought a desperate, losing battle. The overwhelming whole-body radiation doses had completely annihilated the patients' bone marrow stem cells. White blood cell counts plummeted to absolute zero, leaving them totally defenseless against systemic infections, internal hemorrhaging, and multi-organ failure.",
    "37": "In late October, the catastrophe claimed its first lives. Eighteen-year-old junkyard worker Admilson de Souza died on October 18. Thirty-seven-year-old Maria Gabriela Ferreira and six-year-old Leide das Neves both succumbed on October 23. Twenty-two-year-old Israel dos Santos died four days later.",
    "38": "Because their irradiated bodies were still emitting hazardous gamma radiation, public health regulations strictly prohibited conventional burials. Specialized coffins were constructed: thick inner lead sheeting encased inside reinforced waterproof concrete, with each monolithic sarcophagus weighing nearly seven hundred kilograms.",
    "39": "On October 24, when the funeral hearse carrying little Leide das Neves and Maria Gabriela arrived at Cemiterio Parque in Goiania, a violent mob of over two thousand terrified local residents blocked the cemetery gates with trucks, cars, and burning barricades, shouting that radioactive corpses would poison their soil.",
    "40": "The protest erupted into a ferocious riot. Hysterical citizens threw cobblestones, bricks, and bottles at the hearse and government workers. Believing the burials would permanently contaminate the city's groundwater and crater property values, the rioters violently attempted to overturn the funeral vehicles.",
    "41": "State military police deployed tear gas and riot batons to clear the cemetery gates. Under armed military escort, heavy industrial construction cranes hoisted the seven-hundred-kilogram lead coffins high above the shouting crowd, lowering little Leide into a deep, reinforced concrete vault four meters underground.",
    "42": "The survivors bore permanent physical and psychological scars. Roberto Alves suffered severe radiation necrosis and had his right arm amputated. Devair Ferreira survived a lethal seven-Gray exposure, but descended into deep depression and alcoholism, dying in 1994 as a broken, ostracized outcast.",
    "43": "Following the burials, Brazil's nuclear task force launched a ruthless scorched-earth decontamination operation. Entire residential blocks were cordoned off. Seven family houses and three commercial scrap yards were completely demolished down to the bedrock using heavy excavators and wrecking balls.",
    "44": "Heavy earthmovers scraped away the top half-meter of topsoil across entire suburban streets. Thousands of personal possessions—furniture, family photo albums, clothing, automobiles, domestic pets, and mature shade trees—were seized and condemned to eliminate any lingering trace of radioactive caesium.",
    "45": "The colossal cleanup produced three thousand five hundred cubic meters—over six thousand metric tons—of radioactive debris. The hazardous waste filled fourteen shipping containers, forty-two massive concrete packaging boxes, and three thousand eight hundred hermetically sealed heavy steel drums.",
    "46": "A permanent radioactive waste repository was constructed in the rural hills of Abadia de Goias, twenty kilometers outside the city. The six thousand tons of debris were entombed within massive subterranean reinforced concrete vaults engineered to withstand earthquakes, floods, and weathering for centuries.",
    "47": "With a physical half-life of thirty point seventeen years, Caesium-137 decays slowly into Barium-137m, emitting penetrating gamma rays with every disintegration. It will take ten half-lives—three full centuries—until the blue powder entombed beneath Abadia de Goias finally decays into harmless, inert barium.",
    "48": "The Goiania catastrophe remains the world's most sobering testament to the danger of forgotten radioactive sources. It was neither a reactor meltdown nor an act of war, but a simple discarded capsule that ignited an atomic tragedy. Case File zero five is officially archived."
}

for sc in data["scenes"]:
    s_id = sc["scene_id"]
    if s_id in expansions:
        sc["voiceover_text"] = expansions[s_id]
        sc["word_count"] = len(expansions[s_id].split())

total_words = sum(s["word_count"] for s in data["scenes"])
data["total_words"] = total_words

with open(SCRIPT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"[OK] Updated script: Total Scenes = {len(data['scenes'])}, Total Words = {total_words}")

# Re-write Markdown file
with open(MD_FILE, "w", encoding="utf-8") as f:
    f.write("# THE DOSSIER ZERO // CASE FILE #05\n")
    f.write("## THE BLUE POWDER OF DEATH: The Goiânia Radiological Catastrophe (1987)\n\n")
    f.write(f"- **Total Acts**: 8 Acts (Exactly 6 Scenes per Act = 48 Scenes)\n")
    f.write(f"- **Total Words**: {total_words} words\n")
    f.write(f"- **Target Duration**: ~{(total_words/160.0 + 48*0.4/60.0):.2f} minutes\n")
    f.write(f"- **Compliance**: IAEA Official Report 1988 (\"The Radiological Accident in Goiânia\")\n\n---\n\n")
    
    current_act = 0
    for s in data["scenes"]:
        if s["act"] != current_act:
            current_act = s["act"]
            f.write(f"\n## {s['act_title']}\n\n")
        
        f.write(f"### [Scene {s['scene_id']}] {s['kinetic_hook_headline']}\n")
        f.write(f"**Voiceover Narration** ({s['word_count']} words):\n")
        f.write(f"> \"{s['voiceover_text']}\"\n\n")
        f.write(f"- **Telemetry**: `{s['telemetry']}`\n")
        f.write(f"- **Camera Shot**: `{s['camera_shot']}` | Motion: `{s['camera_motion']}`\n")
        f.write(f"- **Visual Prompt**: `{s['codex_image_prompt']}`\n\n---\n")

print(f"[OK] Re-generated Markdown script at {MD_FILE}")
