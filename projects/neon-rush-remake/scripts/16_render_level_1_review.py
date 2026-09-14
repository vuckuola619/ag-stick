import subprocess
import os
import sys
import time
import shutil

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"
ARTIFACT_DIR = r"C:\Users\bati-\.gemini\antigravity\brain\f39d64bf-6e51-40b4-92eb-7bf63798ce0e"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

AUDIO_FILE = os.path.join(EXPORT_DIR, "master_soundtrack_english_8min.wav")

os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

def render_clip(name, start_frame, end_frame):
    total_frames = end_frame - start_frame + 1
    duration_sec = total_frames / 30.0
    print(f"\n=== Rendering {name}: frames {start_frame}-{end_frame} ({total_frames} frames, {duration_sec:.1f}s) ===", flush=True)

    raw_video = os.path.join(EXPORT_DIR, f"temp_{name}_raw.mp4")
    final_output = os.path.join(EXPORT_DIR, f"{name}.mp4")
    artifact_output = os.path.join(ARTIFACT_DIR, f"{name}.mp4")

    if os.path.exists(raw_video):
        try: os.remove(raw_video)
        except: pass

    cmd_remotion = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "MercuryEnglish8Min",
        raw_video,
        f"--frames={start_frame}-{end_frame}",
        "--gl=angle",
        "--muted",
        "--concurrency=4"
    ]

    t0 = time.time()
    res = subprocess.run(cmd_remotion, cwd=REMOTION_DIR, text=True, capture_output=True)
    if res.returncode != 0:
        print("Remotion Error:", res.stderr)
        print("Remotion Stdout:", res.stdout)
        raise RuntimeError(f"Remotion render failed for {name}")

    print(f"  [Remotion OK] Rendered {total_frames} frames in {time.time()-t0:.1f}s", flush=True)

    # Cut matching audio slice and multiplex
    audio_slice = os.path.join(EXPORT_DIR, f"temp_{name}_audio.wav")
    start_sec = start_frame / 30.0

    cmd_audio = [
        FFMPEG, "-y",
        "-ss", f"{start_sec:.3f}",
        "-t", f"{duration_sec:.3f}",
        "-i", AUDIO_FILE,
        audio_slice
    ]
    subprocess.run(cmd_audio, capture_output=True, check=True)

    # Multiplex audio and video
    cmd_mux = [
        FFMPEG, "-y",
        "-i", raw_video,
        "-i", audio_slice,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        final_output
    ]
    subprocess.run(cmd_mux, capture_output=True, check=True)

    # Copy to artifact dir
    shutil.copy2(final_output, artifact_output)

    # Clean up temp files
    try:
        os.remove(raw_video)
        os.remove(audio_slice)
    except:
        pass

    size_mb = os.path.getsize(final_output) / (1024 * 1024)
    print(f"  [SUCCESS] {name}.mp4 ready! ({size_mb:.2f} MB, {duration_sec:.1f}s)", flush=True)
    return final_output

def main():
    print("=== RENDERING LEVEL 1 REVIEW CLIPS (AUTHENTIC NEON RUSH STYLE) ===", flush=True)
    
    # 1. Level 1 - Scene 01 Review (Hook Scene: 0-540 frames, 18s)
    # Scene 1: "FOUND QUICKSILVER?" Prehistoric Caveman discovery
    s1_path = render_clip("neon_rush_level_1_scene01_review", 0, 540)

    # 2. Level 1 - Full Act 1 Review (Scenes 1 to 4: 0-2043 frames, 68.1s)
    # Scene 1: Prehistoric Discovery, Scene 2: Sacred Cinnabar, Scene 3: Ritual Powder, Scene 4: Almaden Roman Mines
    act1_path = render_clip("neon_rush_level_1_act1_review", 0, 2043)

    print("\n[ALL LEVEL 1 REVIEW DELIVERABLES GENERATED SUCCESSFULLY!]", flush=True)

if __name__ == "__main__":
    main()
