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

import manifestData from '../../public/assets/goiania_caesium_137/manifest.json';

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
    radiation_cpm?: number;
    dose_rate?: string;
    status?: string;
    [key: string]: any;
  };
  audio_file: string;
  image_file: string;
  codex_image_prompt: string;
}

const SCENES: SceneItem[] = (manifestData.scenes as SceneItem[]) || [];

export const ACT_THEMES: Record<number, { primary: string; accent: string; glow: string }> = {
  1: { primary: '#00F0FF', accent: '#FFE600', glow: 'rgba(0, 240, 255, 0.4)' }, // The Breach (Electric Cyan)
  2: { primary: '#00D4FF', accent: '#00F0FF', glow: 'rgba(0, 212, 255, 0.5)' }, // Blue Glow (Cherenkov)
  3: { primary: '#FFE600', accent: '#FF5500', glow: 'rgba(255, 230, 0, 0.4)' }, // Carnival of Death (Hazard Gold)
  4: { primary: '#FF2A55', accent: '#FF5500', glow: 'rgba(255, 42, 85, 0.5)' },  // Heroic Commute (Crimson Alert)
  5: { primary: '#FF0033', accent: '#FFE600', glow: 'rgba(255, 0, 51, 0.6)' },   // Geiger Screams (Critical Red)
  6: { primary: '#00F0FF', accent: '#10B981', glow: 'rgba(16, 185, 129, 0.4)' },// 100,000 Stadium (Triage Emerald/Cyan)
  7: { primary: '#A855F7', accent: '#FF2A55', glow: 'rgba(168, 85, 247, 0.5)' },// Stone Riots & Lead Coffins (Violet Sarcophagus)
  8: { primary: '#FFE600', accent: '#00F0FF', glow: 'rgba(255, 230, 0, 0.4)' }, // 300-Year Tomb (Hazard Yellow / Dossier Zero)
};

export const GoianiaCaesium137MasterComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find currently active scene from manifest
  const activeSceneIndex = SCENES.findIndex(
    (s) => frame >= s.start_frame && frame <= s.end_frame
  );
  const activeScene: SceneItem = activeSceneIndex !== -1 ? SCENES[activeSceneIndex] : (SCENES[0] || {
    scene_id: '01',
    act: 1,
    act_title: 'ACT 1: THE ABANDONED CLINIC & THE BREACH',
    kinetic_hook_headline: 'THE FORGOTTEN VAULT',
    start_frame: 0,
    duration_frames: 500,
    end_frame: 500,
    audio_file: '',
    image_file: '',
  });

  const previousScene: SceneItem | null = activeSceneIndex > 0 ? SCENES[activeSceneIndex - 1] : null;

  // Frame relative to active scene start
  const sceneRelativeFrame = Math.max(0, frame - activeScene.start_frame);
  const sceneDuration = activeScene.duration_frames || 500;

  const theme = ACT_THEMES[activeScene.act] || ACT_THEMES[1];

  // 1. Kinetic Entrance Springs for Headline
  const headlineEntrance = spring({
    frame: sceneRelativeFrame,
    fps,
    config: { damping: 14, stiffness: 110, mass: 0.8 },
  });

  const headlineOpacity = interpolate(
    sceneRelativeFrame,
    [0, 12, sceneDuration - 15, sceneDuration],
    [0, 1, 1, 0.85],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 2. Ken Burns Drift (Alternating zoom-in and zoom-out with pan)
  const isEvenScene = activeSceneIndex % 2 === 0;
  const kbScale = interpolate(
    sceneRelativeFrame,
    [0, sceneDuration],
    isEvenScene ? [1.0, 1.05] : [1.05, 1.0],
    { extrapolateRight: 'clamp' }
  );
  const panX = interpolate(
    sceneRelativeFrame,
    [0, sceneDuration],
    isEvenScene ? [-8, 8] : [8, -8],
    { extrapolateRight: 'clamp' }
  );
  const panY = interpolate(
    sceneRelativeFrame,
    [0, sceneDuration],
    isEvenScene ? [-4, 4] : [4, -4],
    { extrapolateRight: 'clamp' }
  );

  // 3. Smooth Crossfade Dissolve (15 frames)
  const CROSSFADE_FRAMES = 15;
  const sceneEntranceOpacity = interpolate(
    sceneRelativeFrame,
    [0, CROSSFADE_FRAMES],
    [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // 4. Dramatic Flash Transitions on Critical Events
  let flashOpacity = 0;
  let flashColor = '#ffffff';

  if (activeScene.scene_id === '06') {
    // Capsule breached
    flashColor = '#00F0FF';
    flashOpacity = interpolate(sceneRelativeFrame, [0, 3, 12, 30], [0.9, 1.0, 0.4, 0.0], { extrapolateRight: 'clamp' });
  } else if (activeScene.scene_id === '08') {
    // Cherenkov glow observed
    flashColor = '#0066FF';
    flashOpacity = interpolate(sceneRelativeFrame, [0, 4, 15, 35], [0.85, 1.0, 0.5, 0.0], { extrapolateRight: 'clamp' });
  } else if (activeScene.scene_id === '17') {
    // Ingestion of Caesium
    flashColor = '#FFE600';
    flashOpacity = interpolate(sceneRelativeFrame, [0, 3, 10, 25], [0.8, 1.0, 0.35, 0.0], { extrapolateRight: 'clamp' });
  } else if (activeScene.scene_id === '26') {
    // Geiger needle pegged off scale
    flashColor = '#FF0033';
    flashOpacity = interpolate(sceneRelativeFrame, [0, 2, 8, 25], [0.9, 1.0, 0.6, 0.0], { extrapolateRight: 'clamp' });
  } else if (activeScene.scene_id === '39') {
    // Cemetery Riot
    flashColor = '#FFFFFF';
    flashOpacity = interpolate(sceneRelativeFrame, [0, 3, 12, 28], [0.75, 0.95, 0.3, 0.0], { extrapolateRight: 'clamp' });
  }

  // 5. Radiation Gauge Telemetry Simulation
  const baseCpm = activeScene.telemetry?.radiation_cpm || 100;
  const targetCpm = Math.min(999999, baseCpm);
  // Add realistic micro jitter
  const jitterSeed = Math.sin(frame * 0.4) * 0.08 + Math.cos(frame * 0.9) * 0.05;
  const displayCpm = Math.round(targetCpm * (1 + jitterSeed));
  const cpmString = displayCpm > 900000 ? 'MAX >999,999' : displayCpm.toLocaleString();

  const doseRate = activeScene.telemetry?.dose_rate || '0.15 uGy/h';
  const locationText = activeScene.telemetry?.location || 'GOIANIA, BRASIL';

  // Format Timecode
  const totalSeconds = Math.floor(frame / fps);
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  const timecodeString = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  // Radiation Alert Level
  let alertLabel = 'NORMAL';
  let alertColor = '#10B981';
  if (displayCpm > 500000 || targetCpm > 500000) {
    alertLabel = 'LETHAL';
    alertColor = '#FF0033';
  } else if (displayCpm > 100000 || targetCpm > 100000) {
    alertLabel = 'CRITICAL';
    alertColor = '#FF2A55';
  } else if (displayCpm > 10000 || targetCpm > 10000) {
    alertLabel = 'HAZARD';
    alertColor = '#FFE600';
  } else if (displayCpm > 1000 || targetCpm > 1000) {
    alertLabel = 'ELEVATED';
    alertColor = '#F59E0B';
  }

  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: '#0A0D14',
        position: 'relative',
        overflow: 'hidden',
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      }}
    >
      {/* 1. MASTER AUDIO TRACK */}
      <Audio
        src={staticFile('assets/goiania_caesium_137/voiceover_mastered.wav')}
        volume={1.0}
      />

      {/* 2. PREVIOUS SCENE CROSSFADE BUFFER */}
      {previousScene && sceneRelativeFrame < CROSSFADE_FRAMES && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            opacity: 1 - sceneEntranceOpacity,
            zIndex: 1,
          }}
        >
          <Img
            src={staticFile(previousScene.image_file)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
            }}
          />
        </div>
      )}

      {/* 3. ACTIVE SCENE IMAGE WITH KEN BURNS DRIFT */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          opacity: sceneEntranceOpacity,
          transform: `scale(${kbScale}) translate(${panX}px, ${panY}px)`,
          transformOrigin: 'center center',
          zIndex: 2,
        }}
      >
        <Img
          src={staticFile(activeScene.image_file)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </div>

      {/* 4. CINEMATIC COLOR GRADE & VIGNETTE OVERLAY */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(ellipse at center, rgba(10, 13, 20, 0.05) 0%, rgba(10, 13, 20, 0.45) 75%, rgba(5, 7, 10, 0.88) 100%)',
          pointerEvents: 'none',
          zIndex: 3,
        }}
      />

      {/* 5. SUBTERRANEAN SCANLINE GRID */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage: 'linear-gradient(rgba(0, 240, 255, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 240, 255, 0.02) 1px, transparent 1px)',
          backgroundSize: '48px 48px',
          pointerEvents: 'none',
          zIndex: 4,
        }}
      />

      {/* 6. DRAMATIC FLASH TRANSITIONS */}
      {flashOpacity > 0.01 && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            backgroundColor: flashColor,
            opacity: flashOpacity,
            pointerEvents: 'none',
            zIndex: 10,
          }}
        />
      )}

      {/* 7. TOP HUD HEADER BAR */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 5,
        }}
      >
        {/* Dossier Zero Case File Badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            background: 'rgba(10, 13, 20, 0.78)',
            backdropFilter: 'blur(12px)',
            border: '1px solid rgba(0, 240, 255, 0.35)',
            boxShadow: '0 8px 32px rgba(0, 240, 255, 0.15)',
            padding: '8px 18px',
            borderRadius: 8,
          }}
        >
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: '50%',
              backgroundColor: '#00F0FF',
              boxShadow: '0 0 12px #00F0FF',
            }}
          />
          <span
            style={{
              color: '#00F0FF',
              fontSize: 14,
              fontWeight: 800,
              letterSpacing: '2px',
              fontFamily: "'JetBrains Mono', monospace",
            }}
          >
            ● THE DOSSIER ZERO // FILE #05: CAESIUM-137
          </span>
          <span style={{ color: 'rgba(255, 255, 255, 0.35)' }}>|</span>
          <span
            style={{
              color: '#FFE600',
              fontSize: 13,
              fontWeight: 700,
              letterSpacing: '1.5px',
              fontFamily: "'JetBrains Mono', monospace",
            }}
          >
            IAEA 1988 COMPLIANT
          </span>
        </div>

        {/* Act & Timecode Badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 16,
            background: 'rgba(10, 13, 20, 0.78)',
            backdropFilter: 'blur(12px)',
            border: `1px solid ${theme.primary}55`,
            padding: '8px 20px',
            borderRadius: 8,
          }}
        >
          <span
            style={{
              color: theme.primary,
              fontSize: 13,
              fontWeight: 800,
              letterSpacing: '2px',
              fontFamily: "'JetBrains Mono', monospace",
            }}
          >
            ACT {String(activeScene.act).padStart(2, '0')} // SCENE {activeScene.scene_id}/48
          </span>
          <span style={{ color: 'rgba(255, 255, 255, 0.3)' }}>|</span>
          <span
            style={{
              color: '#ffffff',
              fontSize: 14,
              fontWeight: 700,
              letterSpacing: '1px',
              fontFamily: "'JetBrains Mono', monospace",
            }}
          >
            {timecodeString} [{frame}F]
          </span>
        </div>
      </div>

      {/* 8. BOTTOM LEFT: LIVE RADIATION TELEMETRY GAUGE */}
      <div
        style={{
          position: 'absolute',
          bottom: 40,
          left: 48,
          background: 'rgba(10, 13, 20, 0.88)',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          boxShadow: '0 12px 40px rgba(0, 0, 0, 0.6)',
          borderRadius: 12,
          padding: '16px 22px',
          width: 380,
          zIndex: 5,
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: 10,
            borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
            paddingBottom: 8,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <div
              style={{
                width: 8,
                height: 8,
                borderRadius: '50%',
                backgroundColor: alertColor,
                boxShadow: `0 0 10px ${alertColor}`,
              }}
            />
            <span
              style={{
                fontSize: 11,
                color: 'rgba(255, 255, 255, 0.6)',
                letterSpacing: '1.5px',
                fontWeight: 700,
                fontFamily: "'JetBrains Mono', monospace",
              }}
            >
              TELEMETRY: {locationText}
            </span>
          </div>
          <span
            style={{
              fontSize: 11,
              fontWeight: 900,
              color: alertColor,
              letterSpacing: '1px',
              fontFamily: "'JetBrains Mono', monospace",
              padding: '2px 6px',
              backgroundColor: `${alertColor}22`,
              borderRadius: 4,
            }}
          >
            STATUS: {alertLabel}
          </span>
        </div>

        {/* Readings Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14 }}>
          {/* Geiger CPM */}
          <div>
            <div
              style={{
                fontSize: 10,
                color: 'rgba(255, 255, 255, 0.45)',
                letterSpacing: '1px',
                fontFamily: "'JetBrains Mono', monospace",
                marginBottom: 2,
              }}
            >
              GEIGER CPM
            </div>
            <div
              style={{
                fontSize: 20,
                fontWeight: 900,
                color: alertColor,
                fontFamily: "'JetBrains Mono', monospace",
                letterSpacing: '0.5px',
              }}
            >
              {cpmString}
            </div>
          </div>

          {/* Dose Rate */}
          <div>
            <div
              style={{
                fontSize: 10,
                color: 'rgba(255, 255, 255, 0.45)',
                letterSpacing: '1px',
                fontFamily: "'JetBrains Mono', monospace",
                marginBottom: 2,
              }}
            >
              DOSE RATE
            </div>
            <div
              style={{
                fontSize: 18,
                fontWeight: 800,
                color: '#00F0FF',
                fontFamily: "'JetBrains Mono', monospace",
                letterSpacing: '0.5px',
              }}
            >
              {doseRate}
            </div>
          </div>
        </div>

        {/* Dynamic Activity Gauge Bar */}
        <div
          style={{
            marginTop: 12,
            width: '100%',
            height: 4,
            backgroundColor: 'rgba(255, 255, 255, 0.1)',
            borderRadius: 2,
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              width: `${Math.min(100, Math.max(8, (targetCpm / 1000000) * 100))}%`,
              height: '100%',
              backgroundColor: alertColor,
              boxShadow: `0 0 8px ${alertColor}`,
              transition: 'width 0.3s ease',
            }}
          />
        </div>
      </div>

      {/* 9. BOTTOM CENTER: KINETIC HOOK HEADLINE CARD */}
      <div
        style={{
          position: 'absolute',
          bottom: 40,
          left: 450,
          right: 48,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'flex-start',
          zIndex: 5,
        }}
      >
        <div
          style={{
            opacity: headlineOpacity,
            transform: `translateY(${interpolate(headlineEntrance, [0, 1], [24, 0])}px)`,
            background: 'rgba(10, 13, 20, 0.92)',
            backdropFilter: 'blur(20px)',
            border: `1px solid ${theme.primary}66`,
            borderLeft: `6px solid ${theme.primary}`,
            boxShadow: `0 16px 48px rgba(0, 0, 0, 0.7), 0 0 24px ${theme.glow}`,
            borderRadius: 10,
            padding: '16px 28px',
            maxWidth: 1100,
          }}
        >
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 12,
              marginBottom: 4,
            }}
          >
            <span
              style={{
                fontSize: 12,
                color: theme.primary,
                fontWeight: 900,
                letterSpacing: '2px',
                fontFamily: "'JetBrains Mono', monospace",
              }}
            >
              {activeScene.act_title}
            </span>
          </div>

          <div
            style={{
              color: '#ffffff',
              fontSize: 28,
              fontWeight: 900,
              letterSpacing: '1px',
              textTransform: 'uppercase',
              fontFamily: "'Inter', sans-serif",
              textShadow: '0 2px 10px rgba(0, 0, 0, 0.8)',
            }}
          >
            {activeScene.kinetic_hook_headline}
          </div>
        </div>
      </div>
    </div>
  );
};
