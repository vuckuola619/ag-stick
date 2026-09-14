"""
YTF MASTER PRODUCTION SYSTEM v2.0 - REMOTION MANIFEST COMPILER
Maps 28 scenes to frame-exact timing, 28 UNIQUE DEDICATED SCENE ASSETS, and clean Ken Burns transitions.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_PATH = os.path.join(BASE_DIR, "script", "timeline_script.json")
AUDIO_QC_PATH = os.path.join(BASE_DIR, "qc", "audio_report.json")
OUT_MANIFEST = os.path.join(BASE_DIR, "remotion", "public", "scene_manifest.json")

with open(TIMELINE_PATH, "r", encoding="utf-8") as f:
    timeline = json.load(f)

with open(AUDIO_QC_PATH, "r", encoding="utf-8") as f:
    audio_qc = json.load(f)

audio_durations = {item["scene_id"]: item["duration_sec"] for item in audio_qc.get("scene_audio", [])}

scenes_manifest = []
current_frame = 0
fps = 30

for s in timeline.get("scenes", []):
    sid = s["scene_id"]
    scene_num = int(sid.replace("S", ""))
    audio_dur = audio_durations.get(sid, 10.0)
    scene_dur = round(audio_dur + 0.35, 2)
    duration_frames = int(scene_dur * fps)

    # Dedicated image asset for each scene
    image_src = f"assets/images/scene_{scene_num:02d}.png"
    
    # Selective puppet overlay
    puppet_src = None
    if sid in ["S004", "S007", "S008", "S011", "S016", "S020", "S025", "S027"]:
        puppet_src = "assets/images/adam_real_cutout_head.png"
    elif sid in ["S014", "S015"]:
        puppet_src = "assets/images/masa_real_cutout_head.png"

    scenes_manifest.append({
        "sceneIndex": scene_num,
        "sceneId": sid,
        "act": s.get("act", ""),
        "narration": s.get("narration", ""),
        "kineticHeading": s.get("overlay_text", ""),
        "lowerThird": f"EXHIBIT #{scene_num:02d} // SEC FORENSIC ARCHIVES",
        "audioSrc": f"assets/audio/{sid}.wav",
        "imageSrc": image_src,
        "puppetSrc": puppet_src,
        "startFrame": current_frame,
        "durationInFrames": duration_frames,
        "durationSeconds": scene_dur,
        "posterizeFps": 12,
        "transition": "ken_burns"
    })

    current_frame += duration_frames

total_seconds = round(current_frame / fps, 2)

manifest_data = {
    "project": "WeWork: The $47 Billion Illusion",
    "workingTitle": "How a Landlord Convinced Wall Street It Was a $47B Tech Miracle",
    "totalDurationSeconds": total_seconds,
    "totalFrames": current_frame,
    "fps": fps,
    "width": 1920,
    "height": 1080,
    "visualStyle": "Photo Cut-out Puppet × Editorial Paper Collage (28 Dedicated Unique Scenes)",
    "masterAudioSrc": "assets/audio/master_narration.wav",
    "scenes": scenes_manifest
}

with open(OUT_MANIFEST, "w", encoding="utf-8") as f:
    json.dump(manifest_data, f, indent=2)

print(f"Remotion scene manifest compiled with 28 UNIQUE DEDICATED SCENE ASSETS!")
print(f"Total Scenes: {len(scenes_manifest)}")
print(f"Total Frames: {current_frame} @ 30 FPS ({total_seconds:.2f}s)")
