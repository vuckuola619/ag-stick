import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

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
  width = 240,
  height = 150,
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
            strokeWidth="4"
            strokeLinecap="round"
            strokeDasharray={width * 3}
            strokeDashoffset={width * 3 * (1 - drawProgress)}
            transform={`rotate(-2, ${width / 2}, ${height / 2})`}
            style={{ filter: `drop-shadow(0 0 10px ${color})` }}
          />
        )}

        {type === 'cross' && (
          <g style={{ filter: 'drop-shadow(0 0 12px #ef4444)' }}>
            <line
              x1="20"
              y1="20"
              x2={20 + (width - 40) * drawProgress}
              y2={20 + (height - 40) * drawProgress}
              stroke="#ef4444"
              strokeWidth="6"
              strokeLinecap="round"
            />
            {drawProgress > 0.5 && (
              <line
                x1={width - 20}
                y1="20"
                x2={width - 20 - (width - 40) * ((drawProgress - 0.5) * 2)}
                y2={20 + (height - 40) * ((drawProgress - 0.5) * 2)}
                stroke="#ef4444"
                strokeWidth="6"
                strokeLinecap="round"
              />
            )}
          </g>
        )}

        {type === 'arrow' && (
          <path
            d={`M 10 ${height / 2} Q ${width / 2} 10 ${width - 15} ${height / 2}`}
            stroke={color}
            strokeWidth="4"
            strokeLinecap="round"
            strokeDasharray={width * 2}
            strokeDashoffset={width * 2 * (1 - drawProgress)}
            style={{ filter: `drop-shadow(0 0 10px ${color})` }}
          />
        )}
      </svg>

      {/* Accompanying Handwritten Sticky Note / Text */}
      {text && drawProgress > 0.4 && (
        <div
          style={{
            position: 'absolute',
            top: `${height + 8}px`,
            left: '50%',
            transform: 'translateX(-50%)',
            backgroundColor: 'rgba(15, 23, 42, 0.96)',
            border: `2px solid ${color}`,
            borderRadius: '10px',
            padding: '8px 16px',
            color: color,
            fontSize: '18px',
            fontWeight: 900,
            fontFamily: 'Inter, system-ui, sans-serif',
            whiteSpace: 'nowrap',
            boxShadow: `0 8px 24px rgba(0,0,0,0.8), 0 0 15px ${color}55`,
            backdropFilter: 'blur(12px)',
          }}
        >
          {text}
        </div>
      )}
    </div>
  );
};
