import React from 'react';
import { Sequence, useCurrentFrame, interpolate, Img, staticFile } from 'remotion';
import { TechStudioBackground } from './components/TechStudioBackground';
import { WhatsAppHeader } from './components/WhatsAppHeader';
import { TCPSocketGauge } from './components/TCPSocketGauge';
import { BEAMProcessCloud } from './components/BEAMProcessCloud';
import { GitHubRepoBadge } from './components/GitHubRepoBadge';
import { MemeDevQuote } from './components/MemeDevQuotes';
import { TechDevActor } from './components/TechDevActor';
import { SystemNodeV2 } from './components/SystemNodeV2';
import { PacketConnection } from './components/PacketConnection';
import { HandDrawnAnnotation } from './components/HandDrawnAnnotation';

export const WhatsAppMasterComposition: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <div
      style={{
        flex: 1,
        width: 1920,
        height: 1080,
        position: 'relative',
        backgroundColor: '#070b14',
        overflow: 'hidden',
        fontFamily: 'Inter, system-ui, sans-serif',
      }}
    >
      {/* Studio Lighting Background */}
      <TechStudioBackground />

      {/* WhatsApp Branded Header */}
      <WhatsAppHeader />

      {/* =========================================================
          ACT 1: THE ERLANG SECRET WEAPON (Frames 0 - 747 | 0.0s - 25.0s)
          ========================================================= */}
      <Sequence from={0} durationInFrames={748}>
        {/* Top Right: Team Size vs Scale HUD */}
        <div
          style={{
            position: 'absolute',
            top: '35px',
            right: '50px',
            display: 'flex',
            gap: '16px',
            zIndex: 100,
          }}
        >
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '2px solid #25d366',
              borderRadius: '16px',
              padding: '14px 20px',
              boxShadow: '0 8px 25px rgba(37, 211, 102, 0.25)',
              display: 'flex',
              flexDirection: 'column',
            }}
          >
            <span style={{ color: '#94a3b8', fontSize: '12px', fontWeight: 800 }}>ENGINEERING TEAM</span>
            <span style={{ color: '#25d366', fontSize: '28px', fontWeight: 900, fontFamily: 'monospace' }}>50 Devs</span>
          </div>

          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '2px solid #38bdf8',
              borderRadius: '16px',
              padding: '14px 20px',
              boxShadow: '0 8px 25px rgba(0,0,0,0.6)',
              display: 'flex',
              flexDirection: 'column',
              textAlign: 'right',
            }}
          >
            <span style={{ color: '#94a3b8', fontSize: '12px', fontWeight: 800 }}>ACTIVE USERS</span>
            <span style={{ color: '#38bdf8', fontSize: '28px', fontWeight: 900, fontFamily: 'monospace' }}>
              {Math.floor(interpolate(frame, [0, 600], [450000000, 2000000000], { extrapolateRight: 'clamp' })).toLocaleString()}
            </span>
          </div>
        </div>

        {/* Phase 1A: 0 - 241 frames (50 devs vs 500 devs) */}
        {frame < 242 ? (
          <>
            <div style={{ position: 'absolute', left: '160px', top: '340px' }}>
              <TechDevActor role="senior_architect" label="50 Erlang Chads" sublabel="Mountain View HQ" size={320} />
            </div>
            <div style={{ position: 'absolute', left: '460px', top: '320px' }}>
              <MemeDevQuote quote="Keep it simple. Plain Erlang, FreeBSD, and zero meeting fluff." author="WhatsApp Engineer" variant="senior" />
            </div>

            <div style={{ position: 'absolute', left: '1060px', top: '340px' }}>
              <TechDevActor role="devops_oncall" label="500 Corporate Devs" sublabel="K8s Pod CrashLoop" isStressed={true} size={320} />
            </div>
            <div style={{ position: 'absolute', left: '1360px', top: '320px' }}>
              <MemeDevQuote quote="WHO TOUCHED THE HELM CHART?! THE LOGIN PAGE IS DOWN AGAIN!" author="Enterprise Architect" variant="panic" />
            </div>
          </>
        ) : (
          /* Phase 1B: 242 - 747 frames (Erlang BEAM Actor vs OS Thread) */
          <>
            <div style={{ position: 'absolute', left: '200px', top: '340px' }}>
              <BEAMProcessCloud />
            </div>

            <div style={{ position: 'absolute', left: '980px', top: '320px' }}>
              <SystemNodeV2
                type="WebServer"
                title="Erlang / BEAM Node"
                tech="Lightweight Actor Concurrency"
                scaleCount="1M+ Sockets"
                status="healthy"
                cpuPercent={18}
                width={380}
                height={170}
              />
            </div>

            <PacketConnection from={{ x: 600, y: 440 }} to={{ x: 980, y: 440 }} label="300B ACTOR MSG" packetColor="#25d366" speedFrames={12} />

            <div style={{ position: 'absolute', left: '1420px', top: '340px' }}>
              <TechDevActor role="senior_architect" label="Erlang Wizard" sublabel="BEAM Master" size={320} />
            </div>
            <div style={{ position: 'absolute', left: '1540px', top: '260px' }}>
              <MemeDevQuote quote="One user connection = One Erlang actor. 2 million? Not even warm." author="Erlang Wizard" variant="senior" />
            </div>

            <div style={{ position: 'absolute', left: '980px', top: '530px' }}>
              <GitHubRepoBadge repo="erlang/otp" stars="12.5k" topic="Telecom Concurrency" />
            </div>

            {/* 9router Erlang Shield Sticker */}
            <div
              style={{
                position: 'absolute',
                left: '840px',
                top: '290px',
                transform: `translateY(${Math.sin(frame / 15) * 6}px)`,
                zIndex: 110,
              }}
            >
              <Img
                src={staticFile('assets/stickers/erlang_shield.png')}
                style={{
                  width: '130px',
                  height: '130px',
                  filter: 'drop-shadow(0 0 25px rgba(37, 211, 102, 0.55))',
                }}
              />
            </div>
          </>
        )}
      </Sequence>

      {/* =========================================================
          ACT 2: THE C2M PROBLEM & FREEBSD HACKING (Frames 748 - 1250 | 25.0s - 41.7s)
          ========================================================= */}
      <Sequence from={748} durationInFrames={503}>
        {(() => {
          const actFrame = frame - 748;
          const sockets = interpolate(actFrame, [0, 400], [500000, 2800000], { extrapolateRight: 'clamp' });
          const isPeak = actFrame > 250;

          return (
            <>
              {/* Top Right Gauge & Specs */}
              <div style={{ position: 'absolute', top: '35px', right: '50px', zIndex: 100 }}>
                <TCPSocketGauge currentSockets={sockets} maxSockets={3000000} isPeak={isPeak} />
              </div>

              {/* Single Physical FreeBSD Server Box */}
              <div style={{ position: 'absolute', left: '260px', top: '340px' }}>
                <SystemNodeV2
                  type="WebServer"
                  title="FreeBSD Bare Metal"
                  tech="Dual Intel Xeon // 24 Cores"
                  scaleCount="1 PHYSICAL BOX"
                  status="healthy"
                  cpuPercent={isPeak ? 48 : 28}
                  width={420}
                  height={190}
                />
              </div>

              {/* 9router FreeBSD Beastie Mascot Sticker */}
              <div
                style={{
                  position: 'absolute',
                  left: '120px',
                  top: '340px',
                  transform: `translateY(${Math.sin((frame + 20) / 14) * 8}px)`,
                  zIndex: 110,
                }}
              >
                <Img
                  src={staticFile('assets/stickers/freebsd_mascot.png')}
                  style={{
                    width: '140px',
                    height: '140px',
                    filter: 'drop-shadow(0 10px 25px rgba(239, 68, 68, 0.45))',
                  }}
                />
              </div>

              {/* Multiple Client Connections Converging */}
              <div style={{ position: 'absolute', left: '40px', top: '240px' }}>
                <TechDevActor role="client_user" label="1.4M EU Users" size={220} />
              </div>
              <div style={{ position: 'absolute', left: '40px', top: '520px' }}>
                <TechDevActor role="client_user" label="1.4M Asia Users" size={220} />
              </div>

              <PacketConnection from={{ x: 160, y: 320 }} to={{ x: 260, y: 410 }} label="TLS TCP" packetColor="#38bdf8" speedFrames={10} />
              <PacketConnection from={{ x: 160, y: 600 }} to={{ x: 260, y: 450 }} label="TLS TCP" packetColor="#38bdf8" speedFrames={10} />

              {/* FreeBSD Kernel Tuning Cards */}
              <div
                style={{
                  position: 'absolute',
                  left: '740px',
                  top: '320px',
                  width: '420px',
                  backgroundColor: 'rgba(15, 23, 42, 0.95)',
                  border: '2px solid #38bdf8',
                  borderRadius: '20px',
                  padding: '24px',
                  boxShadow: '0 12px 30px rgba(0,0,0,0.8)',
                }}
              >
                <div style={{ color: '#38bdf8', fontSize: '16px', fontWeight: 900, marginBottom: '12px' }}>
                  🛠️ FREEBSD KERNEL TUNING SECRETS
                </div>
                <div style={{ fontFamily: 'monospace', fontSize: '13px', color: '#e2e8f0', lineHeight: '1.8' }}>
                  <div>• <span style={{ color: '#25d366' }}>kern.ipc.maxsockets</span> = 3,000,000</div>
                  <div>• <span style={{ color: '#25d366' }}>kern.maxfilesperproc</span> = 2,500,000</div>
                  <div>• Zero Linux epoll lock contention</div>
                  <div>• Custom PCI network driver interrupts</div>
                </div>
              </div>

              <HandDrawnAnnotation
                type="circle"
                x={240}
                y={320}
                width={460}
                height={230}
                text="World Record: 2.8M TCP connections on 1 machine!"
                color="#25d366"
                startFrame={50}
              />

              {/* Dev Quote */}
              <div style={{ position: 'absolute', left: '1220px', top: '340px' }}>
                <TechDevActor role="senior_architect" label="Lead Architect" sublabel="Rick Reed" size={320} />
              </div>
              <div style={{ position: 'absolute', left: '1360px', top: '260px' }}>
                <MemeDevQuote quote="Why rent 500 AWS EC2 instances when 1 tuned FreeBSD box handles 2.8 million users?" author="Rick Reed (WhatsApp)" variant="senior" />
              </div>
            </>
          );
        })()}
      </Sequence>

      {/* =========================================================
          ACT 3: EPHEMERAL ZERO-DISK STORAGE (Frames 1251 - 1702 | 41.7s - 56.8s)
          ========================================================= */}
      <Sequence from={1251} durationInFrames={452}>
        {/* Top Right Storage Cost */}
        <div style={{ position: 'absolute', top: '35px', right: '50px', zIndex: 100 }}>
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '2.5px solid #25d366',
              borderRadius: '16px',
              padding: '16px 24px',
              boxShadow: '0 8px 25px rgba(37, 211, 102, 0.3)',
              textAlign: 'right',
            }}
          >
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>SERVER DISK FOOTPRINT</div>
            <div style={{ color: '#25d366', fontSize: '36px', fontWeight: 900, fontFamily: 'monospace' }}>0 BYTES</div>
            <div style={{ color: '#4ade80', fontSize: '13px', fontWeight: 700 }}>Saved: ~$40M/yr AWS S3/EBS</div>
          </div>
        </div>

        {/* Sender Phone */}
        <div style={{ position: 'absolute', left: '80px', top: '360px' }}>
          <TechDevActor role="client_user" label="Alice (Phone A)" sublabel="Sends Encrypted Chat" size={290} />
        </div>

        {/* Ephemeral WhatsApp Server Queue */}
        <div style={{ position: 'absolute', left: '500px', top: '360px' }}>
          <SystemNodeV2
            type="WebServer"
            title="In-Memory Queue"
            tech="Store-and-Forward (RAM Only)"
            status="healthy"
            cpuPercent={14}
            width={380}
            height={180}
          />
        </div>

        {/* Receiver Phone */}
        <div style={{ position: 'absolute', left: '1020px', top: '360px' }}>
          <TechDevActor role="client_user" label="Bob (Phone B)" sublabel="Message Delivered!" size={290} />
        </div>

        {/* Packet Flow */}
        <PacketConnection from={{ x: 230, y: 460 }} to={{ x: 500, y: 460 }} label="SEND E2E MSG" packetColor="#38bdf8" speedFrames={15} />
        <PacketConnection from={{ x: 880, y: 460 }} to={{ x: 1020, y: 460 }} label="DELIVER TO BOB" packetColor="#25d366" speedFrames={15} />

        {/* Instant Disk Purge Notice */}
        <div
          style={{
            position: 'absolute',
            left: '500px',
            top: '590px',
            width: '380px',
            backgroundColor: 'rgba(37, 211, 102, 0.15)',
            border: '2px solid #25d366',
            borderRadius: '16px',
            padding: '16px 20px',
            textAlign: 'center',
            boxShadow: '0 8px 25px rgba(0,0,0,0.6)',
          }}
        >
          <div style={{ color: '#25d366', fontSize: '15px', fontWeight: 900, marginBottom: '4px' }}>
            🔥 INSTANT DISK PURGE (ACK DELIVERED)
          </div>
          <div style={{ color: '#e2e8f0', fontSize: '13px' }}>
            Server deletes message memory the exact millisecond Bob receives it!
          </div>
        </div>

        {/* DevOps Meme */}
        <div style={{ position: 'absolute', left: '1440px', top: '340px' }}>
          <TechDevActor role="senior_architect" label="Architect" sublabel="Zero Disk Storage" size={320} />
        </div>
        <div style={{ position: 'absolute', left: '1520px', top: '260px' }}>
          <MemeDevQuote quote="The cheapest database query is the one you never store on disk." author="Senior Architect" variant="senior" />
        </div>
      </Sequence>

      {/* =========================================================
          ACT 4: MNESIA CLUSTERING & E2E ENCRYPTION (Frames 1703 - 1935 | 56.8s - 64.5s)
          ========================================================= */}
      <Sequence from={1703} durationInFrames={233}>
        {/* Top Right: 100B Messages HUD */}
        <div style={{ position: 'absolute', top: '35px', right: '50px', zIndex: 100 }}>
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '2px solid #a855f7',
              borderRadius: '16px',
              padding: '14px 24px',
              textAlign: 'right',
            }}
          >
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>GLOBAL THROUGHPUT</div>
            <div style={{ color: '#c084fc', fontSize: '32px', fontWeight: 900, fontFamily: 'monospace' }}>100 Billion / Day</div>
            <div style={{ color: '#25d366', fontSize: '14px', fontWeight: 700 }}>Signal Protocol E2E</div>
          </div>
        </div>

        {/* Mnesia Cluster */}
        <div style={{ position: 'absolute', left: '260px', top: '360px' }}>
          <SystemNodeV2
            type="Cache"
            title="Mnesia RAM Cluster"
            tech="Distributed Erlang Routing Tables"
            status="healthy"
            cpuPercent={22}
            width={380}
            height={180}
          />
        </div>

        {/* E2E Signal Encryption Box */}
        <div style={{ position: 'absolute', left: '740px', top: '360px' }}>
          <SystemNodeV2
            type="WebServer"
            title="Signal Protocol Engine"
            tech="Client-Side Keys // Zero Plaintext"
            status="healthy"
            cpuPercent={16}
            width={380}
            height={180}
          />
        </div>

        <PacketConnection from={{ x: 640, y: 450 }} to={{ x: 740, y: 450 }} label="SUB-MS ROUTING" packetColor="#c084fc" speedFrames={10} />

        <div style={{ position: 'absolute', left: '1240px', top: '360px' }}>
          <TechDevActor role="senior_architect" label="50 Engineers" sublabel="Zero On-Call Chaos" size={320} />
        </div>
        <div style={{ position: 'absolute', left: '1360px', top: '280px' }}>
          <MemeDevQuote quote="No SQL join hell. Just in-memory routing tables and sleep like a king." author="WhatsApp Engineer" variant="senior" />
        </div>
      </Sequence>

      {/* =========================================================
          ACT 5: THE $19B ACQUISITION & THE GRAND MORAL (Frames 1936 - 2370 | 64.5s - 79.0s)
          ========================================================= */}
      <Sequence from={1936} durationInFrames={435}>
        {/* Top Right: Acquisition Valuation */}
        <div style={{ position: 'absolute', top: '35px', right: '50px', zIndex: 100 }}>
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '3px solid #eab308',
              borderRadius: '20px',
              padding: '16px 28px',
              boxShadow: '0 0 35px rgba(234, 179, 8, 0.4)',
              textAlign: 'right',
            }}
          >
            <div style={{ color: '#94a3b8', fontSize: '13px', fontWeight: 800 }}>FACEBOOK ACQUISITION (2014)</div>
            <div style={{ color: '#fbbf24', fontSize: '40px', fontWeight: 900, fontFamily: 'monospace' }}>$19 BILLION</div>
            <div style={{ color: '#4ade80', fontSize: '16px', fontWeight: 800 }}>$380,000,000 / Engineer</div>
          </div>
        </div>

        {/* Celebrating WhatsApp Devs */}
        <div style={{ position: 'absolute', left: '280px', top: '360px' }}>
          <TechDevActor role="senior_architect" label="Jan Koum & Brian Acton" sublabel="50 Legend Engineers" size={340} />
        </div>

        {/* 9router 19 Billion Trophy Asset */}
        <div
          style={{
            position: 'absolute',
            left: '830px',
            top: '175px',
            transform: `scale(${1 + Math.sin(frame / 16) * 0.04})`,
            zIndex: 120,
          }}
        >
          <Img
            src={staticFile('assets/stickers/trophy_19b.png')}
            style={{
              width: '180px',
              height: '180px',
              filter: 'drop-shadow(0 0 35px rgba(251, 191, 36, 0.7))',
            }}
          />
        </div>

        {/* Acquired Trophy Box */}
        <div
          style={{
            position: 'absolute',
            left: '680px',
            top: '360px',
            width: '480px',
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            border: '2.5px solid #fbbf24',
            borderRadius: '24px',
            padding: '28px',
            boxShadow: '0 16px 40px rgba(0,0,0,0.85)',
          }}
        >
          <div style={{ color: '#fbbf24', fontSize: '20px', fontWeight: 900, marginBottom: '12px' }}>
            💰 THE HIGHEST VALUE-PER-DEV IN TECH HISTORY
          </div>
          <div style={{ color: '#f8fafc', fontSize: '16px', lineHeight: '1.6', fontWeight: 600 }}>
            • 2,000,000,000 Daily Active Users<br />
            • 100,000,000,000 Daily Messages<br />
            • Just ~50 Software Engineers<br />
            • Zero Microservice Sprawl
          </div>
        </div>

        {/* Dev Quote */}
        <div style={{ position: 'absolute', left: '1260px', top: '340px' }}>
          <TechDevActor role="cto_panic" label="Big Tech VCs" sublabel="Completely Stunned" isStressed={true} size={320} />
        </div>
        <div style={{ position: 'absolute', left: '1360px', top: '260px' }}>
          <MemeDevQuote quote="Wait... you didn't use 800 microservices and 400 sprint meetings?!" author="Silicon Valley VC" variant="cto" />
        </div>

        {/* Grand Takeaway Finale Banner (detik 73.3s+ / Frame 2197 - 2370) */}
        {frame >= 2197 && (
          <div
            style={{
              position: 'absolute',
              bottom: '45px',
              left: '50%',
              transform: 'translateX(-50%)',
              backgroundColor: 'rgba(15, 23, 42, 0.98)',
              border: '3.5px solid #25d366',
              borderRadius: '24px',
              padding: '18px 48px',
              boxShadow: '0 0 60px rgba(37, 211, 102, 0.6), 0 20px 50px rgba(0,0,0,0.95)',
              display: 'flex',
              alignItems: 'center',
              gap: '20px',
              zIndex: 999,
            }}
          >
            <span style={{ fontSize: '36px' }}>🏆</span>
            <div style={{ color: '#f0fdf4', fontSize: '28px', fontWeight: 900, letterSpacing: '0.04em' }}>
              SIMPLE ARCHITECTURE ALWAYS BEATS RESUME-DRIVEN COMPLEXITY!
            </div>
          </div>
        )}
      </Sequence>
    </div>
  );
};
