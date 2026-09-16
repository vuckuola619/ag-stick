import json
import os

MANIFEST_FILE = r"projects/demon-core-10min/script/demon_core_manifest.json"
OUTPUT_SRT = r"projects/demon-core-10min/packaging/the_demon_core_subtitles.srt"

def format_timestamp(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        millis = 999
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def split_into_phrases(text: str, max_words: int = 12) -> list[str]:
    words = text.split()
    phrases = []
    current = []
    for w in words:
        current.append(w)
        if len(current) >= max_words or (len(current) >= 7 and w.endswith(('.', '!', '?', ';', ','))):
            phrases.append(" ".join(current))
            current = []
    if current:
        phrases.append(" ".join(current))
    return phrases

def generate_srt():
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    srt_entries = []
    entry_idx = 1

    for scene in data["scenes"]:
        scene_start = scene["start_sec"]
        speech_dur = scene["speech_duration_sec"]
        full_text = scene["voiceover_text"]

        phrases = split_into_phrases(full_text)
        if not phrases:
            continue

        total_words = len(full_text.split())
        current_time = scene_start

        for p in phrases:
            p_words = len(p.split())
            p_dur = (p_words / total_words) * speech_dur
            p_end = current_time + p_dur

            start_ts = format_timestamp(current_time)
            end_ts = format_timestamp(p_end)

            srt_entries.append(f"{entry_idx}\n{start_ts} --> {end_ts}\n{p}\n")
            entry_idx += 1
            current_time = p_end

    os.makedirs(os.path.dirname(OUTPUT_SRT), exist_ok=True)
    with open(OUTPUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))

    print(f"[OK] Generated {len(srt_entries)} subtitle cues in {OUTPUT_SRT}")

if __name__ == "__main__":
    generate_srt()
