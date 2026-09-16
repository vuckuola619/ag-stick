import subprocess
import os
import sys
import time
import shutil

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\demon-core-10min"
EXPORT_DIR = os.path.join(PROJECT_DIR, "export")
AUDIO_FILE = os.path.join(PROJECT_DIR, "audio", "voiceover_mastered.wav")
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
ARTIFACT_DIR = r"C:\Users\bati-\.gemini\antigravity\brain\33a2fd32-0c45-4eff-809d-a28cbc3d5760"

os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

def render_level_1_clip(start_frame=0, end_frame=600):
    total_frames = end_frame - start_frame + 1
    duration_sec = total_frames / 30.0
    print(f"\n=== Rendering Level 1 (Scene 1): frames {start_frame}-{end_frame} ({total_frames} frames, {duration_sec:.1f}s) ===", flush=True)

    raw_video = os.path.join(EXPORT_DIR, "temp_level_1_raw.mp4")
    final_output = os.path.join(EXPORT_DIR, "demon_core_level_1_review.mp4")
    artifact_output = os.path.join(ARTIFACT_DIR, "demon_core_level_1_review.mp4")

    if os.path.exists(raw_video):
        try:
            os.remove(raw_video)
        except Exception:
            pass

    cmd_remotion = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "DemonCore10Min",
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
        raise RuntimeError("Remotion render failed for Level 1")

    print(f"  [Remotion OK] Rendered {total_frames} frames in {time.time()-t0:.1f}s", flush=True)

    # Cut matching audio slice and multiplex
    audio_slice = os.path.join(EXPORT_DIR, "temp_level_1_audio.wav")
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

    # Copy to artifact dir for instant playback
    shutil.copy2(final_output, artifact_output)

    # Clean up temp files
    try:
        os.remove(raw_video)
        os.remove(audio_slice)
    except Exception:
        pass

    size_mb = os.path.getsize(final_output) / (1024 * 1024)
    print(f"  [SUCCESS] demon_core_level_1_review.mp4 ready! ({size_mb:.2f} MB, {duration_sec:.1f}s)", flush=True)
    return final_output

if __name__ == "__main__":
    render_level_1_clip(0, 600)
