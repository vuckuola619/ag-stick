import React from 'react';
import { useCurrentFrame } from 'remotion';

export interface AWSBillingMeterProps {
  cost: number;
  label?: string;
  isPanic?: boolean;
}

export const AWSBillingMeter: React.FC<AWSBillingMeterProps> = ({
  cost,
  label = "AWS MONTHLY ESTIMATE",
  isPanic = false,
}) => {
  const frame = useCurrentFrame();
  const shake = isPanic ? (Math.sin(frame * 2.5) * 3) : 0;
  const panicGlow = isPanic ? (Math.sin(frame / 4) > 0 ? '#ef4444' : '#b91c1c') : '#f59e0b';

  return (
    <div
      style={{
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        border: `2px solid ${isPanic ? panicGlow : 'rgba(56, 189, 248, 0.4)'}`,
        borderRadius: '12px',
        padding: '10px 18px',
        boxShadow: `0 12px 30px rgba(0,0,0,0.75), 0 0 ${isPanic ? '24px rgba(239, 68, 68, 0.5)' : '10px rgba(56, 189, 248, 0.2)'}`,
        transform: `translate(${shake}px, 0)`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'flex-start',
        fontFamily: 'Inter, system-ui, sans-serif',
        backdropFilter: 'blur(16px)',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '3px' }}>
        <span style={{ fontSize: '16px' }}>💳</span>
        <span style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800, letterSpacing: '0.06em' }}>
          {label}
        </span>
      </div>
      <div
        style={{
          color: isPanic ? '#f87171' : '#fbbf24',
          fontSize: '32px',
          fontWeight: 900,
          fontFamily: 'monospace',
          letterSpacing: '-0.02em',
          textShadow: isPanic ? '0 0 16px rgba(239, 68, 68, 0.7)' : '0 0 12px rgba(251, 191, 36, 0.4)',
        }}
      >
        ${cost.toLocaleString()}<span style={{ fontSize: '16px', fontWeight: 700, color: '#94a3b8' }}>/mo</span>
      </div>
      {isPanic && (
        <div
          style={{
            marginTop: '4px',
            backgroundColor: '#7f1d1d',
            color: '#fca5a5',
            fontSize: '12px',
            fontWeight: 900,
            padding: '2px 8px',
            borderRadius: '4px',
            letterSpacing: '0.05em',
            boxShadow: '0 0 10px rgba(239, 68, 68, 0.5)',
          }}
        >
          💀 CTO HEART ATTACK
        </div>
      )}
    </div>
  );
};
