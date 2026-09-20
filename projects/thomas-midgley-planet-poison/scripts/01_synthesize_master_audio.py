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

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison"
AUDIO_DIR = os.path.join(PROJECT_DIR, "audio")
SCENES_AUDIO_DIR = os.path.join(AUDIO_DIR, "scenes")
REMOTION_PUBLIC_ASSETS = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\thomas_midgley"
REMOTION_AUDIO_DIR = os.path.join(REMOTION_PUBLIC_ASSETS, "audio", "scenes")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(SCENES_AUDIO_DIR, exist_ok=True)
os.makedirs(REMOTION_PUBLIC_ASSETS, exist_ok=True)
os.makedirs(REMOTION_AUDIO_DIR, exist_ok=True)

MANIFEST_IN = os.path.join(PROJECT_DIR, "script", "storyboard_32_scenes.json")
MANIFEST_OUT = os.path.join(PROJECT_DIR, "script", "thomas_midgley_manifest.json")
MANIFEST_REMOTION = os.path.join(REMOTION_PUBLIC_ASSETS, "manifest.json")

def main():
    print("=== SYNTHESIZING KOKORO 82M ENGLISH VOICEOVER (32 SCENES) ===", flush=True)
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
    
    # 0.4s breathing pause between scenes for natural documentary cadence
    pause_sec = 0.4
    pause_samples = np.zeros(int(sample_rate * pause_sec), dtype=np.float32)
    pause_frames = int(pause_sec * fps)
    
    for idx, sc in enumerate(scenes):
        s_id = sc["scene_id"]
        text = sc["voiceover_text"]
        print(f"[{idx+1:02d}/32] Scene {s_id} | {sc['kinetic_hook_headline']} ({sc['word_count']} words)...", flush=True)
        
        # Synthesize with Kokoro am_adam @ speed 1.05
        samples, sr = kokoro.create(text, voice="am_adam", speed=1.05, lang="en-us")
        dur_sec = len(samples) / sr
        
        # Save individual scene audio locally
        scene_wav_path = os.path.join(SCENES_AUDIO_DIR, f"scene_{s_id}.wav")
        sf.write(scene_wav_path, samples, sr)
        
        # Also copy to Remotion public asset path
        remotion_scene_wav = os.path.join(REMOTION_AUDIO_DIR, f"scene_{s_id}.wav")
        sf.write(remotion_scene_wav, samples, sr)
        
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
            "camera_motion": sc.get("camera_motion", "push_in"),
            "telemetry": sc.get("telemetry", {}),
            "audio_file": f"assets/thomas_midgley/audio/scenes/scene_{s_id}.wav",
            "image_file": f"assets/thomas_midgley/scenes/scene_{s_id}.png",
            "codex_image_prompt": sc["codex_image_prompt"]
        }
        scene_manifest.append(scene_info)
        
        combined_samples.append(samples)
        combined_samples.append(pause_samples)
        
        current_time_sec += dur_sec + pause_sec
        current_frame += total_scene_frames

    # Concatenate all samples
    all_audio = np.concatenate(combined_samples)
    total_audio_sec = len(all_audio) / sample_rate
    total_frames = current_frame
    total_minutes = total_audio_sec / 60.0
    
    print(f"\n[SUMMARY] Total Speech Duration: {total_audio_sec:.2f}s ({total_minutes:.2f} min), Total Frames: {total_frames} @ 30fps", flush=True)
    
    # Write raw unmastered master wav
    raw_wav_path = os.path.join(AUDIO_DIR, "voiceover_raw.wav")
    sf.write(raw_wav_path, all_audio, sample_rate)
    print(f"Saved raw voiceover: {raw_wav_path}", flush=True)
    
    # Audio Mastering via FFmpeg: Highpass 80Hz, Loudnorm -16.0 LUFS, TP -1.0 dBFS
    mastered_wav_path = os.path.join(AUDIO_DIR, "voiceover_mastered.wav")
    mastered_mp3_path = os.path.join(AUDIO_DIR, "voiceover_mastered.mp3")
    remotion_wav_path = os.path.join(REMOTION_PUBLIC_ASSETS, "voiceover_mastered.wav")
    
    print("Mastering audio via FFmpeg (High-pass 80Hz + EBU R128 -16.0 LUFS)...", flush=True)
    cmd = [
        FFMPEG, "-y",
        "-i", raw_wav_path,
        "-af", "highpass=f=80,loudnorm=I=-16.0:TP=-1.0:LRA=11",
        "-ar", "44100",
        mastered_wav_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Saved mastered WAV: {mastered_wav_path}", flush=True)
    
    # Export MP3 for preview
    cmd_mp3 = [
        FFMPEG, "-y",
        "-i", mastered_wav_path,
        "-b:a", "192k",
        mastered_mp3_path
    ]
    subprocess.run(cmd_mp3, check=True)
    print(f"Saved mastered MP3: {mastered_mp3_path}", flush=True)
    
    # Copy to Remotion public assets
    shutil.copyfile(mastered_wav_path, remotion_wav_path)
    print(f"Copied to Remotion: {remotion_wav_path}", flush=True)
    
    # Save final synchronized manifest
    final_manifest = {
        "project": "The Man Who Accidentally Poisoned the Entire Planet (Thomas Midgley Jr. / Lead & CFC)",
        "fps": fps,
        "sample_rate": 44100,
        "total_duration_sec": round(total_audio_sec, 2),
        "total_frames": total_frames,
        "target_wpm": round(sum(s['word_count'] for s in scene_manifest) / total_minutes, 1),
        "total_words": sum(s['word_count'] for s in scene_manifest),
        "voice": "am_adam",
        "speed": 1.05,
        "scenes": scene_manifest
    }
    
    with open(MANIFEST_OUT, 'w', encoding='utf-8') as f:
        json.dump(final_manifest, f, indent=2, ensure_ascii=False)
    with open(MANIFEST_REMOTION, 'w', encoding='utf-8') as f:
        json.dump(final_manifest, f, indent=2, ensure_ascii=False)
        
    print(f"Saved synced manifests: {MANIFEST_OUT} and {MANIFEST_REMOTION}", flush=True)
    print("Audio engineering pipeline completed successfully!", flush=True)

if __name__ == "__main__":
    main()
