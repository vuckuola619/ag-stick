import React from 'react';
import {
  useCurrentFrame,
  interpolate,
  spring,
  useVideoConfig,
  Img,
  staticFile,
} from 'remotion';
import { MercuryCaveBackground } from './MercuryCaveBackground';
import { LiquidMercuryDrop } from './LiquidMercuryDrop';
import { PrehistoricHUD } from './PrehistoricHUD';

const SENTENCES = [
  { startFrame: 3, endFrame: 110, text: 'Bayangkan kamu adalah manusia purba 10.000 tahun lalu.' },
  { startFrame: 110, endFrame: 235, text: 'Kamu menemukan sebuah batu kristal merah delima yang aneh di dalam gua gelap.' },
  { startFrame: 235, endFrame: 369, text: 'Karena penasaran, kamu melemparkan batu merah itu ke dalam kobaran api unggun.' },
  { startFrame: 369, endFrame: 443, text: 'Tiba-tiba hal mustahil terjadi!' },
  { startFrame: 443, endFrame: 610, text: 'Batunya tidak hangus, melainkan berdarah cairan perak mengkilap yang mengalir!' },
  { startFrame: 610, endFrame: 772, text: 'Logam cair ini tidak membasahi kulitmu, memantul licin bagai cermin, dan sangat berat.' },
  { startFrame: 772, endFrame: 859, text: 'Inilah merkuri, atau Quicksilver!' },
  { startFrame: 859, endFrame: 994, text: 'Batu merah tersebut adalah Cinabar, senyawa alami merkuri dan sulfur.' },
  { startFrame: 994, endFrame: 1239, text: 'Panas api unggun di atas 357°C memecah ikatan kimianya, uapnya mengembun jadi air raksa murni.' },
  { startFrame: 1239, endFrame: 1470, text: 'Dari rasa penasaran manusia purba yang bermain api, lahirlah elemen paling mistis dalam sejarah!' },
];

export const MercuryTikTokComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const currentSentence = SENTENCES.find(
    (s) => frame >= s.startFrame && frame < s.endFrame
  );
  const currentCaption = currentSentence ? currentSentence.text : '';

  const temperature = interpolate(
    frame,
    [0, 235, 369, 500, 994, 1150, 1512],
    [25, 28, 160, 365, 375, 410, 320],
    { extrapolateRight: 'clamp' }
  );

  const isShocked = frame >= 369 && frame < 520;
  const shakeX = isShocked ? Math.sin(frame * 2.5) * 12 : 0;
  const shakeY = isShocked ? Math.cos(frame * 2.2) * 8 : 0;

  const cavemanEntrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 90 },
  });

  const idleBob = Math.sin(frame / 6) * 5;

  // Crystal throw trajectory (Vertical coordinates)
  const crystalThrowProgress = interpolate(frame, [260, 310], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const crystalX = interpolate(crystalThrowProgress, [0, 1], [350, 540]);
  const crystalY = interpolate(crystalThrowProgress, [0, 0.5, 1], [980, 720, 1180]);
  const crystalRot = interpolate(crystalThrowProgress, [0, 1], [0, 360]);

  const outroOpacity = interpolate(frame, [1475, 1510], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: 1080,
        height: 1920,
        overflow: 'hidden',
        backgroundColor: '#05070e',
        transform: `translate(${shakeX}px, ${shakeY}px)`,
        opacity: outroOpacity,
      }}
    >
      {/* 1. Background */}
      <MercuryCaveBackground fireActive={frame >= 180} />

      {/* 2. Top Title Billboard (Act 1) */}
      {frame >= 10 && frame < 220 && (
        <div
          style={{
            position: 'absolute',
            top: '220px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 10, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            width: '90%',
            zIndex: 10,
          }}
        >
          <div
            style={{
              backgroundColor: '#fbbf24',
              color: '#0f172a',
              padding: '8px 24px',
              borderRadius: '12px',
              fontWeight: 900,
              fontSize: '22px',
              letterSpacing: '0.12em',
              display: 'inline-block',
              marginBottom: '16px',
            }}
          >
            NEON RUSH REMAKE
          </div>
          <h1
            style={{
              color: '#ffffff',
              fontSize: '62px',
              fontWeight: 900,
              margin: 0,
              textShadow: '0 8px 30px rgba(0,0,0,0.9), 0 0 20px rgba(239, 68, 68, 0.5)',
              lineHeight: 1.15,
            }}
          >
            BAGAIMANA MANUSIA MENEMUKAN <br />
            <span style={{ color: '#38bdf8', textShadow: '0 0 30px rgba(56, 189, 248, 0.9)' }}>
              AIR RAKSA?
            </span>
          </h1>
        </div>
      )}

      {/* 3. Campfire Center Stage (Vertical layout: bottom 520px) */}
      {frame >= 200 && (
        <div
          style={{
            position: 'absolute',
            bottom: '540px',
            left: '540px',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 200, fps, config: { damping: 12 } }) * 1.1})`,
            zIndex: 6,
          }}
        >
          <Img
            src={staticFile('assets/stickers/prehistoric_campfire.png')}
            style={{
              width: '500px',
              filter: `drop-shadow(0 0 ${35 + Math.sin(frame / 4) * 15}px rgba(249, 115, 22, 0.8))`,
            }}
          />
        </div>
      )}

      {/* 4. Cinnabar Crystal */}
      {frame >= 110 && frame < 260 && (
        <div
          style={{
            position: 'absolute',
            left: '380px',
            top: '720px',
            transform: `translateY(${idleBob}px) scale(${spring({ frame: frame - 110, fps, config: { damping: 10 } }) * 0.95})`,
            zIndex: 9,
          }}
        >
          <Img
            src={staticFile('assets/stickers/cinnabar_crystal.png')}
            style={{
              width: '360px',
              filter: 'drop-shadow(0 0 45px rgba(239, 68, 68, 0.95))',
            }}
          />
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.9)',
              border: '2px solid #ef4444',
              borderRadius: '10px',
              padding: '6px 16px',
              color: '#f8fafc',
              fontSize: '18px',
              fontWeight: 800,
              textAlign: 'center',
              marginTop: '-15px',
            }}
          >
            BATU CINABAR (HgS)
          </div>
        </div>
      )}

      {/* Phase B: Crystal Flying into Campfire */}
      {frame >= 260 && frame < 315 && (
        <div
          style={{
            position: 'absolute',
            left: `${crystalX}px`,
            top: `${crystalY}px`,
            transform: `translate(-50%, -50%) rotate(${crystalRot}deg) scale(0.8)`,
            zIndex: 10,
          }}
        >
          <Img
            src={staticFile('assets/stickers/cinnabar_crystal.png')}
            style={{
              width: '260px',
              filter: 'drop-shadow(0 0 35px rgba(239, 68, 68, 0.9))',
            }}
          />
        </div>
      )}

      {/* 5. Liquid Mercury Droplet Simulation */}
      {frame >= 369 && frame < 860 && (
        <div
          style={{
            position: 'absolute',
            bottom: '480px',
            left: '540px',
            transform: 'translateX(-50%)',
            zIndex: 15,
          }}
        >
          <LiquidMercuryDrop startFrame={369} scale={1.4} />
        </div>
      )}

      {/* 6. Caveman Stickman Actor */}
      <div
        style={{
          position: 'absolute',
          bottom: '500px',
          left: isShocked ? '80px' : '180px',
          transform: `scale(${cavemanEntrance * 1.05}) translateY(${idleBob}px)`,
          zIndex: 8,
          transition: 'left 0.4s cubic-bezier(0.16, 1, 0.3, 1)',
        }}
      >
        {isShocked ? (
          <Img
            src={staticFile('assets/stickers/caveman_shocked.png')}
            style={{
              width: '460px',
              filter: 'drop-shadow(0 15px 35px rgba(0,0,0,0.8))',
            }}
          />
        ) : (
          <Img
            src={staticFile('assets/stickers/caveman_curious.png')}
            style={{
              width: '460px',
              filter: 'drop-shadow(0 15px 35px rgba(0,0,0,0.8))',
            }}
          />
        )}
      </div>

      {/* 7. Quicksilver Properties Badges (Vertical layout: top 380px) */}
      {frame >= 610 && frame < 860 && (
        <div
          style={{
            position: 'absolute',
            left: '50%',
            top: '360px',
            transform: 'translateX(-50%)',
            display: 'flex',
            flexDirection: 'column',
            gap: '18px',
            zIndex: 20,
            width: '90%',
          }}
        >
          {[
            { icon: '💧', title: 'TIDAK MEMBASAHI KULIT', desc: 'Tegangan permukaan ultra-tinggi' },
            { icon: '🪞', title: 'MEMANTUL SEPERTI CERMIN', desc: 'Reflektansi logam 100%' },
            { icon: '⚖️', title: 'SANGAT BERAT', desc: 'Densitas 13.5x lebih padat dari air' },
          ].map((item, idx) => {
            const cardSpring = spring({
              frame: Math.max(0, frame - 610 - idx * 25),
              fps,
              config: { damping: 12 },
            });
            return (
              <div
                key={idx}
                style={{
                  transform: `scale(${cardSpring})`,
                  backgroundColor: 'rgba(15, 23, 42, 0.92)',
                  border: '2px solid #38bdf8',
                  borderRadius: '16px',
                  padding: '16px 24px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '16px',
                  boxShadow: '0 10px 30px rgba(0,0,0,0.7)',
                }}
              >
                <span style={{ fontSize: '36px' }}>{item.icon}</span>
                <div>
                  <div style={{ color: '#38bdf8', fontWeight: 800, fontSize: '20px' }}>
                    {item.title}
                  </div>
                  <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 500 }}>
                    {item.desc}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* 8. Alchemist Flask (Vertical Act 5) */}
      {frame >= 860 && frame < 1240 && (
        <div
          style={{
            position: 'absolute',
            right: '80px',
            top: '640px',
            transform: `scale(${spring({ frame: frame - 860, fps, config: { damping: 12 } }) * 0.9})`,
            zIndex: 10,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Img
            src={staticFile('assets/stickers/alchemist_flask.png')}
            style={{
              width: '360px',
              filter: 'drop-shadow(0 0 40px rgba(56, 189, 248, 0.6))',
            }}
          />
        </div>
      )}

      {/* 9. Climax Card (Vertical Act 6) */}
      {frame >= 1240 && (
        <div
          style={{
            position: 'absolute',
            top: '320px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 1240, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            zIndex: 25,
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            border: '3px solid #fbbf24',
            borderRadius: '24px',
            padding: '36px 40px',
            width: '88%',
            boxShadow: '0 20px 50px rgba(0,0,0,0.9), 0 0 30px rgba(251, 191, 36, 0.4)',
          }}
        >
          <div
            style={{
              color: '#fbbf24',
              fontWeight: 900,
              fontSize: '22px',
              letterSpacing: '0.12em',
              marginBottom: '12px',
            }}
          >
            ★ REVOLUSI ALKIMIA PURBA ★
          </div>
          <div
            style={{
              color: '#ffffff',
              fontSize: '40px',
              fontWeight: 900,
              lineHeight: 1.2,
            }}
          >
            DARI API UNGGUN KE SAINS MODERN
          </div>
        </div>
      )}

      {/* 10. HUD & Subtitles */}
      <PrehistoricHUD
        temperature={temperature}
        showReactionBadge={frame >= 860 && frame < 1240}
        currentCaption={currentCaption}
        isTikTok={true}
      />
    </div>
  );
};
