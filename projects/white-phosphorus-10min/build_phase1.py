import json
import os

scenes_data = [
    # ACT 1: THE CELLAR ALCHEMIST (0:00 - 2:30 | 150s)
    {
        'scene_id': '01',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '0:00 - 0:18',
        'start_sec': 0.0,
        'end_sec': 18.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': '1,500 GALLONS?!',
        'voiceover_text': 'In the stifling summer of 1669, deep inside a pitch-black stone cellar in Hamburg, Germany, a bankrupt merchant and amateur alchemist named Hennig Brand stood before a towering pyramid of foul wooden oak barrels. Sloshing inside was one thousand five hundred gallons of human urine, collected from local beer-drinking German soldiers.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple expressive wide cartoon eyes, thin black stick limbs with bold 8-10px stroke, wearing a tattered 17th-century alchemist apron, holding a glowing lantern while standing in front of a giant towering stack of wooden oak barrels leaking amber fluid, dark slate charcoal background (#12141A) with faint paper grain texture and subtle vignette, neon electric cyan (#00E5FF) rim highlights, flat 2D vector cartoon, bold crisp outlines, strictly no 3D CGI, no realistic human skin, no hair textures, no gradients, no photorealism.'
    },
    {
        'scene_id': '02',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '0:18 - 0:38',
        'start_sec': 18.0,
        'end_sec': 38.0,
        'duration_sec': 20.0,
        'kinetic_hook_headline': 'THE GOLD OBSESSION',
        'voiceover_text': 'Brand was desperately broke and ruined, but like hundreds of eccentric European alchemists of his era, he was consumed by an obsessive delusion: synthesizing the mythical Philosopher’s Stone. Brand reasoned with childlike alchemical logic that because urine was golden yellow, it must contain microscopic particles of pure elemental gold waiting to be unlocked.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple expressive scheming cartoon eyes, thin black stick limbs with bold 8-10px stroke, pointing at an ancient mystical alchemical parchment showing a glowing alchemical circle transforming a yellow droplet into shiny gold coins, dark slate charcoal background (#1A1D24) with faint parchment grain, bright flame warning yellow (#FFE600) magical symbols and electric cyan (#00E5FF) runic accents, flat 2D vector illustration, thick black outlines, strictly no 3D shading, no realistic human skin, no hair textures, no gradients.'
    },
    {
        'scene_id': '03',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '0:38 - 0:56',
        'start_sec': 38.0,
        'end_sec': 56.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'ROTTEN SECRET',
        'voiceover_text': 'For grueling weeks, Brand allowed the urine to sit undisturbed in open vats until it fermented into a rancid, putrid broth crawling with maggots. The eye-watering stench was so completely suffocating that furious neighbors threatened to burn down his house, yet Brand stubbornly barricaded himself inside his subterranean dungeon laboratory.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple cartoon eyes with spiral dizzy pupils, pinching nose with one stick hand while stirring a gigantic murky wooden vat bubbling with noxious green gas, green stink waves rising into the air, dark charcoal cellar background (#12141A) with textured grain, toxic phosphor green (#00FF66) bubbling fumes, flat 2D vector style, bold clean black strokes, strictly no 3D render, no skin texture, no hair, no gradients.'
    },
    {
        'scene_id': '04',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '0:56 - 1:15',
        'start_sec': 56.0,
        'end_sec': 75.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'BOILING BLACK TAR',
        'voiceover_text': 'He poured hundreds of gallons of the fermented liquid into massive copper cauldrons, boiling them day and night over roaring wood fires. Thick clouds of steam billowed endlessly until the liquid reduced into a pungent red syrup, which eventually charred into a mysterious, pitch-black crusty residue of concentrated organic salts.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple expressive wide cartoon eyes, thin black stick limbs, holding a large iron ladle over a boiling black iron cauldron on a stone hearth, thick gooey black tar paste bubbling inside, dark slate background (#161920) with subtle vignette, hazard orange (#FF6B00) roaring hearth embers and flame warning yellow (#FFE600) fire glow, clean 2D vector cartoon, bold black outlines, strictly no 3D CGI, no skin textures, no gradients.'
    },
    {
        'scene_id': '05',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '1:15 - 1:35',
        'start_sec': 75.0,
        'end_sec': 95.0,
        'duration_sec': 20.0,
        'kinetic_hook_headline': '1,200°C INFERNO',
        'voiceover_text': 'Brand painstakingly scraped this black sludge into heavy clay retorts, blended it with fine white sand, sealed the vessels airtight, and shoved them into his hottest blast furnace. With giant leather bellows, he pumped the flames until the clay glowed white-hot, surpassing an astonishing twelve hundred degrees Celsius.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple focused cartoon eyes, thin black stick limbs, vigorously pumping a giant dual-bellows feeding air into an intensely glowing red-hot clay furnace retort, sparks flying, dark charcoal workshop background (#12141A) with paper grain texture, blazing hazard orange (#FF6B00) furnace glow and flame warning yellow (#FFE600) flying embers, clean 2D vector aesthetic, 10px bold outlines, strictly no 3D effects, no human skin realism, no gradients.'
    },
    {
        'scene_id': '06',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '1:35 - 1:55',
        'start_sec': 95.0,
        'end_sec': 115.0,
        'duration_sec': 20.0,
        'kinetic_hook_headline': 'GHOSTLY VAPOR',
        'voiceover_text': 'Suddenly, through the curved glass alembic tube leading from the furnace into a receiver tub of cold water, something seemingly impossible materialized. A heavy, ghost-like vapor crept through the tubing. It was not metallic gold vapor. It looked like living, luminous ectoplasm slipping quietly through the glass neck.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple wide-eyed shock cartoon eyes with stick jaw dropped, leaning closely over a curved glass alembic distillation tube submerged in a water trough, eerie luminous vapor winding through the pipe, dark charcoal background (#1A1D24) with faint vignette, brilliant glowing toxic phosphor green (#00FF66) vapor trail and electric cyan (#00E5FF) water reflections, flat 2D vector style, bold black outlines, strictly no 3D CGI, no realistic textures, no gradients.'
    },
    {
        'scene_id': '07',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '1:55 - 2:12',
        'start_sec': 115.0,
        'end_sec': 132.0,
        'duration_sec': 17.0,
        'kinetic_hook_headline': 'COLD GREEN FIRE',
        'voiceover_text': 'The vapor condensed under the cold water into a pale, waxy, translucent solid. When Brand retrieved it into the dark room, his heart froze. The substance blazed with a soft, otherworldly green luminescence. He cautiously touched it—it did not burn his skin. It was cold, glowing light trapped inside solid matter.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple amazed sparkling cartoon eyes, thin black stick hands cupping a glistening waxy lump that radiates an intense alien emerald light illuminating his stick face, dark slate cellar background (#12141A) with subtle paper grain texture, radiant toxic phosphor green (#00FF66) omnidirectional glow and electric cyan (#00E5FF) highlights, clean 2D vector linework, bold 8px black stroke, strictly no 3D shading, no human skin, no hair, no gradients.'
    },
    {
        'scene_id': '08',
        'act': 1,
        'act_title': 'The Cellar Alchemist',
        'timestamp_range': '2:12 - 2:30',
        'start_sec': 132.0,
        'end_sec': 150.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'ELEMENT 15 UNLOCKED',
        'voiceover_text': 'Brand named his miraculous discovery Phosphorus mirabilis—the bringer of light, derived from the Greek name for the morning star Lucifer. He had completely failed to manufacture gold, but he had accomplished something far greater: he became the first human being in recorded history to discover a brand-new chemical element.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple triumphant cartoon eyes, wearing a scholar coat, holding high a glowing glass jar containing the luminous green element, beside a floating periodic table tile showing atomic number 15, symbol P, and name PHOSPHORUS, dark slate background (#14171E), vibrant toxic phosphor green (#00FF66) glow and electric cyan (#00E5FF) atomic diagram rings, 2D vector style, bold 10px black ink outlines, strictly no 3D render, no realistic skin, no gradients.'
    },

    # ACT 2: THE ELEMENT THAT BREATHES FIRE (2:30 - 5:00 | 150s)
    {
        'scene_id': '09',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '2:30 - 2:48',
        'start_sec': 150.0,
        'end_sec': 168.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'ROYAL FREAK SHOW',
        'voiceover_text': 'News of Brand’s cold fire spread like wildfire across the kingdoms of Europe. Wealthy royalty and aristocratic salons clamored for live demonstrations. Brand toured the grand palaces of German princes and dukes, charging small fortunes just to let fascinated monarchs write glowing green love letters on velvet curtains that slowly faded away.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple showman cartoon grin, holding a glowing green quill pen writing glowing words on a dark curtain, while a pompous stickman king wearing a golden crown looks on with popping cartoon eyes, dark charcoal royal hall background (#161A22), luminous toxic phosphor green (#00FF66) cursive glow and flame warning yellow (#FFE600) crown accents, clean 2D vector illustration, thick black strokes, strictly no 3D CGI, no realistic anatomy, no gradients.'
    },
    {
        'scene_id': '10',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '2:48 - 3:07',
        'start_sec': 168.0,
        'end_sec': 187.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'BREATHING LIGHT',
        'voiceover_text': 'What mysterious physics allowed this element to glow in the dark without heat? Unlike phosphorescent minerals that merely absorb daylight, white phosphorus was literally breathing. At the microscopic atomic scale, molecules of four phosphorus atoms bound in a strained tetrahedral cage oxidize with ambient air, shedding excess energy as green photons through chemiluminescence.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure scientist with a solid blank white circular head (#ffffff), simple expressive explanatory eyes, pointing at a giant 2D molecular diagram of a tetrahedral P4 molecule surrounded by floating oxygen O2 molecules emitting glowing light packets (photons), dark slate background (#12141A) with technical grid lines, electric cyan (#00E5FF) molecular bonds and toxic phosphor green (#00FF66) photon burst waves, clean 2D vector flat style, bold black outlines, strictly no 3D shading, no gradients.'
    },
    {
        'scene_id': '11',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '3:07 - 3:26',
        'start_sec': 187.0,
        'end_sec': 206.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'INSTANT FIRE: 30°C',
        'voiceover_text': 'Yet this mesmerizing glow concealed a ferocious monster. Because of the intense bond strain trapped inside its tetrahedral geometry, white phosphorus is hyper-reactive. If the ambient temperature warms past just thirty degrees Celsius—barely eighty-six degrees Fahrenheit—it spontaneously detonates into a savage, blinding orange fireball without any warning spark.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple panicked cartoon eyes leaping backward, as a waxy white lump resting on a table next to a thermometer reading 30°C violently erupts into ferocious roaring flames and thick white billowing smoke, dark slate background (#1A1D24) with textured vignette, blazing hazard orange (#FF6B00) and flame warning yellow (#FFE600) fire burst, flat 2D vector cartoon, bold 10px black strokes, strictly no 3D CGI, no human skin realism, no gradients.'
    },
    {
        'scene_id': '12',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '3:26 - 3:45',
        'start_sec': 206.0,
        'end_sec': 225.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'BURNS UNDERWATER?!',
        'voiceover_text': 'Even more terrifying: white phosphorus cannot be put out with water. Plunge a flaming chunk into a beaker of cold water, and it continues crackling, melting, and smoking right beneath the surface. The exact instant it is exposed back to atmospheric air, it reignites with uncontrollable fury, burning straight through whatever it touches.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple expressive amazed cartoon eyes, watching a transparent glass beaker filled with water where a glowing burning chunk of phosphorus continues sizzling and smoking beneath the water line with bubbles and sparks, dark charcoal lab background (#14171E), electric cyan (#00E5FF) water tank and bright hazard orange (#FF6B00) underwater combustion sparks, 2D vector style, bold black outlines, strictly no 3D render, no gradients, no hair textures.'
    },
    {
        'scene_id': '13',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '3:45 - 4:03',
        'start_sec': 225.0,
        'end_sec': 243.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'SCIENTIFIC MONOPOLY',
        'voiceover_text': 'In 1680, renowned English natural philosopher Robert Boyle independently cracked Brand’s closely guarded secret recipe. Boyle streamlined the distillation process, casting pure white phosphorus into sticks stored safely underwater in sealed glass vials, converting what had been a clandestine parlor trick into London’s most lucrative scientific trade.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple scholarly cartoon eyes, wearing a Victorian wig outline, placing glowing cylindrical phosphorus sticks using iron tongs into water-filled glass apothecary bottles labeled with gold seals, dark slate workshop background (#161A22), glowing toxic phosphor green (#00FF66) cylinders and electric cyan (#00E5FF) glass bottles, clean 2D vector art, bold clean lines, strictly no 3D shading, no photorealism, no gradients.'
    },
    {
        'scene_id': '14',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '4:03 - 4:22',
        'start_sec': 243.0,
        'end_sec': 262.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'INSTANT STRIKE',
        'voiceover_text': 'For thousands of years, starting a fire required flint, steel, dry tinder, and agonizing effort. But in 1830, French chemist Charles Sauria unlocked an invention that transformed the daily life of human civilization: he coated wooden pine splints in white phosphorus, sulfur, and potassium chlorate. The modern friction match was born.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure with a solid blank white circular head (#ffffff), simple joyful cartoon eyes, striking a small wooden match against a rough abrasive strip, creating an instant brilliant burst of sparks and a dancing yellow flame at the match tip, dark charcoal background (#12141A) with faint paper texture, dazzling flame warning yellow (#FFE600) flame corona and hazard orange (#FF6B00) sparks, 2D vector flat art, bold black 8px stroke, strictly no 3D CGI, no realistic textures, no gradients.'
    },
    {
        'scene_id': '15',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '4:22 - 4:41',
        'start_sec': 262.0,
        'end_sec': 281.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'MILLIONS OF MATCHES',
        'voiceover_text': 'Instantly, fire became a cheap, instantaneous commodity resting in every coat pocket. Huge mechanized factories churned out hundreds of millions of matches under brand names like Lucifers and Congreves. From illuminating gas streetlamps to lighting parlor hearths and tobacco pipes, the entire Victorian world was powered by Element 15.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure in a Victorian bowler hat standing next to towering stacks of colorful vintage matchboxes with retro typography, surrounded by dozens of tiny matchsticks forming an industrial geometric pattern, dark slate background (#1A1D24) with subtle grain, bright flame warning yellow (#FFE600) and electric cyan (#00E5FF) box labels, clean 2D vector style, thick black outlines, strictly no 3D render, no gradients, no realistic anatomy.'
    },
    {
        'scene_id': '16',
        'act': 2,
        'act_title': 'The Element That Breathes Fire',
        'timestamp_range': '4:41 - 5:00',
        'start_sec': 281.0,
        'end_sec': 300.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'A DEADLY SECRET',
        'voiceover_text': 'By the mid-nineteenth century, the match industry was an unstoppable global commercial empire producing astronomical fortunes. But behind the sparkling modern convenience that lit Victorian hearths lay a monstrous industrial nightmare festering inside the dark sweatshops of East London—a silent biological curse awaiting the most vulnerable workers.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure factory owner in top hat holding a giant gold coin bag, standing in front of a looming dark Victorian brick factory with tall smoking chimneys, while a sinister green haze creeps out from the cracked cellar windows, dark charcoal slate background (#14171E), toxic phosphor green (#00FF66) smog tentacles and flame warning yellow (#FFE600) factory windows, flat 2D vector cartoon, bold 10px black strokes, strictly no 3D effects, no gradients, no hair textures.'
    },

    # ACT 3: THE VICTORIAN NIGHTMARE — PHOSSY JAW (5:00 - 7:30 | 150s)
    {
        'scene_id': '17',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '5:00 - 5:18',
        'start_sec': 300.0,
        'end_sec': 318.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'TEEN FACTORY SLAVES',
        'voiceover_text': 'Inside the colossal Bryant and May match manufactory in Bow, East London, over one thousand four hundred Irish immigrant women and teenage girls labored fourteen punishing hours every day. Known as the Matchgirls, they stood in stifling, unventilated rooms, hand-dipping bundles of splints into steaming vats of hot white phosphorus paste.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figures with solid blank white circular heads (#ffffff), simple exhausted droopy cartoon eyes, thin black stick limbs, wearing ragged Victorian work aprons, lined up along long wooden assembly tables dipping matchstick frames into steaming toxic chemical vats, dark slate industrial background (#12141A) with paper grain, toxic phosphor green (#00FF66) vat steam, clean 2D vector style, bold black outlines, strictly no 3D CGI, no realistic human skin, no hair textures, no gradients.'
    },
    {
        'scene_id': '18',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '5:18 - 5:37',
        'start_sec': 318.0,
        'end_sec': 337.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'BREATHING THE POISON',
        'voiceover_text': 'The air inside the dipping sheds hung heavy with a suffocating, pungent garlic stench—the telltale signature of airborne phosphorus vapor. The young workers were given no masks, ventilation, or protective gear. With no washbasins on the factory floor, they ate their meager bread crusts with hands caked in toxic yellow chemical grime.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure girl with a solid blank white circular head (#ffffff), simple sorrowful cartoon eyes, holding a dry piece of bread with glowing green dust on her stick fingers, surrounded by thick floating swirling gas molecules and dust motes, dark charcoal background (#181B24) with faint textured vignette, toxic phosphor green (#00FF66) particle haze, clean 2D vector linework, bold 8px black stroke, strictly no 3D render, no skin texture, no gradients.'
    },
    {
        'scene_id': '19',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '5:37 - 5:56',
        'start_sec': 337.0,
        'end_sec': 356.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'THE ROT BEGINS',
        'voiceover_text': 'The affliction invariably began with what felt like an ordinary, irritating toothache. A factory girl would seek out a back-alley barber to have the aching tooth yanked. But the empty gum socket refused to close. Instead, the wound festered endlessly, weeping putrid fluid while the deep bone underneath began to throb with unbearable agony.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure clutching the side of its round white head with both stick hands in visible pain, small lightning bolt cartoon agony lines radiating from the jaw area, sitting across from an old Victorian dental chair with antique forceps, dark slate background (#14171E), toxic phosphor green (#00FF66) pain aura and flame warning yellow (#FFE600) agony sparks, clean 2D vector style, bold black outlines, strictly no 3D CGI, no realistic human teeth, no gradients.'
    },
    {
        'scene_id': '20',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '5:56 - 6:15',
        'start_sec': 356.0,
        'end_sec': 375.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'PHOSSY JAW HORROR',
        'voiceover_text': 'This was Phosphorus Necrosis of the Jaw, grimly known as Phossy Jaw. Inhaled phosphorus entered open cavities, forming toxic bisphosphonates that strangled the microscopic blood vessels supplying the jawbone. Completely starved of vital blood flow, the mandible underwent necrosis—literally rotting away and decomposing inside the living patient.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure medical diagram showing a cross-section of a clean white cartoon skull, with the lower jawbone highlighted in a decaying lattice structure cut off from blood vessels, with warning crossbones and scientific calipers, dark charcoal medical slate background (#12141A) with blueprint grid lines, toxic phosphor green (#00FF66) necrosis highlight and electric cyan (#00E5FF) technical lines, clean 2D vector flat art, bold outlines, strictly no 3D CGI, no realistic gore, no gradients.'
    },
    {
        'scene_id': '21',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '6:15 - 6:33',
        'start_sec': 375.0,
        'end_sec': 393.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'GLOWING JAWBONES',
        'voiceover_text': 'The most horrifying symptom appeared in absolute darkness. In the pitch-black shadows of cramped tenement bedrooms, terrified families watched as the sick girl’s mouth, gums, and rotting jaw emitted an eerie, fluorescent greenish glow. The dying, decaying necrotic bone was literally phosphorescing inside her living face.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure sitting on the edge of a simple wooden cot in a completely pitch-black Victorian tenement bedroom, where its lower jaw and mouth area glow with an eerie, vivid, radioactive-style green phosphorescence casting faint light on its stick body, pitch-black charcoal background (#0E1015) with subtle grain texture, intense radiant toxic phosphor green (#00FF66) facial bioluminescence, clean 2D vector style, bold black outlines, strictly no 3D shading, no human skin, no hair, no gradients.'
    },
    {
        'scene_id': '22',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '6:33 - 6:52',
        'start_sec': 393.0,
        'end_sec': 412.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'SURGICAL MUTILATION',
        'voiceover_text': 'Because antibiotics did not exist, there was only one brutal intervention to prevent the infection from reaching the brain: radical surgical amputation. Victorian surgeons held down conscious patients and sawed out the entire lower jawbone. Survivors were left permanently mutilated, unable to speak clearly or chew solid food for life.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure surgeon in a vintage physician apron holding surgical bone instruments next to an antique medical tray, looking somber beside an anatomical chart of a removed lower jawbone, dark slate hospital room background (#161A22), electric cyan (#00E5FF) surgical tool reflections and toxic phosphor green (#00FF66) medical chart accents, flat 2D vector cartoon, bold 10px black strokes, strictly no 3D CGI, no blood, no realistic gore, no gradients.'
    },
    {
        'scene_id': '23',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '6:52 - 7:11',
        'start_sec': 412.0,
        'end_sec': 431.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': '1,400 GIRLS REVOLT!',
        'voiceover_text': 'In July 1888, the Matchgirls refused to be sacrificed for industrial profit. Led by social reformer Annie Besant, fourteen hundred young women dropped their dipping frames and marched out into the streets of London. They rallied outside the British Parliament, creating the historic 1888 Matchgirls Strike that exposed the horrors of Phossy Jaw to the world.',
        'codex_image_prompt': 'Group of minimalist 2D cartoon stick figures with solid blank white circular heads (#ffffff), determined angry cartoon eyes, thin black stick arms thrusting protest signs into the air reading "FAIR WAGES" and "STOP THE POISON", marching united down a cobblestone London street, dark slate city background (#14171E) with paper grain texture, flame warning yellow (#FFE600) protest banners and electric cyan (#00E5FF) lamplight, clean 2D vector linework, bold 8px black stroke, strictly no 3D render, no hair textures, no gradients.'
    },
    {
        'scene_id': '24',
        'act': 3,
        'act_title': 'The Victorian Nightmare: Phossy Jaw',
        'timestamp_range': '7:11 - 7:30',
        'start_sec': 431.0,
        'end_sec': 450.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'THE GLOBAL BAN',
        'voiceover_text': 'Their courageous uprising secured a historic victory. The strike forced sweeping safety regulations and catalyzed modern trade unionism. In 1906, the international Berne Convention officially banned white phosphorus matches across the globe, replacing them with completely harmless Red Phosphorus and safe striking strips that could not ignite accidentally.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure holding up a giant official legal document with a red wax seal and a bold red stamp reading "BANNED", standing beside a modern safe red matchbox labeled "SAFETY MATCH", dark slate government hall background (#181C26), electric cyan (#00E5FF) document glow and hazard orange (#FF6B00) safety match accents, clean 2D vector style, bold black outlines, strictly no 3D shading, no realistic human skin, no gradients.'
    },

    # ACT 4: THE WEAPON & THE MIRACLE (7:30 - 10:00 | 150s)
    {
        'scene_id': '25',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '7:30 - 7:48',
        'start_sec': 450.0,
        'end_sec': 468.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'WEAPONIZED TERROR',
        'voiceover_text': 'Although banned from household matches, the horrific properties of white phosphorus immediately drew the attention of global military arsenals. In the brutal trenches of World War One and across World War Two, militaries packed Element 15 into artillery shells, mortar rounds, and aerial bombs, feared under the combat shorthand Willie Pete.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure soldier with a simple 2D steel helmet outline, crouching behind sandbags as military artillery shells with "WP" stenciled in bold yellow impact in the background, dark charcoal battlefield background (#12141A) with faint smoke texture, blazing hazard orange (#FF6B00) shell explosions and flame warning yellow (#FFE600) blast shockwaves, clean 2D vector art, bold 10px black strokes, strictly no 3D CGI, no blood, no realistic military uniforms, no gradients.'
    },
    {
        'scene_id': '26',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '7:48 - 8:07',
        'start_sec': 468.0,
        'end_sec': 487.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'BURNING TO THE BONE',
        'voiceover_text': 'Exploding WP munitions disperse thousands of burning chemical fragments reaching temperatures over two thousand seven hundred degrees Celsius. The substance adheres tightly to skin, burning aggressively straight through muscle tissue down to bare bone while generating blinding, suffocating white smoke screens that blanket entire battlefields.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure military silhouette standing at a safe distance watching a colossal mushrooming pillar of impenetrable bright white chemical smoke streaked with blinding yellow sparks billowing into the sky, dark slate night horizon background (#14171E), dazzling flame warning yellow (#FFE600) incendiary streamers and electric cyan (#00E5FF) tactical grid lines, flat 2D vector cartoon, bold black outlines, strictly no 3D render, no gore, no gradients.'
    },
    {
        'scene_id': '27',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '8:07 - 8:26',
        'start_sec': 487.0,
        'end_sec': 506.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'THE CODE OF LIFE',
        'voiceover_text': 'Yet here lies the most breathtaking paradox in chemistry: the identical atom capable of horrific devastation is also the indispensable molecular architecture of all life on Earth. Phosphorus forms the structural sugar-phosphate backbone of human DNA and drives every cellular metabolic process through energy-carrying ATP molecules.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure looking upward in wondrous awe at a gigantic luminous 2D glowing DNA double helix structure with sparkling phosphorus atom nodes labeled "P" connected along the spiral ribbon, dark slate cosmic background (#12141A) with subtle star dust grain, electric cyan (#00E5FF) DNA backbone ribbons and toxic phosphor green (#00FF66) atomic nodes, clean 2D vector style, bold clean lines, strictly no 3D shading, no human skin, no gradients.'
    },
    {
        'scene_id': '28',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '8:26 - 8:44',
        'start_sec': 506.0,
        'end_sec': 524.0,
        'duration_sec': 18.0,
        'kinetic_hook_headline': 'FEEDING THE PLANET',
        'voiceover_text': 'Without phosphorus, no plant can establish roots, photosynthesize solar energy, or yield edible grain. In the 20th century, agricultural scientists unlocked techniques to quarry prehistoric marine phosphate rock, processing it into synthetic superphosphate fertilizers that sparked the global Green Revolution and averted planetary famine.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure farmer wearing a simple straw hat outline, standing happily in a vast, lush field of golden wheat, holding a sack of fertilizer marked with the chemical symbol "P - PHOSPHATE", dark charcoal sunrise background (#161A22) with textured paper grain, flame warning yellow (#FFE600) wheat stalks and toxic phosphor green (#00FF66) nutrient energy sprouts, clean 2D vector illustration, bold 8px black stroke, strictly no 3D CGI, no realistic plants, no gradients.'
    },
    {
        'scene_id': '29',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '8:44 - 9:03',
        'start_sec': 524.0,
        'end_sec': 543.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': '4 BILLION FED',
        'voiceover_text': 'The scale of this miracle is almost beyond comprehension. Today, synthetic phosphorus fertilizers are directly responsible for sustaining nearly fifty percent of all human life. Four billion people on Earth are fed because of Element 15. Without synthetic phosphates, global food harvests would immediately drop by half.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure standing beside a giant split globe diagram: one half showing lush green wheat fields with a giant digital counter reading "4,000,000,000 PEOPLE FED", the other half showing a dynamic bar chart surging upward, dark slate background (#12141A) with blueprint lines, electric cyan (#00E5FF) data charts and toxic phosphor green (#00FF66) continent fills, clean 2D vector graphics, bold black outlines, strictly no 3D render, no gradients.'
    },
    {
        'scene_id': '30',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '9:03 - 9:22',
        'start_sec': 543.0,
        'end_sec': 562.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'RUNNING OUT OF ELEMENT 15',
        'voiceover_text': 'However, humanity is hurtling toward an inevitable geological deadline. Unlike nitrogen, phosphorus cannot be extracted from the atmosphere. More than seventy percent of the planet’s remaining high-grade phosphate deposits are concentrated in a single nation: Morocco. Geologists warn that global Peak Phosphorus could arrive within this century.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure geologist pointing a laser pointer at a stylized minimalist world map highlighting a glowing concentrated hotspot over North Africa with a warning gauge reading "70% RESERVES", alarm sirens flashing, dark charcoal command center background (#14171E), hazard orange (#FF6B00) alert icons and electric cyan (#00E5FF) vector continent outlines, flat 2D vector aesthetic, bold 10px black strokes, strictly no 3D CGI, no gradients.'
    },
    {
        'scene_id': '31',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '9:22 - 9:41',
        'start_sec': 562.0,
        'end_sec': 581.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'FULL CIRCLE: PEE TO PRAYER',
        'voiceover_text': 'To avert future agricultural collapse, modern science has arrived at an astounding full circle. Municipal wastewater treatment centers are now constructing high-tech bioreactors to extract pure crystalline struvite fertilizer directly out of human urine and municipal sewage—reclaiming the exact raw material Hennig Brand boiled in his cellar 350 years ago.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure engineer in a hard hat standing beside a futuristic clean recycling loop diagram showing human wastewater transforming inside a transparent bioreactor into sparkling crystal fertilizer pellets, dark slate eco-tech background (#12141A) with subtle grid, electric cyan (#00E5FF) fluid pipes and toxic phosphor green (#00FF66) crystalline struvite pellets, clean 2D vector linework, bold black outlines, strictly no 3D shading, no human skin, no gradients.'
    },
    {
        'scene_id': '32',
        'act': 4,
        'act_title': 'The Weapon and The Miracle',
        'timestamp_range': '9:41 - 10:00',
        'start_sec': 581.0,
        'end_sec': 600.0,
        'duration_sec': 19.0,
        'kinetic_hook_headline': 'THE DEVIL’S ELEMENT',
        'voiceover_text': 'From fifteen hundred gallons of fermented urine in a Hamburg dungeon to glowing jaws, wartime skies, and the grain that feeds four billion living humans today—Element 15 remains our most profound scientific paradox: conceived in decay, crowned in unquenchable fire, and quietly sustaining the survival of the human race.',
        'codex_image_prompt': 'Minimalist 2D cartoon stick figure standing at the center of the frame, split down the middle: left side engulfed in glowing toxic green and orange flames, right side blooming with electric cyan DNA helices and vibrant green wheat stalks, holding a glowing glass flask of Element 15, dark slate charcoal background (#12141A) with textured paper grain and vignette, vibrant toxic phosphor green (#00FF66), electric cyan (#00E5FF), and hazard orange (#FF6B00) rim lights, iconic 2D vector stickman, bold 10px black ink outlines, strictly no 3D CGI, no realistic human skin, no hair textures, no gradients, no photorealism.'
    }
]

total_words = sum(len(s['voiceover_text'].split()) for s in scenes_data)
for s in scenes_data:
    s['word_count'] = len(s['voiceover_text'].split())

print(f"Total scenes: {len(scenes_data)}")
print(f"Total word count: {total_words}")

manifest_payload = {
    'project': "The Devil's Element: How 1,500 Gallons of Pee Changed Human History",
    'fps': 30,
    'total_duration_sec': 600.0,
    'total_frames': 18000,
    'target_wpm': 150,
    'total_words': total_words,
    'scenes': scenes_data
}

manifest_path = 'projects/white-phosphorus-10min/script/storyboard_32_scenes.json'
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest_payload, f, indent=2, ensure_ascii=False)
print(f"Saved manifest: {manifest_path}")

md_lines = [
    "# Episode 2: The Devil's Element — How 1,500 Gallons of Pee Changed Human History",
    "**Format**: 16:9 Widescreen (1920x1080 @ 30fps) | **Duration**: ~10:00 (18,000 frames) | **Voice**: Kokoro 82M English (`am_adam`, speed 1.05)",
    f"**Word Count**: {total_words} words (~150 WPM documentary pacing) | **32 Scenes Across 4 Acts**",
    "",
    "---",
    ""
]

current_act = None
for s in scenes_data:
    if s['act'] != current_act:
        current_act = s['act']
        md_lines.append(f"## ACT {current_act}: {s['act_title'].upper()}")
        md_lines.append("")
    md_lines.append(f"### Scene {s['scene_id']} ({s['timestamp_range']}) — [{s['kinetic_hook_headline']}]")
    md_lines.append(f"**Narration ({s['word_count']} words)**:")
    md_lines.append(f"> {s['voiceover_text']}")
    md_lines.append("")
    md_lines.append("**Codex Image Prompt (2D Stickman Architecture)**:")
    md_lines.append(f"```text\n{s['codex_image_prompt']}\n```")
    md_lines.append("")

script_path = 'projects/white-phosphorus-10min/script/narration_script_10min.md'
with open(script_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Saved script: {script_path}")
