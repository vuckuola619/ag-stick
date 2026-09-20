"""
AG-Stick v2 Core Schema Specification.

Defines the hierarchical structure:
Episode -> Act -> Scene -> Beat
along with Asset, Character Rig, Camera Grammar, Motion Grammar, and SFX models.
"""

from __future__ import annotations
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class VisualFunction(str, Enum):
    ESTABLISH = "establish"
    ACTION = "action"
    REACTION = "reaction"
    EXPLAIN = "explain"
    DIAGRAM = "diagram"
    COMPARISON = "comparison"
    TIMELINE = "timeline"
    MAP = "map"
    OBJECT_FOCUS = "object_focus"
    CHARACTER = "character"
    FORESHADOW = "foreshadow"
    PAYOFF = "payoff"
    JOKE = "joke"
    TRANSITION = "transition"
    PAUSE = "pause"
    CLIMAX = "climax"
    AFTERMATH = "aftermath"


class CameraShot(str, Enum):
    WIDE = "wide"
    MEDIUM = "medium"
    CLOSEUP = "closeup"
    MACRO = "macro"
    EXTREME_CLOSEUP = "extreme_closeup"
    DUTCH = "dutch"


class CameraMotion(str, Enum):
    STATIC = "static"
    PUSH_IN = "push_in"
    PULL_OUT = "pull_out"
    PAN_LEFT = "pan_left"
    PAN_RIGHT = "pan_right"
    TRACK = "track"
    SNAP_ZOOM = "snap_zoom"
    SHAKE = "shake"
    WHIP = "whip"


class SubjectMotionType(str, Enum):
    ENTER = "enter"
    EXIT = "exit"
    DROP = "drop"
    BOUNCE = "bounce"
    ROTATE = "rotate"
    SCALE = "scale"
    PULSE = "pulse"
    VIBRATE = "vibrate"
    POINT = "point"
    HIGHLIGHT = "highlight"
    MICRO_SHAKE = "micro_shake"


class AssetTier(str, Enum):
    T0_PROCEDURAL = "T0"      # Pure programmatic (particles, diagram, shapes)
    T1_REUSABLE = "T1"        # Modular vector character rigs, canonical props
    T2_COMPOSED = "T2"        # Multi-element scene composition (lab room + multiple rigs)
    T3_AI_GENERATED = "T3"    # Detailed AI background or specific illustration
    T4_HERO = "T4"            # Rare cinematic hero frame (e.g. blue flash, explosion)


class ExpressionType(str, Enum):
    NEUTRAL = "neutral"
    CONFIDENT = "confident"
    AMUSED = "amused"
    FOCUSED = "focused"
    WORRIED = "worried"
    SHOCKED = "shocked"
    EXHAUSTED = "exhausted"
    TERRIFIED = "terrified"
    CURIOUS = "curious"


class PoseType(str, Enum):
    IDLE = "idle"
    CONFIDENT = "confident"
    HOLDING_SCREWDRIVER = "holding_screwdriver"
    LIFTING_DOME = "lifting_dome"
    SHOCKED = "shocked"
    THROWING_DOME = "throwing_dome"
    KNEELING = "kneeling"
    POINTING = "pointing"
    EXPLAINING = "explaining"
    RECOILING = "recoiling"
    STACKING_BRICK = "stacking_brick"
    BRICK_SLIPPED = "brick_slipped"


class SFXEvent(BaseModel):
    cue: str
    start_sec: float
    duration_sec: Optional[float] = None
    gain: float = 1.0
    pattern: Optional[str] = None  # e.g., "accelerating", "single_hit", "reverberant"


class CameraConfig(BaseModel):
    shot: CameraShot = CameraShot.MEDIUM
    motion: CameraMotion = CameraMotion.STATIC
    strength: float = 0.35
    focus: Optional[str] = None  # target subject or prop ID


class CharacterTransform(BaseModel):
    x: float = 0.0          # Percentage (-100 to 100 or px offset)
    y: float = 0.0
    scale: float = 1.0
    rotation: float = 0.0   # Degrees
    flip_x: bool = False


class CharacterState(BaseModel):
    character_id: str
    pose: str = "idle"
    expression: str = "neutral"
    mouth_state: str = "closed"  # "closed", "open", "talking", "grimace"
    hand_pose: Optional[str] = None
    transform: CharacterTransform = Field(default_factory=CharacterTransform)
    z_index: int = 10


class PropState(BaseModel):
    prop_id: str
    state: str = "default"
    attached_to: Optional[str] = None  # e.g., "CHAR_SLOTIN.hand_r"
    transform: CharacterTransform = Field(default_factory=CharacterTransform)
    z_index: int = 5


class SubjectMotion(BaseModel):
    target: str                  # Prop or Character ID
    motion: SubjectMotionType
    start_pct: float = 0.0       # 0.0 - 1.0 within beat
    duration_pct: float = 1.0    # fraction of beat duration
    intensity: float = 1.0


class FXEvent(BaseModel):
    effect_type: str             # "blue_flash", "sweat_drop", "neutrons", "shockwave"
    intensity: float = 1.0
    start_pct: float = 0.0
    duration_pct: float = 1.0
    color: Optional[str] = None


class Beat(BaseModel):
    id: str
    duration_sec: float
    start_sec: float = 0.0
    start_frame: int = 0
    duration_frames: int = 0
    visual_function: VisualFunction = VisualFunction.ACTION
    visual_grammar: Optional[str] = None
    tier: AssetTier = AssetTier.T1_REUSABLE
    tension: float = Field(default=0.3, ge=0.0, le=1.0)
    description: str = ""
    camera: CameraConfig = Field(default_factory=CameraConfig)
    characters: List[CharacterState] = Field(default_factory=list)
    props: List[PropState] = Field(default_factory=list)
    environment_id: str = "omega_lab"
    subject_motion: List[SubjectMotion] = Field(default_factory=list)
    fx: List[FXEvent] = Field(default_factory=list)
    sfx_events: List[SFXEvent] = Field(default_factory=list)
    text_overlay: Optional[str] = None


class Scene(BaseModel):
    scene_id: str
    act_id: int
    act_title: str = ""
    headline: str = ""
    narration: str
    duration_sec: float
    start_sec: float = 0.0
    start_frame: int = 0
    duration_frames: int = 0
    story_function: str = "narrative_beat"
    tension: float = Field(default=0.3, ge=0.0, le=1.0)
    audio_file: Optional[str] = None
    image_fallback: Optional[str] = None
    beats: List[Beat] = Field(default_factory=list)


class Act(BaseModel):
    act_id: int
    title: str
    scenes: List[Scene] = Field(default_factory=list)


class Episode(BaseModel):
    project_name: str
    series: str = "Deadly Elements & Bizarre Scientific Disasters"
    channel: str = "NEON ATOM (@NeonAtomDocs)"
    fps: int = 30
    total_duration_sec: float = 0.0
    total_frames: int = 0
    style: str = "neon-atom"
    acts: List[Act] = Field(default_factory=list)
    scenes: List[Scene] = Field(default_factory=list)
