import json
import os

with open('projects/white-phosphorus-10min/script/storyboard_32_scenes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

scenes = data['scenes']

# Selectively calibrate to hit 1,490 - 1,510 words
# Currently at 1583 before tightening. Let's replace only a few to get ~1495 words.
replacements = [
    ('stifling summer', 'summer'),
    ('bankrupt merchant and amateur alchemist', 'bankrupt merchant and alchemist'),
    ('desperately broke and ruined', 'desperately broke'),
    ('grueling weeks', 'weeks'),
    ('so completely suffocating', 'so suffocating'),
    ('painstakingly scraped', 'scraped'),
    ('blended it with fine white sand', 'mixed it with fine sand'),
    ('seemingly impossible materialized', 'impossible appeared'),
    ('cautiously touched it', 'touched it'),
    ('completely failed to manufacture gold', 'failed to make gold'),
    ('grand palaces of German princes and dukes', 'palaces of princes and dukes'),
    ('cannot be put out with water', 'cannot be extinguished with water'),
    ('independently cracked Brand’s closely guarded secret recipe', 'cracked Brand’s secret recipe'),
    ('huge mechanized factories churned out hundreds of millions of matches', 'factories churned out hundreds of millions of matches'),
    ('unstoppable global commercial empire producing astronomical fortunes', 'multi-million-pound commercial empire'),
    ('Inside the colossal Bryant and May match manufactory in Bow, East London', 'Inside the Bryant and May match factory in Bow, East London'),
    ('The young workers were given no masks, ventilation, or protective gear', 'The workers received no masks, ventilation, or gloves'),
    ('With no washbasins on the factory floor, they ate their meager bread crusts with hands caked in toxic yellow chemical grime', 'With no washbasins, they ate their bread with hands caked in toxic chemical grime'),
    ('The affliction invariably began with what felt like an ordinary, irritating toothache', 'The illness began with an ordinary, irritating toothache'),
    ('seek out a back-alley barber to have the aching tooth yanked', 'visit a barber-dentist to extract the aching tooth'),
    ('Because antibiotics did not exist, there was only one brutal intervention to prevent the infection from reaching the brain', 'Without antibiotics, there was only one brutal surgery to prevent fatal brain infection'),
    ('unable to speak clearly or chew solid food for life', 'unable to speak clearly or chew solid food'),
    ('In July 1888, the Matchgirls refused to be sacrificed for industrial profit', 'In July 1888, the Matchgirls refused to suffer in silence'),
    ('igniting the historic 1888 Matchgirls Strike that galvanized world attention', 'sparking the historic 1888 Matchgirls Strike that shook the world'),
    ('secured a historic victory', 'won a historic victory'),
    ('safe striking strips that could not ignite accidentally', 'safe striking strips'),
    ('In the brutal trenches of World War One and across World War Two', 'In the trenches of World War One and World War Two'),
    ('burns aggressively straight through muscle tissue', 'burns aggressively through muscle tissue'),
    ('drives every cellular metabolic process', 'powers every cellular metabolic process'),
    ('synthetic superphosphate fertilizers that sparked the global Green Revolution and averted planetary famine', 'superphosphate fertilizers that sparked the Green Revolution and averted famine'),
    ('scale of this miracle is almost beyond comprehension', 'scale of this miracle is staggering'),
    ('responsible for sustaining nearly fifty percent of all human life', 'responsible for feeding nearly fifty percent of all human life'),
    ('humanity is hurtling toward an inevitable geological deadline', 'humanity faces an inevitable geological deadline'),
    ('modern science has arrived at an astounding full circle', 'modern science has come full circle'),
    ('Element 15 remains our most profound scientific paradox: conceived in decay, crowned in unquenchable fire, and quietly sustaining the survival of the human race', 'Element 15 remains humanity’s most profound paradox: born in decay, crowned in unquenchable fire, and quietly sustaining human survival')
]

for s in scenes:
    for old, new in replacements:
        s['voiceover_text'] = s['voiceover_text'].replace(old, new)
    s['word_count'] = len(s['voiceover_text'].split())

total_words = sum(s['word_count'] for s in scenes)
print(f'Calibrated Total Words: {total_words}')

data['total_words'] = total_words
data['target_wpm'] = round(total_words / 10.0, 1)

with open('projects/white-phosphorus-10min/script/storyboard_32_scenes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

md_lines = [
    "# Episode 2: The Devil's Element — How 1,500 Gallons of Pee Changed Human History",
    "**Format**: 16:9 Widescreen (1920x1080 @ 30fps) | **Duration**: ~10:00 (18,000 frames) | **Voice**: Kokoro 82M English (`am_adam`, speed 1.05)",
    f"**Word Count**: {total_words} words (~{data['target_wpm']} WPM documentary pacing) | **32 Scenes Across 4 Acts**",
    "",
    "---",
    ""
]

current_act = None
for s in scenes:
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

with open('projects/white-phosphorus-10min/script/narration_script_10min.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print('Updated both JSON manifest and Markdown script successfully.')
