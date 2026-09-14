import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export interface HandDrawnAnnotationProps {
  type: 'circle' | 'arrow' | 'callout' | 'cross';
  x: number;
  y: number;
  width?: number;
  height?: number;
  text?: string;
  color?: string;
  startFrame?: number;
}

export const HandDrawnAnnotation: React.FC<HandDrawnAnnotationProps> = ({
  type,
  x,
  y,
  width = 220,
  height = 140,
  text,
  color = '#f59e0b',
  startFrame = 0,
}) => {
  const frame = useCurrentFrame();
  const relFrame = Math.max(0, frame - startFrame);

  // Draw-on progress (0 to 1 over 20 frames)
  const drawProgress = interpolate(relFrame, [0, 20], [0, 1], {
    extrapolateRight: 'clamp',
  });

  if (frame < startFrame) return null;

  return (
    <div
      style={{
        position: 'absolute',
        left: `${x}px`,
        top: `${y}px`,
        pointerEvents: 'none',
        zIndex: 90,
      }}
    >
      <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`} fill="none">
        {type === 'circle' && (
          <ellipse
            cx={width / 2}
            cy={height / 2}
            rx={width / 2 - 8}
            ry={height / 2 - 8}
            stroke={color}
            strokeWidth="3.5"
            strokeLinecap="round"
            strokeDasharray={width * 3}
            strokeDashoffset={width * 3 * (1 - drawProgress)}
            transform={`rotate(-2, ${width / 2}, ${height / 2})`}
          />
        )}

        {type === 'cross' && (
          <g>
            <line
              x1="15"
              y1="15"
              x2={15 + (width - 30) * drawProgress}
              y2={15 + (height - 30) * drawProgress}
              stroke="#ef4444"
              strokeWidth="5"
              strokeLinecap="round"
            />
            {drawProgress > 0.5 && (
              <line
                x1={width - 15}
                y1="15"
                x2={width - 15 - (width - 30) * ((drawProgress - 0.5) * 2)}
                y2={15 + (height - 30) * ((drawProgress - 0.5) * 2)}
                stroke="#ef4444"
                strokeWidth="5"
                strokeLinecap="round"
              />
            )}
          </g>
        )}

        {type === 'arrow' && (
          <path
            d={`M 10 ${height / 2} Q ${width / 2} 10 ${width - 15} ${height / 2}`}
            stroke={color}
            strokeWidth="3"
            strokeLinecap="round"
            strokeDasharray={width * 2}
            strokeDashoffset={width * 2 * (1 - drawProgress)}
          />
        )}
      </svg>

      {/* Accompanying Handwritten Sticky Note / Text */}
      {text && drawProgress > 0.4 && (
        <div
          style={{
            position: 'absolute',
            top: `${height + 6}px`,
            left: '50%',
            transform: 'translateX(-50%)',
            backgroundColor: '#1e1b4b',
            border: `1.5px solid ${color}`,
            borderRadius: '6px',
            padding: '4px 10px',
            color: color,
            fontSize: '12px',
            fontWeight: 800,
            fontFamily: 'monospace',
            whiteSpace: 'nowrap',
            boxShadow: '0 6px 16px rgba(0,0,0,0.6)',
          }}
        >
          {text}
        </div>
      )}
    </div>
  );
};
