import asyncio
import os
import math
import json
import edge_tts

VOICE = "id-ID-ArdiNeural"
SCRIPT_FILE = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\scripts\full_documentary_script.md"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
AUDIO_OUT = os.path.join(EXPORT_DIR, "narration_8min.mp3")
TIMESTAMPS_OUT = os.path.join(EXPORT_DIR, "sentence_timestamps_8min.json")
REMOTION_PUBLIC = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets"

os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(REMOTION_PUBLIC, exist_ok=True)

def load_script():
    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract paragraphs excluding headers
    acts = []
    current_act = {"title": "Intro", "paragraphs": []}
    
    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("## BABAK"):
            if current_act["paragraphs"]:
                acts.append(current_act)
            current_act = {"title": line.replace("##", "").strip(), "paragraphs": []}
        elif not line.startswith("#"):
            current_act["paragraphs"].append(line)
    if current_act["paragraphs"]:
        acts.append(current_act)
    
    full_text = " ".join([" ".join(a["paragraphs"]) for a in acts])
    return acts, full_text

async def main():
    acts, full_text = load_script()
    print(f"Loaded {len(acts)} acts, {len(full_text.split())} words.")
    
    # We want a comfortable, authoritative documentary pace (+4% rate)
    rate = "+4%"
    print(f"Generating voiceover with {VOICE} at rate={rate}...")
    communicate = edge_tts.Communicate(full_text, VOICE, rate=rate, pitch="+0Hz")
    
    boundaries = []
    with open(AUDIO_OUT, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                boundaries.append({
                    "offset": chunk["offset"],
                    "duration": chunk["duration"],
                    "text": chunk["text"]
                })
    
    print(f"[OK] Voiceover saved: {AUDIO_OUT} ({os.path.getsize(AUDIO_OUT)} bytes)")
    
    # Parse boundaries
    parsed = []
    total_sec = 0
    for item in boundaries:
        s = item["offset"] / 10000000.0
        d = item["duration"] / 10000000.0
        f = int(s * 30)
        total_sec = max(total_sec, s + d)
        parsed.append({
            "start_sec": round(s, 2),
            "duration_sec": round(d, 2),
            "start_frame": f,
            "duration_frames": int(d * 30),
            "text": item["text"]
        })
    
    total_frames = int(math.ceil((total_sec + 2.0) * 30))
    minutes = total_sec / 60.0
    print(f"\n[SUMMARY]")
    print(f"Total Audio Duration: {total_sec:.2f} seconds ({minutes:.2f} minutes)")
    print(f"Total Sentences: {len(parsed)}")
    print(f"Remotion Target Frames: {total_frames} frames @ 30fps")
    
    data = {
        "voice": VOICE,
        "total_sec": total_sec,
        "total_frames": total_frames,
        "minutes": round(minutes, 2),
        "acts": acts,
        "sentences": parsed
    }
    
    with open(TIMESTAMPS_OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Timestamps saved to {TIMESTAMPS_OUT}")
    
    # Also copy to remotion public
    remotion_audio = os.path.join(REMOTION_PUBLIC, "narration_8min.mp3")
    remotion_json = os.path.join(REMOTION_PUBLIC, "sentence_timestamps_8min.json")
    import shutil
    shutil.copy2(AUDIO_OUT, remotion_audio)
    shutil.copy2(TIMESTAMPS_OUT, remotion_json)
    print(f"[OK] Deployed to Remotion public assets: {remotion_audio}")

if __name__ == "__main__":
    asyncio.run(main())
