"""
AG-Stick v2 Compiler Script for Demon Core (10-Minute Master).

Transforms 32 static scenes (1 scene = 1 image) into ~145 dynamic visual beats
(1 scene = 3-8 beats), with canonical character rigs, procedural diagrams,
and SFX event scheduling.
"""

import os
import sys
import json
import shutil

# Add repo root to sys.path
ROOT_DIR = r"c:\Users\bati-\Documents\AG-Stick"
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from engine.schema import Episode, Act, Scene, Beat, AssetTier
from engine.style_engine import StyleEngine
from engine.compiler.beat_compiler import BeatCompiler
from engine.compiler.retention_auditor import RetentionAuditor

DEMON_CORE_DIR = os.path.join(ROOT_DIR, "projects", "demon-core-10min")
SCRIPT_DIR = os.path.join(DEMON_CORE_DIR, "script")
MANIFEST_SRC = os.path.join(SCRIPT_DIR, "demon_core_manifest.json")
OUT_BEATS_JSON = os.path.join(SCRIPT_DIR, "demon_core_v2_beats_manifest.json")
AUDIT_REPORT_MD = os.path.join(DEMON_CORE_DIR, "RETENTION_AUDIT_V2.md")
REMOTION_PUBLIC_DEST = os.path.join(
    ROOT_DIR, "projects", "wework-47-billion-illusion", "remotion", "public", "assets", "demon_core"
)


def run_compilation():
    print("=======================================================================", flush=True)
    print("=== AG-Stick v2: Compiling Demon Core to Multi-Beat Visual Pipeline ===", flush=True)
    print("=== Architecture: Episode -> Act -> Scene -> Beat                   ===", flush=True)
    print("=======================================================================\n", flush=True)

    with open(MANIFEST_SRC, "r", encoding="utf-8") as f:
        src_manifest = json.load(f)

    style_engine = StyleEngine(style_name="neon-atom", styles_root=os.path.join(ROOT_DIR, "styles"))
    compiler = BeatCompiler(style_engine=style_engine, fps=src_manifest.get("fps", 30))
    auditor = RetentionAuditor()

    scenes_v2 = []
    total_beats_count = 0

    for s_data in src_manifest.get("scenes", []):
        scene_obj = Scene(
            scene_id=s_data["scene_id"],
            act_id=s_data.get("act", 1),
            act_title=s_data.get("act_title", ""),
            headline=s_data.get("kinetic_hook_headline", ""),
            narration=s_data.get("voiceover_text", ""),
            duration_sec=s_data.get("total_scene_duration_sec", 20.0),
            start_sec=s_data.get("start_sec", 0.0),
            start_frame=s_data.get("start_frame", 0),
            duration_frames=s_data.get("duration_frames", 600),
            audio_file=s_data.get("audio_file"),
            image_fallback=s_data.get("image_file"),
            tension=0.95 if s_data["scene_id"] in ["24", "25"] else (0.85 if s_data["scene_id"] in ["15", "16"] else 0.4)
        )

        # Highlight Master Scenes
        if scene_obj.scene_id == "24":
            beats = compiler.create_demon_core_scene_24_beats(scene_obj)
        elif scene_obj.scene_id == "04":
            beats = compiler.create_demon_core_scene_04_diagram_beats(scene_obj)
        else:
            beats = compiler.compile_scene(scene_obj)

        scene_obj.beats = beats
        total_beats_count += len(beats)
        scenes_v2.append(scene_obj)

    episode = Episode(
        project_name=src_manifest.get("project", "The Demon Core"),
        series=src_manifest.get("series", "Deadly Elements"),
        channel=src_manifest.get("channel", "NEON ATOM"),
        fps=src_manifest.get("fps", 30),
        total_duration_sec=src_manifest.get("total_duration_sec", 600.0),
        total_frames=src_manifest.get("total_frames", 18000),
        style="neon-atom",
        scenes=scenes_v2
    )

    # Serialize V2 Manifest
    v2_dict = episode.model_dump()
    with open(OUT_BEATS_JSON, "w", encoding="utf-8") as f:
        json.dump(v2_dict, f, indent=2)
    print(f"[SUCCESS] Compiled {len(scenes_v2)} scenes into {total_beats_count} visual beats!")
    print(f"  Saved to: {OUT_BEATS_JSON}", flush=True)

    # Copy to Remotion public assets
    os.makedirs(REMOTION_PUBLIC_DEST, exist_ok=True)
    remotion_dest_file = os.path.join(REMOTION_PUBLIC_DEST, "demon_core_v2_beats_manifest.json")
    shutil.copyfile(OUT_BEATS_JSON, remotion_dest_file)
    print(f"  Mirrored to Remotion: {remotion_dest_file}", flush=True)

    # Retention Audit
    print("\n--- Running Retention Audit (8 Documentary Laws) ---", flush=True)
    audit_res = auditor.audit_episode(episode)
    md_report = auditor.generate_markdown_report(audit_res)
    with open(AUDIT_REPORT_MD, "w", encoding="utf-8") as f:
        f.write(md_report)

    print(f"  Retention Rating       : {audit_res['rating']}")
    print(f"  Avg Beat Duration      : {audit_res['average_beat_duration_sec']}s")
    print(f"  Tier Breakdown         : {audit_res['tier_distribution']}")
    print(f"  Warnings/Errors        : {audit_res['issue_counts']['warning']} warnings, {audit_res['issue_counts']['error']} errors")
    print(f"  Audit Report Saved To  : {AUDIT_REPORT_MD}\n", flush=True)

    # Print Scene 24 Breakdown
    scene_24 = next(s for s in scenes_v2 if s.scene_id == "24")
    print("=======================================================================", flush=True)
    print("=== SCENE 24 UPGRADE: 'ONE MILLIMETER SLIP' (9 Micro-Beats)         ===", flush=True)
    print("=======================================================================", flush=True)
    for b in scene_24.beats:
        chars = ", ".join(c.character_id.replace("CHAR_", "") + ":" + c.pose for c in b.characters) or "None"
        cam = f"{b.camera.shot.value} ({b.camera.motion.value})"
        sfx = ", ".join(s.cue for s in b.sfx_events) or "None"
        print(f"[{b.id}] {b.duration_sec:.1f}s | {b.visual_function.value.upper():<12} | Cam: {cam:<20} | Chars: {chars} | SFX: {sfx}")


if __name__ == "__main__":
    run_compilation()
