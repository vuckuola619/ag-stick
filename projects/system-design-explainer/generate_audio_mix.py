import math
import struct
import wave
import subprocess
import os

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
VOICE_FILE = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\narration.mp3"
SFX_WAV = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\procedural_sfx.wav"
FINAL_AUDIO = r"c:\Users\bati-\Documents\AG-Stick\projects\system-design-explainer\export\master_soundtrack.wav"

SAMPLE_RATE = 48000
TOTAL_SECONDS = 74.0  # covers full 2200 frames @ 30fps (73.33s)
TOTAL_SAMPLES = int(SAMPLE_RATE * TOTAL_SECONDS)

def generate_sfx_and_ambient():
    print("[1/3] Synthesizing procedural SFX and tech ambient track...")
    audio = [0.0] * TOTAL_SAMPLES

    def add_tone(freq, start_sec, duration_sec, amplitude, decay_rate=0.0):
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(duration_sec * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            env = math.exp(-decay_rate * t) if decay_rate > 0 else 1.0
            # Fade in/out to prevent clicks
            if i < 480:
                env *= (i / 480)
            elif i > num_samples - 480:
                env *= ((num_samples - i) / 480)
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    # 1. Subtle Ambient Tech Bed (-24 dB = ~0.06 amplitude)
    # Slow pulsing chords changing with Acts
    print("  -> Generating atmospheric tech drone & pulse...")
    for i in range(TOTAL_SAMPLES):
        t = i / SAMPLE_RATE
        # Gentle 120 bpm tech pulse (2 Hz)
        pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 2.0 * t)
        
        # Base fundamental frequencies evolving across Acts
        if t < 15.2:       # Act 1: Chill Day 1 (D minor: 146.8 Hz)
            f1, f2 = 146.8, 220.0
        elif t < 28.5:     # Act 2A: Tense Alarm (F# diminished: 185 Hz, 277 Hz)
            f1, f2 = 185.0, 277.2
        elif t < 35.4:     # Act 2B: Resolving Compute (A minor: 220 Hz)
            f1, f2 = 220.0, 329.6
        elif t < 44.8:     # Act 3: Scale Up (E minor: 164.8 Hz, 246.9 Hz)
            f1, f2 = 164.8, 246.9
        elif t < 55.6:     # Act 4: Smooth Cache (G major: 196 Hz, 293.7 Hz)
            f1, f2 = 196.0, 293.7
        else:              # Act 5: Triumphant C Major (261.6 Hz, 392.0 Hz)
            f1, f2 = 261.6, 392.0
            
        drone = (math.sin(2 * math.pi * f1 * t) * 0.035 +
                 math.sin(2 * math.pi * f2 * t) * 0.025 +
                 math.sin(2 * math.pi * (f1 * 0.5) * t) * 0.04) * (0.7 + 0.3 * pulse)
        audio[i] += drone

    # 2. SFX: Act 2 Crash Alarm at 15.20s (Rapid urgent pulses)
    print("  -> Adding Crash Alert SFX at 15.20s...")
    for beep in range(6):
        b_time = 15.20 + (beep * 0.22)
        add_tone(880.0, b_time, 0.12, 0.18, decay_rate=2.0)
        add_tone(659.3, b_time + 0.06, 0.12, 0.15, decay_rate=2.0)

    # 3. SFX: Horizontal Scale Whoosh / Tech Spin at 35.38s
    print("  -> Adding Scale Cluster Whoosh at 35.38s...")
    add_tone(330.0, 35.38, 0.8, 0.12, decay_rate=1.5)
    add_tone(660.0, 35.50, 0.6, 0.09, decay_rate=2.0)

    # 4. SFX: Redis Cache Hit Crystal Chime at 44.81s (Sub-ms RAM ding!)
    print("  -> Adding Redis Cache Hit Chime at 44.81s...")
    add_tone(1760.0, 44.81, 1.2, 0.22, decay_rate=3.5)
    add_tone(2637.0, 44.85, 1.0, 0.15, decay_rate=4.0)
    add_tone(3520.0, 44.90, 0.8, 0.08, decay_rate=5.0)

    # 5. SFX: Victory Chime at 69.34s ("Zero Single Points of Failure")
    print("  -> Adding Triumphant Climax Chords at 69.34s...")
    add_tone(523.25, 69.34, 3.5, 0.20, decay_rate=0.8) # C5
    add_tone(659.25, 69.40, 3.5, 0.18, decay_rate=0.8) # E5
    add_tone(783.99, 69.46, 3.5, 0.18, decay_rate=0.8) # G5
    add_tone(1046.5, 69.52, 3.5, 0.16, decay_rate=0.8) # C6

    # Write 16-bit PCM WAV
    with wave.open(SFX_WAV, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        raw = bytearray()
        for sample in audio:
            clamped = max(-1.0, min(1.0, sample))
            val = int(clamped * 32767.0)
            raw.extend(struct.pack('<h', val))
        wf.writeframes(raw)
    print(f"[OK] SFX track saved: {SFX_WAV}")

def mix_with_voice():
    print("[2/3] Mixing voiceover + SFX + ambient bed via FFmpeg...")
    # Voice track is primary (louder), SFX and bed provide rich dimension
    cmd = [
        FFMPEG, "-y",
        "-i", VOICE_FILE,
        "-i", SFX_WAV,
        "-filter_complex",
        "[0:a]volume=1.0[voice];"
        "[1:a]volume=0.85[sfx];"
        "[voice][sfx]amix=inputs=2:duration=longest:dropout_transition=2[mixed];"
        "[mixed]loudnorm=I=-14:LRA=11:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "pcm_s16le",
        FINAL_AUDIO
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[ERROR]", res.stderr)
        return False
    print(f"[3/3] [SUCCESS] Broadcast master audio ready: {FINAL_AUDIO}")
    return True

if __name__ == "__main__":
    generate_sfx_and_ambient()
    mix_with_voice()
