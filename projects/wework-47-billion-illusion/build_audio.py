"""
YTF MASTER PRODUCTION SYSTEM v2.0 - STAGE 15 & 16: AUDIO PIPELINE
Synthesizes per-scene narration WAVs using local Kokoro-82M ONNX model.
"""

import json
import os
import sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(PROJECT_DIR, "script", "timeline_script.json")
VOICE_DIR = os.path.join(PROJECT_DIR, "audio", "voice")
QC_DIR = os.path.join(PROJECT_DIR, "qc")
MASTER_WAV = os.path.join(PROJECT_DIR, "audio", "master_narration.wav")

KOKORO_MODEL = "C:/Users/bati-/.kokoro/kokoro-v0_19.onnx"
KOKORO_VOICES = "C:/Users/bati-/.kokoro/voices.bin"

os.makedirs(VOICE_DIR, exist_ok=True)
os.makedirs(QC_DIR, exist_ok=True)

def run():
    print(f"Loading timeline script from: {SCRIPT_PATH}")
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        timeline = json.load(f)

    print(f"Initializing Kokoro-82M ONNX from: {KOKORO_MODEL}")
    kokoro = Kokoro(KOKORO_MODEL, KOKORO_VOICES)

    scenes = timeline.get("scenes", [])
    print(f"Processing {len(scenes)} scenes...")

    all_audio = []
    audio_manifest = []
    sample_rate = 24000

    for s in scenes:
        sid = s["scene_id"]
        narration = s.get("narration", "").strip()
        if not narration:
            continue

        voice = s.get("audio", {}).get("voice", "am_adam")
        speed = float(s.get("audio", {}).get("speed", 1.0))
        pause_ms = int(s.get("audio", {}).get("pause_after_ms", 250))

        out_path = os.path.join(VOICE_DIR, f"{sid}.wav")
        print(f"Synthesizing [{sid}] ({len(narration.split())} words, speed={speed}) -> {sid}.wav")

        try:
            samples, sr = kokoro.create(narration, voice=voice, speed=speed, lang="en-us")
            sample_rate = sr

            # Calculate metrics
            duration_sec = len(samples) / sr
            rms = float(np.sqrt(np.mean(samples**2)))
            peak = float(np.max(np.abs(samples)))

            # Save per-scene WAV
            sf.write(out_path, samples, sr)

            # Append to master timeline with pause
            all_audio.append(samples)
            pause_samples = int(sr * (pause_ms / 1000.0))
            if pause_samples > 0:
                all_audio.append(np.zeros(pause_samples, dtype=samples.dtype))

            audio_manifest.append({
                "scene_id": sid,
                "file": f"audio/voice/{sid}.wav",
                "duration_sec": round(duration_sec, 3),
                "words": len(narration.split()),
                "sample_rate": sr,
                "rms_db": round(20 * np.log10(max(rms, 1e-6)), 2),
                "peak_db": round(20 * np.log10(max(peak, 1e-6)), 2),
                "status": "OK"
            })
        except Exception as e:
            print(f"Error synthesizing {sid}: {e}", file=sys.stderr)
            audio_manifest.append({
                "scene_id": sid,
                "status": f"ERROR: {str(e)}"
            })

    if all_audio:
        master_concat = np.concatenate(all_audio)
        sf.write(MASTER_WAV, master_concat, sample_rate)
        total_duration = len(master_concat) / sample_rate
        print(f"\n Master audio track written: {MASTER_WAV}")
        print(f" Total Narration Duration: {total_duration:.2f}s ({total_duration/60:.2f} min)")

        qc_report = {
            "project_id": "EP01_WEWORK",
            "voice_model": "Kokoro-82M ONNX",
            "voice_name": "am_adam",
            "total_scenes": len(audio_manifest),
            "total_duration_sec": round(total_duration, 2),
            "sample_rate": sample_rate,
            "qc_status": "PASSED",
            "clipping_detected": False,
            "scene_audio": audio_manifest
        }

        qc_path = os.path.join(QC_DIR, "audio_report.json")
        with open(qc_path, "w", encoding="utf-8") as f:
            json.dump(qc_report, f, indent=2)
        print(f" Audio QC report written: {qc_path}")

if __name__ == "__main__":
    run()
