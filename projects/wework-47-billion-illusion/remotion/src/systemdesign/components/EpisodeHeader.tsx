import React from 'react';

export interface EpisodeHeaderProps {
  seriesTitle?: string;
  episodeTitle: string;
  topicTag: string;
}

export const EpisodeHeader: React.FC<EpisodeHeaderProps> = ({
  seriesTitle = 'SYSTEM DESIGN PRIMER // HIGH SCALE',
  episodeTitle,
  topicTag,
}) => {
  return (
    <div
      style={{
        position: 'absolute',
        top: '32px',
        left: '50px',
        display: 'flex',
        flexDirection: 'column',
        gap: '8px',
        fontFamily: 'Inter, system-ui, sans-serif',
        zIndex: 100,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <div
          style={{
            backgroundColor: '#0284c7',
            color: '#ffffff',
            fontSize: '14px',
            fontWeight: 900,
            padding: '4px 12px',
            borderRadius: '6px',
            letterSpacing: '0.08em',
            boxShadow: '0 4px 14px rgba(2, 132, 199, 0.45)',
          }}
        >
          {topicTag}
        </div>
        <div
          style={{
            color: '#94a3b8',
            fontSize: '13px',
            fontWeight: 800,
            letterSpacing: '0.08em',
            fontFamily: 'monospace',
          }}
        >
          {seriesTitle}
        </div>
      </div>
      <div
        style={{
          color: '#ffffff',
          fontSize: '34px',
          fontWeight: 900,
          letterSpacing: '-0.03em',
          lineHeight: '1.2',
          textShadow: '0 4px 20px rgba(0,0,0,0.9), 0 0 30px rgba(56, 189, 248, 0.25)',
        }}
      >
        {episodeTitle}
      </div>
    </div>
  );
};
