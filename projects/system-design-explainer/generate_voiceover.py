import asyncio
import os
import subprocess
import edge_tts

VOICE = "en-US-ChristopherNeural" # Deep, crisp documentary tech narrator
OUTPUT_AUDIO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\narration.mp3"
INPUT_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\scaling_10m_master.mp4"
FINAL_VIDEO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\scaling_10m_master_voiced.mp4"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

SCRIPT = (
    "Day one. You launch your application with a single monolithic server. "
    "The web tier and the database live on the exact same machine. "
    "It is simple, cheap, and easily serves your first one hundred users with eight-millisecond latency. "
    "Then, you go viral. At ten thousand concurrent users, the server hits a wall. "
    "CPU spikes to one hundred percent, memory is exhausted, and users see five-oh-four gateway timeouts. "
    "Rule number one: separate compute from storage. We extract the database to a dedicated tier. "
    "Next, at one hundred thousand users, we scale horizontally. "
    "A load balancer distributes traffic across a fleet of stateless web containers. "
    "At one million users, ninety percent of traffic is read-heavy. "
    "We introduce an in-memory Redis cache, answering queries in sub-milliseconds, and add read replicas. "
    "Finally, at ten million users, we achieve global scale. "
    "A worldwide CDN caches edge traffic, Apache Kafka handles asynchronous event streams, "
    "and the database is sharded across multiple clusters. Zero single points of failure."
)

async def main():
    print("[1/3] Generating Neural Voice Narration via edge_tts...")
    communicate = edge_tts.Communicate(SCRIPT, VOICE, rate="+6%")
    await communicate.save(OUTPUT_AUDIO)
    print(f"[OK] Voice narration saved: {OUTPUT_AUDIO}")

    print("[2/3] Merging video + voice narration with EBU R128 mastering...")
    cmd = [
        FFMPEG, "-y",
        "-i", INPUT_VIDEO,
        "-i", OUTPUT_AUDIO,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-af", "loudnorm=I=-14:LRA=11:TP=-1.0",
        "-shortest",
        FINAL_VIDEO
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[ERROR]", res.stderr)
        return

    size_mb = os.path.getsize(FINAL_VIDEO) / (1024 * 1024)
    print(f"[3/3] [SUCCESS] Final voiced video ready: {FINAL_VIDEO} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    asyncio.run(main())
