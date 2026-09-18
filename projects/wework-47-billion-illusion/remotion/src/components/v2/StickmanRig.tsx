import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export type CharacterId =
  | 'CHAR_SLOTIN'
  | 'CHAR_DAGHLIAN'
  | 'CHAR_RAEMER_SCHREIBER'
  | 'CHAR_GUARD_BARRERA'
  | 'CHAR_GENERIC_SCIENTIST';

export type PoseType =
  | 'idle'
  | 'confident'
  | 'holding_screwdriver'
  | 'stacking_brick'
  | 'shocked_recoil'
  | 'turning_away'
  | 'standing_guard'
  | 'observing';

export type ExpressionType =
  | 'neutral'
  | 'confident'
  | 'focused'
  | 'worried'
  | 'shocked'
  | 'terrified'
  | 'alarmed';

export interface StickmanRigProps {
  characterId: CharacterId;
  pose?: PoseType;
  expression?: ExpressionType;
  size?: number;
  x?: number;
  y?: number;
  scale?: number;
  flipX?: boolean;
  isTrembling?: boolean;
  showSweat?: boolean;
}

export const StickmanRig: React.FC<StickmanRigProps> = ({
  characterId,
  pose = 'idle',
  expression = 'neutral',
  size = 280,
  x = 0,
  y = 0,
  scale = 1.0,
  flipX = false,
  isTrembling = false,
  showSweat = false,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Subtle natural breathing / idle bob
  const idleBob = Math.sin(frame / 7) * 3;
  // High tension panic micro-shake
  const trembleOffset = isTrembling ? (Math.sin(frame * 2.8) * 3.5) : 0;

  // Spring entrance or posture shift
  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });

  // Unique character visual identities
  const isSlotin = characterId === 'CHAR_SLOTIN';
  const isDaghlian = characterId === 'CHAR_DAGHLIAN';
  const isSchreiber = characterId === 'CHAR_RAEMER_SCHREIBER';
  const isGuard = characterId === 'CHAR_GUARD_BARRERA';

  return (
    <div
      style={{
        position: 'absolute',
        left: '50%',
        top: '50%',
        transform: `translate(-50%, -50%) translate(${x + trembleOffset}px, ${y + idleBob}px) scale(${scale * (flipX ? -1 : 1)}, ${scale})`,
        transformOrigin: 'bottom center',
        zIndex: 10,
        pointerEvents: 'none',
      }}
    >
      <svg
        width={size}
        height={size * 1.5}
        viewBox="0 0 160 240"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        style={{ filter: 'drop-shadow(0 12px 18px rgba(0,0,0,0.6))' }}
      >
        {/* Panic Sweat Drops */}
        {(showSweat || expression === 'terrified') && (
          <g>
            <path
              d="M 104 42 Q 110 38 112 45 Q 110 52 105 50 Z"
              fill="#00E5FF"
              opacity="0.9"
            />
            {expression === 'terrified' && (
              <path
                d="M 54 40 Q 50 36 48 43 Q 50 50 55 48 Z"
                fill="#00E5FF"
                opacity="0.8"
              />
            )}
          </g>
        )}

        {/* 1. Torso / Costume Layer */}
        {isSlotin ? (
          // Slotin's rolled-up blue denim shirt with red tie
          <g>
            <path d="M 80 88 L 80 155" stroke="#0b0d13" strokeWidth="10" strokeLinecap="round" />
            {/* Denim Shirt vest */}
            <path d="M 68 96 L 92 96 L 88 145 L 72 145 Z" fill="#2563EB" stroke="#0b0d13" strokeWidth="4" />
            {/* Red necktie */}
            <path d="M 80 94 L 83 125 L 80 135 L 77 125 Z" fill="#DC2626" />
          </g>
        ) : isDaghlian ? (
          // Daghlian's formal white shirt with dark tie
          <g>
            <path d="M 80 88 L 80 155" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <path d="M 70 96 L 90 96 L 86 142 L 74 142 Z" fill="#F8FAFC" stroke="#0b0d13" strokeWidth="4" />
            <path d="M 80 94 L 82 125 L 80 132 L 78 125 Z" fill="#1E293B" />
          </g>
        ) : isSchreiber ? (
          // Schreiber's white lab coat over dark shirt
          <g>
            <path d="M 80 88 L 80 155" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <path d="M 66 94 L 94 94 L 92 152 L 68 152 Z" fill="#F1F5F9" stroke="#0b0d13" strokeWidth="4" />
            <path d="M 80 94 L 80 148" stroke="#CBD5E1" strokeWidth="2" strokeDasharray="3 3" />
          </g>
        ) : isGuard ? (
          // Guard's military olive uniform with duty belt
          <g>
            <path d="M 80 88 L 80 155" stroke="#0b0d13" strokeWidth="10" strokeLinecap="round" />
            <path d="M 66 94 L 94 94 L 90 148 L 70 148 Z" fill="#4D7C0F" stroke="#0b0d13" strokeWidth="4" />
            <rect x="68" y="136" width="24" height="6" fill="#1F2937" stroke="#0b0d13" strokeWidth="2" />
          </g>
        ) : (
          // Standard Stickman Torso
          <line x1="80" y1="88" x2="80" y2="155" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
        )}

        {/* 2. Legs & Shoes Layer */}
        {pose === 'shocked_recoil' ? (
          <g>
            <line x1="80" y1="155" x2="55" y2="200" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <line x1="55" y1="200" x2="40" y2="228" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <line x1="80" y1="155" x2="105" y2="198" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <line x1="105" y1="198" x2="115" y2="228" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
          </g>
        ) : pose === 'standing_guard' ? (
          <g>
            <line x1="80" y1="155" x2="68" y2="225" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <line x1="80" y1="155" x2="92" y2="225" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
          </g>
        ) : (
          // Default standing legs
          <g>
            <line x1="80" y1="155" x2="62" y2="225" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
            <line x1="80" y1="155" x2="98" y2="225" stroke="#0b0d13" strokeWidth="9" strokeLinecap="round" />
          </g>
        )}

        {/* Slotin's distinctive Brown Cowboy Boots */}
        {isSlotin && (
          <g>
            <path d="M 52 222 L 64 222 L 66 230 L 48 230 Z" fill="#78350F" stroke="#0b0d13" strokeWidth="2.5" />
            <path d="M 88 222 L 100 222 L 106 230 L 86 230 Z" fill="#78350F" stroke="#0b0d13" strokeWidth="2.5" />
          </g>
        )}

        {/* 3. Arms & Hands Layer with Pose System */}
        {pose === 'holding_screwdriver' ? (
          <g>
            {/* Left arm: bracing on hip/table */}
            <line x1="74" y1="100" x2="45" y2="125" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="45" y1="125" x2="52" y2="152" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            {/* Right arm extending forward gripping screwdriver */}
            <line x1="86" y1="100" x2="115" y2="115" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="115" y1="115" x2="135" y2="128" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            {/* Hand node holding tool */}
            <circle cx="137" cy="130" r="5.5" fill="#ffffff" stroke="#0b0d13" strokeWidth="3" />
            {/* Screwdriver Prop Rendered in Hand */}
            <g transform="rotate(32 137 130)">
              {/* Yellow Handle */}
              <rect x="133" y="122" width="16" height="7" rx="2" fill="#FACC15" stroke="#0b0d13" strokeWidth="2" />
              {/* Steel Blade */}
              <rect x="149" y="124" width="22" height="3" fill="#94A3B8" stroke="#0b0d13" strokeWidth="1.5" />
              <polygon points="171,123 174,125.5 171,128" fill="#CBD5E1" />
            </g>
          </g>
        ) : pose === 'stacking_brick' ? (
          <g>
            {/* Both arms holding heavy tungsten carbide block */}
            <line x1="72" y1="100" x2="52" y2="120" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="52" y1="120" x2="68" y2="135" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="88" y1="100" x2="108" y2="120" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="108" y1="120" x2="92" y2="135" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            {/* Heavy Brick */}
            <rect x="65" y="132" width="30" height="15" rx="2" fill="#475569" stroke="#0b0d13" strokeWidth="3" />
            <text x="80" y="143" fontSize="7" fill="#F8FAFC" textAnchor="middle" fontWeight="bold">WC</text>
          </g>
        ) : pose === 'shocked_recoil' ? (
          <g>
            {/* Arms thrown backward in horror */}
            <line x1="72" y1="100" x2="42" y2="78" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="42" y1="78" x2="28" y2="60" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="88" y1="100" x2="118" y2="78" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="118" y1="78" x2="132" y2="60" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
          </g>
        ) : pose === 'turning_away' ? (
          <g>
            {/* Schreiber turning away with clipboard */}
            <line x1="72" y1="100" x2="50" y2="122" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="88" y1="100" x2="98" y2="126" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            {/* Clipboard in hand */}
            <rect x="42" y="118" width="16" height="22" rx="2" fill="#D97706" stroke="#0b0d13" strokeWidth="2.5" />
            <rect x="44" y="122" width="12" height="15" fill="#FFFFFF" />
          </g>
        ) : (
          // Idle / Confident arms
          <g>
            <line x1="74" y1="100" x2="52" y2="135" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
            <line x1="86" y1="100" x2="108" y2="135" stroke="#0b0d13" strokeWidth="8" strokeLinecap="round" />
          </g>
        )}

        {/* 4. Head Layer (Solid White Circular Head with Bold Outline) */}
        <circle
          cx="80"
          cy="52"
          r="26"
          fill="#ffffff"
          stroke="#0b0d13"
          strokeWidth="8"
        />

        {/* 5. Accessories: Glasses or Headwear */}
        {isDaghlian && (
          // Harry Daghlian's round spectacles
          <g>
            <circle cx="70" cy="50" r="7.5" fill="none" stroke="#0b0d13" strokeWidth="2.5" />
            <circle cx="90" cy="50" r="7.5" fill="none" stroke="#0b0d13" strokeWidth="2.5" />
            <line x1="77.5" y1="50" x2="82.5" y2="50" stroke="#0b0d13" strokeWidth="2" />
          </g>
        )}

        {isSchreiber && (
          // Raemer Schreiber's horn-rimmed glasses
          <g>
            <rect x="62" y="45" width="14" height="10" rx="2" fill="none" stroke="#0b0d13" strokeWidth="3" />
            <rect x="84" y="45" width="14" height="10" rx="2" fill="none" stroke="#0b0d13" strokeWidth="3" />
            <line x1="76" y1="48" x2="84" y2="48" stroke="#0b0d13" strokeWidth="2.5" />
          </g>
        )}

        {isGuard && (
          // Guard's Military Peaked Visor Cap
          <g>
            <path d="M 52 38 Q 80 20 108 38 Z" fill="#3F6212" stroke="#0b0d13" strokeWidth="3.5" />
            <path d="M 50 38 Q 80 44 110 38" stroke="#0b0d13" strokeWidth="5" strokeLinecap="round" />
            <circle cx="80" cy="30" r="3" fill="#FACC15" />
          </g>
        )}

        {/* 6. Facial Expressions (Eyes & Eyebrows & Mouth) */}
        {expression === 'confident' ? (
          <g>
            {/* Narrowed confident eyes */}
            <path d="M 68 49 Q 72 47 75 49" stroke="#0b0d13" strokeWidth="3.5" strokeLinecap="round" />
            <path d="M 85 49 Q 88 47 92 49" stroke="#0b0d13" strokeWidth="3.5" strokeLinecap="round" />
            {/* Thick arched confident brows */}
            <path d="M 66 43 Q 71 40 76 43" stroke="#0b0d13" strokeWidth="4" strokeLinecap="round" />
            <path d="M 84 43 Q 89 40 94 43" stroke="#0b0d13" strokeWidth="4" strokeLinecap="round" />
            {/* Smirk */}
            <path d="M 77 60 Q 82 63 86 60" stroke="#0b0d13" strokeWidth="3" strokeLinecap="round" />
          </g>
        ) : expression === 'worried' ? (
          <g>
            {/* Worried slanted eyes */}
            <circle cx="71" cy="52" r="3.5" fill="#0b0d13" />
            <circle cx="89" cy="52" r="3.5" fill="#0b0d13" />
            {/* Slanted inner brows */}
            <line x1="67" y1="44" x2="75" y2="47" stroke="#0b0d13" strokeWidth="3.5" strokeLinecap="round" />
            <line x1="93" y1="44" x2="85" y2="47" stroke="#0b0d13" strokeWidth="3.5" strokeLinecap="round" />
            {/* Wavy mouth */}
            <path d="M 74 63 Q 77 60 80 63 Q 83 66 86 63" stroke="#0b0d13" strokeWidth="2.5" strokeLinecap="round" />
          </g>
        ) : expression === 'shocked' || expression === 'terrified' ? (
          <g>
            {/* Oversized wide round horror eyes */}
            <circle cx="70" cy="49" r="6.5" fill="#ffffff" stroke="#0b0d13" strokeWidth="3" />
            <circle cx="70" cy="49" r="2.5" fill="#0b0d13" />
            <circle cx="90" cy="49" r="6.5" fill="#ffffff" stroke="#0b0d13" strokeWidth="3" />
            <circle cx="90" cy="49" r="2.5" fill="#0b0d13" />
            {/* Raised high brows */}
            <path d="M 64 38 Q 70 34 76 38" stroke="#0b0d13" strokeWidth="4" strokeLinecap="round" />
            <path d="M 84 38 Q 90 34 96 38" stroke="#0b0d13" strokeWidth="4" strokeLinecap="round" />
            {/* Gaping round mouth */}
            <ellipse cx="80" cy="62" rx="5" ry="7" fill="#0b0d13" />
          </g>
        ) : (
          // Default Neutral
          <g>
            <circle cx="72" cy="50" r="3.5" fill="#0b0d13" />
            <circle cx="88" cy="50" r="3.5" fill="#0b0d13" />
            <line x1="75" y1="62" x2="85" y2="62" stroke="#0b0d13" strokeWidth="2.5" strokeLinecap="round" />
          </g>
        )}
      </svg>
    </div>
  );
};
