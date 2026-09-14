import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export type StickmanPose =
  | 'mobile_user'
  | 'desktop_user'
  | 'stressed_engineer'
  | 'happy_engineer'
  | 'hacker_bot'
  | 'junior_dev'
  | 'senior_coffee'
  | 'cto_crying';

export interface StickmanProps {
  pose?: StickmanPose;
  size?: number;
  label?: string;
  sublabel?: string;
  isStressed?: boolean;
}

export const StickmanActor: React.FC<StickmanProps> = ({
  pose = 'mobile_user',
  size = 180,
  label,
  sublabel,
  isStressed = false,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Subtle breathing / idle motion
  const bob = Math.sin(frame / 8) * 3;
  const panicShake = isStressed || pose === 'cto_crying' || pose === 'stressed_engineer' ? (Math.sin(frame * 1.8) * 4) : 0;

  // Spring entrance
  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        transform: `scale(${entrance}) translate(${panicShake}px, ${bob}px)`,
        transformOrigin: 'bottom center',
      }}
    >
      <svg
        width={size}
        height={size * 1.35}
        viewBox="0 0 100 135"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        style={{ filter: 'drop-shadow(0 10px 15px rgba(0,0,0,0.5))' }}
      >
        {/* Panic sweat drops / exclamation if stressed */}
        {(isStressed || pose === 'cto_crying' || pose === 'stressed_engineer') && (
          <g>
            <circle cx="50" cy="8" r="7" fill="#ef4444" />
            <text
              x="50"
              y="12"
              textAnchor="middle"
              fill="#ffffff"
              fontSize="10"
              fontWeight="900"
              fontFamily="sans-serif"
            >
              !
            </text>
            <path
              d="M 68 22 Q 72 20 74 25 Q 73 29 69 28 Z"
              fill="#38bdf8"
              opacity="0.8"
            />
          </g>
        )}

        {/* Head */}
        <circle
          cx="50"
          cy="32"
          r="14"
          fill="#0f172a"
          stroke="#f8fafc"
          strokeWidth="3.5"
        />

        {/* Junior Dev: Backwards Cap */}
        {pose === 'junior_dev' && (
          <g>
            <path d="M 36 28 Q 50 18 64 28 Z" fill="#ef4444" />
            <path d="M 64 28 L 74 26 L 72 30 Z" fill="#b91c1c" />
          </g>
        )}

        {/* Face Expressions */}
        {pose === 'stressed_engineer' || isStressed ? (
          <g>
            <line x1="43" y1="28" x2="47" y2="30" stroke="#f8fafc" strokeWidth="2.5" strokeLinecap="round" />
            <line x1="57" y1="28" x2="53" y2="30" stroke="#f8fafc" strokeWidth="2.5" strokeLinecap="round" />
            <path d="M 44 38 Q 47 41 50 38 Q 53 35 56 38" stroke="#ef4444" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          </g>
        ) : pose === 'cto_crying' ? (
          <g>
            {/* Crying eyes with tears streaming */}
            <circle cx="44" cy="29" r="3" fill="#38bdf8" />
            <circle cx="56" cy="29" r="3" fill="#38bdf8" />
            <line x1="44" y1="32" x2="44" y2="44" stroke="#38bdf8" strokeWidth="2" strokeDasharray="2 2" />
            <line x1="56" y1="32" x2="56" y2="44" stroke="#38bdf8" strokeWidth="2" strokeDasharray="2 2" />
            {/* Screaming O mouth */}
            <ellipse cx="50" cy="38" rx="4" ry="5" fill="#ef4444" />
          </g>
        ) : pose === 'hacker_bot' ? (
          <g>
            <rect x="40" y="27" width="20" height="7" rx="2" fill="#22c55e" />
            <line x1="40" y1="30" x2="60" y2="30" stroke="#000" strokeWidth="1.5" />
            <path d="M 46 40 Q 52 42 56 39" stroke="#f8fafc" strokeWidth="2" fill="none" strokeLinecap="round" />
          </g>
        ) : pose === 'senior_coffee' ? (
          <g>
            {/* Chill smug smile */}
            <circle cx="45" cy="29" r="2" fill="#34d399" />
            <circle cx="55" cy="29" r="2" fill="#34d399" />
            <path d="M 45 36 Q 52 42 57 37" stroke="#34d399" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          </g>
        ) : (
          <g>
            <circle cx="45" cy="30" r="2" fill="#38bdf8" />
            <circle cx="55" cy="30" r="2" fill="#38bdf8" />
            <path d="M 45 37 Q 50 41 55 37" stroke="#f8fafc" strokeWidth="2.2" fill="none" strokeLinecap="round" />
          </g>
        )}

        {/* Spine / Torso */}
        <line x1="50" y1="46" x2="50" y2="82" stroke="#f8fafc" strokeWidth="3.5" strokeLinecap="round" />

        {/* Arms and Props based on Pose */}
        {pose === 'mobile_user' && (
          <g>
            <line x1="50" y1="54" x2="38" y2="65" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="38" y1="65" x2="48" y2="68" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="50" y1="54" x2="60" y2="64" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="60" y1="64" x2="52" y2="68" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <rect x="47" y="60" width="9" height="15" rx="1.5" fill="#1e293b" stroke="#38bdf8" strokeWidth="1.5" />
            <rect x="48.5" y="62" width="6" height="10" rx="1" fill="#38bdf8" opacity="0.8" />
          </g>
        )}

        {pose === 'senior_coffee' && (
          <g>
            {/* Left arm relaxed */}
            <line x1="50" y1="54" x2="34" y2="66" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="34" y1="66" x2="36" y2="78" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            {/* Right arm holding coffee mug */}
            <line x1="50" y1="54" x2="64" y2="62" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="64" y1="62" x2="68" y2="52" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            {/* Coffee Mug */}
            <rect x="66" y="46" width="10" height="12" rx="2" fill="#334155" stroke="#f59e0b" strokeWidth="1.5" />
            <path d="M 76 49 C 79 49 79 55 76 55" fill="none" stroke="#f59e0b" strokeWidth="1.5" />
            {/* Steam */}
            <path d="M 68 43 Q 70 40 68 37" fill="none" stroke="#f8fafc" opacity="0.6" strokeWidth="1" />
            <path d="M 73 43 Q 75 40 73 37" fill="none" stroke="#f8fafc" opacity="0.6" strokeWidth="1" />
          </g>
        )}

        {pose === 'junior_dev' && (
          <g>
            {/* Arms reaching to desk/keyboard */}
            <line x1="50" y1="54" x2="36" y2="64" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="36" y1="64" x2="44" y2="72" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="50" y1="54" x2="64" y2="64" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="64" y1="64" x2="56" y2="72" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            {/* Laptop */}
            <line x1="40" y1="73" x2="60" y2="73" stroke="#94a3b8" strokeWidth="2" strokeLinecap="round" />
            <line x1="42" y1="73" x2="46" y2="63" stroke="#38bdf8" strokeWidth="1.5" strokeLinecap="round" />
          </g>
        )}

        {(pose === 'stressed_engineer' || pose === 'cto_crying' || isStressed) && (
          <g>
            <line x1="50" y1="54" x2="32" y2="44" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="32" y1="44" x2="40" y2="30" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="50" y1="54" x2="68" y2="44" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="68" y1="44" x2="60" y2="30" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
          </g>
        )}

        {pose === 'happy_engineer' && (
          <g>
            <line x1="50" y1="54" x2="30" y2="40" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="30" y1="40" x2="24" y2="28" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="50" y1="54" x2="70" y2="40" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
            <line x1="70" y1="40" x2="76" y2="28" stroke="#f8fafc" strokeWidth="3.2" strokeLinecap="round" />
          </g>
        )}

        {/* Legs */}
        <line x1="50" y1="82" x2="36" y2="114" stroke="#f8fafc" strokeWidth="3.5" strokeLinecap="round" />
        <line x1="50" y1="82" x2="64" y2="114" stroke="#f8fafc" strokeWidth="3.5" strokeLinecap="round" />
        <line x1="36" y1="114" x2="28" y2="114" stroke="#f8fafc" strokeWidth="3.5" strokeLinecap="round" />
        <line x1="64" y1="114" x2="72" y2="114" stroke="#f8fafc" strokeWidth="3.5" strokeLinecap="round" />
      </svg>

      {/* Label Badge */}
      {label && (
        <div
          style={{
            marginTop: '8px',
            backgroundColor: isStressed || pose === 'cto_crying' ? '#7f1d1d' : '#1e293b',
            border: `1.5px solid ${isStressed || pose === 'cto_crying' ? '#ef4444' : '#38bdf8'}`,
            borderRadius: '6px',
            padding: '4px 10px',
            textAlign: 'center',
            boxShadow: '0 4px 12px rgba(0,0,0,0.5)',
          }}
        >
          <div
            style={{
              color: '#f8fafc',
              fontSize: '13px',
              fontWeight: 700,
              fontFamily: 'Inter, system-ui, sans-serif',
              letterSpacing: '0.04em',
              whiteSpace: 'nowrap',
            }}
          >
            {label}
          </div>
          {sublabel && (
            <div
              style={{
                color: isStressed || pose === 'cto_crying' ? '#fca5a5' : '#94a3b8',
                fontSize: '11px',
                fontWeight: 500,
                fontFamily: 'monospace',
                marginTop: '1px',
              }}
            >
              {sublabel}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
