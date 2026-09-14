import asyncio
import os
import subprocess
import edge_tts

VOICE = "en-US-ChristopherNeural"
SCRIPT = (
    "How did fifty engineers run WhatsApp for two billion users, "
    "while your company needs five hundred developers just to keep the login page online? "
    "The secret weapon was Erlang and the BEAM virtual machine. "
    "Unlike traditional OS threads that take two megabytes of RAM each, "
    "an Erlang actor process takes only three hundred bytes. "
    "Millions of live user connections run concurrently inside user space without breaking a sweat. "
    "Next, WhatsApp tackled the C-two-million problem: "
    "running two point eight million concurrent TCP connections on a single physical FreeBSD server. "
    "By hacking the FreeBSD kernel and optimizing socket memory tables, "
    "they squeezed insane throughput out of bare-metal hardware. "
    "Third: the ephemeral storage architecture. "
    "WhatsApp server never stores your message history. "
    "The instant a message is delivered to your phone, it is purged from server disk forever, "
    "saving petabytes of storage and millions in cloud bills. "
    "Combined with custom in-memory Mnesia clustering and end-to-end encryption, "
    "fifty engineers handled one hundred billion messages per day. "
    "In 2014, Facebook acquired WhatsApp for nineteen billion dollars. "
    "That is three hundred and eighty million dollars per engineer. "
    "Simple architecture always beats resume-driven complexity."
)

OUTPUT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\whatsapp-system-design\export"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_AUDIO = os.path.join(OUTPUT_DIR, "narration.mp3")

async def main():
    print("[1/2] Generating Neural Voice Narration via edge_tts...")
    communicate = edge_tts.Communicate(SCRIPT, VOICE, rate="+6%")
    
    sentences = []
    with open(OUTPUT_AUDIO, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                sentences.append((chunk["offset"], chunk["duration"], chunk["text"]))

    print(f"[OK] Voice narration saved: {OUTPUT_AUDIO}")
    print("\n[2/2] Exact Acoustic Sentence Boundaries (for Remotion sync):")
    print(f"{'SEC':<7} | {'FRAME (30fps)':<14} | {'DUR(s)':<6} | SENTENCE")
    print("-" * 85)
    
    total_sec = 0
    for offset, dur, text in sentences:
        s = offset / 10000000
        d = dur / 10000000
        f = int(s * 30)
        total_sec = max(total_sec, s + d)
        print(f"{s:6.2f}s | Frame {f:5d}       | {d:5.2f}s | {text}")
    
    total_frames = int(math.ceil((total_sec + 1.5) * 30))
    print(f"\nTotal Audio Duration: {total_sec:.2f}s")
    print(f"Target Remotion Duration: {total_frames} frames ({total_frames/30:.2f}s with outro buffer)")

if __name__ == "__main__":
    import math
    asyncio.run(main())
