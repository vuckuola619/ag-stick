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

// Precise Sentence Timestamps from Edge-TTS
const SENTENCES = [
  { startFrame: 3, endFrame: 110, text: 'Bayangkan kamu adalah manusia purba 10.000 tahun lalu.' },
  { startFrame: 110, endFrame: 235, text: 'Kamu menemukan sebuah batu kristal merah delima yang aneh di dalam gua gelap.' },
  { startFrame: 235, endFrame: 369, text: 'Karena penasaran, kamu melemparkan batu merah itu ke dalam kobaran api unggun.' },
  { startFrame: 369, endFrame: 443, text: 'Tiba-tiba hal mustahil terjadi!' },
  { startFrame: 443, endFrame: 610, text: 'Batunya tidak hangus menjadi abu, melainkan mulai berdarah cairan perak mengkilap yang menetes dan mengalir!' },
  { startFrame: 610, endFrame: 772, text: 'Logam cair ini tidak membasahi kulitmu, memantul licin bagai cermin, dan sangat berat.' },
  { startFrame: 772, endFrame: 859, text: 'Inilah merkuri, atau Quicksilver!' },
  { startFrame: 859, endFrame: 994, text: 'Batu merah tersebut adalah Cinabar, senyawa alami merkuri dan sulfur.' },
  { startFrame: 994, endFrame: 1239, text: 'Panas api unggun di atas 357°C memecah ikatan kimianya, sehingga uapnya langsung mengembun menjadi tetesan air raksa murni.' },
  { startFrame: 1239, endFrame: 1470, text: 'Dari ketidaksengajaan manusia purba yang bermain api, lahirlah elemen paling mistis dan mematikan dalam sejarah peradaban!' },
];

export const MercuryMasterComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Determine current active caption
  const currentSentence = SENTENCES.find(
    (s) => frame >= s.startFrame && frame < s.endFrame
  );
  const currentCaption = currentSentence ? currentSentence.text : '';

  // Dynamic Temperature ramp
  const temperature = interpolate(
    frame,
    [0, 235, 369, 500, 994, 1150, 1512],
    [25, 28, 160, 365, 375, 410, 320],
    { extrapolateRight: 'clamp' }
  );

  // Screen shake on dramatic moments (Frame 369 - 450)
  const isShocked = frame >= 369 && frame < 520;
  const shakeX = isShocked ? Math.sin(frame * 2.2) * 8 : 0;
  const shakeY = isShocked ? Math.cos(frame * 2.0) * 6 : 0;

  // Caveman entrance spring
  const cavemanEntrance = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 90 },
  });

  // Bobbing animation for characters
  const idleBob = Math.sin(frame / 7) * 4;

  // Crystal throw trajectory (Frame 260 to 320)
  const crystalThrowProgress = interpolate(frame, [260, 310], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const crystalX = interpolate(crystalThrowProgress, [0, 1], [620, 960]);
  const crystalY = interpolate(crystalThrowProgress, [0, 0.5, 1], [520, 320, 620]);
  const crystalRot = interpolate(crystalThrowProgress, [0, 1], [0, 360]);

  // Outro fade to black
  const outroOpacity = interpolate(frame, [1475, 1510], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: 1920,
        height: 1080,
        overflow: 'hidden',
        backgroundColor: '#05070e',
        transform: `translate(${shakeX}px, ${shakeY}px)`,
        opacity: outroOpacity,
      }}
    >
      {/* 1. Layered Prehistoric Cave Background */}
      <MercuryCaveBackground fireActive={frame >= 180} />

      {/* 2. Main Title Billboard (Act 1: Frames 10 - 210) */}
      {frame >= 10 && frame < 220 && (
        <div
          style={{
            position: 'absolute',
            top: '120px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 10, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            zIndex: 10,
          }}
        >
          <div
            style={{
              backgroundColor: '#fbbf24',
              color: '#0f172a',
              padding: '6px 20px',
              borderRadius: '8px',
              fontWeight: 900,
              fontSize: '18px',
              letterSpacing: '0.1em',
              display: 'inline-block',
              marginBottom: '10px',
              boxShadow: '0 4px 15px rgba(251, 191, 36, 0.4)',
            }}
          >
            NEON RUSH REMAKE // MASTERCLASS
          </div>
          <h1
            style={{
              color: '#ffffff',
              fontSize: '56px',
              fontWeight: 900,
              fontFamily: "'Inter', sans-serif",
              margin: 0,
              textShadow: '0 8px 30px rgba(0,0,0,0.9), 0 0 20px rgba(239, 68, 68, 0.4)',
              lineHeight: 1.15,
            }}
          >
            BAGAIMANA MANUSIA MENEMUKAN <br />
            <span style={{ color: '#38bdf8', textShadow: '0 0 25px rgba(56, 189, 248, 0.8)' }}>
              AIR RAKSA (QUICKSILVER)?
            </span>
          </h1>
        </div>
      )}

      {/* 3. Prehistoric Campfire Center Stage (Appears frame 200+) */}
      {frame >= 200 && (
        <div
          style={{
            position: 'absolute',
            bottom: '220px',
            left: '960px',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 200, fps, config: { damping: 12 } }) * 0.95})`,
            zIndex: 5,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Img
            src={staticFile('assets/stickers/prehistoric_campfire.png')}
            style={{
              width: '460px',
              filter: `drop-shadow(0 0 ${30 + Math.sin(frame / 4) * 15}px rgba(249, 115, 22, 0.75))`,
            }}
          />
        </div>
      )}

      {/* 4. Glowing Cinnabar Crystal */}
      {/* Phase A: In caveman hand / floating (Frame 110 - 260) */}
      {frame >= 110 && frame < 260 && (
        <div
          style={{
            position: 'absolute',
            left: '700px',
            top: '400px',
            transform: `translateY(${idleBob}px) scale(${spring({ frame: frame - 110, fps, config: { damping: 10 } }) * 0.85})`,
            zIndex: 8,
          }}
        >
          <Img
            src={staticFile('assets/stickers/cinnabar_crystal.png')}
            style={{
              width: '320px',
              filter: 'drop-shadow(0 0 35px rgba(239, 68, 68, 0.9)) drop-shadow(0 0 60px rgba(239, 68, 68, 0.5))',
            }}
          />
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.85)',
              border: '2px solid #ef4444',
              borderRadius: '8px',
              padding: '4px 12px',
              color: '#f8fafc',
              fontSize: '14px',
              fontWeight: 800,
              textAlign: 'center',
              marginTop: '-15px',
              boxShadow: '0 4px 15px rgba(0,0,0,0.6)',
            }}
          >
            BATU CINABAR (HgS)
          </div>
        </div>
      )}

      {/* Phase B: Flying into the fire (Frame 260 - 315) */}
      {frame >= 260 && frame < 315 && (
        <div
          style={{
            position: 'absolute',
            left: `${crystalX}px`,
            top: `${crystalY}px`,
            transform: `translate(-50%, -50%) rotate(${crystalRot}deg) scale(0.65)`,
            zIndex: 9,
          }}
        >
          <Img
            src={staticFile('assets/stickers/cinnabar_crystal.png')}
            style={{
              width: '240px',
              filter: 'drop-shadow(0 0 30px rgba(239, 68, 68, 0.9))',
            }}
          />
        </div>
      )}

      {/* 5. Liquid Mercury Droplet Simulation & Puddle */}
      {frame >= 369 && frame < 860 && (
        <div
          style={{
            position: 'absolute',
            bottom: '180px',
            left: '960px',
            transform: 'translateX(-50%)',
            zIndex: 15,
          }}
        >
          <LiquidMercuryDrop startFrame={369} scale={1.25} />
        </div>
      )}

      {/* Act 4: Liquid Chrome Quicksilver Puddle Close-up */}
      {frame >= 610 && frame < 860 && (
        <div
          style={{
            position: 'absolute',
            bottom: '210px',
            left: '960px',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 610, fps, config: { damping: 12 } }) * 0.85})`,
            zIndex: 14,
          }}
        >
          <Img
            src={staticFile('assets/stickers/mercury_puddle.png')}
            style={{
              width: '450px',
              filter: 'drop-shadow(0 0 25px rgba(255,255,255,0.7)) drop-shadow(0 15px 35px rgba(0,0,0,0.8))',
            }}
          />
        </div>
      )}

      {/* 6. Caveman Stickman Actor */}
      <div
        style={{
          position: 'absolute',
          bottom: '220px',
          left: isShocked ? '320px' : '480px',
          transform: `scale(${cavemanEntrance * 0.92}) translateY(${idleBob}px)`,
          zIndex: 8,
          transition: 'left 0.4s cubic-bezier(0.16, 1, 0.3, 1)',
        }}
      >
        {isShocked ? (
          <Img
            src={staticFile('assets/stickers/caveman_shocked.png')}
            style={{
              width: '420px',
              filter: 'drop-shadow(0 15px 30px rgba(0,0,0,0.8))',
            }}
          />
        ) : (
          <Img
            src={staticFile('assets/stickers/caveman_curious.png')}
            style={{
              width: '420px',
              filter: 'drop-shadow(0 15px 30px rgba(0,0,0,0.8))',
            }}
          />
        )}
      </div>

      {/* 7. Quicksilver Properties Badges (Act 4: Frames 610 - 859) */}
      {frame >= 610 && frame < 860 && (
        <div
          style={{
            position: 'absolute',
            right: '180px',
            top: '280px',
            display: 'flex',
            flexDirection: 'column',
            gap: '20px',
            zIndex: 20,
          }}
        >
          {[
            { icon: '💧', title: 'TIDAK MEMBASAHI', desc: 'Tegangan permukaan ultra-tinggi' },
            { icon: '🪞', title: 'MEMANTUL SEPERTI CERMIN', desc: 'Reflektansi logam 100%' },
            { icon: '⚖️', title: 'BERAT SEPERTI TIMAH', desc: 'Densitas 13.5x lebih padat dari air' },
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
                  backgroundColor: 'rgba(15, 23, 42, 0.9)',
                  border: '2px solid #38bdf8',
                  borderRadius: '16px',
                  padding: '16px 24px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '16px',
                  boxShadow: '0 10px 25px rgba(0,0,0,0.6)',
                  width: '380px',
                }}
              >
                <span style={{ fontSize: '32px' }}>{item.icon}</span>
                <div>
                  <div style={{ color: '#38bdf8', fontWeight: 800, fontSize: '18px' }}>
                    {item.title}
                  </div>
                  <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 500 }}>
                    {item.desc}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* 8. Ancient Alchemical Retorta & Qin Shi Huang Lore (Act 5: Frames 860 - 1240) */}
      {frame >= 860 && frame < 1240 && (
        <div
          style={{
            position: 'absolute',
            right: '220px',
            bottom: '160px',
            transform: `scale(${spring({ frame: frame - 860, fps, config: { damping: 12 } }) * 0.85})`,
            zIndex: 10,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Img
            src={staticFile('assets/stickers/alchemist_flask.png')}
            style={{
              width: '380px',
              filter: 'drop-shadow(0 0 35px rgba(56, 189, 248, 0.6))',
            }}
          />
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.9)',
              border: '2px solid #fbbf24',
              borderRadius: '12px',
              padding: '8px 20px',
              color: '#fbbf24',
              fontSize: '15px',
              fontWeight: 800,
              marginTop: '-20px',
              textAlign: 'center',
              boxShadow: '0 6px 20px rgba(0,0,0,0.8)',
            }}
          >
            LABU DISTILASI ALKIMIA KUNO
          </div>
        </div>
      )}

      {/* 9. Climax & Outro Badge (Act 6: Frames 1240 - 1512) */}
      {frame >= 1240 && (
        <div
          style={{
            position: 'absolute',
            top: '200px',
            left: '50%',
            transform: `translateX(-50%) scale(${spring({ frame: frame - 1240, fps, config: { damping: 12 } })})`,
            textAlign: 'center',
            zIndex: 25,
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            border: '3px solid #fbbf24',
            borderRadius: '24px',
            padding: '36px 60px',
            boxShadow: '0 20px 50px rgba(0,0,0,0.9), 0 0 30px rgba(251, 191, 36, 0.4)',
          }}
        >
          <div
            style={{
              color: '#fbbf24',
              fontWeight: 900,
              fontSize: '20px',
              letterSpacing: '0.15em',
              marginBottom: '10px',
            }}
          >
            ★ REVOLUSI ALKIMIA & SAINS PURBA ★
          </div>
          <div
            style={{
              color: '#ffffff',
              fontSize: '44px',
              fontWeight: 900,
              lineHeight: 1.2,
            }}
          >
            DARI GUA BATU KE TEKNOLOGI MODERN
          </div>
          <div
            style={{
              color: '#94a3b8',
              fontSize: '18px',
              marginTop: '15px',
              fontWeight: 600,
            }}
          >
            Termometer • Ekstraksi Emas • Barometer • Fisika Fluida
          </div>
        </div>
      )}

      {/* 10. Live Prehistoric HUD & Subtitles */}
      <PrehistoricHUD
        temperature={temperature}
        showReactionBadge={frame >= 860 && frame < 1240}
        currentCaption={currentCaption}
        isTikTok={false}
      />
    </div>
  );
};
