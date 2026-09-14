import asyncio
import os
import math
import edge_tts

VOICE = "id-ID-ArdiNeural"
# Alternative English: "en-US-ChristopherNeural"

SENTENCES_TEXT = [
    "Bayangkan kamu adalah manusia purba 10.000 tahun lalu.",
    "Kamu menemukan sebuah batu kristal merah delima yang aneh di dalam gua gelap.",
    "Karena penasaran, kamu melemparkan batu merah itu ke dalam kobaran api unggun.",
    "Tiba-tiba hal mustahil terjadi! Batunya tidak hangus menjadi abu,",
    "melainkan mulai berdarah cairan perak mengkilap yang menetes dan mengalir!",
    "Logam cair ini tidak membasahi kulitmu, memantul licin bagai cermin, dan sangat berat.",
    "Inilah merkuri, atau Quicksilver!",
    "Batu merah tersebut adalah Cinabar, senyawa alami merkuri dan sulfur.",
    "Panas api unggun di atas 357 derajat Celsius memecah ikatan kimianya,",
    "sehingga uapnya langsung mengembun menjadi tetesan air raksa murni.",
    "Dari ketidaksengajaan manusia purba yang bermain api,",
    "lahirlah elemen paling mistis dan mematikan dalam sejarah sains peradaban manusia!"
]

FULL_SCRIPT = " ".join(SENTENCES_TEXT)

OUTPUT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_AUDIO = os.path.join(OUTPUT_DIR, "narration.mp3")
TIMESTAMP_FILE = os.path.join(OUTPUT_DIR, "sentence_timestamps.json")

async def main():
    print("[1/2] Generating Indonesian Neural Voiceover (id-ID-ArdiNeural)...")
    communicate = edge_tts.Communicate(FULL_SCRIPT, VOICE, rate="+8%", pitch="+0Hz")
    
    boundaries = []
    with open(OUTPUT_AUDIO, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                boundaries.append({
                    "offset": chunk["offset"],
                    "duration": chunk["duration"],
                    "text": chunk["text"]
                })

    print(f"[OK] Voice narration saved: {OUTPUT_AUDIO}")
    print("\n[2/2] Precise Sentence Boundaries for Remotion Keyframing:")
    print(f"{'SEC':<7} | {'FRAME (30fps)':<14} | {'DUR(s)':<6} | SENTENCE")
    print("-" * 80)
    
    parsed_timestamps = []
    total_sec = 0
    for item in boundaries:
        s = item["offset"] / 10000000.0
        d = item["duration"] / 10000000.0
        f = int(s * 30)
        total_sec = max(total_sec, s + d)
        text = item["text"]
        print(f"{s:6.2f}s | Frame {f:5d}       | {d:5.2f}s | {text}")
        parsed_timestamps.append({
            "start_sec": round(s, 2),
            "duration_sec": round(d, 2),
            "start_frame": f,
            "duration_frames": int(d * 30),
            "text": text
        })

    total_frames = int(math.ceil((total_sec + 2.0) * 30))
    print(f"\nTotal Audio Duration: {total_sec:.2f}s")
    print(f"Target Remotion Duration: {total_frames} frames ({total_frames/30:.2f}s with outro buffer)")

    import json
    with open(TIMESTAMP_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "total_sec": total_sec,
            "total_frames": total_frames,
            "sentences": parsed_timestamps
        }, f, indent=2, ensure_ascii=False)
    print(f"[OK] Timestamps saved to {TIMESTAMP_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
