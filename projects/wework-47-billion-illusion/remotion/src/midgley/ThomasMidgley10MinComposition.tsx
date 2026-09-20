import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  Audio,
  staticFile,
} from 'remotion';

import manifestData from '../../public/assets/thomas_midgley/manifest.json';

interface SceneItem {
  scene_id: string;
  act: number;
  act_title: string;
  kinetic_hook_headline: string;
  voiceover_text: string;
  word_count: number;
  start_sec: number;
  speech_duration_sec: number;
  total_scene_duration_sec: number;
  start_frame: number;
  speech_frames: number;
  duration_frames: number;
  end_frame: number;
  camera_shot?: string;
  camera_motion?: string;
  telemetry?: {
    year?: number;
    location?: string;
    lead_blood?: string;
    ozone?: string;
    status?: string;
  };
  audio_file: string;
  image_file: string;
  codex_image_prompt: string;
}

const SCENES: SceneItem[] = manifestData.scenes || [];
const TOTAL_FRAMES: number = manifestData.total_frames || 18450;

export interface EraMilestone {
  act: number;
  label: string;
  sub: string;
  location: string;
  condition: string;
  leadBlood: string;
  ozoneLevel: string;
  startFrame: number;
  endFrame: number;
  accent: string;
  subAccent: string;
  alertLevel: 'PRISTINE' | 'ELEVATED' | 'HAZARD' | 'CRITICAL' | 'CATASTROPHIC';
}

export const HISTORICAL_TIMELINE: EraMilestone[] = [
  {
    act: 1,
    label: '1921: THE KNOCK',
    sub: 'TETRAETHYL LEAD SYNTHESIS',
    location: 'DAYTON RESEARCH LABS, OH',
    condition: 'ENGINE PISTON KNOCK SOLVED',
    leadBlood: '0.8 ug/dL',
    ozoneLevel: '350 DU',
    startFrame: 0,
    endFrame: 3000,
    accent: '#F59E0B',
    subAccent: '#D97706',
    alertLevel: 'PRISTINE',
  },
  {
    act: 2,
    label: '1924: LOONY GAS',
    sub: 'BAYWAY REFINERY DELIRIUM',
    location: 'BAYWAY, NJ // ETHYL CORP',
    condition: 'ACUTE WORKER PSYCHOSIS (5 DEAD)',
    leadBlood: '85.0 ug/dL',
    ozoneLevel: '350 DU',
    startFrame: 3000,
    endFrame: 6500,
    accent: '#EF4444',
    subAccent: '#10B981',
    alertLevel: 'HAZARD',
  },
  {
    act: 3,
    label: '1955: GLOBAL SMOG',
    sub: '68 MILLION TONS OF LEAD',
    location: 'GLOBAL HIGHWAYS // ATMOSPHERE',
    condition: 'PLANETARY PEDIATRIC TOXICITY',
    leadBlood: '22.0 ug/dL',
    ozoneLevel: '340 DU',
    startFrame: 6500,
    endFrame: 9800,
    accent: '#DC2626',
    subAccent: '#B91C1C',
    alertLevel: 'CRITICAL',
  },
  {
    act: 4,
    label: '1928: FREON-12',
    sub: 'NON-FLAMMABLE CFC REFRIGERANT',
    location: 'ACS CONVENTION, ATLANTA',
    condition: 'CANDLE EXTINGUISHED (NON-TOXIC)',
    leadBlood: '12.5 ug/dL',
    ozoneLevel: '350 DU',
    startFrame: 9800,
    endFrame: 13000,
    accent: '#06B6D4',
    subAccent: '#38BDF8',
    alertLevel: 'ELEVATED',
  },
  {
    act: 5,
    label: '1985: THE OZONE TEAR',
    sub: 'ANTARCTIC HOLE // 100K:1 CATALYST',
    location: 'HALLEY BAY // STRATOSPHERE',
    condition: '60% STRATOSPHERIC COLLAPSE',
    leadBlood: '12.0 ug/dL',
    ozoneLevel: '120 DU',
    startFrame: 13000,
    endFrame: 16000,
    accent: '#8B5CF6',
    subAccent: '#EC4899',
    alertLevel: 'CATASTROPHIC',
  },
  {
    act: 6,
    label: '1944: ULTIMATE IRONY',
    sub: 'STRANGLED BY PULLEY HOIST',
    location: 'WORTHINGTON, OH // BIO-LEGACY',
    condition: 'WORST BIOLOGICAL IMPACT IN HISTORY',
    leadBlood: '0.9 ug/dL',
    ozoneLevel: '310 DU',
    startFrame: 16000,
    endFrame: 20000,
    accent: '#F59E0B',
    subAccent: '#E2E8F0',
    alertLevel: 'PRISTINE',
  },
];

const ACT_THEMES: Record<number, { primary: string; accent: string; subAccent: string }> = {
  1: { primary: '#F59E0B', accent: '#FBBF24', subAccent: '#B45309' }, // Industrial Amber
  2: { primary: '#EF4444', accent: '#10B981', subAccent: '#7F1D1D' }, // Loony Gas & Toxic Green
  3: { primary: '#DC2626', accent: '#F87171', subAccent: '#991B1B' }, // Global Blood Lead
  4: { primary: '#06B6D4', accent: '#38BDF8', subAccent: '#0E7490' }, // Frost Freon Cyan
  5: { primary: '#8B5CF6', accent: '#C084FC', subAccent: '#4C1D95' }, // Ultraviolet Ozone
  6: { primary: '#F59E0B', accent: '#FCD34D', subAccent: '#64748B' }, // Retrospective Legacy
};

export const ThomasMidgley10MinComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find currently active scene from manifest
  const activeSceneIndex = SCENES.findIndex(
    (s) => frame >= s.start_frame && frame <= s.end_frame
  );
  const activeScene = activeSceneIndex !== -1 ? SCENES[activeSceneIndex] : (SCENES[0] || {
    scene_id: '01',
    act: 1,
    act_title: 'ACT 1: THE DEADLY KNOCK',
    kinetic_hook_headline: 'THE DEADLIEST ORGANISM',
    start_frame: 0,
    duration_frames: 540,
    end_frame: 540,
  });
  const previousScene = activeSceneIndex > 0 ? SCENES[activeSceneIndex - 1] : null;

  // Frame relative to active scene start
  const sceneRelativeFrame = Math.max(0, frame - activeScene.start_frame);

  // Active Historical Era
  const currentEra =
    HISTORICAL_TIMELINE.find(
      (m) => frame >= m.startFrame && frame < m.endFrame
    ) || HISTORICAL_TIMELINE[HISTORICAL_TIMELINE.length - 1];

  const theme = ACT_THEMES[activeScene.act] || ACT_THEMES[1];

  // 1. Kinetic Entrance Springs for Headline
  const headlineEntrance = spring({
    frame: sceneRelativeFrame,
    fps,
    config: { damping: 13, stiffness: 120, mass: 0.7 },
  });

  const headlineOpacity = interpolate(
    sceneRelativeFrame,
    [0, 10, (activeScene.duration_frames || 500) - 15, activeScene.duration_frames || 500],
    [0, 1, 1, 0.85],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 2. Smooth Linear Ken Burns (Zero wobble, calm cinematic motion)
  const isEvenScene = activeSceneIndex % 2 === 0;
  const kbScale = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames || 500],
    isEvenScene ? [1.0, 1.045] : [1.045, 1.0],
    { extrapolateRight: 'clamp' }
  );
  const panX = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames || 500],
    isEvenScene ? [-6, 6] : [6, -6],
    { extrapolateRight: 'clamp' }
  );
  const panY = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames || 500],
    isEvenScene ? [-3, 3] : [3, -3],
    { extrapolateRight: 'clamp' }
  );

  // 3. Smooth Scene Transition (Crossfade Dissolve: 15 frames / 0.5s)
  const CROSSFADE_FRAMES = 15;
  const sceneEntranceOpacity = interpolate(
    sceneRelativeFrame,
    [0, CROSSFADE_FRAMES],
    [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 4. Dramatic Flash Transitions:
  // Scene 05: Toxic Emerald Flash (Lead breakthrough)
  // Scene 24: Ultraviolet Ozone Flash (UV breaking chlorine)
  let flashOpacity = 0;
  let flashColor = '#ffffff';

  if (activeScene.scene_id === '05') {
    flashColor = '#10B981'; // Toxic Emerald
    flashOpacity = interpolate(
      sceneRelativeFrame,
      [0, 3, 10, 30],
      [0.85, 1.0, 0.45, 0.0],
      { extrapolateRight: 'clamp' }
    );
  } else if (activeScene.scene_id === '24') {
    flashColor = '#C084FC'; // UV Ozone Violet
    flashOpacity = interpolate(
      sceneRelativeFrame,
      [0, 3, 10, 30],
      [0.9, 1.0, 0.5, 0.0],
      { extrapolateRight: 'clamp' }
    );
  }

  // 5. Volumetric Ambient Glow Pulses
  const glowPulse1 = 0.45 + 0.15 * Math.sin(frame / 35);
  const glowPulse2 = 0.35 + 0.12 * Math.cos(frame / 48);

  // 6. Broadcast Timecode & Progress
  const totalSec = frame / fps;
  const tcH = Math.floor(totalSec / 3600);
  const tcM = Math.floor((totalSec % 3600) / 60);
  const tcS = Math.floor(totalSec % 60);
  const tcF = frame % fps;
  const timecode = `${String(tcH).padStart(2, '0')}:${String(tcM).padStart(2, '0')}:${String(tcS).padStart(2, '0')}:${String(tcF).padStart(2, '0')}`;
  const progressPercent = Math.min(100, (frame / TOTAL_FRAMES) * 100);

  // Active scene image path
  const sceneImagePath = `assets/thomas_midgley/scenes/scene_${activeScene.scene_id}.png`;
  const prevSceneImagePath = previousScene ? `assets/thomas_midgley/scenes/scene_${previousScene.scene_id}.png` : '';

  // Chemical Formula Overlay based on Act
  let chemicalFormula = '';
  let chemicalSub = '';
  if (activeScene.act === 1 || activeScene.act === 2 || activeScene.act === 3) {
    chemicalFormula = 'Pb(C₂H₅)₄';
    chemicalSub = 'TETRAETHYL LEAD [TEL] // CAS 78-00-2';
  } else if (activeScene.act === 4) {
    chemicalFormula = 'CCl₂F₂';
    chemicalSub = 'DICHLORODIFLUOROMETHANE [FREON-12]';
  } else if (activeScene.act === 5) {
    chemicalFormula = 'Cl + O₃ → ClO + O₂';
    chemicalSub = '1:100,000 CATALYTIC OZONE DESTRUCTION';
  }

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        backgroundColor: '#090d16',
        overflow: 'hidden',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        color: '#f8fafc',
      }}
    >
      {/* 0. MASTER AUDIO TRACK (Mastered Voiceover) */}
      <Audio src={staticFile('assets/thomas_midgley/voiceover_mastered.wav')} />

      {/* 1. LAYERED BACKGROUND ARCHITECTURE */}
      <div
        style={{
          position: 'absolute',
          top: -200,
          left: -200,
          width: 900,
          height: 900,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.primary}22 0%, transparent 70%)`,
          opacity: glowPulse1,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -250,
          right: -250,
          width: 1100,
          height: 1100,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.subAccent}25 0%, transparent 70%)`,
          opacity: glowPulse2,
          pointerEvents: 'none',
        }}
      />

      {/* Engineering Precision Grid */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage: `linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                            linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px)`,
          backgroundSize: '80px 80px',
          opacity: 0.45,
          pointerEvents: 'none',
        }}
      />

      {/* 2. PREVIOUS SCENE CROSSFADE BUFFER */}
      {previousScene && sceneRelativeFrame < CROSSFADE_FRAMES && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            opacity: 1 - sceneEntranceOpacity,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Img
            src={staticFile(prevSceneImagePath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
            }}
          />
        </div>
      )}

      {/* 3. ACTIVE SCENE ARTWORK WITH SMOOTH KEN BURNS */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          opacity: sceneEntranceOpacity,
          transform: `scale(${kbScale}) translate(${panX}px, ${panY}px)`,
          transformOrigin: 'center center',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Img
          src={staticFile(sceneImagePath)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </div>

      {/* 4. DRAMATIC FLASH TRANSITION BURST */}
      {flashOpacity > 0 && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            backgroundColor: flashColor,
            opacity: flashOpacity,
            mixBlendMode: 'screen',
            pointerEvents: 'none',
            zIndex: 10,
          }}
        />
      )}

      {/* 5. CINEMATIC VIGNETTE */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(circle at center, transparent 55%, rgba(6, 9, 15, 0.75) 100%)',
          pointerEvents: 'none',
        }}
      />

      {/* 6. TOP TELEMETRY HUD BAR */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 60,
          right: 60,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 20,
        }}
      >
        {/* Left: Channel Brand & Act Badge */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div
            style={{
              padding: '6px 14px',
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              backdropFilter: 'blur(12px)',
              border: `1px solid ${theme.primary}55`,
              borderRadius: 6,
              fontSize: 13,
              fontWeight: 800,
              letterSpacing: '0.12em',
              color: theme.accent,
              boxShadow: `0 0 16px ${theme.primary}33`,
            }}
          >
            ● THE DOSSIER ZERO // FILE #04
          </div>

          <div
            style={{
              padding: '6px 14px',
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              backdropFilter: 'blur(12px)',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              borderRadius: 6,
              fontSize: 13,
              fontWeight: 700,
              letterSpacing: '0.08em',
              color: '#e2e8f0',
            }}
          >
            {activeScene.act_title}
          </div>
        </div>

        {/* Right: Broadcast Timecode & Scene Index */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div
            style={{
              padding: '6px 14px',
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              backdropFilter: 'blur(12px)',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              borderRadius: 6,
              fontSize: 13,
              fontFamily: 'JetBrains Mono, monospace',
              fontWeight: 700,
              letterSpacing: '0.05em',
              color: '#94a3b8',
            }}
          >
            SCENE {activeScene.scene_id} / 32
          </div>

          <div
            style={{
              padding: '6px 14px',
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              backdropFilter: 'blur(12px)',
              border: `1px solid ${theme.accent}66`,
              borderRadius: 6,
              fontSize: 13,
              fontFamily: 'JetBrains Mono, monospace',
              fontWeight: 800,
              letterSpacing: '0.05em',
              color: '#f8fafc',
              boxShadow: `0 0 14px ${theme.accent}22`,
            }}
          >
            {timecode}
          </div>
        </div>
      </div>

      {/* 7. FLOATING CHEMICAL FORMULA CARD (TOP RIGHT) */}
      {chemicalFormula && (
        <div
          style={{
            position: 'absolute',
            top: 96,
            right: 60,
            padding: '12px 20px',
            backgroundColor: 'rgba(11, 17, 32, 0.85)',
            backdropFilter: 'blur(16px)',
            border: `1px solid ${theme.primary}44`,
            borderRadius: 8,
            boxShadow: `0 8px 32px rgba(0, 0, 0, 0.6), 0 0 16px ${theme.primary}22`,
            zIndex: 20,
            maxWidth: 360,
          }}
        >
          <div
            style={{
              fontSize: 22,
              fontWeight: 900,
              letterSpacing: '0.06em',
              color: theme.accent,
              fontFamily: 'JetBrains Mono, monospace',
            }}
          >
            {chemicalFormula}
          </div>
          <div
            style={{
              fontSize: 11,
              fontWeight: 700,
              letterSpacing: '0.08em',
              color: '#94a3b8',
              marginTop: 4,
            }}
          >
            {chemicalSub}
          </div>
        </div>
      )}

      {/* 8. DYNAMIC SCIENTIFIC TELEMETRY PANEL (BOTTOM LEFT) */}
      <div
        style={{
          position: 'absolute',
          bottom: 50,
          left: 60,
          display: 'flex',
          flexDirection: 'column',
          gap: 12,
          zIndex: 20,
        }}
      >
        {/* Era & Location Tag */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <div
            style={{
              padding: '6px 12px',
              backgroundColor: theme.primary,
              borderRadius: 4,
              fontSize: 11,
              fontWeight: 900,
              letterSpacing: '0.12em',
              color: '#090d16',
            }}
          >
            {currentEra.label}
          </div>
          <div
            style={{
              fontSize: 12,
              fontWeight: 800,
              letterSpacing: '0.1em',
              color: '#cbd5e1',
            }}
          >
            {currentEra.location}
          </div>
        </div>

        {/* Real-time Telemetry Metrics Card */}
        <div
          style={{
            display: 'flex',
            gap: 24,
            padding: '14px 22px',
            backgroundColor: 'rgba(11, 17, 32, 0.88)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            borderRadius: 8,
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.6)',
          }}
        >
          {/* Blood Lead Metric */}
          <div>
            <div style={{ fontSize: 10, fontWeight: 700, color: '#64748b', letterSpacing: '0.1em' }}>
              BLOOD LEAD LEVEL
            </div>
            <div
              style={{
                fontSize: 18,
                fontWeight: 900,
                fontFamily: 'JetBrains Mono, monospace',
                color: '#ef4444',
                marginTop: 2,
              }}
            >
              {activeScene.telemetry?.lead_blood || currentEra.leadBlood}
            </div>
          </div>

          <div style={{ width: 1, backgroundColor: 'rgba(255, 255, 255, 0.1)' }} />

          {/* Ozone Layer Metric */}
          <div>
            <div style={{ fontSize: 10, fontWeight: 700, color: '#64748b', letterSpacing: '0.1em' }}>
              OZONE INTEGRITY
            </div>
            <div
              style={{
                fontSize: 18,
                fontWeight: 900,
                fontFamily: 'JetBrains Mono, monospace',
                color: '#06b6d4',
                marginTop: 2,
              }}
            >
              {activeScene.telemetry?.ozone || currentEra.ozoneLevel}
            </div>
          </div>

          <div style={{ width: 1, backgroundColor: 'rgba(255, 255, 255, 0.1)' }} />

          {/* Planetary Threat Level */}
          <div>
            <div style={{ fontSize: 10, fontWeight: 700, color: '#64748b', letterSpacing: '0.1em' }}>
              BIOSPHERE STATUS
            </div>
            <div
              style={{
                fontSize: 14,
                fontWeight: 900,
                color: currentEra.alertLevel === 'CATASTROPHIC' || currentEra.alertLevel === 'CRITICAL' ? '#ef4444' : theme.accent,
                letterSpacing: '0.08em',
                marginTop: 4,
              }}
            >
              {currentEra.condition}
            </div>
          </div>
        </div>
      </div>

      {/* 9. KINETIC HEADLINE & STORY HOOK OVERLAY (CENTER TOP / HERO) */}
      <div
        style={{
          position: 'absolute',
          top: 105,
          left: 0,
          right: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          pointerEvents: 'none',
          zIndex: 25,
          opacity: headlineOpacity,
          transform: `translateY(${(1 - headlineEntrance) * -24}px)`,
        }}
      >
        <div
          style={{
            padding: '8px 32px',
            backgroundColor: 'rgba(9, 13, 22, 0.72)',
            backdropFilter: 'blur(12px)',
            borderRadius: 12,
            border: `1px solid ${theme.primary}44`,
            fontSize: 42,
            fontWeight: 900,
            textTransform: 'uppercase',
            letterSpacing: '0.06em',
            color: '#ffffff',
            textShadow: `0 4px 24px rgba(0, 0, 0, 0.9), 0 0 24px ${theme.primary}55`,
            textAlign: 'center',
            maxWidth: 1400,
            lineHeight: 1.15,
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.5)',
          }}
        >
          {activeScene.kinetic_hook_headline}
        </div>
      </div>

      {/* 10. BOTTOM PROGRESS BAR */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 5,
          backgroundColor: 'rgba(15, 23, 42, 0.8)',
          zIndex: 30,
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progressPercent}%`,
            background: `linear-gradient(to right, ${theme.primary}, ${theme.accent})`,
            boxShadow: `0 0 12px ${theme.accent}`,
          }}
        />
      </div>
    </div>
  );
};
