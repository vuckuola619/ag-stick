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

// Import the generated synchronized manifest
import manifestData from '../../public/assets/white_phosphorus/manifest.json';

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
  audio_file: string;
  image_file: string;
  codex_image_prompt: string;
}

const SCENES: SceneItem[] = manifestData.scenes;
const TOTAL_FRAMES: number = manifestData.total_frames;

// Act Theme Palettes adhering strictly to Neon Rush 2D Color Rules
const ACT_THEMES: Record<number, {
  accent: string;
  subAccent: string;
  badge: string;
  actName: string;
  chemicalState: string;
}> = {
  1: {
    accent: '#00FF66', // Toxic Phosphor Green
    subAccent: '#FFAA00', // Amber Urine / Hearth Glow
    badge: 'ACT I: THE CELLAR ALCHEMIST',
    actName: 'HAMBURG, 1669 — ELEMENT 15 DISCOVERY',
    chemicalState: 'DISCOVERY: PHOSPHORUS MIRABILIS',
  },
  2: {
    accent: '#FFE600', // Flame Warning Yellow
    subAccent: '#FF6B00', // Hazard Orange
    badge: 'ACT II: THE ELEMENT THAT BREATHES FIRE',
    actName: 'P₄ TETRAHEDRAL CHEMILUMINESCENCE',
    chemicalState: 'SPONTANEOUS IGNITION: 30°C / 86°F',
  },
  3: {
    accent: '#00FF66', // Sickly Green Necrosis
    subAccent: '#00E5FF', // Ghost Glow Cyan
    badge: 'ACT III: THE VICTORIAN NIGHTMARE',
    actName: 'LONDON 1888 — THE MATCHGIRLS STRIKE',
    chemicalState: 'PATHOLOGY: PHOSSY JAW NECROSIS',
  },
  4: {
    accent: '#00E5FF', // Electric Cyan / DNA Backbone
    subAccent: '#FFE600', // Golden Wheat / Fertilizer
    badge: 'ACT IV: THE WEAPON & THE MIRACLE',
    actName: 'GREEN REVOLUTION & THE RECYCLING LOOP',
    chemicalState: 'BIOLOGY: DNA & ATP ENERGY CURRENCY',
  },
};

export const WhitePhosphorus10MinComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Active scene determination based on frame ranges
  let activeScene = SCENES[0];
  for (let i = 0; i < SCENES.length; i++) {
    if (frame >= SCENES[i].start_frame) {
      activeScene = SCENES[i];
    }
  }

  const theme = ACT_THEMES[activeScene.act] || ACT_THEMES[1];
  const sceneRelativeFrame = Math.max(0, frame - activeScene.start_frame);

  // 1. Kinetic Headline Entrance Spring
  const headlineEntrance = spring({
    frame: sceneRelativeFrame,
    fps,
    config: { damping: 13, stiffness: 120, mass: 0.7 },
  });

  const headlineOpacity = interpolate(
    sceneRelativeFrame,
    [0, 10, activeScene.duration_frames - 15, activeScene.duration_frames],
    [0, 1, 1, 0.85],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 2. Living Stickman Puppet Breathing & Camera Crawl
  // Ken Burns subtle scale: 1.00 -> 1.055
  const kbScale = interpolate(
    sceneRelativeFrame,
    [0, activeScene.duration_frames],
    [1.0, 1.055],
    { extrapolateRight: 'clamp' }
  );
  
  // Living puppet subtle breathing scale (0.985 - 1.015)
  const breathingScale = 1.0 + Math.sin(frame / 26) * 0.012;
  
  // Floating tilt (-1.2° to +1.2°)
  const floatingTilt = Math.sin(frame / 42) * 1.1;
  
  // Slow cinematic pan
  const panX = Math.sin((frame + Number(activeScene.scene_id) * 75) / 85) * 12;
  const panY = Math.cos((frame + Number(activeScene.scene_id) * 75) / 105) * 7;

  // 3. Ambient Volumetric Glow Breathing Pulses
  const glowPulse1 = 0.45 + 0.15 * Math.sin(frame / 35);
  const glowPulse2 = 0.35 + 0.12 * Math.cos(frame / 48);

  // 4. Broadcast Timecode Calculation
  const totalSec = frame / fps;
  const tcH = Math.floor(totalSec / 3600);
  const tcM = Math.floor((totalSec % 3600) / 60);
  const tcS = Math.floor(totalSec % 60);
  const tcF = frame % fps;
  const timecode = `${String(tcH).padStart(2, '0')}:${String(tcM).padStart(2, '0')}:${String(tcS).padStart(2, '0')}:${String(tcF).padStart(2, '0')}`;

  // Timeline Progress percentage
  const progressPercent = Math.min(100, (frame / TOTAL_FRAMES) * 100);

  // Scene image path
  const sceneImagePath = `assets/white_phosphorus/scenes/scene_${activeScene.scene_id}.png`;

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        backgroundColor: '#0c0e14',
        overflow: 'hidden',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        color: '#f8fafc',
      }}
    >
      {/* 0. MASTER AUDIO TRACK (Mastered Voiceover) */}
      <Audio src={staticFile('assets/white_phosphorus/voiceover_mastered.wav')} />

      {/* 1. LAYERED BACKGROUND ARCHITECTURE */}
      {/* Base Dark Charcoal / Slate Gradient with Paper Grain Vignette */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(ellipse at 50% 35%, #141824 0%, #0c0e14 75%, #05060a 100%)',
          zIndex: 1,
        }}
      />

      {/* Volumetric Breathing Neons */}
      <div
        style={{
          position: 'absolute',
          top: -150,
          left: '20%',
          width: 950,
          height: 650,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.accent}33 0%, transparent 70%)`,
          opacity: glowPulse1,
          filter: 'blur(90px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -120,
          right: '18%',
          width: 850,
          height: 550,
          borderRadius: '50%',
          background: `radial-gradient(circle, ${theme.subAccent}28 0%, transparent 70%)`,
          opacity: glowPulse2,
          filter: 'blur(95px)',
          zIndex: 2,
          pointerEvents: 'none',
        }}
      />

      {/* Engineering Scientific Dot Grid & Crosshairs */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px), linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px)',
          backgroundSize: '45px 45px, 225px 225px, 225px 225px',
          opacity: 0.65,
          zIndex: 3,
          pointerEvents: 'none',
        }}
      />

      {/* 2. VISUAL STAGE: 2D CARTOON STICKMAN SCENE */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          zIndex: 4,
          overflow: 'hidden',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            width: '100%',
            height: '100%',
            transform: `scale(${kbScale * breathingScale}) translate(${panX}px, ${panY}px) rotate(${floatingTilt}deg)`,
            transformOrigin: 'center center',
          }}
        >
          <Img
            src={staticFile(sceneImagePath)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              filter: 'contrast(1.06) brightness(1.02) saturate(1.05)',
            }}
          />
        </div>

        {/* Cinematic Vignette & Bottom Text Contrast Falloff */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background:
              'radial-gradient(circle at center, transparent 45%, rgba(10, 12, 18, 0.5) 85%, rgba(5, 6, 10, 0.85) 100%), linear-gradient(to top, rgba(5, 8, 17, 0.88) 0%, rgba(5, 8, 17, 0.4) 28%, transparent 60%)',
            pointerEvents: 'none',
          }}
        />
      </div>

      {/* 3. FLOATING AMBIENT PHOSPHOR DUST PARTICLES */}
      <div style={{ position: 'absolute', inset: 0, zIndex: 5, pointerEvents: 'none' }}>
        {[...Array(12)].map((_, i) => {
          const speed = 1.2 + (i % 4) * 0.4;
          const yPos = 1080 - (((frame * speed + i * 95) % 1150) - 50);
          const xPos = 80 + ((i * 157 + Math.sin(frame / 30 + i) * 35) % 1760);
          const pSize = 3 + (i % 3) * 2;
          const pOpacity = 0.2 + 0.35 * Math.sin(frame / 20 + i);
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: xPos,
                top: yPos,
                width: pSize,
                height: pSize,
                borderRadius: '50%',
                backgroundColor: i % 2 === 0 ? theme.accent : theme.subAccent,
                boxShadow: `0 0 ${pSize * 3}px ${theme.accent}`,
                opacity: pOpacity,
              }}
            />
          );
        })}
      </div>

      {/* 4. TOP GLASSMORPHIC TELEMETRY HUD */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 10,
        }}
      >
        {/* Left: Channel Badge & Active Act Tag */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '8px 18px',
              borderRadius: 10,
              background: 'rgba(15, 23, 42, 0.88)',
              border: `1px solid ${theme.accent}aa`,
              boxShadow: `0 0 16px ${theme.accent}33`,
              backdropFilter: 'blur(16px)',
            }}
          >
            <div
              style={{
                width: 10,
                height: 10,
                borderRadius: '50%',
                backgroundColor: theme.accent,
                boxShadow: `0 0 14px ${theme.accent}`,
              }}
            />
            <span
              style={{
                fontSize: 13,
                fontWeight: 900,
                letterSpacing: '0.14em',
                color: '#ffffff',
                textTransform: 'uppercase',
              }}
            >
              NEON ATOM DOCS
            </span>
          </div>

          <div
            style={{
              padding: '8px 16px',
              borderRadius: 10,
              background: 'rgba(30, 41, 59, 0.75)',
              border: '1px solid rgba(255, 255, 255, 0.14)',
              fontSize: 12,
              fontWeight: 700,
              letterSpacing: '0.08em',
              color: '#94a3b8',
              backdropFilter: 'blur(12px)',
            }}
          >
            {theme.actName}
          </div>
        </div>

        {/* Right: Element 15 Periodic Badge Card */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            padding: '6px 18px',
            borderRadius: 12,
            background: 'rgba(15, 23, 42, 0.88)',
            border: `1px solid ${theme.accent}88`,
            boxShadow: `0 8px 32px rgba(0, 0, 0, 0.5), 0 0 20px ${theme.accent}26`,
            backdropFilter: 'blur(16px)',
          }}
        >
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              width: 44,
              height: 44,
              borderRadius: 8,
              background: `linear-gradient(135deg, ${theme.accent} 0%, ${theme.subAccent} 100%)`,
              color: '#090d16',
              fontWeight: 900,
              fontSize: 21,
              lineHeight: 1,
            }}
          >
            P
            <span style={{ fontSize: 10, fontWeight: 800, marginTop: 1 }}>15</span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontSize: 13, fontWeight: 900, color: '#ffffff', letterSpacing: '0.05em' }}>
              PHOSPHORUS (WHITE / P₄)
            </span>
            <span style={{ fontSize: 11, color: '#94a3b8', fontFamily: 'monospace', letterSpacing: '0.02em' }}>
              MASS: 30.974 u | {theme.chemicalState}
            </span>
          </div>
        </div>
      </div>

      {/* 5. LARGE PUNCHY EDITORIAL HEADLINE (Strict Neon Rush Typography) */}
      <div
        style={{
          position: 'absolute',
          bottom: 64,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-end',
          zIndex: 10,
          opacity: headlineOpacity,
          transform: `translateY(${(1 - headlineEntrance) * 18}px)`,
        }}
      >
        {/* Left Column: Act Badge & Kinetic Hook Headline */}
        <div style={{ maxWidth: 1200 }}>
          {/* Act Badge Tag */}
          <div
            style={{
              display: 'inline-block',
              padding: '6px 16px',
              borderRadius: 6,
              background: `${theme.accent}26`,
              border: `1px solid ${theme.accent}aa`,
              fontSize: 13,
              fontWeight: 900,
              letterSpacing: '0.14em',
              color: theme.accent,
              marginBottom: 12,
              textTransform: 'uppercase',
            }}
          >
            {theme.badge}
          </div>

          {/* Kinetic Hook Headline */}
          <div
            style={{
              fontSize: 62,
              fontWeight: 900,
              fontFamily: '"Montserrat", "Arial Black", "Impact", sans-serif',
              letterSpacing: '0.01em',
              lineHeight: 1.04,
              color: '#FFE600',
              WebkitTextStroke: '3px #000000',
              textShadow:
                '3px 3px 0 #000000, -3px -3px 0 #000000, 3px -3px 0 #000000, -3px 3px 0 #000000, 0 8px 28px rgba(0, 0, 0, 0.95)',
              textTransform: 'uppercase',
            }}
          >
            {activeScene.kinetic_hook_headline.replace('’', "'").replace('°', '°')}
          </div>
        </div>

        {/* Right Column: Broadcast Timecode & Scene Index */}
        <div
          style={{
            padding: '12px 22px',
            borderRadius: 12,
            background: 'rgba(15, 23, 42, 0.92)',
            border: `1px solid rgba(255, 255, 255, 0.16)`,
            boxShadow: `0 8px 32px rgba(0, 0, 0, 0.5)`,
            backdropFilter: 'blur(20px)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'flex-end',
          }}
        >
          <span style={{ fontSize: 11, fontWeight: 700, color: '#94a3b8', letterSpacing: '0.12em', textTransform: 'uppercase' }}>
            SCENE {activeScene.scene_id} / 32
          </span>
          <span style={{ fontSize: 22, fontWeight: 900, color: theme.accent, fontFamily: 'monospace', marginTop: 2 }}>
            {timecode}
          </span>
        </div>
      </div>

      {/* 6. BOTTOM RUNNING TIMELINE PROGRESS SCRUBBER */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 6,
          backgroundColor: 'rgba(255, 255, 255, 0.08)',
          zIndex: 20,
        }}
      >
        <div
          style={{
            height: '100%',
            width: `${progressPercent}%`,
            background: `linear-gradient(to right, #00FF66, #FFE600, #FF6B00, #00E5FF)`,
            boxShadow: `0 0 12px ${theme.accent}`,
          }}
        />
      </div>
    </div>
  );
};
