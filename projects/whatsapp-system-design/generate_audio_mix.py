import math
import struct
import wave
import subprocess
import os

FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
VOICE_FILE = r"c:\Users\bati-\Documents\AG-Stick\projects\whatsapp-system-design\export\narration.mp3"
SFX_WAV = r"c:\Users\bati-\Documents\AG-Stick\projects\whatsapp-system-design\export\procedural_sfx.wav"
FINAL_AUDIO = r"c:\Users\bati-\Documents\AG-Stick\projects\whatsapp-system-design\export\master_soundtrack.wav"

SAMPLE_RATE = 48000
TOTAL_SECONDS = 79.5  # covers full 2370 frames @ 30fps (79.0s)
TOTAL_SAMPLES = int(SAMPLE_RATE * TOTAL_SECONDS)

def generate_sfx_and_ambient():
    print("[1/3] Synthesizing WhatsApp SFX and tech documentary ambient track...")
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
            if i < 480:
                env *= (i / 480)
            elif i > num_samples - 480:
                env *= ((num_samples - i) / 480)
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    def add_pop(start_sec, amplitude=0.3):
        # WhatsApp style bubble pop / 'tuk' (frequency sweep down 900Hz -> 250Hz in 40ms)
        start_idx = int(start_sec * SAMPLE_RATE)
        num_samples = int(0.045 * SAMPLE_RATE)
        for i in range(num_samples):
            idx = start_idx + i
            if idx >= TOTAL_SAMPLES:
                break
            t = i / SAMPLE_RATE
            freq = 900.0 - (650.0 * (i / num_samples))
            env = math.exp(-40.0 * t)
            audio[idx] += amplitude * env * math.sin(2 * math.pi * freq * t)

    # 1. Subtle Ambient Tech Score (-24 dB = ~0.06 amplitude)
    print("  -> Generating evolving tech synthesizer bed...")
    for i in range(TOTAL_SAMPLES):
        t = i / SAMPLE_RATE
        pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 2.0 * t) # 120 bpm pulse
        
        if t < 24.95:      # Act 1: Chill Curiosities (D minor: 146.8 Hz, 220 Hz)
            f1, f2 = 146.8, 220.0
        elif t < 41.72:    # Act 2: High Throughput C2M (E minor: 164.8 Hz, 246.9 Hz)
            f1, f2 = 164.8, 246.9
        elif t < 56.77:    # Act 3: Ephemeral Purge (G major: 196.0 Hz, 293.7 Hz)
            f1, f2 = 196.0, 293.7
        elif t < 64.55:    # Act 4: Mnesia Encryption (A minor: 220.0 Hz, 329.6 Hz)
            f1, f2 = 220.0, 329.6
        else:              # Act 5: $19B Victory Climax (C major: 261.6 Hz, 392.0 Hz)
            f1, f2 = 261.6, 392.0
            
        drone = (math.sin(2 * math.pi * f1 * t) * 0.035 +
                 math.sin(2 * math.pi * f2 * t) * 0.025 +
                 math.sin(2 * math.pi * (f1 * 0.5) * t) * 0.035) * (0.75 + 0.25 * pulse)
        audio[i] += drone

    # 2. SFX: 500 devs microservice alarm at 4.5s
    print("  -> Adding Corporate Chaos Alarm at 4.5s...")
    add_tone(660.0, 4.5, 0.15, 0.14, decay_rate=2.0)
    add_tone(550.0, 4.7, 0.15, 0.12, decay_rate=2.0)

    # 3. SFX: BEAM Actor Spawn Pop at 8.09s (Erlang secret weapon)
    print("  -> Adding BEAM Actor Activation at 8.09s...")
    add_tone(880.0, 8.09, 0.6, 0.16, decay_rate=3.0)
    add_tone(1320.0, 8.18, 0.5, 0.12, decay_rate=3.5)

    # 4. SFX: C2M 2.8M TCP Socket Bursts at 24.95s to 27.5s
    print("  -> Adding 2.8M Socket Connection Bursts at 24.95s...")
    for s_step in range(8):
        s_time = 24.95 + (s_step * 0.28)
        freq = 1200.0 + (s_step * 150.0)
        add_tone(freq, s_time, 0.12, 0.15, decay_rate=4.0)

    # 5. SFX: WhatsApp Chat Message Pop ("tuk!") at 48.29s
    print("  -> Adding WhatsApp chat bubble pop at 48.29s...")
    add_pop(48.29, amplitude=0.35)
    add_pop(49.10, amplitude=0.30)
    # Instant disk purge whoosh at 50.2s
    add_tone(440.0, 50.2, 0.4, 0.15, decay_rate=3.0)
    add_tone(220.0, 50.35, 0.4, 0.18, decay_rate=2.5)

    # 6. SFX: Cash Register Cha-Ching at 64.55s ($19 Billion acquisition)
    print("  -> Adding $19B Cash Register Cha-Ching at 64.55s...")
    add_tone(2093.0, 64.55, 0.8, 0.22, decay_rate=3.0) # C7
    add_tone(2637.0, 64.62, 0.8, 0.20, decay_rate=3.0) # E7
    add_tone(3135.0, 64.70, 1.2, 0.25, decay_rate=2.5) # G7

    # 7. SFX: Grand Finale Victory Chime at 73.27s
    print("  -> Adding Victory Chime at 73.27s...")
    add_tone(523.25, 73.27, 4.0, 0.22, decay_rate=0.7) # C5
    add_tone(659.25, 73.33, 4.0, 0.20, decay_rate=0.7) # E5
    add_tone(783.99, 73.39, 4.0, 0.20, decay_rate=0.7) # G5
    add_tone(1046.5, 73.45, 4.0, 0.18, decay_rate=0.7) # C6

    # Write WAV
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
