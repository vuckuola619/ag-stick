import os
import subprocess
import sys

FFMPEG_EXE = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
INPUT_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\export\wework_master_1080p_v3.mp4"
OUTPUT_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\export\wework_master_1080p_v3_mastered.mp4"

def master_audio():
    if not os.path.exists(INPUT_VIDEO):
        print(f"[ERROR] Input video not found: {INPUT_VIDEO}")
        sys.exit(1)

    print(f"[START] Mastering audio to YouTube/EBU R128 standard (-14 LUFS, -1.0 dBFS TP)...")
    print(f"  Input : {INPUT_VIDEO}")
    print(f"  Output: {OUTPUT_VIDEO}")

    cmd = [
        FFMPEG_EXE,
        "-y",
        "-i", INPUT_VIDEO,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-af", "loudnorm=I=-14:LRA=11:TP=-1.0",
        OUTPUT_VIDEO
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] FFmpeg failed with exit code {result.returncode}")
        print(result.stderr[-1000:])
        sys.exit(result.returncode)

    file_size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
    print(f"[SUCCESS] Mastered video generated: {OUTPUT_VIDEO} ({file_size_mb:.2f} MB)")

if __name__ == '__main__':
    master_audio()
