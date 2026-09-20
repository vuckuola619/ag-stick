"""
Visual Beat Compiler for AG-Stick v2.

Decomposes high-level editorial scenes and voiceover narration into 3-8 micro-beats.
Assigns visual functions, character states, prop interactions, camera motions,
and sound design cues.
"""

from typing import List, Dict, Any, Optional
import re
from engine.schema import (
    Scene, Beat, VisualFunction, CameraShot, CameraMotion,
    CameraConfig, CharacterState, PropState, SubjectMotion,
    SubjectMotionType, FXEvent, SFXEvent, AssetTier,
    CharacterTransform
)
from engine.style_engine import StyleEngine


class BeatCompiler:
    def __init__(self, style_engine: Optional[StyleEngine] = None, fps: int = 30):
        self.style_engine = style_engine or StyleEngine()
        self.fps = fps

    def compile_scene(self, scene: Scene) -> List[Beat]:
        """
        Compile a Scene into 3-8 sequential Beats.
        If scene has pre-defined custom beats (e.g. key dramatic scenes),
        normalizes frames/timings. Otherwise compiles heuristically.
        """
        if scene.beats and len(scene.beats) > 0:
            beats = scene.beats
        else:
            beats = self._heuristic_decompile(scene)

        # Normalize timings and frames
        self._normalize_beat_timings(scene, beats)
        return beats

    def _normalize_beat_timings(self, scene: Scene, beats: List[Beat]):
        """Ensure beat durations sum up exactly to scene duration and calculate frame boundaries."""
        total_beat_sec = sum(b.duration_sec for b in beats)
        if total_beat_sec <= 0:
            # Distribute equally
            dur = scene.duration_sec / max(1, len(beats))
            for b in beats:
                b.duration_sec = dur
            total_beat_sec = scene.duration_sec

        # Post-process: Split any beat > 5.5s to prevent retention drop (Rule 01)
        refined_beats: List[Beat] = []
        for b in beats:
            if b.duration_sec > 5.5:
                # Split in half
                half_dur = round(b.duration_sec / 2.0, 2)
                b1 = b.model_copy(deep=True)
                b1.id = f"{b.id}_1"
                b1.duration_sec = half_dur
                
                b2 = b.model_copy(deep=True)
                b2.id = f"{b.id}_2"
                b2.duration_sec = round(b.duration_sec - half_dur, 2)
                # Shift camera motion for variety
                b2.camera.motion = CameraMotion.PUSH_IN if b1.camera.motion == CameraMotion.STATIC else CameraMotion.STATIC
                b2.camera.shot = CameraShot.CLOSEUP if b1.camera.shot == CameraShot.MEDIUM else CameraShot.MEDIUM
                refined_beats.extend([b1, b2])
            else:
                refined_beats.append(b)

        beats.clear()
        beats.extend(refined_beats)

        # Scale durations to match scene duration exactly
        total_beat_sec = sum(b.duration_sec for b in beats)
        scale = scene.duration_sec / total_beat_sec
        current_time = scene.start_sec
        current_frame = scene.start_frame

        for i, b in enumerate(beats):
            b.duration_sec = round(b.duration_sec * scale, 2)
            b.start_sec = round(current_time, 2)
            b.duration_frames = int(round(b.duration_sec * self.fps))
            b.start_frame = current_frame

            current_time += b.duration_sec
            current_frame += b.duration_frames

        # Fix rounding difference on last beat
        diff_frames = scene.duration_frames - (current_frame - scene.start_frame)
        if beats and diff_frames != 0:
            beats[-1].duration_frames += diff_frames
            beats[-1].duration_sec = round(beats[-1].duration_frames / self.fps, 2)

    def _heuristic_decompile(self, scene: Scene) -> List[Beat]:
        """
        Decomposes scene narration text into micro-beats based on semantic cues,
        clauses, verbs, characters, and dramatic tension.
        Aims for 3.0s - 4.2s average beat duration to eliminate static visual holds.
        """
        text = scene.narration.strip()
        # Split by sentences first
        raw_sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
        
        # Further split long sentences (> 16 words) by commas, dashes, or semicolons
        fragments: List[str] = []
        for s in raw_sentences:
            words = s.split()
            if len(words) > 16:
                sub_parts = re.split(r'[,;—–]\s+|\s+(?:but|while|as|leaving|yet)\s+', s)
                sub_parts = [p.strip() for p in sub_parts if len(p.strip().split()) >= 4]
                if len(sub_parts) >= 2:
                    fragments.extend(sub_parts)
                else:
                    fragments.append(s)
            else:
                fragments.append(s)

        if not fragments:
            fragments = [text]

        beats: List[Beat] = []
        scene_tension = scene.tension

        # Target 3-8 beats per scene
        for i, sentence in enumerate(fragments):
            lower = sentence.lower()
            beat_id = f"{scene.scene_id}_{chr(ord('a') + len(beats))}"

            # 1. Determine Visual Function & Tension
            if any(w in lower for w in ["slipped", "drops", "fell", "slams", "shut", "closing"]):
                vf = VisualFunction.ACTION
                tier = AssetTier.T1_REUSABLE
                tension = max(scene_tension, 0.85)
                shot = CameraShot.CLOSEUP
                cam_motion = CameraMotion.SHAKE
            elif any(w in lower for w in ["tense", "worried", "horror", "shock", "looked away", "nervous", "flinched"]):
                vf = VisualFunction.REACTION
                tier = AssetTier.T1_REUSABLE
                tension = max(scene_tension, 0.75)
                shot = CameraShot.CLOSEUP
                cam_motion = CameraMotion.SNAP_ZOOM
            elif any(w in lower for w in ["fission", "neutrons", "cascade", "reflect", "particle", "crossfire"]):
                vf = VisualFunction.DIAGRAM
                tier = AssetTier.T0_PROCEDURAL
                tension = scene_tension
                shot = CameraShot.MEDIUM
                cam_motion = CameraMotion.STATIC
            elif any(w in lower for w in ["screwdriver", "brick", "dome", "gap", "millimeter", "core"]):
                vf = VisualFunction.OBJECT_FOCUS
                tier = AssetTier.T1_REUSABLE
                tension = scene_tension
                shot = CameraShot.MACRO
                cam_motion = CameraMotion.PUSH_IN
            elif any(w in lower for w in ["flash", "supercriticality", "blue", "cherenkov", "burst"]):
                vf = VisualFunction.CLIMAX
                tier = AssetTier.T4_HERO
                tension = 1.0
                shot = CameraShot.WIDE
                cam_motion = CameraMotion.SHAKE
            else:
                # Alternate visual function to prevent exposition fatigue (Rule 03)
                if i > 0 and beats and beats[-1].visual_function in [VisualFunction.EXPLAIN, VisualFunction.ESTABLISH]:
                    if i % 3 == 1:
                        vf = VisualFunction.OBJECT_FOCUS
                        shot = CameraShot.CLOSEUP
                        cam_motion = CameraMotion.PUSH_IN
                    elif i % 3 == 2:
                        vf = VisualFunction.REACTION
                        shot = CameraShot.MEDIUM
                        cam_motion = CameraMotion.STATIC
                    else:
                        vf = VisualFunction.DIAGRAM
                        shot = CameraShot.MEDIUM
                        cam_motion = CameraMotion.STATIC
                else:
                    vf = VisualFunction.EXPLAIN if i > 0 else VisualFunction.ESTABLISH
                    shot = CameraShot.WIDE if i == 0 else CameraShot.MEDIUM
                    cam_motion = CameraMotion.PUSH_IN if i == 0 else CameraMotion.STATIC

                tier = AssetTier.T2_COMPOSED if vf != VisualFunction.DIAGRAM else AssetTier.T0_PROCEDURAL
                tension = scene_tension

            # 2. Extract Character references
            chars: List[CharacterState] = []
            if "slotin" in lower:
                pose = "holding_screwdriver" if "screwdriver" in lower else ("shocked_recoil" if tension > 0.8 else "confident")
                expr = "terrified" if tension > 0.8 else ("worried" if tension > 0.6 else "confident")
                chars.append(CharacterState(
                    character_id="CHAR_SLOTIN",
                    pose=pose,
                    expression=expr,
                    transform=CharacterTransform(x=0.0, y=0.0, scale=1.0)
                ))
            elif "daghlian" in lower:
                pose = "brick_slipped" if "slipped" in lower else "stacking_brick"
                expr = "shocked" if tension > 0.8 else "focused"
                chars.append(CharacterState(
                    character_id="CHAR_DAGHLIAN",
                    pose=pose,
                    expression=expr,
                    transform=CharacterTransform(x=0.0, y=0.0, scale=1.0)
                ))
            else:
                chars.append(CharacterState(
                    character_id="CHAR_GENERIC_SCIENTIST",
                    pose="observing" if vf == VisualFunction.REACTION else "idle",
                    expression="worried" if tension > 0.7 else "neutral"
                ))

            # 3. Props
            props: List[PropState] = []
            if "screwdriver" in lower:
                props.append(PropState(
                    prop_id="PROP_FLATHEAD_SCREWDRIVER",
                    state="wedged" if "gap" in lower or "blade" in lower else "default"
                ))
            if "core" in lower or "plutonium" in lower:
                props.append(PropState(prop_id="PROP_PLUTONIUM_CORE"))
            if "dome" in lower or "beryllium" in lower:
                props.append(PropState(prop_id="PROP_BERYLLIUM_UPPER"))

            # 4. SFX Events
            sfx: List[SFXEvent] = []
            if "click" in lower or "clack" in lower or "shut" in lower:
                sfx.append(SFXEvent(cue="metal_clack", start_sec=0.1, gain=1.2))
            if "flash" in lower or "blue" in lower:
                sfx.append(SFXEvent(cue="cherenkov_burst", start_sec=0.0, gain=1.0))
            if "neutrons" in lower or "counter" in lower:
                sfx.append(SFXEvent(cue="geiger_accelerating", start_sec=0.2, pattern="accelerating"))

            # Approximate duration by word count
            word_count = len(sentence.split())
            est_duration = max(1.5, round(word_count / 2.6, 1))

            beats.append(Beat(
                id=beat_id,
                duration_sec=est_duration,
                visual_function=vf,
                tier=tier,
                tension=tension,
                description=sentence,
                camera=CameraConfig(shot=shot, motion=cam_motion, strength=0.4 if tension > 0.7 else 0.2),
                characters=chars,
                props=props,
                sfx_events=sfx
            ))

        return beats

    def create_demon_core_scene_24_beats(self, scene: Scene) -> List[Beat]:
        """
        Specialized Master Beat Choreography for Scene 24 ('ONE MILLIMETER SLIP').
        Upgrades 1 static image into 9 dynamic micro-beats!
        """
        beats = [
            Beat(
                id="24a",
                duration_sec=3.0,
                visual_function=VisualFunction.ESTABLISH,
                tier=AssetTier.T2_COMPOSED,
                tension=0.65,
                description="Wide lab room: Louis Slotin leaning over the workbench demonstrating the dangerous experiment to colleagues.",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.PUSH_IN, strength=0.25),
                characters=[
                    CharacterState(character_id="CHAR_SLOTIN", pose="holding_screwdriver", expression="confident", transform=CharacterTransform(x=0, y=0)),
                    CharacterState(character_id="CHAR_RAEMER_SCHREIBER", pose="observing", expression="worried", transform=CharacterTransform(x=45, y=0)),
                    CharacterState(character_id="CHAR_GUARD_BARRERA", pose="standing_guard", expression="neutral", transform=CharacterTransform(x=-50, y=0)),
                ],
                props=[
                    PropState(prop_id="PROP_WOODEN_WORKBENCH"),
                    PropState(prop_id="PROP_BERYLLIUM_LOWER"),
                    PropState(prop_id="PROP_PLUTONIUM_CORE"),
                    PropState(prop_id="PROP_BERYLLIUM_UPPER", state="propped_open"),
                    PropState(prop_id="PROP_FLATHEAD_SCREWDRIVER", attached_to="CHAR_SLOTIN.hand_r"),
                ],
                sfx_events=[SFXEvent(cue="lab_room_hum", start_sec=0.0, gain=0.6)]
            ),
            Beat(
                id="24b",
                duration_sec=2.0,
                visual_function=VisualFunction.REACTION,
                tier=AssetTier.T1_REUSABLE,
                tension=0.75,
                description="Observer closeup: Raemer Schreiber looks away for a split second, sensing extreme unease.",
                camera=CameraConfig(shot=CameraShot.CLOSEUP, motion=CameraMotion.STATIC, focus="CHAR_RAEMER_SCHREIBER"),
                characters=[
                    CharacterState(character_id="CHAR_RAEMER_SCHREIBER", pose="turning_away", expression="worried", transform=CharacterTransform(x=0, y=0, scale=1.4))
                ],
                sfx_events=[SFXEvent(cue="tense_drone", start_sec=0.0, gain=0.8)]
            ),
            Beat(
                id="24c",
                duration_sec=2.5,
                visual_function=VisualFunction.OBJECT_FOCUS,
                tier=AssetTier.T1_REUSABLE,
                tension=0.82,
                description="Macro closeup: Blade of the yellow-handled screwdriver wedged into the razor-thin beryllium dome gap.",
                camera=CameraConfig(shot=CameraShot.MACRO, motion=CameraMotion.PUSH_IN, strength=0.15, focus="PROP_FLATHEAD_SCREWDRIVER"),
                props=[
                    PropState(prop_id="PROP_BERYLLIUM_UPPER", state="slanted"),
                    PropState(prop_id="PROP_BERYLLIUM_LOWER"),
                    PropState(prop_id="PROP_FLATHEAD_SCREWDRIVER", state="wedged_critical"),
                ],
                subject_motion=[
                    SubjectMotion(target="PROP_FLATHEAD_SCREWDRIVER", motion=SubjectMotionType.MICRO_SHAKE, start_pct=0.4, duration_pct=0.6, intensity=1.5)
                ],
                sfx_events=[SFXEvent(cue="geiger_rapid_clicks", start_sec=0.0, pattern="accelerating", gain=0.9)]
            ),
            Beat(
                id="24d",
                duration_sec=1.5,
                visual_function=VisualFunction.REACTION,
                tier=AssetTier.T1_REUSABLE,
                tension=0.88,
                description="Hand closeup: Slotin's stick figure hand gripping the tool, a single cartoon sweat drop beads and falls.",
                camera=CameraConfig(shot=CameraShot.EXTREME_CLOSEUP, motion=CameraMotion.STATIC),
                characters=[
                    CharacterState(character_id="CHAR_SLOTIN", pose="holding_screwdriver", expression="focused", transform=CharacterTransform(scale=1.6))
                ],
                fx=[FXEvent(effect_type="sweat_drop", start_pct=0.2, duration_pct=0.8, intensity=1.0)],
                sfx_events=[SFXEvent(cue="heavy_breathing", start_sec=0.1, gain=1.0)]
            ),
            Beat(
                id="24e",
                duration_sec=0.7,
                visual_function=VisualFunction.ACTION,
                tier=AssetTier.T1_REUSABLE,
                tension=0.95,
                description="Screwdriver blade suddenly slips one millimeter off the polished metal lip!",
                camera=CameraConfig(shot=CameraShot.CLOSEUP, motion=CameraMotion.SNAP_ZOOM, strength=0.5),
                props=[
                    PropState(prop_id="PROP_FLATHEAD_SCREWDRIVER", state="slipping"),
                    PropState(prop_id="PROP_BERYLLIUM_UPPER", state="falling")
                ],
                subject_motion=[
                    SubjectMotion(target="PROP_FLATHEAD_SCREWDRIVER", motion=SubjectMotionType.DROP, start_pct=0.0, duration_pct=1.0, intensity=2.0)
                ],
                sfx_events=[SFXEvent(cue="metal_scrape_sharp", start_sec=0.0, gain=1.3)]
            ),
            Beat(
                id="24f",
                duration_sec=0.4,
                visual_function=VisualFunction.ACTION,
                tier=AssetTier.T1_REUSABLE,
                tension=0.98,
                description="The heavy beryllium hemisphere drops completely flush onto the lower shell.",
                camera=CameraConfig(shot=CameraShot.MEDIUM, motion=CameraMotion.STATIC),
                props=[
                    PropState(prop_id="PROP_BERYLLIUM_UPPER", state="slammed_shut"),
                    PropState(prop_id="PROP_BERYLLIUM_LOWER")
                ],
                subject_motion=[
                    SubjectMotion(target="PROP_BERYLLIUM_UPPER", motion=SubjectMotionType.DROP, start_pct=0.0, duration_pct=0.5, intensity=3.0)
                ],
                sfx_events=[]
            ),
            Beat(
                id="24g",
                duration_sec=0.3,
                visual_function=VisualFunction.PAUSE,
                tier=AssetTier.T0_PROCEDURAL,
                tension=1.0,
                description="TOTAL BLACKOUT & SILENCE — Heavy metallic impact.",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.STATIC),
                environment_id="full_black",
                sfx_events=[
                    SFXEvent(cue="metal_clack_loud", start_sec=0.0, gain=1.5),
                    SFXEvent(cue="room_tone_cut", start_sec=0.0)
                ]
            ),
            Beat(
                id="24h",
                duration_sec=1.0,
                visual_function=VisualFunction.CLIMAX,
                tier=AssetTier.T4_HERO,
                tension=1.0,
                description="BLINDING CHERENKOV BLUE FLASH floods the entire frame!",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.SHAKE, strength=0.8),
                fx=[FXEvent(effect_type="blue_flash", start_pct=0.0, duration_pct=1.0, intensity=1.5, color="#00E5FF")],
                sfx_events=[SFXEvent(cue="cherenkov_radiation_burst", start_sec=0.0, gain=1.4)]
            ),
            Beat(
                id="24i",
                duration_sec=3.5,
                visual_function=VisualFunction.AFTERMATH,
                tier=AssetTier.T2_COMPOSED,
                tension=0.92,
                description="Room reaction: Scientists recoil in sheer terror, Slotin realizes he has taken a lethal dose.",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.SHAKE, strength=0.3),
                characters=[
                    CharacterState(character_id="CHAR_SLOTIN", pose="shocked_recoil", expression="terrified", transform=CharacterTransform(x=0, y=0)),
                    CharacterState(character_id="CHAR_RAEMER_SCHREIBER", pose="recoiling", expression="alarmed", transform=CharacterTransform(x=45, y=0)),
                    CharacterState(character_id="CHAR_GUARD_BARRERA", pose="startled", expression="shocked", transform=CharacterTransform(x=-50, y=0))
                ],
                props=[
                    PropState(prop_id="PROP_BERYLLIUM_UPPER", state="slammed_shut")
                ],
                sfx_events=[
                    SFXEvent(cue="geiger_screaming_continuous", start_sec=0.0, gain=1.1),
                    SFXEvent(cue="sub_bass_rumble", start_sec=0.0, gain=0.9)
                ]
            )
        ]
        self._normalize_beat_timings(scene, beats)
        return beats

    def create_demon_core_scene_04_diagram_beats(self, scene: Scene) -> List[Beat]:
        """
        Specialized Master Beat Choreography for Scene 04 ('NEUTRON CROSSFIRE').
        Decomposes nuclear physics into 5 procedural SVG diagram beats (T0/MinutePhysics).
        """
        beats = [
            Beat(
                id="04a",
                duration_sec=3.5,
                visual_function=VisualFunction.EXPLAIN,
                tier=AssetTier.T0_PROCEDURAL,
                visual_grammar="particle_emission",
                tension=0.3,
                description="Core idle: Spontaneous fission begins. Single neutron particle shoots out from plutonium sphere.",
                camera=CameraConfig(shot=CameraShot.MEDIUM, motion=CameraMotion.STATIC),
                props=[PropState(prop_id="PROP_PLUTONIUM_CORE")],
                fx=[FXEvent(effect_type="neutrons_spontaneous", start_pct=0.3, duration_pct=0.7, intensity=1.0)],
                sfx_events=[SFXEvent(cue="geiger_single_click", start_sec=1.0, gain=0.8)]
            ),
            Beat(
                id="04b",
                duration_sec=3.5,
                visual_function=VisualFunction.DIAGRAM,
                tier=AssetTier.T0_PROCEDURAL,
                visual_grammar="escape_pathways",
                tension=0.35,
                description="Most neutrons escape harmlessly into room space (arrows radiate outward past screen boundaries).",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.PULL_OUT, strength=0.2),
                props=[PropState(prop_id="PROP_PLUTONIUM_CORE")],
                fx=[FXEvent(effect_type="neutron_escape_vectors", start_pct=0.0, duration_pct=1.0)],
                sfx_events=[SFXEvent(cue="whoosh_escape", start_sec=0.5, gain=0.7)]
            ),
            Beat(
                id="04c",
                duration_sec=4.0,
                visual_function=VisualFunction.DIAGRAM,
                tier=AssetTier.T0_PROCEDURAL,
                visual_grammar="reflection_barrier",
                tension=0.5,
                description="Reflection wall appears: Escaping neutrons bounce off beryllium shell back toward core.",
                camera=CameraConfig(shot=CameraShot.CLOSEUP, motion=CameraMotion.PUSH_IN, strength=0.2),
                props=[
                    PropState(prop_id="PROP_PLUTONIUM_CORE"),
                    PropState(prop_id="PROP_BERYLLIUM_UPPER")
                ],
                fx=[FXEvent(effect_type="neutron_reflection_bounce", start_pct=0.2, duration_pct=0.8, color="#00E5FF")],
                sfx_events=[SFXEvent(cue="deflection_ping", start_sec=1.2, gain=0.9)]
            ),
            Beat(
                id="04d",
                duration_sec=4.5,
                visual_function=VisualFunction.DIAGRAM,
                tier=AssetTier.T0_PROCEDURAL,
                visual_grammar="exponential_multiplication",
                tension=0.7,
                description="Each fission triggers two more: 1 -> 2 -> 4 -> 8 -> 16 exponential neutron cascade.",
                camera=CameraConfig(shot=CameraShot.MEDIUM, motion=CameraMotion.STATIC),
                props=[PropState(prop_id="PROP_PLUTONIUM_CORE")],
                fx=[FXEvent(effect_type="fission_multiplication_tree", start_pct=0.0, duration_pct=1.0)],
                text_overlay="2^n EXPONENTIAL CASCADE",
                sfx_events=[SFXEvent(cue="geiger_cascade_building", start_sec=0.0, pattern="exponential", gain=1.1)]
            ),
            Beat(
                id="04e",
                duration_sec=4.5,
                visual_function=VisualFunction.CLIMAX,
                tier=AssetTier.T0_PROCEDURAL,
                visual_grammar="prompt_criticality_flood",
                tension=0.85,
                description="Prompt Criticality: Screen floods with electric cyan radiation glow as k exceeds 1.0.",
                camera=CameraConfig(shot=CameraShot.WIDE, motion=CameraMotion.SNAP_ZOOM, strength=0.4),
                fx=[FXEvent(effect_type="cyan_radiation_flood", start_pct=0.0, duration_pct=1.0, color="#00E5FF")],
                text_overlay="k >= 1.0 // PROMPT CRITICAL",
                sfx_events=[SFXEvent(cue="critical_hum_surge", start_sec=0.0, gain=1.2)]
            )
        ]
        self._normalize_beat_timings(scene, beats)
        return beats
