import subprocess
import os
import sys
import time

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
REMOTION_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion"
EXPORT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\neon-rush-remake\export"

MASTER_AUDIO = os.path.join(EXPORT_DIR, "master_soundtrack.wav")

RAW_16_9 = os.path.join(EXPORT_DIR, "mercury_scene_video_raw.mp4").replace('\\', '/')
FINAL_16_9 = os.path.join(EXPORT_DIR, "neon_rush_remake_16x9_master.mp4")

RAW_9_16 = os.path.join(EXPORT_DIR, "mercury_scene_tiktok_raw.mp4").replace('\\', '/')
FINAL_9_16 = os.path.join(EXPORT_DIR, "neon_rush_remake_9x16_tiktok.mp4")

def render_remotion(comp_id, out_raw):
    print(f"\n==========================================")
    print(f"[REMOTION] Rendering '{comp_id}' (1512 frames)...")
    print(f"==========================================")
    cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts",
        comp_id,
        out_raw,
        "--muted",
        "--gl=angle"
    ]
    t0 = time.time()
    res = subprocess.run(cmd, cwd=REMOTION_DIR, shell=True)
    dt = time.time() - t0
    if res.returncode != 0:
        print(f"[ERROR] Failed to render {comp_id}")
        return False
    print(f"[SUCCESS] {comp_id} rendered in {dt:.1f}s -> {out_raw}")
    return True

def mux_audio(raw_video, final_video):
    print(f"\n[FFMPEG] Multiplexing broadcast audio with {os.path.basename(raw_video)}...")
    cmd = [
        FFMPEG, "-y",
        "-i", raw_video,
        "-i", MASTER_AUDIO,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "256k",
        "-shortest",
        final_video
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[ERROR]", res.stderr)
        return False
    sz = os.path.getsize(final_video) / (1024 * 1024)
    print(f"[SUCCESS] Master video created: {final_video} ({sz:.2f} MB)")
    return True

def main():
    if not os.path.exists(MASTER_AUDIO):
        print(f"[ERROR] Master audio not found: {MASTER_AUDIO}")
        sys.exit(1)

    # 1. Render 16:9 YouTube Master
    if render_remotion("MercurySceneMaster", RAW_16_9):
        mux_audio(RAW_16_9, FINAL_16_9)

    # 2. Render 9:16 TikTok Master
    if render_remotion("MercurySceneTikTok", RAW_9_16):
        mux_audio(RAW_9_16, FINAL_9_16)

    print("\n==========================================")
    print("ALL SCENE-BY-SCENE MASTERS RENDERED SUCCESSFULLY!")
    print("==========================================")

if __name__ == "__main__":
    main()
