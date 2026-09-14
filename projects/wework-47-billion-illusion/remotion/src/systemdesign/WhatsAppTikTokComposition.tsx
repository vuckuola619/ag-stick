import React from 'react';
import { Sequence, useCurrentFrame, interpolate, Img, staticFile } from 'remotion';
import { TechStudioBackground } from './components/TechStudioBackground';
import { TCPSocketGauge } from './components/TCPSocketGauge';
import { BEAMProcessCloud } from './components/BEAMProcessCloud';
import { GitHubRepoBadge } from './components/GitHubRepoBadge';
import { MemeDevQuote } from './components/MemeDevQuotes';
import { TechDevActor } from './components/TechDevActor';
import { SystemNodeV2 } from './components/SystemNodeV2';
import { PacketConnection } from './components/PacketConnection';
import { HandDrawnAnnotation } from './components/HandDrawnAnnotation';

export const WhatsAppTikTokComposition: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <div
      style={{
        flex: 1,
        width: 1080,
        height: 1920,
        position: 'relative',
        backgroundColor: '#070b14',
        overflow: 'hidden',
        fontFamily: 'Inter, system-ui, sans-serif',
      }}
    >
      <TechStudioBackground />

      {/* Top TikTok Header */}
      <div
        style={{
          position: 'absolute',
          top: '70px',
          left: '50px',
          right: '50px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          zIndex: 100,
        }}
      >
        <div
          style={{
            backgroundColor: '#25d366',
            color: '#064e3b',
            fontSize: '18px',
            fontWeight: 900,
            padding: '8px 24px',
            borderRadius: '24px',
            letterSpacing: '0.08em',
            marginBottom: '12px',
            boxShadow: '0 4px 20px rgba(37, 211, 102, 0.5)',
          }}
        >
          🔥 SYSTEM DESIGN MASTERCLASS
        </div>
        <div
          style={{
            color: '#f8fafc',
            fontSize: '48px',
            fontWeight: 900,
            letterSpacing: '-0.03em',
            lineHeight: '1.15',
            textShadow: '0 4px 25px rgba(0,0,0,0.95)',
          }}
        >
          How <span style={{ color: '#25d366' }}>50 Devs</span> Scaled WhatsApp to <span style={{ color: '#38bdf8' }}>2 Billion</span> Users
        </div>
      </div>

      {/* =========================================================
          ACT 1: THE ERLANG SECRET WEAPON (Frames 0 - 747 | 0.0s - 25.0s)
          ========================================================= */}
      <Sequence from={0} durationInFrames={748}>
        {/* Metric Bar */}
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2px solid #25d366', borderRadius: '16px', padding: '12px 20px' }}>
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>TEAM SIZE</div>
            <div style={{ color: '#25d366', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>50 Devs</div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800 }}>ACTIVE USERS</div>
            <div style={{ color: '#38bdf8', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>2,000,000,000</div>
            <div style={{ color: '#34d399', fontSize: '18px', fontWeight: 800 }}>Erlang / BEAM VM</div>
          </div>
        </div>

        {frame < 242 ? (
          <>
            <div style={{ position: 'absolute', left: '380px', top: '420px' }}>
              <TechDevActor role="senior_architect" label="50 Erlang Chads" sublabel="Mountain View" size={320} />
            </div>
            <div style={{ position: 'absolute', left: '80px', top: '820px' }}>
              <MemeDevQuote quote="Keep it simple. Plain Erlang, FreeBSD, and zero meeting fluff." author="WhatsApp Dev" variant="senior" />
            </div>

            <div style={{ position: 'absolute', left: '380px', top: '1060px' }}>
              <TechDevActor role="devops_oncall" label="500 Corporate Devs" sublabel="Login Page Down" isStressed={true} size={320} />
            </div>
            <div style={{ position: 'absolute', left: '80px', top: '1440px' }}>
              <MemeDevQuote quote="WHO TOUCHED THE HELM CHART?! THE LOGIN PAGE IS DOWN AGAIN!" author="Enterprise Dev" variant="panic" />
            </div>
          </>
        ) : (
          <>
            <div style={{ position: 'absolute', left: '180px', top: '420px' }}>
              <BEAMProcessCloud />
            </div>

            <div style={{ position: 'absolute', left: '340px', top: '760px' }}>
              <SystemNodeV2
                type="WebServer"
                title="Erlang / BEAM Server"
                tech="Lightweight Actor Concurrency"
                scaleCount="1M+ Processes"
                status="healthy"
                cpuPercent={18}
                width={400}
                height={180}
              />
            </div>

            <div style={{ position: 'absolute', left: '340px', top: '980px' }}>
              <GitHubRepoBadge repo="erlang/otp" stars="12.5k" topic="Telecom Concurrency" />
            </div>

            {/* 9router Erlang Shield Sticker */}
            <div
              style={{
                position: 'absolute',
                left: '120px',
                top: '760px',
                transform: `translateY(${Math.sin(frame / 14) * 6}px)`,
                zIndex: 110,
              }}
            >
              <Img
                src={staticFile('assets/stickers/erlang_shield.png')}
                style={{
                  width: '170px',
                  height: '170px',
                  filter: 'drop-shadow(0 0 25px rgba(37, 211, 102, 0.6))',
                }}
              />
            </div>

            <div style={{ position: 'absolute', left: '80px', top: '1120px' }}>
              <TechDevActor role="senior_architect" label="Erlang Wizard" sublabel="BEAM Master" size={340} />
            </div>
            <div style={{ position: 'absolute', left: '440px', top: '1180px' }}>
              <MemeDevQuote quote="One user = One Erlang process. 300 bytes of RAM. We can run millions!" author="Erlang Wizard" variant="senior" />
            </div>
          </>
        )}

        {/* Caption Card */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #25d366', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              {frame < 242
                ? '50 engineers ran WhatsApp for 2B users while big tech needs 500 devs for a login page!'
                : 'Secret: Erlang BEAM processes take 300 bytes of RAM vs 2MB OS threads. Millions concurrent!'}
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 2: THE C2M PROBLEM (Frames 748 - 1250 | 25.0s - 41.7s)
          ========================================================= */}
      <Sequence from={748} durationInFrames={503}>
        {(() => {
          const actFrame = frame - 748;
          const sockets = interpolate(actFrame, [0, 400], [500000, 2800000], { extrapolateRight: 'clamp' });
          const isPeak = actFrame > 250;

          return (
            <>
              {/* Gauge */}
              <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', zIndex: 90 }}>
                <TCPSocketGauge currentSockets={sockets} maxSockets={3000000} isPeak={isPeak} />
              </div>

              {/* Single Server Node */}
              <div style={{ position: 'absolute', left: '330px', top: '480px' }}>
                <SystemNodeV2
                  type="WebServer"
                  title="FreeBSD Bare Metal"
                  tech="Dual Intel Xeon (No Cloud VM)"
                  scaleCount="1 PHYSICAL BOX"
                  status="healthy"
                  cpuPercent={isPeak ? 48 : 26}
                  width={420}
                  height={180}
                />
              </div>

              {/* 9router FreeBSD Beastie Mascot Sticker */}
              <div
                style={{
                  position: 'absolute',
                  left: '120px',
                  top: '470px',
                  transform: `translateY(${Math.sin((frame + 20) / 14) * 8}px)`,
                  zIndex: 110,
                }}
              >
                <Img
                  src={staticFile('assets/stickers/freebsd_mascot.png')}
                  style={{
                    width: '180px',
                    height: '180px',
                    filter: 'drop-shadow(0 10px 25px rgba(239, 68, 68, 0.45))',
                  }}
                />
              </div>

              {/* Tuning secrets box */}
              <div
                style={{
                  position: 'absolute',
                  left: '80px',
                  top: '700px',
                  right: '80px',
                  backgroundColor: 'rgba(15, 23, 42, 0.95)',
                  border: '2px solid #38bdf8',
                  borderRadius: '20px',
                  padding: '24px',
                  boxShadow: '0 12px 30px rgba(0,0,0,0.8)',
                }}
              >
                <div style={{ color: '#38bdf8', fontSize: '18px', fontWeight: 900, marginBottom: '10px' }}>
                  🛠️ FREEBSD KERNEL TUNING SECRETS
                </div>
                <div style={{ fontFamily: 'monospace', fontSize: '15px', color: '#e2e8f0', lineHeight: '1.8' }}>
                  <div>• <span style={{ color: '#25d366' }}>kern.ipc.maxsockets</span> = 3,000,000</div>
                  <div>• <span style={{ color: '#25d366' }}>kern.maxfilesperproc</span> = 2,500,000</div>
                  <div>• Custom PCI network driver interrupts</div>
                </div>
              </div>

              <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
                <TechDevActor role="senior_architect" label="Rick Reed" sublabel="WhatsApp Architect" size={340} />
              </div>
              <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
                <MemeDevQuote quote="Why pay AWS for 500 EC2 instances when 1 FreeBSD box handles 2.8M users?" author="Rick Reed" variant="senior" />
              </div>

              {/* Caption */}
              <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
                <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #38bdf8', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
                  <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
                    "C2M Problem Solved: 2.8 Million concurrent TCP connections on a SINGLE physical FreeBSD server!"
                  </div>
                </div>
              </div>
            </>
          );
        })()}
      </Sequence>

      {/* =========================================================
          ACT 3: EPHEMERAL ZERO-DISK STORAGE (Frames 1251 - 1702 | 41.7s - 56.8s)
          ========================================================= */}
      <Sequence from={1251} durationInFrames={452}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #25d366', borderRadius: '16px', padding: '12px 20px' }}>
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>SERVER DISK FOOTPRINT</div>
            <div style={{ color: '#25d366', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>0 BYTES</div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800 }}>SAVED ON STORAGE</div>
            <div style={{ color: '#4ade80', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>$40M / Year</div>
          </div>
        </div>

        {/* Sender & Receiver */}
        <div style={{ position: 'absolute', left: '160px', top: '440px' }}>
          <TechDevActor role="client_user" label="Alice (Phone A)" size={260} />
        </div>
        <div style={{ position: 'absolute', left: '660px', top: '440px' }}>
          <TechDevActor role="client_user" label="Bob (Phone B)" size={260} />
        </div>

        <div style={{ position: 'absolute', left: '330px', top: '740px' }}>
          <SystemNodeV2
            type="WebServer"
            title="In-Memory Queue"
            tech="Store-and-Forward (RAM Only)"
            status="healthy"
            cpuPercent={14}
            width={420}
            height={180}
          />
        </div>

        <div
          style={{
            position: 'absolute',
            left: '80px',
            top: '960px',
            right: '80px',
            backgroundColor: 'rgba(37, 211, 102, 0.15)',
            border: '2px solid #25d366',
            borderRadius: '20px',
            padding: '20px',
            textAlign: 'center',
          }}
        >
          <div style={{ color: '#25d366', fontSize: '18px', fontWeight: 900, marginBottom: '6px' }}>
            🔥 INSTANT DISK PURGE ON DELIVERY
          </div>
          <div style={{ color: '#f8fafc', fontSize: '15px', lineHeight: '1.4' }}>
            WhatsApp server never stores message history. Delivered $\to$ Purged forever!
          </div>
        </div>

        <div style={{ position: 'absolute', left: '80px', top: '1180px' }}>
          <TechDevActor role="senior_architect" label="Architect" sublabel="Zero Disk" size={320} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1240px' }}>
          <MemeDevQuote quote="The cheapest database query is the one you never store on disk." author="Senior Architect" variant="senior" />
        </div>

        {/* Caption */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #25d366', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "Zero-disk storage: The second a message is delivered to your phone, it is purged forever from server disk!"
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 4: MNESIA CLUSTERING (Frames 1703 - 1935 | 56.8s - 64.5s)
          ========================================================= */}
      <Sequence from={1703} durationInFrames={233}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2px solid #c084fc', borderRadius: '16px', padding: '12px 20px' }}>
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>DAILY MESSAGES</div>
            <div style={{ color: '#c084fc', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>100 Billion</div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800 }}>SECURITY</div>
            <div style={{ color: '#25d366', fontSize: '32px', fontWeight: 900 }}>E2E Signal Protocol</div>
          </div>
        </div>

        <div style={{ position: 'absolute', left: '120px', top: '460px' }}>
          <SystemNodeV2 type="Cache" title="Mnesia RAM Cluster" tech="Distributed In-Memory Tables" status="healthy" cpuPercent={22} width={380} height={170} />
        </div>
        <div style={{ position: 'absolute', left: '580px', top: '460px' }}>
          <SystemNodeV2 type="WebServer" title="Signal Protocol" tech="Keys on Client Phones" status="healthy" cpuPercent={16} width={380} height={170} />
        </div>

        <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
          <TechDevActor role="senior_architect" label="50 Engineers" sublabel="Quiet Mountain View Office" size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
          <MemeDevQuote quote="No SQL join hell. Just in-memory routing tables and sleep like a king." author="WhatsApp Dev" variant="senior" />
        </div>

        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #c084fc', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "100 Billion messages a day: Mnesia in-memory routing tables + end-to-end client encryption!"
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 5: $19B ACQUISITION & THE MORAL (Frames 1936 - 2370 | 64.5s - 79.0s)
          ========================================================= */}
      <Sequence from={1936} durationInFrames={435}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #fbbf24', borderRadius: '16px', padding: '12px 20px' }}>
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>ACQUISITION (2014)</div>
            <div style={{ color: '#fbbf24', fontSize: '40px', fontWeight: 900, fontFamily: 'monospace' }}>$19 BILLION</div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800 }}>VALUE PER DEV</div>
            <div style={{ color: '#4ade80', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>$380,000,000</div>
          </div>
        </div>

        <div style={{ position: 'absolute', left: '80px', top: '480px', right: '80px', backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #fbbf24', borderRadius: '24px', padding: '28px', boxShadow: '0 16px 40px rgba(0,0,0,0.85)' }}>
          <div style={{ color: '#fbbf24', fontSize: '24px', fontWeight: 900, marginBottom: '14px' }}>
            💰 HIGHEST VALUE PER ENGINEER IN TECH HISTORY
          </div>
          <div style={{ color: '#f8fafc', fontSize: '18px', lineHeight: '1.7', fontWeight: 600 }}>
            • 2 Billion Daily Active Users<br />
            • 100 Billion Messages Daily<br />
            • Just 50 Software Engineers<br />
            • Zero Microservice Sprawl
          </div>
        </div>

        {/* 9router 19 Billion Trophy Sticker */}
        <div
          style={{
            position: 'absolute',
            left: '50%',
            top: '770px',
            transform: `translateX(-50%) scale(${1 + Math.sin(frame / 16) * 0.04})`,
            zIndex: 110,
          }}
        >
          <Img
            src={staticFile('assets/stickers/trophy_19b.png')}
            style={{
              width: '280px',
              height: '280px',
              filter: 'drop-shadow(0 0 40px rgba(251, 191, 36, 0.75))',
            }}
          />
        </div>

        <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
          <TechDevActor role="cto_panic" label="Silicon Valley VC" sublabel="Completely Stunned" isStressed={true} size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
          <MemeDevQuote quote="Wait... you didn't use 800 microservices and 400 sprint meetings?!" author="Tech VC" variant="cto" />
        </div>

        {/* Caption */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #fbbf24', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "Facebook acquired WhatsApp for $19 Billion ($380M per engineer!). Simple architecture wins!"
            </div>
          </div>
        </div>

        {/* Mobile Grand Finale Card (Frame 2197 - 2370) */}
        {frame >= 2197 && (
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              transform: 'translate(-50%, -50%)',
              width: '920px',
              backgroundColor: 'rgba(15, 23, 42, 0.98)',
              border: '4px solid #25d366',
              borderRadius: '28px',
              padding: '36px 28px',
              boxShadow: '0 0 70px rgba(37, 211, 102, 0.7), 0 30px 60px rgba(0,0,0,0.95)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              textAlign: 'center',
              zIndex: 999,
            }}
          >
            <div style={{ fontSize: '64px', marginBottom: '12px' }}>🏆</div>
            <div style={{ color: '#25d366', fontSize: '38px', fontWeight: 900, letterSpacing: '0.02em', marginBottom: '10px' }}>
              SIMPLE ARCHITECTURE ALWAYS BEATS
            </div>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900 }}>
              RESUME-DRIVEN COMPLEXITY!
            </div>
          </div>
        )}
      </Sequence>
    </div>
  );
};
