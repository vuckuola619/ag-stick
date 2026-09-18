import React from 'react';
import { useCurrentFrame, useVideoConfig, Img, staticFile } from 'remotion';
import { StickmanRig, CharacterId, PoseType, ExpressionType } from './StickmanRig';
import { CameraRig, CameraShotType, CameraMotionType } from './CameraRig';
import { ProceduralFX } from './ProceduralFX';

export interface BeatManifestItem {
  id: string;
  start_frame: number;
  duration_frames: number;
  duration_sec: number;
  visual_function: string;
  tier: string;
  tension: number;
  description: string;
  camera: {
    shot: CameraShotType;
    motion: CameraMotionType;
    strength: number;
  };
  characters: Array<{
    character_id: CharacterId;
    pose: PoseType;
    expression: ExpressionType;
    transform: {
      x: number;
      y: number;
      scale: number;
      flip_x?: boolean;
    };
  }>;
  fx: Array<{
    effect_type: string;
    intensity?: number;
  }>;
  text_overlay?: string;
  environment_id?: string;
}

export interface BeatTimelineMasterProps {
  beats: BeatManifestItem[];
  sceneTitle?: string;
  headline?: string;
}

export const BeatTimelineMaster: React.FC<BeatTimelineMasterProps> = ({
  beats,
  sceneTitle = 'INCIDENT 2: LOUIS SLOTIN & THE SCREWDRIVER',
  headline = 'ONE MILLIMETER SLIP',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Find active beat
  let activeBeatIndex = 0;
  for (let i = 0; i < beats.length; i++) {
    if (frame >= beats[i].start_frame) {
      activeBeatIndex = i;
    }
  }

  const activeBeat = beats[activeBeatIndex] || beats[0];
  const beatRelativeFrame = Math.max(0, frame - activeBeat.start_frame);
  const isBlackout = activeBeat.environment_id === 'full_black';

  return (
    <div
      style={{
        position: 'relative',
        width: '100%',
        height: '100%',
        backgroundColor: isBlackout ? '#000000' : '#12141A',
        overflow: 'hidden',
        fontFamily: 'Inter, Montserrat, sans-serif',
      }}
    >
      {/* 1. Camera Choreography Layer */}
      <CameraRig
        shot={activeBeat.camera.shot}
        motion={activeBeat.camera.motion}
        strength={activeBeat.camera.strength}
        durationFrames={activeBeat.duration_frames}
        currentFrame={beatRelativeFrame}
      >
        {/* Environment & 9Router Asset Layer */}
        {!isBlackout && (
          <>
            {activeBeat.id === '24c' ? (
              // Macro 9Router asset for Beat 24c (Screwdriver lip gap)
              <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
                <Img
                  src={staticFile('assets/demon_core/v2/macro_screwdriver_gap.png')}
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                  }}
                />
              </div>
            ) : activeBeat.id === '24h' ? (
              // Hero 9Router cinematic frame for Beat 24h (Cherenkov Blue Flash)
              <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
                <Img
                  src={staticFile('assets/demon_core/v2/hero_cherenkov_flash.png')}
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                  }}
                />
              </div>
            ) : (
              // 9Router Los Alamos Omega Lab Environment (Beats 24a, 24b, 24d, 24e, 24f, 24i)
              <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
                <Img
                  src={staticFile('assets/demon_core/v2/bg_omega_lab.png')}
                  style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    filter: 'brightness(0.75) contrast(1.15)',
                  }}
                />
                {/* Vignette & Workbench shadow to ground characters */}
                <div
                  style={{
                    position: 'absolute',
                    inset: 0,
                    background:
                      'radial-gradient(ellipse at 50% 65%, rgba(0,0,0,0.1) 0%, rgba(18,20,26,0.7) 80%)',
                  }}
                />
              </div>
            )}
          </>
        )}

        {/* Foreground Characters (active when not in pure macro/hero shot) */}
        {!isBlackout &&
          activeBeat.id !== '24c' &&
          activeBeat.id !== '24h' &&
          activeBeat.characters.map((char, idx) => (
            <StickmanRig
              key={`${char.character_id}-${idx}`}
              characterId={char.character_id}
              pose={char.pose}
              expression={char.expression}
              x={char.transform.x * 5}
              y={char.transform.y * 3 + 20}
              scale={char.transform.scale || 1.0}
              flipX={char.transform.flip_x}
              isTrembling={activeBeat.tension > 0.8}
            />
          ))}

        {/* Procedural FX (Neutrons / Flash / Cascades) */}
        {activeBeat.fx.map((fx, idx) => (
          <ProceduralFX
            key={idx}
            effectType={fx.effect_type as any}
            intensity={fx.intensity || 1.0}
            durationFrames={activeBeat.duration_frames}
            currentFrame={beatRelativeFrame}
          />
        ))}
      </CameraRig>

      {/* 2. Programmatic Titanium Telemetry HUD (Anti-Slop Overlay) */}
      <div
        style={{
          position: 'absolute',
          top: 36,
          left: 48,
          right: 48,
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          pointerEvents: 'none',
          zIndex: 60,
        }}
      >
        <div>
          <div
            style={{
              fontSize: 13,
              letterSpacing: '0.22em',
              color: '#00E5FF',
              fontWeight: 800,
              textTransform: 'uppercase',
              marginBottom: 4,
            }}
          >
            {sceneTitle}
          </div>
          <div
            style={{
              fontSize: 32,
              fontWeight: 900,
              color: '#F8FAFC',
              letterSpacing: '-0.02em',
              textShadow: '0 4px 12px rgba(0,0,0,0.8)',
            }}
          >
            {headline}
          </div>
        </div>

        {/* Dynamic Beat & Tension Telemetry */}
        <div
          style={{
            backgroundColor: 'rgba(18, 20, 26, 0.85)',
            backdropFilter: 'blur(12px)',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            borderRadius: 8,
            padding: '10px 18px',
            textAlign: 'right',
            boxShadow: '0 8px 24px rgba(0,0,0,0.6)',
          }}
        >
          <div style={{ fontSize: 11, color: '#94A3B8', fontFamily: 'JetBrains Mono, monospace' }}>
            BEAT <span style={{ color: '#FFE600', fontWeight: 'bold' }}>{activeBeat.id.toUpperCase()}</span> // {activeBeat.visual_function.toUpperCase()}
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
            <span style={{ fontSize: 11, color: '#94A3B8' }}>TENSION:</span>
            <div style={{ width: 80, height: 6, backgroundColor: '#334155', borderRadius: 3, overflow: 'hidden' }}>
              <div
                style={{
                  width: `${activeBeat.tension * 100}%`,
                  height: '100%',
                  backgroundColor: activeBeat.tension > 0.8 ? '#EF4444' : activeBeat.tension > 0.5 ? '#F59E0B' : '#00E5FF',
                  transition: 'width 0.2s ease',
                }}
              />
            </div>
            <span style={{ fontSize: 11, color: '#F8FAFC', fontFamily: 'JetBrains Mono, monospace' }}>
              {(activeBeat.tension * 100).toFixed(0)}%
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
