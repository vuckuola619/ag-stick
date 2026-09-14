import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

export interface TechStudioBackgroundProps {
  isAlert?: boolean;
}

export const TechStudioBackground: React.FC<TechStudioBackgroundProps> = ({
  isAlert = false,
}) => {
  const frame = useCurrentFrame();

  // Smooth undulating studio ambient lighting
  const pulse1 = Math.sin(frame / 35) * 0.2 + 0.8;
  const pulse2 = Math.cos(frame / 40) * 0.2 + 0.8;
  const pulse3 = Math.sin(frame / 25) * 0.15 + 0.85;

  // Circuit trace signal pulses traveling along coordinates
  const signalPos1 = (frame * 6) % 2400 - 200;
  const signalPos2 = (frame * 8) % 2600 - 300;
  const signalPos3 = (frame * 5) % 2200 - 200;

  // Server LED blinking states (procedural deterministic blink based on frame)
  const leds = [
    { color: '#25d366', blinkRate: 15 },
    { color: '#38bdf8', blinkRate: 23 },
    { color: '#25d366', blinkRate: 31 },
    { color: '#fbbf24', blinkRate: 41 },
    { color: '#38bdf8', blinkRate: 19 },
    { color: '#25d366', blinkRate: 27 },
  ];

  // Technical coordinate ruler markings
  const timecodeSec = Math.floor(frame / 30);
  const timecodeFrame = frame % 30;
  const timecodeStr = `00:00:${timecodeSec.toString().padStart(2, '0')}:${timecodeFrame.toString().padStart(2, '0')}`;

  return (
    <div
      style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        backgroundColor: '#060a14',
        overflow: 'hidden',
        zIndex: 0,
      }}
    >
      {/* 1. LAYER 1: Deep Studio Lighting Foundation (Multi-stop Mesh Gradients) */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: isAlert
            ? 'radial-gradient(circle at 50% 40%, #2e0d15 0%, #17070b 50%, #060204 100%)'
            : 'radial-gradient(circle at 50% 35%, #0d2247 0%, #08162e 40%, #050a16 100%)',
          transition: 'background 0.4s ease',
        }}
      />

      {/* 2. LAYER 2: Luminous Volumetric Studio Spotlights */}
      {/* Top Left: Electric Cyan / Emerald Studio Key Light */}
      <div
        style={{
          position: 'absolute',
          top: '-15%',
          left: '5%',
          width: '900px',
          height: '900px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(14, 165, 233, 0.32) 0%, rgba(37, 211, 102, 0.18) 40%, rgba(0, 0, 0, 0) 70%)',
          filter: 'blur(100px)',
          opacity: pulse1,
          pointerEvents: 'none',
        }}
      />

      {/* Center Stage: Indigo / Sapphire Concurrency Horizon */}
      <div
        style={{
          position: 'absolute',
          top: '25%',
          left: '30%',
          width: '1000px',
          height: '800px',
          borderRadius: '50%',
          background: isAlert
            ? 'radial-gradient(circle, rgba(239, 68, 68, 0.45) 0%, rgba(220, 38, 38, 0.2) 45%, rgba(0,0,0,0) 70%)'
            : 'radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, rgba(14, 165, 233, 0.18) 45%, rgba(0, 0, 0, 0) 70%)',
          filter: 'blur(110px)',
          opacity: pulse2,
          pointerEvents: 'none',
        }}
      />

      {/* Bottom Right: Emerald Concurrency Pool */}
      <div
        style={{
          position: 'absolute',
          bottom: '-15%',
          right: '5%',
          width: '800px',
          height: '800px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(37, 211, 102, 0.25) 0%, rgba(16, 185, 129, 0.12) 50%, rgba(0,0,0,0) 70%)',
          filter: 'blur(90px)',
          opacity: pulse3,
          pointerEvents: 'none',
        }}
      />

      {/* 3. LAYER 3: Interactive SVG Circuit Traces & Signal Pulses */}
      <svg
        width="100%"
        height="100%"
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          pointerEvents: 'none',
        }}
      >
        <defs>
          {/* Glowing linear gradient for traveling packets */}
          <linearGradient id="cyanPulse" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#38bdf8" stopOpacity="0" />
            <stop offset="50%" stopColor="#38bdf8" stopOpacity="1" />
            <stop offset="100%" stopColor="#25d366" stopOpacity="0" />
          </linearGradient>

          <linearGradient id="emeraldPulse" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#25d366" stopOpacity="0" />
            <stop offset="50%" stopColor="#34d399" stopOpacity="1" />
            <stop offset="100%" stopColor="#38bdf8" stopOpacity="0" />
          </linearGradient>

          {/* Micro Engineering Grid Pattern (60px) */}
          <pattern
            id="eng-grid-minor"
            x="0"
            y="0"
            width="60"
            height="60"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 60 0 L 0 0 0 60"
              fill="none"
              stroke="rgba(56, 189, 248, 0.08)"
              strokeWidth="0.8"
            />
            {/* Center dot */}
            <circle cx="30" cy="30" r="1" fill="#38bdf8" opacity="0.25" />
          </pattern>

          {/* Major Structural Grid Pattern (240px) with Blueprint Crosshairs */}
          <pattern
            id="eng-grid-major"
            x="0"
            y="0"
            width="240"
            height="240"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 240 0 L 0 0 0 240"
              fill="none"
              stroke="rgba(56, 189, 248, 0.18)"
              strokeWidth="1.2"
            />
            {/* Precision Crosshairs at Grid Intersections */}
            <path
              d="M -8 0 L 8 0 M 0 -8 L 0 8"
              stroke="#38bdf8"
              strokeWidth="1.4"
              opacity="0.45"
            />
            <circle cx="0" cy="0" r="3" fill="none" stroke="#25d366" strokeWidth="0.8" opacity="0.4" />
          </pattern>
        </defs>

        {/* Fill Grids */}
        <rect width="100%" height="100%" fill="url(#eng-grid-minor)" />
        <rect width="100%" height="100%" fill="url(#eng-grid-major)" />

        {/* Circuit Bus Highway 1: Top Technical Header Bus */}
        <path
          d="M 0 110 L 450 110 L 490 140 L 1400 140 L 1440 110 L 1920 110"
          fill="none"
          stroke="rgba(56, 189, 248, 0.22)"
          strokeWidth="1.5"
          strokeDasharray="8 6"
        />
        {/* Signal Packet 1 */}
        <circle
          cx={(signalPos1 + 1920) % 1920}
          cy={110}
          r="4"
          fill="#38bdf8"
          filter="drop-shadow(0 0 8px #38bdf8)"
        />

        {/* Circuit Bus Highway 2: Center Concurrency Spine */}
        <path
          d="M 100 540 L 600 540 L 660 600 L 1260 600 L 1320 540 L 1820 540"
          fill="none"
          stroke="rgba(37, 211, 102, 0.2)"
          strokeWidth="1.5"
          strokeDasharray="6 8"
        />
        {/* Signal Packet 2 */}
        <circle
          cx={(signalPos2 + 1920) % 1920}
          cy={540}
          r="4.5"
          fill="#25d366"
          filter="drop-shadow(0 0 10px #25d366)"
        />

        {/* Circuit Bus Highway 3: Lower Hardware Telemetry Bus */}
        <path
          d="M 0 940 L 520 940 L 560 970 L 1380 970 L 1420 940 L 1920 940"
          fill="none"
          stroke="rgba(56, 189, 248, 0.2)"
          strokeWidth="1.2"
        />
        {/* Signal Packet 3 */}
        <circle
          cx={(signalPos3 + 1920) % 1920}
          cy={940}
          r="3.5"
          fill="#38bdf8"
          filter="drop-shadow(0 0 6px #38bdf8)"
        />

        {/* Corner Diagonal Technical Hatch Lines */}
        <line x1="0" y1="40" x2="40" y2="0" stroke="#38bdf8" strokeWidth="1" opacity="0.3" />
        <line x1="0" y1="60" x2="60" y2="0" stroke="#38bdf8" strokeWidth="1" opacity="0.2" />
        <line x1="1880" y1="1080" x2="1920" y2="1040" stroke="#25d366" strokeWidth="1" opacity="0.3" />
        <line x1="1860" y1="1080" x2="1920" y2="1020" stroke="#25d366" strokeWidth="1" opacity="0.2" />
      </svg>

      {/* 4. LAYER 4: Technical Telemetry Rulers & Hardware HUD Markers */}
      {/* Top Left Telemetry Coordinate Stamp */}
      <div
        style={{
          position: 'absolute',
          top: '20px',
          left: '30px',
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          fontFamily: 'monospace',
          fontSize: '12px',
          fontWeight: 700,
          color: 'rgba(56, 189, 248, 0.65)',
          letterSpacing: '0.08em',
          pointerEvents: 'none',
        }}
      >
        <span style={{ color: '#25d366' }}>● SYSTEM ONLINE</span>
        <span>|</span>
        <span>REC {timecodeStr}</span>
        <span>|</span>
        <span>FREEBSD_KERNEL // v9.2-RELEASE</span>
      </div>

      {/* Top Right Rack Activity Status LEDs */}
      <div
        style={{
          position: 'absolute',
          top: '20px',
          right: '40px',
          display: 'flex',
          alignItems: 'center',
          gap: '10px',
          pointerEvents: 'none',
        }}
      >
        <span
          style={{
            fontFamily: 'monospace',
            fontSize: '11px',
            color: 'rgba(148, 163, 184, 0.7)',
            letterSpacing: '0.05em',
            marginRight: '6px',
          }}
        >
          CLUSTER RACK 01-A
        </span>
        {leds.map((led, i) => {
          const isLit = Math.floor(frame / led.blinkRate) % 2 === 0;
          return (
            <div
              key={i}
              style={{
                width: '7px',
                height: '7px',
                borderRadius: '50%',
                backgroundColor: isLit ? led.color : 'rgba(30, 41, 59, 0.6)',
                boxShadow: isLit ? `0 0 8px ${led.color}` : 'none',
                transition: 'background-color 0.1s ease',
              }}
            />
          );
        })}
      </div>

      {/* Bottom Left Hardware Bus Coordinate */}
      <div
        style={{
          position: 'absolute',
          bottom: '20px',
          left: '30px',
          fontFamily: 'monospace',
          fontSize: '11px',
          color: 'rgba(56, 189, 248, 0.5)',
          letterSpacing: '0.06em',
          pointerEvents: 'none',
        }}
      >
        BUS_ADDR: 0x7FFF_2800000 // ARCH: BEAM_OTP // CONCURRENCY_LOCK: ZERO
      </div>

      {/* Bottom Right Scale Metric Monitor */}
      <div
        style={{
          position: 'absolute',
          bottom: '20px',
          right: '40px',
          fontFamily: 'monospace',
          fontSize: '11px',
          color: 'rgba(37, 211, 102, 0.6)',
          letterSpacing: '0.06em',
          pointerEvents: 'none',
        }}
      >
        IO_THREADS: 24 // TCP_SNDBUF: 4KB // ZERO_DISK_LATENCY: OK
      </div>

      {/* 5. LAYER 5: Studio Vignette Framing */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'radial-gradient(circle at center, rgba(0,0,0,0) 50%, rgba(3, 7, 18, 0.65) 100%)',
          pointerEvents: 'none',
        }}
      />
    </div>
  );
};
