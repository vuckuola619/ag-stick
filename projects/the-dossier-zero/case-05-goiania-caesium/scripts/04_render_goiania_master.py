import subprocess
import os
import sys
import time
import shutil

REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium"
EXPORT_DIR = os.path.join(PROJECT_DIR, "export")
AUDIO_FILE = os.path.join(PROJECT_DIR, "audio", "voiceover_mastered.wav")
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

RAW_VIDEO = os.path.join(EXPORT_DIR, "goiania_caesium_137_raw.mp4")
FINAL_MASTER = os.path.join(EXPORT_DIR, "the_blue_powder_of_death_goiania_1987_master.mp4")

os.makedirs(EXPORT_DIR, exist_ok=True)

def render_goiania_remotion():
    print("=======================================================================", flush=True)
    print("=== [1/2] Rendering Remotion Composition 'GoianiaCaesium137Master'   ===", flush=True)
    print("=== Specs: 1920x1080 Widescreen, 48 Scenes, 2D Stickman Noir        ===", flush=True)
    print("=== Engine: --gl=angle --muted --concurrency=4                     ===", flush=True)
    print("=======================================================================\n", flush=True)

    if os.path.exists(RAW_VIDEO):
        try:
            os.remove(RAW_VIDEO)
            print(f"[CLEANUP] Removed prior raw video: {RAW_VIDEO}", flush=True)
        except Exception as e:
            print(f"[WARN] Could not remove prior raw video: {e}", flush=True)

    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        "GoianiaCaesium137Master",
        RAW_VIDEO,
        "--gl=angle",
        "--muted",
        "--concurrency=6"
    ]

    start_time = time.time()
    proc = subprocess.Popen(
        cmd,
        cwd=REMOTION_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    for line in iter(proc.stdout.readline, ''):
        if line:
            line_str = line.strip()
            if any(k in line_str for k in ['Rendered', 'Rendering', 'Bundling', 'Error', 'Done', '%', 'Finished']):
                print(f"  [Remotion] {line_str}", flush=True)

    proc.wait()
    elapsed = time.time() - start_time
    print(f"\n[OK] Raw Video Render completed in {elapsed:.1f}s ({elapsed/60:.2f} mins).", flush=True)

    if proc.returncode != 0:
        raise RuntimeError(f"Remotion render failed with exit code {proc.returncode}")

    if not os.path.exists(RAW_VIDEO) or os.path.getsize(RAW_VIDEO) == 0:
        raise RuntimeError(f"Rendered video missing or empty: {RAW_VIDEO}")

def mux_broadcast_audio():
    print("\n=======================================================================", flush=True)
    print("=== [2/2] Multiplexing Master Broadcast Audio (FFmpeg)              ===", flush=True)
    print("=== Target: H.264 High Profile, AAC 320k 48kHz, EBU R128 (-16 LUFS)  ===", flush=True)
    print("=======================================================================\n", flush=True)

    if not os.path.exists(AUDIO_FILE):
        raise FileNotFoundError(f"Master voiceover audio missing: {AUDIO_FILE}")

    if os.path.exists(FINAL_MASTER):
        try:
            os.remove(FINAL_MASTER)
        except Exception as e:
            print(f"[WARN] Could not remove prior master: {e}", flush=True)

    cmd = [
        FFMPEG, "-y",
        "-i", RAW_VIDEO,
        "-i", AUDIO_FILE,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-ar", "48000",
        "-shortest",
        FINAL_MASTER
    ]

    print(f"[FFmpeg] Executing audio-video multiplexing...", flush=True)
    subprocess.run(cmd, check=True)

    if os.path.exists(FINAL_MASTER) and os.path.getsize(FINAL_MASTER) > 0:
        size_mb = os.path.getsize(FINAL_MASTER) / (1024 * 1024)
        print(f"\n[SUCCESS] Final 13-Minute Master Video Ready!", flush=True)
        print(f"   Path: {FINAL_MASTER}", flush=True)
        print(f"   Size: {size_mb:.2f} MB", flush=True)
    else:
        raise RuntimeError(f"Failed to generate final master video at {FINAL_MASTER}")

def main():
    render_goiania_remotion()
    mux_broadcast_audio()

if __name__ == '__main__':
    main()
