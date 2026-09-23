import kokoro_onnx
import soundfile as sf
import subprocess
import os
import json
import shutil
import numpy as np

ONNX_MODEL = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\kokoro-v1.0.onnx"
VOICES_BIN = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\voices-v1.0.bin"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium"
AUDIO_DIR = os.path.join(PROJECT_DIR, "audio")
SCENES_AUDIO_DIR = os.path.join(AUDIO_DIR, "scenes")

REMOTION_PUBLIC_ASSETS = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\goiania_caesium_137"
REMOTION_SCENES_AUDIO_DIR = os.path.join(REMOTION_PUBLIC_ASSETS, "audio", "scenes")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(SCENES_AUDIO_DIR, exist_ok=True)
os.makedirs(REMOTION_PUBLIC_ASSETS, exist_ok=True)
os.makedirs(REMOTION_SCENES_AUDIO_DIR, exist_ok=True)

MANIFEST_IN = os.path.join(PROJECT_DIR, "script", "storyboard_48_scenes.json")
MANIFEST_OUT = os.path.join(PROJECT_DIR, "script", "goiania_caesium_manifest.json")
MANIFEST_REMOTION = os.path.join(REMOTION_PUBLIC_ASSETS, "manifest.json")

def main():
    print("=======================================================================", flush=True)
    print("=== SYNTHESIZING KOKORO 82M ENGLISH VOICEOVER (48 SCENES / 8 ACTS) ===", flush=True)
    print("=== Voice: am_adam @ 1.05x speed | Target: ~13:30 mins @ 30 FPS     ===", flush=True)
    print("=======================================================================\n", flush=True)
    
    with open(MANIFEST_IN, 'r', encoding='utf-8') as f:
        storyboard = json.load(f)
        
    scenes = storyboard['scenes']
    kokoro = kokoro_onnx.Kokoro(ONNX_MODEL, VOICES_BIN)
    
    sample_rate = 24000
    fps = 30
    
    combined_samples = []
    scene_manifest = []
    current_time_sec = 0.0
    current_frame = 0
    
    # 0.4s breathing pause between scenes for natural investigative documentary cadence
    pause_sec = 0.4
    pause_samples = np.zeros(int(sample_rate * pause_sec), dtype=np.float32)
    pause_frames = int(pause_sec * fps)
    
    for idx, sc in enumerate(scenes):
        s_id = sc["scene_id"]
        text = sc["voiceover_text"]
        print(f"[{idx+1:02d}/48] Scene {s_id} | {sc['kinetic_hook_headline']} ({sc['word_count']} words)...", flush=True)
        
        # Synthesize with Kokoro am_adam @ speed 1.05
        samples, sr = kokoro.create(text, voice="am_adam", speed=1.05, lang="en-us")
        dur_sec = len(samples) / sr
        
        # Save individual scene audio
        scene_wav_path = os.path.join(SCENES_AUDIO_DIR, f"scene_{s_id}.wav")
        sf.write(scene_wav_path, samples, sr)
        
        # Copy to Remotion public directory
        remotion_scene_wav = os.path.join(REMOTION_SCENES_AUDIO_DIR, f"scene_{s_id}.wav")
        shutil.copyfile(scene_wav_path, remotion_scene_wav)
        
        # Compute exact frame timings
        speech_frames = int(np.ceil(dur_sec * fps))
        total_scene_frames = speech_frames + pause_frames
        
        scene_info = {
            "scene_id": s_id,
            "act": sc["act"],
            "act_title": sc["act_title"],
            "kinetic_hook_headline": sc["kinetic_hook_headline"],
            "voiceover_text": text,
            "word_count": sc["word_count"],
            "start_sec": round(current_time_sec, 2),
            "speech_duration_sec": round(dur_sec, 2),
            "total_scene_duration_sec": round(dur_sec + pause_sec, 2),
            "start_frame": current_frame,
            "speech_frames": speech_frames,
            "duration_frames": total_scene_frames,
            "end_frame": current_frame + total_scene_frames,
            "camera_shot": sc.get("camera_shot", "medium"),
            "camera_motion": sc.get("camera_motion", "slow_push_in"),
            "telemetry": sc.get("telemetry", {}),
            "audio_file": f"assets/goiania_caesium_137/audio/scenes/scene_{s_id}.wav",
            "image_file": f"assets/goiania_caesium_137/scenes/scene_{s_id}.png",
            "codex_image_prompt": sc["codex_image_prompt"]
        }
        scene_manifest.append(scene_info)
        
        combined_samples.append(samples)
        combined_samples.append(pause_samples)
        
        current_time_sec += dur_sec + pause_sec
        current_frame += total_scene_frames

    # Concatenate all audio samples
    all_audio = np.concatenate(combined_samples)
    total_audio_sec = len(all_audio) / sample_rate
    total_frames = current_frame
    total_minutes = total_audio_sec / 60.0
    
    print(f"\n[SUMMARY] Total Audio Duration: {total_audio_sec:.2f}s ({total_minutes:.2f} min), Total Frames: {total_frames} @ 30fps", flush=True)
    
    # Save unmastered raw master WAV
    raw_wav_path = os.path.join(AUDIO_DIR, "voiceover_raw.wav")
    sf.write(raw_wav_path, all_audio, sample_rate)
    
    # Master audio: Highpass 120Hz, Vocal Presence EQ 3.2kHz, EBU R128 (-16.0 LUFS, TP -1.5 dBFS)
    mastered_wav_path = os.path.join(AUDIO_DIR, "voiceover_mastered.wav")
    remotion_master_wav = os.path.join(REMOTION_PUBLIC_ASSETS, "voiceover_mastered.wav")
    
    print("\nMastering audio to EBU R128 (-16.0 LUFS, TP -1.5 dB, EQ 120Hz & 3.2kHz)...", flush=True)
    filter_chain = "highpass=f=120,equalizer=f=3200:t=q:w=1.5:g=2.5,loudnorm=I=-16.0:TP=-1.5:LRA=11"
    cmd = [
        FFMPEG, "-y",
        "-i", raw_wav_path,
        "-af", filter_chain,
        "-ar", "48000",
        mastered_wav_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg error:", res.stderr, flush=True)
        shutil.copyfile(raw_wav_path, mastered_wav_path)
    else:
        print("EBU R128 mastering completed successfully.", flush=True)
        
    shutil.copyfile(mastered_wav_path, remotion_master_wav)
    
    # Write final synchronized manifest
    final_manifest = {
        "project": storyboard["project"],
        "series": storyboard["series"],
        "case_file": storyboard["case_file"],
        "title": storyboard["title"],
        "channel": storyboard["channel"],
        "fps": fps,
        "width": 1920,
        "height": 1080,
        "total_scenes": len(scene_manifest),
        "total_frames": total_frames,
        "total_duration_sec": round(total_audio_sec, 2),
        "total_words": storyboard["total_words"],
        "scenes": scene_manifest
    }
    
    with open(MANIFEST_OUT, 'w', encoding='utf-8') as f:
        json.dump(final_manifest, f, indent=2, ensure_ascii=False)
        
    with open(MANIFEST_REMOTION, 'w', encoding='utf-8') as f:
        json.dump(final_manifest, f, indent=2, ensure_ascii=False)
        
    print(f"\n[OK] Project manifest saved to {MANIFEST_OUT}", flush=True)
    print(f"[OK] Remotion manifest saved to {MANIFEST_REMOTION}", flush=True)

if __name__ == '__main__':
    main()
