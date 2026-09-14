import React from 'react';
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export type TechDevRole =
  | 'junior_dev'
  | 'devops_oncall'
  | 'senior_architect'
  | 'cto_panic'
  | 'client_user';

export interface TechDevActorProps {
  role?: TechDevRole;
  size?: number;
  label?: string;
  sublabel?: string;
  isStressed?: boolean;
}

export const TechDevActor: React.FC<TechDevActorProps> = ({
  role = 'junior_dev',
  size = 320,
  label,
  sublabel,
  isStressed = false,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Organic Breathing Motion
  const breath = Math.sin(frame / 6) * 3;
  const headBob = Math.sin((frame + 2) / 6) * 2;

  // Stress & Panic Jitter
  const isPanic = isStressed || role === 'devops_oncall' || role === 'cto_panic';
  const jitterX = isPanic ? Math.sin(frame * 2.2) * 5 : 0;
  const jitterY = isPanic ? Math.cos(frame * 2.5) * 3 : 0;

  // Spring Entrance
  const entrance = spring({
    frame,
    fps,
    config: { damping: 13, stiffness: 120 },
  });

  // Natural Blinking Cycle
  const blinkCycle = frame % 80;
  const isBlinking = blinkCycle >= 74 && blinkCycle <= 78;
  const eyeHeight = isBlinking ? 0.12 : 1;

  // Typing Motion for Devs
  const leftHandTyping = Math.sin(frame * 1.6) * 6;
  const rightHandTyping = Math.cos(frame * 1.6) * 6;

  // Phone tapping motion for Client User
  const phoneTap = Math.sin(frame * 2.0) * 4;

  // Rising Coffee Steam Waves
  const steamPhase = (frame * 1.8) % 50;
  const steamCurve1 = Math.sin(frame / 5) * 8;
  const steamCurve2 = Math.cos(frame / 6) * 10;

  // Panicked Sweat Drop with Gravity
  const sweatPhase = (frame * 2.5) % 40;
  const sweatOpacity = interpolate(sweatPhase, [0, 8, 38], [0, 1, 0]);

  // CTO Escaping Money Physics
  const cashFly1 = (frame * 3) % 100;
  const cashFly2 = (frame * 3 + 50) % 100;

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        transform: `scale(${entrance}) translate(${jitterX}px, ${jitterY}px)`,
        transformOrigin: 'bottom center',
      }}
    >
      <svg
        width={size}
        height={size * 1.15}
        viewBox="0 0 240 270"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        style={{
          filter: isPanic
            ? 'drop-shadow(0 15px 30px rgba(239, 68, 68, 0.45))'
            : 'drop-shadow(0 20px 35px rgba(0, 0, 0, 0.7))',
        }}
      >
        <defs>
          {/* Natural Premium Studio Skin Tones */}
          <linearGradient id="studioSkin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#fed7aa" />
            <stop offset="100%" stopColor="#fdba74" />
          </linearGradient>
          <linearGradient id="studioSkinShadow" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#ea580c" stopOpacity="0.2" />
            <stop offset="100%" stopColor="#c2410c" stopOpacity="0.4" />
          </linearGradient>

          {/* Premium Clothing Gradients */}
          <linearGradient id="hoodieJuniorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#3b82f6" />
            <stop offset="100%" stopColor="#1d4ed8" />
          </linearGradient>
          <linearGradient id="hoodieOnCallGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#ef4444" />
            <stop offset="100%" stopColor="#991b1b" />
          </linearGradient>
          <linearGradient id="seniorOutfitGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#334155" />
            <stop offset="100%" stopColor="#0f172a" />
          </linearGradient>
          <linearGradient id="phoneGlow" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#38bdf8" />
            <stop offset="100%" stopColor="#0284c7" />
          </linearGradient>
        </defs>

        {/* -------------------------------------------------------------
            CLIENT USER VARIANT: Mobile Phone App User (No Desk!)
            ------------------------------------------------------------- */}
        {role === 'client_user' ? (
          <g transform={`translate(120, ${110 + breath})`}>
            {/* Pulsing WiFi/Signal Waves radiating from phone */}
            <circle cx="0" cy="40" r={35 + (frame % 30)} stroke="#38bdf8" strokeWidth="2" fill="none" opacity={interpolate(frame % 30, [0, 30], [0.8, 0])} />
            <circle cx="0" cy="40" r={20 + (frame % 30)} stroke="#38bdf8" strokeWidth="2" fill="none" opacity={interpolate(frame % 30, [0, 30], [0.8, 0])} />

            {/* Torso: Casual Tech T-Shirt */}
            <path
              d="M -36 30 C -42 8 -18 -4 0 -4 C 18 -4 42 8 36 30 L 30 85 L -30 85 Z"
              fill="#1e293b"
              stroke="#334155"
              strokeWidth="2.5"
            />
            {/* Mobile App Icon on Shirt */}
            <rect x="-10" y="24" width="20" height="20" rx="5" fill="#0284c7" />
            <path d="M -4 34 L 0 30 L 4 34" stroke="#ffffff" strokeWidth="2" fill="none" strokeLinecap="round" />

            {/* Arms Holding Smartphone */}
            <path d="M -32 24 Q -38 52 -16 58" stroke="#1e293b" strokeWidth="12" strokeLinecap="round" fill="none" />
            <path d="M 32 24 Q 38 52 16 58" stroke="#1e293b" strokeWidth="12" strokeLinecap="round" fill="none" />
            <circle cx="-16" cy="58" r="6" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.2" />
            <circle cx="16" cy={`58 - ${phoneTap}`} r="6" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.2" />

            {/* Glowing Modern Smartphone */}
            <g transform={`translate(-18, ${32 + phoneTap * 0.5})`}>
              <rect x="0" y="0" width="36" height="64" rx="7" fill="#0f172a" stroke="#38bdf8" strokeWidth="2" />
              <rect x="3" y="4" width="30" height="56" rx="4" fill="#020617" />
              <rect x="5" y="6" width="26" height="52" rx="3" fill="url(#phoneGlow)" opacity="0.4" />
              {/* App Feed Cards */}
              <rect x="7" y="12" width="22" height="10" rx="2" fill="#38bdf8" opacity="0.8" />
              <rect x="7" y="26" width="22" height="10" rx="2" fill="#818cf8" opacity="0.8" />
              <rect x="7" y="40" width="22" height="10" rx="2" fill="#34d399" opacity="0.8" />
              {/* Home Indicator */}
              <line x1="12" y1="56" x2="24" y2="56" stroke="#ffffff" strokeWidth="1.5" strokeLinecap="round" />
            </g>

            {/* Head & Neck */}
            <rect x="-8" y="-16" width="16" height="18" rx="4" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.2" />
            <path
              d="M -24 -36 C -26 -54 -16 -66 0 -66 C 16 -66 26 -54 24 -36 C 23 -18 15 -10 0 -10 C -15 -10 -23 -18 -24 -36 Z"
              fill="url(#studioSkin)"
              stroke="#ea580c"
              strokeWidth="2"
            />
            {/* Hair */}
            <path d="M -25 -40 C -27 -62 -12 -70 0 -70 C 14 -70 27 -60 25 -40 Z" fill="#334155" />
            {/* Eyes Looking Down at Phone */}
            <g transform={`translate(0, -34) scale(1, ${eyeHeight})`}>
              <circle cx="-10" cy="2" r="3.5" fill="#0f172a" />
              <circle cx="-9" cy="1" r="1.2" fill="#ffffff" />
              <circle cx="10" cy="2" r="3.5" fill="#0f172a" />
              <circle cx="11" cy="1" r="1.2" fill="#ffffff" />
            </g>
            {/* Smile */}
            <path d="M -7 -20 Q 0 -15 7 -20" stroke="#9a3412" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          </g>
        ) : (
          /* -------------------------------------------------------------
              DEVELOPER & ARCHITECT ROLES (With High-End Workstation)
              ------------------------------------------------------------- */
          <>
            {/* Ambient desk cast */}
            <ellipse cx="120" cy="180" rx="75" ry="25" fill="#38bdf8" opacity="0.12" />

            {/* 3:00 AM Flashing Emergency Beacon */}
            {role === 'devops_oncall' && (
              <g transform="translate(185, 135)">
                <circle cx="15" cy="15" r="32" fill="#ef4444" opacity={Math.abs(Math.sin(frame * 0.35)) * 0.7} />
                <path d="M 6 22 L 9 8 Q 15 3 21 8 L 24 22 Z" fill="#ef4444" stroke="#b91c1c" strokeWidth="2" />
                <rect x="3" y="22" width="24" height="6" rx="2" fill="#1e293b" />
              </g>
            )}

            {/* CTO Flying Dollar Bills */}
            {role === 'cto_panic' && (
              <g>
                <g transform={`translate(${170 + Math.sin(frame / 3) * 15}, ${135 - cashFly1}) rotate(${frame * 4})`}>
                  <rect x="0" y="0" width="28" height="15" rx="2" fill="#22c55e" stroke="#15803d" strokeWidth="1.5" />
                  <text x="14" y="11" textAnchor="middle" fill="#ffffff" fontSize="9" fontWeight="900">$</text>
                </g>
                <g transform={`translate(${40 - Math.cos(frame / 4) * 15}, ${145 - cashFly2}) rotate(${-frame * 3})`}>
                  <rect x="0" y="0" width="28" height="15" rx="2" fill="#22c55e" stroke="#15803d" strokeWidth="1.5" />
                  <text x="14" y="11" textAnchor="middle" fill="#ffffff" fontSize="9" fontWeight="900">$</text>
                </g>
              </g>
            )}

            {/* Desk Surface */}
            <g transform="translate(10, 200)">
              <rect x="0" y="0" width="220" height="16" rx="5" fill="#1e293b" stroke="#334155" strokeWidth="2" />
              <rect x="18" y="16" width="14" height="50" rx="3" fill="#0f172a" />
              <rect x="188" y="16" width="14" height="50" rx="3" fill="#0f172a" />
              <line x1="4" y1="15" x2="216" y2="15" stroke="#38bdf8" strokeWidth="2" strokeOpacity="0.8" />
            </g>

            {/* Coffee Mug with Procedural Steam */}
            {(role === 'junior_dev' || role === 'senior_architect') && (
              <g transform="translate(180, 172)">
                <rect x="0" y="8" width="22" height="24" rx="4" fill="#f8fafc" stroke="#94a3b8" strokeWidth="2" />
                <path d="M 22 13 C 29 13 29 23 22 23" stroke="#cbd5e1" strokeWidth="3" fill="none" strokeLinecap="round" />
                <text x="11" y="24" textAnchor="middle" fill="#2563eb" fontSize="10" fontWeight="900">
                  {role === 'senior_architect' ? '☕' : '⚡'}
                </text>
                <path
                  d={`M 7 ${5 - steamPhase * 0.4} Q ${10 + steamCurve1} ${-5 - steamPhase * 0.4} 8 ${-16 - steamPhase * 0.4}`}
                  stroke="#e2e8f0"
                  strokeWidth="2.2"
                  fill="none"
                  strokeLinecap="round"
                  opacity={interpolate(steamPhase, [0, 25, 50], [0.85, 0.4, 0])}
                />
                <path
                  d={`M 15 ${5 - steamPhase * 0.4} Q ${12 + steamCurve2} ${-8 - steamPhase * 0.4} 16 ${-18 - steamPhase * 0.4}`}
                  stroke="#e2e8f0"
                  strokeWidth="2.2"
                  fill="none"
                  strokeLinecap="round"
                  opacity={interpolate(steamPhase, [0, 25, 50], [0.75, 0.3, 0])}
                />
              </g>
            )}

            {/* Laptop & Syntax Code */}
            {role === 'junior_dev' && (
              <g transform="translate(75, 150)">
                <rect x="5" y="0" width="80" height="52" rx="5" fill="#0f172a" stroke="#475569" strokeWidth="2.5" />
                <rect x="9" y="4" width="72" height="44" rx="3" fill="#020617" />
                <g opacity="0.95">
                  <line x1="15" y1="12" x2="38" y2="12" stroke="#38bdf8" strokeWidth="2.5" strokeLinecap="round" />
                  <line x1="15" y1="18" x2="58" y2="18" stroke="#a855f7" strokeWidth="2.5" strokeLinecap="round" />
                  <line x1="20" y1="24" x2="68" y2="24" stroke="#22c55e" strokeWidth="2.5" strokeLinecap="round" />
                  <line x1="20" y1="30" x2="50" y2="30" stroke="#f59e0b" strokeWidth="2.5" strokeLinecap="round" />
                  <line x1="15" y1="36" x2="32" y2="36" stroke="#ef4444" strokeWidth="2.5" strokeLinecap="round" />
                </g>
                <polygon points="0,52 90,52 82,60 8,60" fill="#1e293b" stroke="#334155" strokeWidth="1.5" />
                <rect x="32" y="54" width="26" height="4" rx="1" fill="#475569" />
              </g>
            )}

            {/* DevOps Vibrating Smartphone with PagerDuty Alert */}
            {role === 'devops_oncall' && (
              <g transform={`translate(${140 + Math.sin(frame * 2.5) * 3}, 170) rotate(${Math.cos(frame * 2.2) * 10})`}>
                <rect x="0" y="0" width="26" height="40" rx="5" fill="#0f172a" stroke="#ef4444" strokeWidth="2" />
                <rect x="3" y="4" width="20" height="32" rx="3" fill="#7f1d1d" />
                <circle cx="13" cy="16" r="6" fill="#ef4444" />
                <text x="13" y="30" textAnchor="middle" fill="#ffffff" fontSize="8" fontWeight="900">500</text>
              </g>
            )}

            {/* Character Torso & Rig */}
            <g transform={`translate(120, ${115 + breath})`}>
              {role === 'junior_dev' && (
                <g>
                  <path
                    d="M -40 32 C -46 8 -20 -4 0 -4 C 20 -4 46 8 40 32 L 34 85 L -34 85 Z"
                    fill="url(#hoodieJuniorGrad)"
                    stroke="#1d4ed8"
                    strokeWidth="3"
                  />
                  <path d="M -20 56 L 20 56 L 26 82 L -26 82 Z" fill="#1e40af" stroke="#1d4ed8" strokeWidth="2" />
                  <line x1="-8" y1="8" x2={-10 + Math.sin(frame / 6) * 3} y2="38" stroke="#f8fafc" strokeWidth="2.5" strokeLinecap="round" />
                  <line x1="8" y1="8" x2={10 + Math.sin(frame / 6) * 3} y2="38" stroke="#f8fafc" strokeWidth="2.5" strokeLinecap="round" />
                </g>
              )}

              {role === 'devops_oncall' && (
                <g>
                  <path
                    d="M -42 32 C -48 8 -20 -4 0 -4 C 20 -4 48 8 42 32 L 36 85 L -36 85 Z"
                    fill="url(#hoodieOnCallGrad)"
                    stroke="#991b1b"
                    strokeWidth="3"
                  />
                  <rect x="-18" y="30" width="36" height="14" rx="3" fill="#7f1d1d" stroke="#fca5a5" strokeWidth="1.5" />
                  <text x="0" y="40" textAnchor="middle" fill="#ffffff" fontSize="7" fontWeight="900">PAGERDUTY 3AM</text>
                </g>
              )}

              {role === 'senior_architect' && (
                <g>
                  <path
                    d="M -38 32 C -44 6 -16 -6 0 -6 C 16 -6 44 6 38 32 L 32 85 L -32 85 Z"
                    fill="url(#seniorOutfitGrad)"
                    stroke="#475569"
                    strokeWidth="2.5"
                  />
                  <rect x="-10" y="-14" width="20" height="16" rx="3" fill="#1e293b" stroke="#334155" strokeWidth="1.5" />
                </g>
              )}

              {role === 'cto_panic' && (
                <g>
                  <path
                    d="M -40 32 C -46 8 -20 -4 0 -4 C 20 -4 46 8 40 32 L 34 85 L -34 85 Z"
                    fill="#334155"
                    stroke="#1e293b"
                    strokeWidth="3"
                  />
                  <polygon points="0,5 -6,16 6,16" fill="#ef4444" />
                  <polygon points={`-5,16 5,16 ${Math.sin(frame * 1.6) * 10},55 0,62`} fill="#ef4444" />
                </g>
              )}

              {/* Arms & Typing / Panic Hands */}
              {role === 'junior_dev' && (
                <g>
                  <path d={`M -36 26 Q -48 58 -22 ${66 + leftHandTyping}`} stroke="#1d4ed8" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="-22" cy={66 + leftHandTyping} r="7" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                  <path d={`M 36 26 Q 48 58 22 ${66 + rightHandTyping}`} stroke="#1d4ed8" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="22" cy={66 + rightHandTyping} r="7" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                </g>
              )}

              {role === 'devops_oncall' && (
                <g>
                  <path d="M -38 28 Q -55 -10 -25 -22" stroke="#991b1b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="-25" cy="-22" r="8" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                  <path d="M 38 28 Q 55 -10 25 -22" stroke="#991b1b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="25" cy="-22" r="8" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                </g>
              )}

              {role === 'senior_architect' && (
                <g>
                  <path d="M 34 26 Q 56 48 48 68" stroke="#1e293b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="48" cy="68" r="7" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                  <path d="M -34 26 Q -52 48 -42 68" stroke="#1e293b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <circle cx="-42" cy="68" r="7" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                </g>
              )}

              {role === 'cto_panic' && (
                <g>
                  <path d="M -36 28 Q -50 -5 -24 -14" stroke="#1e293b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <ellipse cx="-24" cy="-14" rx="8" ry="9" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                  <path d="M 36 28 Q 50 -5 24 -14" stroke="#1e293b" strokeWidth="13" strokeLinecap="round" fill="none" />
                  <ellipse cx="24" cy="-14" rx="8" ry="9" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                </g>
              )}

              {/* Head & Neck */}
              <g transform={`translate(0, ${headBob})`}>
                <rect x="-9" y="-16" width="18" height="18" rx="4" fill="url(#studioSkin)" stroke="#ea580c" strokeWidth="1.5" />
                <path d="M -9 -14 L 9 -14 L 6 -6 L -6 -6 Z" fill="url(#studioSkinShadow)" />

                <path
                  d="M -26 -38 C -28 -56 -18 -68 0 -68 C 18 -68 28 -56 26 -38 C 25 -20 16 -10 0 -10 C -16 -10 -25 -20 -26 -38 Z"
                  fill="url(#studioSkin)"
                  stroke="#ea580c"
                  strokeWidth="2"
                />

                {/* Hair / Hats */}
                {role === 'junior_dev' && (
                  <g>
                    <path d="M -28 -42 C -30 -66 -16 -76 0 -76 C 16 -76 30 -66 28 -42 L 24 -34 L -24 -34 Z" fill="#ef4444" stroke="#b91c1c" strokeWidth="2" />
                    <path d="M 22 -40 L 38 -38 Q 36 -30 18 -32 Z" fill="#b91c1c" stroke="#991b1b" strokeWidth="1.5" />
                    <circle cx="-3" cy="-40" r="2" fill="#fca5a5" />
                    <circle cx="3" cy="-40" r="2" fill="#fca5a5" />
                    <path d="M -27 -34 C -31 -22 -26 -16 -22 -14" stroke="#1e293b" strokeWidth="4" strokeLinecap="round" />
                  </g>
                )}

                {role === 'devops_oncall' && (
                  <g>
                    <path
                      d="M -26 -40 L -36 -56 L -24 -52 L -18 -72 L -4 -58 L 10 -76 L 18 -56 L 32 -64 L 26 -40 Z"
                      fill="#1e293b"
                      stroke="#0f172a"
                      strokeWidth="2"
                    />
                  </g>
                )}

                {role === 'senior_architect' && (
                  <g>
                    <path
                      d="M -28 -42 C -30 -68 -10 -74 0 -74 C 18 -74 30 -64 28 -42 C 26 -30 22 -22 18 -22 C 14 -46 -18 -44 -24 -36 Z"
                      fill="#475569"
                      stroke="#334155"
                      strokeWidth="2"
                    />
                  </g>
                )}

                {role === 'cto_panic' && (
                  <g>
                    <path d="M -27 -36 C -32 -20 -28 -14 -22 -10" stroke="#64748b" strokeWidth="5" strokeLinecap="round" />
                    <path d="M 27 -36 C 32 -20 28 -14 22 -10" stroke="#64748b" strokeWidth="5" strokeLinecap="round" />
                    <path d="M -5 -68 Q 0 -82 5 -68" stroke="#64748b" strokeWidth="2.5" fill="none" strokeLinecap="round" />
                  </g>
                )}

                {/* Eyebrows */}
                {role === 'junior_dev' && (
                  <g>
                    <line x1="-18" y1="-48" x2="-6" y2="-45" stroke="#18181b" strokeWidth="3.5" strokeLinecap="round" />
                    <line x1="6" y1="-45" x2="18" y2="-48" stroke="#18181b" strokeWidth="3.5" strokeLinecap="round" />
                  </g>
                )}

                {role === 'devops_oncall' && (
                  <g>
                    <line x1="-19" y1="-56" x2="-6" y2="-49" stroke="#18181b" strokeWidth="4" strokeLinecap="round" />
                    <line x1="6" y1="-49" x2="19" y2="-56" stroke="#18181b" strokeWidth="4" strokeLinecap="round" />
                  </g>
                )}

                {role === 'senior_architect' && (
                  <g>
                    <path d="M -18 -48 Q -12 -52 -5 -48" stroke="#1e293b" strokeWidth="3.5" fill="none" strokeLinecap="round" />
                    <path d="M 5 -48 Q 12 -52 18 -48" stroke="#1e293b" strokeWidth="3.5" fill="none" strokeLinecap="round" />
                  </g>
                )}

                {role === 'cto_panic' && (
                  <g>
                    <line x1="-18" y1="-48" x2="-6" y2="-56" stroke="#1e293b" strokeWidth="4" strokeLinecap="round" />
                    <line x1="6" y1="-56" x2="18" y2="-48" stroke="#1e293b" strokeWidth="4" strokeLinecap="round" />
                  </g>
                )}

                {/* Eyes with Blinking */}
                <g transform={`translate(0, -38) scale(1, ${eyeHeight})`}>
                  {role === 'junior_dev' && (
                    <g>
                      <rect x="-22" y="-10" width="18" height="15" rx="4" fill="#0f172a" />
                      <rect x="4" y="-10" width="18" height="15" rx="4" fill="#0f172a" />
                      <line x1="-4" y1="-3" x2="4" y2="-3" stroke="#0f172a" strokeWidth="3" />
                      <line x1="-20" y1="-7" x2="-10" y2="3" stroke="#ffffff" strokeWidth="1.5" strokeOpacity="0.8" />
                      <line x1="6" y1="-7" x2="16" y2="3" stroke="#ffffff" strokeWidth="1.5" strokeOpacity="0.8" />
                      <circle cx="-13" cy="-2" r="3.5" fill="#38bdf8" />
                      <circle cx="-12" cy="-3" r="1.2" fill="#ffffff" />
                      <circle cx="13" cy="-2" r="3.5" fill="#38bdf8" />
                      <circle cx="14" cy="-3" r="1.2" fill="#ffffff" />
                    </g>
                  )}

                  {role === 'devops_oncall' && (
                    <g>
                      <ellipse cx="-13" cy="-2" rx="9" ry="10" fill="#ffffff" stroke="#ef4444" strokeWidth="2" />
                      <ellipse cx="13" cy="-2" rx="9" ry="10" fill="#ffffff" stroke="#ef4444" strokeWidth="2" />
                      <circle cx="-13" cy="-2" r="3.5" fill="#7f1d1d" />
                      <circle cx="13" cy="-2" r="3.5" fill="#7f1d1d" />
                      <path d="M -19 -5 L -15 -2" stroke="#ef4444" strokeWidth="1.2" />
                      <path d="M 19 -5 L 15 -2" stroke="#ef4444" strokeWidth="1.2" />
                    </g>
                  )}

                  {role === 'senior_architect' && (
                    <g>
                      <path d="M -22 -8 L -3 -8 L -5 5 L -20 5 Z" fill="#0f172a" stroke="#334155" strokeWidth="1.5" />
                      <path d="M 3 -8 L 22 -8 L 20 5 L 5 5 Z" fill="#0f172a" stroke="#334155" strokeWidth="1.5" />
                      <line x1="-3" y1="-4" x2="3" y2="-4" stroke="#0f172a" strokeWidth="2.5" />
                      <line x1="-19" y1="-5" x2="-8" y2="2" stroke="#10b981" strokeWidth="1.8" strokeOpacity="0.9" />
                      <line x1="6" y1="-5" x2="17" y2="2" stroke="#10b981" strokeWidth="1.8" strokeOpacity="0.9" />
                    </g>
                  )}

                  {role === 'cto_panic' && (
                    <g>
                      <ellipse cx="-13" cy="-2" rx="9" ry="9" fill="#ffffff" />
                      <ellipse cx="13" cy="-2" rx="9" ry="9" fill="#ffffff" />
                      <circle cx="-13" cy="-2" r="4" fill="#0284c7" />
                      <circle cx="13" cy="-2" r="4" fill="#0284c7" />
                    </g>
                  )}
                </g>

                {/* Mouths */}
                {role === 'junior_dev' && (
                  <g transform="translate(0, -22)">
                    <path d="M -10 0 Q 0 8 11 1" stroke="#9a3412" strokeWidth="3" fill="none" strokeLinecap="round" />
                  </g>
                )}

                {role === 'devops_oncall' && (
                  <g transform="translate(0, -22)">
                    <path d="M -14 0 Q -7 8 0 0 Q 7 -8 14 0" stroke="#7f1d1d" strokeWidth="3.5" fill="none" strokeLinecap="round" />
                  </g>
                )}

                {role === 'senior_architect' && (
                  <g transform="translate(0, -22)">
                    <path d="M -8 1 Q 0 6 10 2" stroke="#334155" strokeWidth="3" fill="none" strokeLinecap="round" />
                  </g>
                )}

                {role === 'cto_panic' && (
                  <g transform="translate(0, -22)">
                    <ellipse cx="0" cy="5" rx="8" ry="11" fill="#991b1b" stroke="#450a0a" strokeWidth="2" />
                    <ellipse cx="0" cy="9" rx="5" ry="4" fill="#f87171" />
                  </g>
                )}

                {/* Sweat Drop on Stress */}
                {(isStressed || role === 'devops_oncall' || role === 'cto_panic') && (
                  <g transform={`translate(30, ${-46 + sweatPhase})`} opacity={sweatOpacity}>
                    <path d="M 0 0 C -5 5 -5 10 0 13 C 5 10 5 5 0 0 Z" fill="#38bdf8" />
                  </g>
                )}
              </g>
            </g>
          </>
        )}
      </svg>

      {/* Titanium MDM Glassmorphic Label Badge */}
      {label && (
        <div
          style={{
            marginTop: '8px',
            padding: '7px 18px',
            backgroundColor: isPanic ? 'rgba(239, 68, 68, 0.25)' : 'rgba(15, 23, 42, 0.92)',
            backdropFilter: 'blur(14px)',
            border: isPanic ? '1.5px solid rgba(239, 68, 68, 0.6)' : '1.5px solid rgba(56, 189, 248, 0.45)',
            borderRadius: '20px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            boxShadow: '0 8px 24px rgba(0,0,0,0.6)',
          }}
        >
          <span
            style={{
              fontSize: '15px',
              fontWeight: 900,
              color: isPanic ? '#fca5a5' : '#f8fafc',
              letterSpacing: '0.06em',
              textTransform: 'uppercase',
            }}
          >
            {label}
          </span>
          {sublabel && (
            <span
              style={{
                fontSize: '12px',
                color: isPanic ? '#f87171' : '#38bdf8',
                fontWeight: 700,
                marginTop: '2px',
              }}
            >
              {sublabel}
            </span>
          )}
        </div>
      )}
    </div>
  );
};
