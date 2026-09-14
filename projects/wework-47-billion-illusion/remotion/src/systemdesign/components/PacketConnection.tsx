import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

export interface PacketConnectionProps {
  from: { x: number; y: number };
  to: { x: number; y: number };
  label?: string;
  packetColor?: string;
  speedFrames?: number; // lower = faster
  protocol?: string;
  isOverloaded?: boolean;
}

export const PacketConnection: React.FC<PacketConnectionProps> = ({
  from,
  to,
  label,
  packetColor = '#38bdf8',
  speedFrames = 30,
  protocol,
  isOverloaded = false,
}) => {
  const frame = useCurrentFrame();

  // Calculate packet progress (0 to 1)
  const progress = (frame % speedFrames) / speedFrames;

  // Calculate mid-point control curve
  const midX = (from.x + to.x) / 2;
  const midY = (from.y + to.y) / 2;
  const curvature = (to.x - from.x) * 0.08;

  // Quadratic bezier coordinates
  const t = progress;
  const qx = midX;
  const qy = midY + curvature;

  const currentX = (1 - t) * (1 - t) * from.x + 2 * (1 - t) * t * qx + t * t * to.x;
  const currentY = (1 - t) * (1 - t) * from.y + 2 * (1 - t) * t * qy + t * t * to.y;

  const wireColor = isOverloaded ? '#ef4444' : '#334155';
  const effectivePacketColor = isOverloaded ? '#f87171' : packetColor;

  return (
    <svg
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        pointerEvents: 'none',
      }}
    >
      {/* Connection Wire */}
      <path
        d={`M ${from.x} ${from.y} Q ${qx} ${qy} ${to.x} ${to.y}`}
        fill="none"
        stroke={wireColor}
        strokeWidth={isOverloaded ? 3 : 2}
        strokeDasharray={isOverloaded ? '6 4' : 'none'}
      />

      {/* Target Dot */}
      <circle cx={to.x} cy={to.y} r={4} fill={wireColor} />

      {/* Animated Traveling Packet */}
      <circle
        cx={currentX}
        cy={currentY}
        r={isOverloaded ? 7 : 5}
        fill={effectivePacketColor}
      />

      {/* Second packet staggered if high traffic */}
      {speedFrames <= 20 && (
        <circle
          cx={
            (1 - ((progress + 0.5) % 1)) * (1 - ((progress + 0.5) % 1)) * from.x +
            2 * (1 - ((progress + 0.5) % 1)) * ((progress + 0.5) % 1) * qx +
            ((progress + 0.5) % 1) * ((progress + 0.5) % 1) * to.x
          }
          cy={
            (1 - ((progress + 0.5) % 1)) * (1 - ((progress + 0.5) % 1)) * from.y +
            2 * (1 - ((progress + 0.5) % 1)) * ((progress + 0.5) % 1) * qy +
            ((progress + 0.5) % 1) * ((progress + 0.5) % 1) * to.y
          }
          r={4}
          fill={effectivePacketColor}
          opacity={0.8}
        />
      )}

      {/* Protocol / Label Badge centered on wire */}
      {label && (
        <g transform={`translate(${qx}, ${qy - 14})`}>
          <rect
            x="-45"
            y="-10"
            width="90"
            height="20"
            rx="4"
            fill="#0f172a"
            stroke={wireColor}
            strokeWidth="1"
          />
          <text
            x="0"
            y="4"
            textAnchor="middle"
            fill={effectivePacketColor}
            fontSize="10"
            fontWeight="700"
            fontFamily="monospace"
          >
            {label}
          </text>
        </g>
      )}
    </svg>
  );
};
