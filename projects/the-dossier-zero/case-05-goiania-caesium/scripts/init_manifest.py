import json
import os

src = r"projects/the-dossier-zero/case-05-goiania-caesium/script/storyboard_48_scenes.json"
dst = r"projects/wework-47-billion-illusion/remotion/public/assets/goiania_caesium_137/manifest.json"

with open(src, 'r', encoding='utf-8') as f:
    d = json.load(f)

current_frame = 0
for sc in d['scenes']:
    dur_frames = int(len(sc['voiceover_text'].split()) / 160.0 * 60 * 30) + 12
    sc['start_frame'] = current_frame
    sc['duration_frames'] = dur_frames
    sc['end_frame'] = current_frame + dur_frames
    sc['speech_frames'] = dur_frames - 12
    sc['start_sec'] = round(current_frame / 30.0, 2)
    sc['speech_duration_sec'] = round((dur_frames - 12) / 30.0, 2)
    sc['total_scene_duration_sec'] = round(dur_frames / 30.0, 2)
    sc['audio_file'] = f"assets/goiania_caesium_137/audio/scenes/scene_{sc['scene_id']}.wav"
    sc['image_file'] = f"assets/goiania_caesium_137/scenes/scene_{sc['scene_id']}.png"
    current_frame += dur_frames

d['total_frames'] = current_frame
d['total_duration_sec'] = round(current_frame / 30.0, 2)

os.makedirs(os.path.dirname(dst), exist_ok=True)
with open(dst, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print('Initial manifest created with total_frames:', current_frame)
