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

PROJECT_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\the-dossier-zero\case-05-goiania-caesium"
SHORTS_DIR = os.path.join(PROJECT_DIR, "shorts")
AUDIO_DIR = os.path.join(SHORTS_DIR, "audio")
EXPORT_DIR = os.path.join(SHORTS_DIR, "export")
REMOTION_ASSETS = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\goiania_shorts"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(REMOTION_ASSETS, exist_ok=True)
os.makedirs(os.path.join(REMOTION_ASSETS, "audio"), exist_ok=True)

SHORTS_DATA = [
    {
        "shorts_id": "goiania_short_01",
        "title": "The 6-Year-Old Girl Who Glowed in the Dark",
        "case_tag": "● THE DOSSIER ZERO // CASE #05: CAESIUM-137",
        "voiceover_text": (
            "In September 1987, inside a modest home in central Brazil, a six-year-old girl named Leide das Neves was handed a sandwich while sitting on the kitchen floor. "
            "Moments earlier, her father had brought home a handful of glowing blue dust he believed was magical glitter. "
            "Leide played with the radiant powder, rubbing it across her hands, face, and arms. Then, without washing her hands, she ate her food. "
            "Hours later, when her mother turned off the bedroom lights, she screamed. In the dark, Leide was glowing with an ethereal blue luminescence. "
            "It was not magic. It was fifty terabecquerels of Caesium-137. "
            "Little Leide had ingested over one gigabecquerel of pure radioactive salt—absorbing a lethal six-Gray dose. "
            "She would become the youngest victim of the deadliest radiological disaster in South American history."
        ),
        "theme": {
            "primary": "#00F0FF",
            "accent": "#FFE600",
            "warning": "#FF0033",
            "bg": "#0A0D14"
        },
        "scenes": [
            {
                "scene_id": "01",
                "headline": "THE INNOCENT CURIOSITY",
                "voiceover_text": "In September 1987, inside a modest home in central Brazil, a six-year-old girl named Leide das Neves was handed a sandwich while sitting on the kitchen floor.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_16.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "02",
                "headline": "THE BLUE GLITTER",
                "voiceover_text": "Moments earlier, her father had brought home a handful of glowing blue dust he believed was magical glitter. Leide played with the radiant powder, rubbing it across her hands, face, and arms.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_17.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "03",
                "headline": "GLOWING IN THE DARK",
                "voiceover_text": "Then, without washing her hands, she ate her food. Hours later, when her mother turned off the bedroom lights, she screamed. In the dark, Leide was glowing with an ethereal blue luminescence.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_18.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "04",
                "headline": "50 TERABECQUERELS",
                "voiceover_text": "It was not magic. It was fifty terabecquerels of Caesium-137. Little Leide had ingested over one gigabecquerel of pure radioactive salt—absorbing a lethal six-Gray dose.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_09.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "05",
                "headline": "THE YOUNGEST VICTIM",
                "voiceover_text": "She would become the youngest victim of the deadliest radiological disaster in South American history.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_37.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.05, "pan_y": -3}
            }
        ]
    },
    {
        "shorts_id": "goiania_short_02",
        "title": "The Deadliest Bus Ride in Human History",
        "case_tag": "● THE DOSSIER ZERO // CASE #05: CAESIUM-137",
        "voiceover_text": (
            "On September 28, 1987, thirty-seven-year-old Maria Gabriela Ferreira boarded a crowded public city bus in central Goiania. "
            "Between her feet sat a simple plastic shopping bag. "
            "None of the passengers around her had any idea that inside that bag lay an unshielded nuclear source emitting one thousand three hundred and seventy-five Curies of Caesium-137. "
            "Her husband had bought the glowing scrap metal, thinking it held supernatural powers. "
            "While local doctors were baffled by dozens of residents falling violently ill with vomiting and skin burns, Maria Gabriela realized the blue dust was poisoning her family. "
            "She rode the bus across the city, walked into the State Health Department, and slammed the bag onto a doctor's desk: 'This is what is killing my family.' "
            "Her solitary courage saved an entire city—even as the radiation sealed her own tragic death."
        ),
        "theme": {
            "primary": "#FF2A55",
            "accent": "#FFE600",
            "warning": "#FF0033",
            "bg": "#0A0D14"
        },
        "scenes": [
            {
                "scene_id": "01",
                "headline": "THE DEADLIEST COMMUTE",
                "voiceover_text": "On September 28, 1987, thirty-seven-year-old Maria Gabriela Ferreira boarded a crowded public city bus in central Goiania. Between her feet sat a simple plastic shopping bag.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_22.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "02",
                "headline": "1,375 CURIES ON BOARD",
                "voiceover_text": "None of the passengers around her had any idea that inside that bag lay an unshielded nuclear source emitting one thousand three hundred and seventy-five Curies of Caesium-137.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_09.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "03",
                "headline": "THE HEROIC INTUITION",
                "voiceover_text": "Her husband had bought the glowing scrap metal, thinking it held supernatural powers. While local doctors were baffled by dozens of residents falling violently ill with vomiting and skin burns, Maria Gabriela realized the blue dust was poisoning her family.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_21.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "04",
                "headline": "THE ULTIMATUM",
                "voiceover_text": "She rode the bus across the city, walked into the State Health Department, and slammed the bag onto a doctor's desk: 'This is what is killing my family.'",
                "image_file": "assets/goiania_caesium_137/scenes/scene_23.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "05",
                "headline": "A CITY SAVED",
                "voiceover_text": "Her solitary courage saved an entire city—even as the radiation sealed her own tragic death.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_24.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.05, "pan_y": -3}
            }
        ]
    },
    {
        "shorts_id": "goiania_short_03",
        "title": "The 700 KG Coffin That Sparked a Riot",
        "case_tag": "● THE DOSSIER ZERO // CASE #05: CAESIUM-137",
        "voiceover_text": (
            "On October 24, 1987, a funeral hearse in central Brazil was met by an angry mob of two thousand terrified citizens armed with bricks and cobblestones. "
            "Inside the vehicle lay the body of a six-year-old girl. But she wasn't buried in a normal wooden casket. "
            "Because her body was still emitting intense gamma radiation, engineers had constructed a monolithic sarcophagus: thick inner lead sheeting encased in waterproof reinforced concrete, weighing nearly seven hundred kilograms. "
            "Terrified that the radioactive corpses would poison their groundwater, the mob blocked the cemetery gates with trucks and hurled cobblestones at the hearse. "
            "Military police had to clear the barricades with tear gas. Under armed guard, industrial cranes hoisted the 700-kilo vault high into the sky, lowering it into a four-meter concrete tomb. "
            "It remains buried today—a chilling monument to Case File zero five."
        ),
        "theme": {
            "primary": "#A855F7",
            "accent": "#FF2A55",
            "warning": "#FFE600",
            "bg": "#0A0D14"
        },
        "scenes": [
            {
                "scene_id": "01",
                "headline": "THE CEMETERY MOB",
                "voiceover_text": "On October 24, 1987, a funeral hearse in central Brazil was met by an angry mob of two thousand terrified citizens armed with bricks and cobblestones.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_39.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "02",
                "headline": "THE 700-KG LEAD TOMB",
                "voiceover_text": "Inside the vehicle lay the body of a six-year-old girl. But she wasn't buried in a normal wooden casket. Because her body was still emitting intense gamma radiation, engineers had constructed a monolithic sarcophagus: thick inner lead sheeting encased in waterproof reinforced concrete, weighing nearly seven hundred kilograms.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_38.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "03",
                "headline": "HAIL OF STONES",
                "voiceover_text": "Terrified that the radioactive corpses would poison their groundwater, the mob blocked the cemetery gates with trucks and hurled cobblestones at the hearse.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_40.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.06, "pan_y": -4}
            },
            {
                "scene_id": "04",
                "headline": "CRANE BURIAL UNDER FIRE",
                "voiceover_text": "Military police had to clear the barricades with tear gas. Under armed guard, industrial cranes hoisted the 700-kilo vault high into the sky, lowering it into a four-meter concrete tomb.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_41.png",
                "ken_burns": {"scale_from": 1.06, "scale_to": 1.0, "pan_y": 4}
            },
            {
                "scene_id": "05",
                "headline": "CASE FILE #05 ARCHIVED",
                "voiceover_text": "It remains buried today—a chilling monument to Case File zero five.",
                "image_file": "assets/goiania_caesium_137/scenes/scene_48.png",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.05, "pan_y": -3}
            }
        ]
    }
]

def main():
    print("=== SYNTHESIZING KOKORO 82M AUDIO FOR 3 YOUTUBE SHORTS ===", flush=True)
    kokoro = kokoro_onnx.Kokoro(ONNX_MODEL, VOICES_BIN)
    fps = 30
    sample_rate = 24000
    
    shorts_manifest = []

    for item in SHORTS_DATA:
        s_id = item["shorts_id"]
        text = item["voiceover_text"]
        print(f"\nProcessing {s_id}: {item['title']}...", flush=True)

        samples, sr = kokoro.create(text, voice="am_adam", speed=1.05, lang="en-us")
        dur_sec = len(samples) / sr
        total_frames = int(np.ceil(dur_sec * fps))

        raw_wav = os.path.join(AUDIO_DIR, f"{s_id}_raw.wav")
        sf.write(raw_wav, samples, sr)

        mastered_wav = os.path.join(AUDIO_DIR, f"{s_id}_master.wav")
        remotion_wav = os.path.join(REMOTION_ASSETS, "audio", f"{s_id}_master.wav")

        # Master to EBU R128 (-16.0 LUFS)
        cmd = [
            FFMPEG, "-y",
            "-i", raw_wav,
            "-af", "highpass=f=120,equalizer=f=3200:t=q:w=1.5:g=2.5,loudnorm=I=-16.0:TP=-1.5:LRA=11",
            "-ar", "48000",
            mastered_wav
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        shutil.copyfile(mastered_wav, remotion_wav)

        # Distribute frames evenly across scenes for vertical composition
        scenes = item["scenes"]
        per_scene_frames = total_frames // len(scenes)
        cur_f = 0
        computed_scenes = []

        for idx, sc in enumerate(scenes):
            dur = per_scene_frames if idx < len(scenes) - 1 else (total_frames - cur_f)
            computed_scenes.append({
                "scene_id": sc["scene_id"],
                "headline": sc["headline"],
                "voiceover_text": sc["voiceover_text"],
                "image_file": sc["image_file"],
                "ken_burns": sc["ken_burns"],
                "start_frame": cur_f,
                "end_frame": cur_f + dur,
                "duration_frames": dur,
                "speech_frames": dur - 10,
                "words": []
            })
            cur_f += dur

        manifest_item = {
            "shorts_id": s_id,
            "title": item["title"],
            "case_tag": item["case_tag"],
            "fps": fps,
            "total_frames": total_frames,
            "duration_sec": round(dur_sec, 2),
            "audio_file": f"assets/goiania_shorts/audio/{s_id}_master.wav",
            "theme": item["theme"],
            "scenes": computed_scenes
        }
        shorts_manifest.append(manifest_item)
        print(f"  [OK] {s_id}: Duration {dur_sec:.1f}s ({total_frames} frames @ 30fps)", flush=True)

    out_json = os.path.join(SHORTS_DIR, "manifest_shorts.json")
    remotion_json = os.path.join(REMOTION_ASSETS, "manifest_shorts.json")

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(shorts_manifest, f, indent=2, ensure_ascii=False)
    with open(remotion_json, "w", encoding="utf-8") as f:
        json.dump(shorts_manifest, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Shorts manifest saved to {out_json} & {remotion_json}", flush=True)

if __name__ == "__main__":
    main()
