import os
import json
import numpy as np
import soundfile as sf
import subprocess
import kokoro_onnx

ONNX_MODEL = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\kokoro-v1.0.onnx"
VOICES_BIN = r"C:\Users\bati-\Documents\AG-VOX\models\kokoro\voices-v1.0.bin"
FFMPEG = r"C:\Users\bati-\AppData\Local\Programs\Python\Python313\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

BASE_DIR = r"c:\Users\bati-\Documents\AG-Stick\projects\thomas-midgley-planet-poison\shorts"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
EXPORT_DIR = os.path.join(BASE_DIR, "export")

REMOTION_BASE = r"c:\Users\bati-\Documents\AG-Stick\projects\wework-47-billion-illusion\remotion\public\assets\dossier_shorts"
REMOTION_AUDIO = os.path.join(REMOTION_BASE, "audio")
REMOTION_SCENES = os.path.join(REMOTION_BASE, "scenes")

for d in [AUDIO_DIR, ASSETS_DIR, SCRIPTS_DIR, EXPORT_DIR, REMOTION_BASE, REMOTION_AUDIO, REMOTION_SCENES]:
    os.makedirs(d, exist_ok=True)

SHORTS_DATA = [
    {
        "shorts_id": "shorts_01",
        "title": "The Chemist Who Inhaled Lead On Live TV",
        "case_tag": "● THE DOSSIER ZERO // SHORTS #01",
        "fps": 30,
        "sample_rate": 24000,
        "theme": {
            "primary": "#00F0FF",
            "accent": "#FFE600",
            "warning": "#FF2A55",
            "bg": "#0A0D14"
        },
        "scenes": [
            {
                "scene_id": "s1_01",
                "headline": "THE DEADLY STANDARD OIL ASYLUM",
                "voiceover_text": "On October 30th, 1924, workers at the Standard Oil plant were violently losing their minds. They hallucinated black insects crawling on walls, leapt from windows, and died in straightjackets from a mystery chemical called Loony Gas.",
                "image_prompt": "Vertical 9:16 format composition. Grim industrial chemical refinery factory interior, dim shadowy atmospheric lighting with amber volumetric smoke. A minimalist 2D cartoon stickman worker with round white head and expressive terrified cartoon eyes clutching his head in madness. Shadowy silhouettes of phantom giant insects crawling across steel girders. Graphic novel noir style, stark chiaroscuro, heavy black ink outlines, textured vintage paper aesthetic. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.05, "scale_to": 1.18, "pan_y": -20}
            },
            {
                "scene_id": "s1_02",
                "headline": "MIDGLEY'S EMERGENCY PRESS STUNT",
                "voiceover_text": "To stop the national panic, inventor Thomas Midgley Jr. called an emergency press conference. Smiling before reporters under blazing flashbulbs, he poured the clear, deadly liquid straight over his bare hands.",
                "image_prompt": "Vertical 9:16 format composition. 1920s vintage press conference. Minimalist 2D cartoon stickman chemist with round white head, round black spectacles, bowtie, and vest. Standing behind an oak table with vintage chrome standing microphones. He holds a glass flask pouring a stream of glowing toxic amber liquid over his bare stick hands with a defiant smile. Bright vintage flashbulbs creating stark rim lighting and deep shadows. Noir graphic novel style, clean outlines. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.15, "scale_to": 1.02, "pan_y": 15}
            },
            {
                "scene_id": "s1_03",
                "headline": "60 SECONDS OF LETHAL FUMES",
                "voiceover_text": "Then, he raised the open flask to his face, and inhaled the concentrated lead vapor deep into his lungs for sixty unbroken seconds, boldly declaring it completely harmless.",
                "image_prompt": "Vertical 9:16 format composition. Extreme dramatic close-up of 2D stickman chemist inhaling vapor from a boiling glass chemical beaker held right beneath his nose. Thick glowing amber and toxic yellow chemical smoke swirling into his face. Wide manic cartoon eyes behind thick round spectacles, intense dramatic expression. Deep obsidian black background with glowing golden-yellow rim light, graphic novel cinematic noir. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.14, "pan_y": -15}
            },
            {
                "scene_id": "s1_04",
                "headline": "THE SECRET COLLAPSE IN MIAMI",
                "voiceover_text": "What Midgley hid from the world was that he was already poisoned. Within weeks of the stunt, his nervous system collapsed, and he secretly fled to Miami for months just to survive.",
                "image_prompt": "Vertical 9:16 format composition. Dark dimly-lit vintage room in Florida. A minimalist 2D cartoon stickman lying sick in an old iron bed under a slowly rotating wooden ceiling fan. Moonlight filtering through wooden window blinds casting dramatic Venetian zebra shadows. Glass medicine bottles on a wooden nightstand with amber glowing liquids. Cold cyan and pale amber atmospheric color palette, melancholic graphic novel noir. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.08, "scale_to": 1.0, "pan_y": 20}
            },
            {
                "scene_id": "s1_05",
                "headline": "60 YEARS OF GLOBAL POISON",
                "voiceover_text": "For the next sixty years, that exact same poison, tetraethyl lead, was pumped into billions of cars worldwide, silently polluting the atmosphere and contaminating the blood of every child on Earth.",
                "image_prompt": "Vertical 9:16 format composition. The planet Earth viewed from low orbit, enveloped in a dense suffocating amber-brown and toxic smog layer glowing ominously. At the bottom silhouette of an endless highway grid with retro 1950s cars spewing glowing exhaust fumes. 2D graphic novel art style, deep space black with electric amber and poisonous yellow atmospheric ring. Highly cinematic, poignant and alarming. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.02, "scale_to": 1.15, "pan_y": -25}
            }
        ]
    },
    {
        "shorts_id": "shorts_02",
        "title": "How 1 Single Atom Destroyed 100,000 Ozone Molecules",
        "case_tag": "● THE DOSSIER ZERO // SHORTS #02",
        "fps": 30,
        "sample_rate": 24000,
        "theme": {
            "primary": "#00F0FF",
            "accent": "#00FF66",
            "warning": "#FF2A55",
            "bg": "#050B14"
        },
        "scenes": [
            {
                "scene_id": "s2_01",
                "headline": "THE MIRACLE REFRIGERANT DEMO",
                "voiceover_text": "In 1930, the man who put lead in gasoline had another brilliant idea. Early refrigerators leaked deadly toxic ammonia that regularly killed entire families in their sleep. So Thomas Midgley invented Freon, the world's first CFC.",
                "image_prompt": "Vertical 9:16 format composition. 1930s lecture hall stage. Minimalist 2D cartoon stickman chemist with round white head and spectacles in a lab apron standing before an audience. Beside him is a vintage cylindrical refrigerator with exposed condenser coils. He calmly blows out a lit yellow candle flame using invisible gas poured from a laboratory beaker. Dramatic stage lighting, deep teal and amber noir palette. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.03, "scale_to": 1.15, "pan_y": -15}
            },
            {
                "scene_id": "s2_02",
                "headline": "THE 30-YEAR ASCENT TO SPACE",
                "voiceover_text": "Millions of air conditioners and spray cans flooded the globe. Freon seemed completely harmless. But it had a catastrophic secret. It was so stable that nothing on Earth could break it down. For thirty years, it drifted invisibly toward the stratosphere.",
                "image_prompt": "Vertical 9:16 format composition. Cross-section of Earth's atmosphere stretching from a retro city skyline into the dark violet stratosphere. Tiny glowing cyan geometric molecular structures (CFC molecules) floating silently upward through soft cumulus clouds like luminous spores into space. Atmospheric depth of field, electric cyan rim lighting, dark cosmic blue void. Graphic novel noir style. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.15, "scale_to": 1.02, "pan_y": -30}
            },
            {
                "scene_id": "s2_03",
                "headline": "ULTRAVIOLET CRACKS THE MOLECULE",
                "voiceover_text": "High above the protective clouds, raw ultraviolet radiation from the sun struck the molecule with full force, cracking the chemical bonds open and releasing a single atom of atomic chlorine.",
                "image_prompt": "Vertical 9:16 format composition. Cosmic stratosphere. A blinding beam of intense violet-purple solar ultraviolet light striking a central cyan molecule floating in the vacuum. The molecule fractures with bright electric sparks, ejecting a menacing, neon-emerald glowing circular chlorine atom. Explosive cosmic energy, deep space black, neon ultraviolet and toxic green contrast. Graphic novel style. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.20, "pan_y": 0}
            },
            {
                "scene_id": "s2_04",
                "headline": "1 ATOM DESTROYS 100,000 MOLECULES",
                "voiceover_text": "That single chlorine atom was an unstoppable chemical assassin. It reacted with ozone, stole an oxygen atom, regenerated itself, and continued the cycle, destroying one hundred thousand ozone molecules one by one.",
                "image_prompt": "Vertical 9:16 format composition. High-action chemical microscopic scale. A radiant radioactive-green neon chlorine atom ripping apart fragile triangular glowing-cyan ozone molecules (O3). Debris of oxygen atoms scattering in shockwaves. Dramatic motion blur, graphic novel comic book action lines, neon green and deep cyan on pitch black background. Dynamic and intense. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.12, "scale_to": 1.02, "pan_y": 15}
            },
            {
                "scene_id": "s2_05",
                "headline": "THE ANTARCTIC SKY TEARS OPEN",
                "voiceover_text": "By 1985, satellite sensors over Antarctica confirmed the nightmare. The upper atmosphere had been torn wide open, leaving a continent-sized radiation hole that almost destroyed life on Earth.",
                "image_prompt": "Vertical 9:16 format composition. Epic orbital view of the frozen white Antarctic continent with ice shelves. In the sky above it, an enormous dark violet, jagged hole in the cyan ozone layer exposing raw cosmic blackness and intense purple solar glare pouring onto the ice below. Chilling, catastrophic, awe-inspiring graphic novel noir artwork. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.02, "scale_to": 1.16, "pan_y": -20}
            }
        ]
    },
    {
        "shorts_id": "shorts_03",
        "title": "He Built A Machine To Help Him Move. It Strangled Him.",
        "case_tag": "● THE DOSSIER ZERO // SHORTS #03",
        "fps": 30,
        "sample_rate": 24000,
        "theme": {
            "primary": "#FFAA00",
            "accent": "#FF2A55",
            "warning": "#FFE600",
            "bg": "#08090E"
        },
        "scenes": [
            {
                "scene_id": "s3_01",
                "headline": "STRICKEN BY POLIO AT 51",
                "voiceover_text": "He poisoned the atmosphere and tore a hole in the ozone layer. But the way Thomas Midgley Jr. died was the darkest irony in scientific history. In 1940, at age fifty-one, he was stricken by polio, leaving him paralyzed from the waist down.",
                "image_prompt": "Vertical 9:16 format composition. Moody dimly lit 1940s room. A minimalist 2D cartoon stickman in a heavy oak wheelchair, wearing brass and leather leg braces. Sitting near a tall rainy window overlooking gloomy barren trees. Strong chiaroscuro shadows, warm banker lamp amber on one side and cold rainy blue on the other. Melancholic graphic novel noir. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.04, "scale_to": 1.16, "pan_y": -10}
            },
            {
                "scene_id": "s3_02",
                "headline": "THE INGENIOUS PULLEY HARNESS",
                "voiceover_text": "Midgley was an obsessive mechanical engineer. He refused to rely on nurses. Instead, he engineered an elaborate ceiling apparatus: motorized electric winches, heavy steel cables, brass pulleys, and leather slings suspended over his bed.",
                "image_prompt": "Vertical 9:16 format composition. Intricate mechanical engineering marvel inside a vintage bedroom. The ceiling is covered with an elaborate web of brass gear cogs, steel pulleys, taut cables, and leather lifting harnesses hanging down over a wooden bed. Minimalist 2D stickman looking up in proud contemplation holding blueprints. Industrial aesthetic, warm tungsten lighting, steampunk-leaning vintage noir. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.15, "scale_to": 1.02, "pan_y": 20}
            },
            {
                "scene_id": "s3_03",
                "headline": "FOUR YEARS OF FLAWLESS HOISTING",
                "voiceover_text": "For four years, the machine worked like clockwork. With the flip of a switch, Midgley could effortlessly lift his own body from his sheets and lower himself safely into his wheelchair.",
                "image_prompt": "Vertical 9:16 format composition. The pulley harness in action. 2D cartoon stickman suspended in mid-air in leather slings above his bed, smoothly reaching for his wheelchair with a confident smile. Cables humming with mechanical tension, polished brass pulleys glinting under a bedroom lamp. Crisp graphic novel lines, warm amber and vintage sepia tone. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.02, "scale_to": 1.14, "pan_y": -15}
            },
            {
                "scene_id": "s3_04",
                "headline": "NOVEMBER 2, 1944: THE FATAL SLIP",
                "voiceover_text": "Then came the morning of November 2nd, 1944. As Midgley operated the hoist alone, a steel cable slipped off its grooved pulley. The motorized winch jammed, twisting the heavy ropes violently around his neck.",
                "image_prompt": "Vertical 9:16 format composition. Sudden mechanical malfunction. Dramatic high-tension moment: a heavy cable snapping off a brass pulley track with flying sparks. Thick braided ropes tangling chaotically around the overhead rigging. Stark diagonal shadows, intense emergency rim lighting in flashing crimson and tungsten. Graphic novel comic noir, high suspense. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.0, "scale_to": 1.22, "pan_y": 0}
            },
            {
                "scene_id": "s3_05",
                "headline": "STRANGLED BY HIS OWN MACHINE",
                "voiceover_text": "Paralyzed and unable to reach the power switch, Midgley could not break free. The man who accidentally poisoned the entire planet died in silence, strangled by his very own invention.",
                "image_prompt": "Vertical 9:16 format composition. Somber symbolic conclusion. Silhouette of an old cemetery headstone on an autumn hill under heavy stormy overcast rain clouds. Entwined around the headstone are broken mechanical cables and snapped pulleys. In the distant foggy background, retro factory smokestacks spew amber smog into the sky. Atmospheric, poignant, unforgettable graphic novel noir art. Absolutely zero text, zero letters, zero numbers.",
                "ken_burns": {"scale_from": 1.05, "scale_to": 1.18, "pan_y": -20}
            }
        ]
    }
]

def main():
    print("=== INITIALIZING KOKORO 82M TTS FOR 3 SHORTS ===", flush=True)
    kokoro = kokoro_onnx.Kokoro(ONNX_MODEL, VOICES_BIN)
    
    fps = 30
    sample_rate = 24000
    
    manifest_result = []
    
    for sh in SHORTS_DATA:
        s_id = sh["shorts_id"]
        title = sh["title"]
        print(f"\n>>> PROCESSING {s_id.upper()}: {title} <<<", flush=True)
        
        combined_samples = []
        scenes_info = []
        current_frame = 0
        
        pause_sec = 0.35
        pause_samples = np.zeros(int(sample_rate * pause_sec), dtype=np.float32)
        pause_frames = int(pause_sec * fps)
        
        for sc in sh["scenes"]:
            sc_id = sc["scene_id"]
            text = sc["voiceover_text"]
            
            # Synthesize Kokoro am_adam @ 1.08 speed for fast Shorts tempo
            samples, sr = kokoro.create(text, voice="am_adam", speed=1.08, lang="en-us")
            dur_sec = len(samples) / sr
            speech_frames = int(np.ceil(dur_sec * fps))
            total_scene_frames = speech_frames + pause_frames
            
            start_frame = current_frame
            end_frame = current_frame + total_scene_frames
            
            # Split words for kinetic captions
            words = text.split()
            words_info = []
            if len(words) > 0:
                frames_per_word = speech_frames / len(words)
                for w_idx, w in enumerate(words):
                    w_start = start_frame + int(w_idx * frames_per_word)
                    w_end = start_frame + int((w_idx + 1) * frames_per_word)
                    words_info.append({
                        "word": w,
                        "start_frame": w_start,
                        "end_frame": w_end
                    })
            
            # Save scene audio
            scene_wav = os.path.join(AUDIO_DIR, f"{sc_id}.wav")
            remotion_scene_wav = os.path.join(REMOTION_AUDIO, f"{sc_id}.wav")
            sf.write(scene_wav, samples, sr)
            sf.write(remotion_scene_wav, samples, sr)
            
            scenes_info.append({
                "scene_id": sc_id,
                "headline": sc["headline"],
                "voiceover_text": text,
                "image_prompt": sc["image_prompt"],
                "image_file": f"{sc_id}.png",
                "ken_burns": sc["ken_burns"],
                "start_frame": start_frame,
                "end_frame": end_frame,
                "duration_frames": total_scene_frames,
                "speech_frames": speech_frames,
                "words": words_info
            })
            
            combined_samples.append(samples)
            combined_samples.append(pause_samples)
            current_frame += total_scene_frames
        
        full_audio = np.concatenate(combined_samples)
        raw_wav_path = os.path.join(AUDIO_DIR, f"{s_id}_raw.wav")
        master_wav_path = os.path.join(AUDIO_DIR, f"{s_id}_master.wav")
        remotion_master_wav = os.path.join(REMOTION_AUDIO, f"{s_id}_master.wav")
        
        sf.write(raw_wav_path, full_audio, sample_rate)
        
        # Master with FFmpeg EBU R128 to -16.0 LUFS
        print(f"Mastering audio with FFmpeg to -16 LUFS...", flush=True)
        ffmpeg_cmd = [
            FFMPEG, "-y",
            "-i", raw_wav_path,
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,equalizer=f=120:width_type=o:width=2:g=2.0,equalizer=f=3200:width_type=o:width=1.5:g=1.5",
            "-ar", "48000",
            "-ac", "2",
            master_wav_path
        ]
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run([FFMPEG, "-y", "-i", master_wav_path, remotion_master_wav], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        total_duration_sec = current_frame / fps
        print(f"[OK] {s_id}: Total Frames = {current_frame} ({total_duration_sec:.2f}s)", flush=True)
        
        manifest_result.append({
            "shorts_id": s_id,
            "title": title,
            "case_tag": sh["case_tag"],
            "fps": fps,
            "total_frames": current_frame,
            "duration_sec": total_duration_sec,
            "audio_file": f"{s_id}_master.wav",
            "theme": sh["theme"],
            "scenes": scenes_info
        })
    
    # Save manifest
    manifest_path = os.path.join(BASE_DIR, "manifest_shorts.json")
    remotion_manifest = os.path.join(REMOTION_BASE, "manifest_shorts.json")
    
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_result, f, indent=2)
    with open(remotion_manifest, 'w', encoding='utf-8') as f:
        json.dump(manifest_result, f, indent=2)
        
    print(f"\n=== MANIFEST SAVED SUCCESSFULLY ({len(manifest_result)} SHORTS) ===", flush=True)

if __name__ == "__main__":
    main()
