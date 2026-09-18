import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export interface ProceduralFXProps {
  effectType:
    | 'fission_multiplication_tree'
    | 'neutron_reflection_bounce'
    | 'blue_flash'
    | 'cyan_radiation_flood'
    | 'screwdrive_slip_drop'
    | 'none';
  intensity?: number;
  durationFrames: number;
  currentFrame?: number;
}

export const ProceduralFX: React.FC<ProceduralFXProps> = ({
  effectType,
  intensity = 1.0,
  durationFrames,
  currentFrame: customFrame,
}) => {
  const globalFrame = useCurrentFrame();
  const frame = customFrame !== undefined ? customFrame : globalFrame;
  const { fps } = useVideoConfig();

  if (effectType === 'blue_flash' || effectType === 'cyan_radiation_flood') {
    const flashOpacity = interpolate(
      frame,
      [0, 3, 14, durationFrames],
      [0.95 * intensity, 1.0 * intensity, 0.45, 0.0],
      { extrapolateRight: 'clamp' }
    );

    const radialScale = interpolate(
      frame,
      [0, durationFrames],
      [0.6, 2.4 * intensity],
      { extrapolateRight: 'clamp' }
    );

    return (
      <div
        style={{
          position: 'absolute',
          inset: 0,
          opacity: flashOpacity,
          pointerEvents: 'none',
          zIndex: 50,
          background: 'radial-gradient(circle, rgba(0, 229, 255, 0.95) 0%, rgba(0, 102, 255, 0.7) 40%, rgba(18, 20, 26, 0.9) 85%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          transform: `scale(${radialScale})`,
        }}
      >
        <svg width="100%" height="100%" viewBox="0 0 1920 1080">
          {/* Radial ionizing rays */}
          {Array.from({ length: 16 }).map((_, i) => {
            const angle = (i * 360) / 16;
            return (
              <line
                key={i}
                x1="960"
                y1="540"
                x2={960 + Math.cos((angle * Math.PI) / 180) * 1200}
                y2={540 + Math.sin((angle * Math.PI) / 180) * 1200}
                stroke="#FFFFFF"
                strokeWidth={frame % 2 === 0 ? '6' : '3'}
                opacity={0.8}
              />
            );
          })}
        </svg>
      </div>
    );
  }

  if (effectType === 'fission_multiplication_tree') {
    // 1 -> 2 -> 4 -> 8 particle cascade
    const progress = Math.min(1.0, frame / Math.max(1, durationFrames));
    const stage = Math.min(4, Math.floor(progress * 4.5)); // 0, 1, 2, 3, 4

    return (
      <div
        style={{
          position: 'absolute',
          inset: 0,
          pointerEvents: 'none',
          zIndex: 25,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <svg width="1200" height="700" viewBox="0 0 1200 700">
          {/* Generation 0 (Center Core) */}
          <circle cx="600" cy="350" r="32" fill="#94A3B8" stroke="#F8FAFC" strokeWidth="4" />
          <text x="600" y="356" fill="#0F172A" fontSize="14" fontWeight="bold" textAnchor="middle">Pu-239</text>

          {/* Generation 1 (2 Neutrons) */}
          {stage >= 1 && (
            <g>
              <line x1="600" y1="350" x2="480" y2="230" stroke="#00E5FF" strokeWidth="4" strokeDasharray="6 4" />
              <line x1="600" y1="350" x2="720" y2="230" stroke="#00E5FF" strokeWidth="4" strokeDasharray="6 4" />
              <circle cx="480" cy="230" r="9" fill="#FFE600" stroke="#0b0d13" strokeWidth="2" />
              <circle cx="720" cy="230" r="9" fill="#FFE600" stroke="#0b0d13" strokeWidth="2" />
            </g>
          )}

          {/* Generation 2 (4 Neutrons) */}
          {stage >= 2 && (
            <g>
              <line x1="480" y1="230" x2="400" y2="130" stroke="#00E5FF" strokeWidth="3" strokeDasharray="4 4" />
              <line x1="480" y1="230" x2="520" y2="130" stroke="#00E5FF" strokeWidth="3" strokeDasharray="4 4" />
              <line x1="720" y1="230" x2="680" y2="130" stroke="#00E5FF" strokeWidth="3" strokeDasharray="4 4" />
              <line x1="720" y1="230" x2="800" y2="130" stroke="#00E5FF" strokeWidth="3" strokeDasharray="4 4" />

              <circle cx="400" cy="130" r="7" fill="#FFE600" />
              <circle cx="520" cy="130" r="7" fill="#FFE600" />
              <circle cx="680" cy="130" r="7" fill="#FFE600" />
              <circle cx="800" cy="130" r="7" fill="#FFE600" />
            </g>
          )}

          {/* Generation 3 (8 Neutrons) */}
          {stage >= 3 && (
            <g>
              {[-140, -100, -60, -20, 20, 60, 100, 140].map((dx, idx) => (
                <circle
                  key={idx}
                  cx={600 + dx * 2.8}
                  cy={50 + (idx % 2) * 20}
                  r="6"
                  fill="#FF5500"
                  stroke="#FFE600"
                  strokeWidth="1.5"
                />
              ))}
            </g>
          )}
        </svg>
      </div>
    );
  }

  if (effectType === 'neutron_reflection_bounce') {
    const bounceProgress = Math.min(1.0, frame / Math.max(1, durationFrames));
    const neutronY = interpolate(bounceProgress, [0, 0.45, 1.0], [350, 190, 350]);
    const neutronX = interpolate(bounceProgress, [0, 0.45, 1.0], [580, 600, 620]);

    return (
      <div
        style={{
          position: 'absolute',
          inset: 0,
          pointerEvents: 'none',
          zIndex: 25,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <svg width="1200" height="700" viewBox="0 0 1200 700">
          {/* Top Beryllium Shell (Reflector Wall) */}
          <path
            d="M 450 190 A 150 150 0 0 1 750 190"
            stroke="#CBD5E1"
            strokeWidth="16"
            fill="none"
            strokeLinecap="round"
          />
          <text x="600" y="160" fill="#CBD5E1" fontSize="13" fontWeight="bold" textAnchor="middle">
            BERYLLIUM REFLECTOR WALL
          </text>

          {/* Plutonium Core */}
          <circle cx="600" cy="350" r="40" fill="#94A3B8" stroke="#F8FAFC" strokeWidth="4" />

          {/* Ricocheting Neutron particle */}
          <circle cx={neutronX} cy={neutronY} r="8" fill="#00E5FF" stroke="#FFFFFF" strokeWidth="2" />
          <path
            d={`M 580 350 Q 600 190 ${neutronX} ${neutronY}`}
            stroke="#00E5FF"
            strokeWidth="3"
            strokeDasharray="4 4"
            fill="none"
          />
        </svg>
      </div>
    );
  }

  return null;
};
