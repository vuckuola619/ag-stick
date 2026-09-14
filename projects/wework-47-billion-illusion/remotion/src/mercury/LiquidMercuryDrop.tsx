import React from 'react';
import { useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';

export interface LiquidMercuryDropProps {
  startFrame?: number;
  scale?: number;
}

export const LiquidMercuryDrop: React.FC<LiquidMercuryDropProps> = ({
  startFrame = 0,
  scale = 1.0,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const relFrame = Math.max(0, frame - startFrame);

  // Droplet 1: main drop falling and splashing
  const drop1Y = interpolate(relFrame, [0, 25], [-120, 100], {
    extrapolateRight: 'clamp',
  });

  const splashSpring = spring({
    frame: Math.max(0, relFrame - 25),
    fps,
    config: { damping: 10, stiffness: 120 },
  });

  // Secondary droplets wobbling around
  const wobbleX = Math.sin(relFrame / 6) * 12;
  const wobbleY = Math.cos(relFrame / 7) * 8;

  // Droplet merging pulse
  const poolScale = 1 + splashSpring * 0.45;

  return (
    <div
      style={{
        position: 'relative',
        width: 400 * scale,
        height: 300 * scale,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <svg
        width={400 * scale}
        height={300 * scale}
        viewBox="0 0 400 300"
        style={{
          overflow: 'visible',
          filter: 'drop-shadow(0 15px 25px rgba(0,0,0,0.7))',
        }}
      >
        <defs>
          {/* Gooey Liquid Fusion Filter */}
          <filter id="mercuryGoo" x="-40%" y="-40%" width="180%" height="180%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="9" result="blur" />
            <feColorMatrix
              in="blur"
              mode="matrix"
              values="
                1 0 0 0 0
                0 1 0 0 0
                0 0 1 0 0
                0 0 0 19 -8"
              result="goo"
            />
            <feBlend in="SourceGraphic" in2="goo" />
          </filter>

          {/* Chrome Liquid Metallic Gradient */}
          <radialGradient id="chromeLiquid" cx="35%" cy="30%" r="65%">
            <stop offset="0%" stopColor="#ffffff" />
            <stop offset="25%" stopColor="#e2e8f0" />
            <stop offset="55%" stopColor="#94a3b8" />
            <stop offset="85%" stopColor="#475569" />
            <stop offset="100%" stopColor="#1e293b" />
          </radialGradient>

          {/* Specular Highlight Gloss */}
          <linearGradient id="specularGlow" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#ffffff" stopOpacity="0.9" />
            <stop offset="50%" stopColor="#cbd5e1" stopOpacity="0.4" />
            <stop offset="100%" stopColor="#64748b" stopOpacity="0.0" />
          </linearGradient>
        </defs>

        {/* Liquid Surface Goo Container */}
        <g filter="url(#mercuryGoo)">
          {/* Base Pool */}
          <ellipse
            cx="200"
            cy="210"
            rx={95 * poolScale}
            ry={28 * poolScale}
            fill="url(#chromeLiquid)"
          />

          {/* Droplet 1 (Falling) */}
          {relFrame < 60 && (
            <circle
              cx="200"
              cy={drop1Y}
              r={relFrame > 25 ? Math.max(0, 18 - (relFrame - 25)) : 18}
              fill="url(#chromeLiquid)"
            />
          )}

          {/* Splashing Micro-Beads */}
          {relFrame > 24 && (
            <>
              <circle
                cx={200 - 55 * splashSpring + wobbleX * 0.5}
                cy={205 - 25 * Math.sin(splashSpring * Math.PI)}
                r="14"
                fill="url(#chromeLiquid)"
              />
              <circle
                cx={200 + 62 * splashSpring - wobbleX * 0.4}
                cy={207 - 20 * Math.sin(splashSpring * Math.PI)}
                r="12"
                fill="url(#chromeLiquid)"
              />
              <circle
                cx={200 + wobbleX * 1.2}
                cy={195 - 40 * Math.sin(splashSpring * Math.PI)}
                r="10"
                fill="url(#chromeLiquid)"
              />
              <circle
                cx={200 - 85 * splashSpring}
                cy="212"
                r="9"
                fill="url(#chromeLiquid)"
              />
              <circle
                cx={200 + 90 * splashSpring}
                cy="213"
                r="8"
                fill="url(#chromeLiquid)"
              />
            </>
          )}
        </g>

        {/* High-Gloss Mirror Highlight Overlays */}
        <g pointerEvents="none">
          <ellipse
            cx="175"
            cy="200"
            rx={50 * poolScale}
            ry={9 * poolScale}
            fill="url(#specularGlow)"
          />
          <circle
            cx="155"
            cy="197"
            r="4"
            fill="#ffffff"
            opacity="0.95"
            filter="drop-shadow(0 0 4px #ffffff)"
          />
        </g>
      </svg>
    </div>
  );
};
