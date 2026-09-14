import React from 'react';

export interface WhatsAppHeaderProps {
  episodeTitle?: string;
  topicTag?: string;
  statsTag?: string;
}

export const WhatsAppHeader: React.FC<WhatsAppHeaderProps> = ({
  episodeTitle = 'How 50 Engineers Run WhatsApp for 2 Billion Users',
  topicTag = 'WHATSAPP ARCHITECTURE // CONCURRENCY MASTERCLASS',
  statsTag = '50 DEVS // 2B USERS // 100B MSGS/DAY',
}) => {
  return (
    <div
      style={{
        position: 'absolute',
        top: '35px',
        left: '50px',
        display: 'flex',
        flexDirection: 'column',
        zIndex: 100,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '8px' }}>
        <div
          style={{
            backgroundColor: '#25d366',
            color: '#064e3b',
            fontSize: '13px',
            fontWeight: 900,
            padding: '5px 14px',
            borderRadius: '8px',
            letterSpacing: '0.08em',
            boxShadow: '0 0 20px rgba(37, 211, 102, 0.4)',
          }}
        >
          {topicTag}
        </div>
        <div
          style={{
            color: '#38bdf8',
            fontSize: '12px',
            fontWeight: 800,
            letterSpacing: '0.05em',
            fontFamily: 'monospace',
          }}
        >
          {statsTag}
        </div>
      </div>
      <div
        style={{
          color: '#f8fafc',
          fontSize: '34px',
          fontWeight: 900,
          letterSpacing: '-0.02em',
          textShadow: '0 4px 20px rgba(0,0,0,0.85)',
          maxWidth: '850px',
          lineHeight: '1.2',
        }}
      >
        {episodeTitle}
      </div>
    </div>
  );
};
