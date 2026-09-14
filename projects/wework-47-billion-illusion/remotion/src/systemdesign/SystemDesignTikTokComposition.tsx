import React from 'react';
import { Sequence, useCurrentFrame, interpolate } from 'remotion';
import { TechStudioBackground } from './components/TechStudioBackground';
import { AWSBillingMeter } from './components/AWSBillingMeter';
import { GitHubRepoBadge } from './components/GitHubRepoBadge';
import { MemeDevQuote } from './components/MemeDevQuotes';
import { TechDevActor } from './components/TechDevActor';
import { SystemNodeV2 } from './components/SystemNodeV2';
import { PacketConnection } from './components/PacketConnection';
import { HandDrawnAnnotation } from './components/HandDrawnAnnotation';

export const SystemDesignTikTokComposition: React.FC = () => {
  const frame = useCurrentFrame();

  // Screen shake on Act 2 crash (15.2s to 28.5s)
  const isAct2Crash = frame >= 456 && frame < 854;
  const cameraShakeX = isAct2Crash ? Math.sin(frame * 2.5) * 6 : 0;
  const cameraShakeY = isAct2Crash ? Math.cos(frame * 2.8) * 5 : 0;

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
        transform: `translate(${cameraShakeX}px, ${cameraShakeY}px)`,
      }}
    >
      <TechStudioBackground isAlert={isAct2Crash} />

      {/* Emergency Red Flashing Strobe Vignette on Act 2 Crash */}
      {isAct2Crash && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            boxShadow: `inset 0 0 ${120 + Math.sin(frame * 0.8) * 70}px rgba(239, 68, 68, 0.6)`,
            pointerEvents: 'none',
            zIndex: 999,
          }}
        />
      )}

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
            backgroundColor: '#0284c7',
            color: '#f0f9ff',
            fontSize: '18px',
            fontWeight: 800,
            padding: '8px 22px',
            borderRadius: '24px',
            letterSpacing: '0.08em',
            marginBottom: '12px',
            boxShadow: '0 4px 20px rgba(2, 132, 199, 0.6)',
          }}
        >
          🔥 SYSTEM DESIGN INTERVIEW GUIDE
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
          Scale an App: <span style={{ color: '#38bdf8' }}>1</span> to <span style={{ color: '#10b981' }}>10 Million</span> Users
        </div>
      </div>

      {/* =========================================================
          ACT 1: 1 USER — SINGLE MONOLITH (Frames 0 - 455 | 0.0s - 15.2s)
          ========================================================= */}
      <Sequence from={0} durationInFrames={456}>
        {/* Metric HUD & AWS Bill */}
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <AWSBillingMeter cost={12} label="EC2 T4G.MICRO" />
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800, letterSpacing: '0.05em' }}>ACTIVE USERS</div>
            <div style={{ color: '#38bdf8', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>100</div>
            <div style={{ color: '#34d399', fontSize: '18px', fontWeight: 800 }}>8ms Latency</div>
          </div>
        </div>

        {/* Vertical Flow: Client at Top, Server in Center */}
        <div style={{ position: 'absolute', left: '420px', top: '290px' }}>
          <TechDevActor role="client_user" label="User Mobile App" size={240} />
        </div>

        <PacketConnection from={{ x: 540, y: 560 }} to={{ x: 540, y: 720 }} label="HTTPS GET" speedFrames={20} />

        <div style={{ position: 'absolute', left: '340px', top: '720px' }}>
          <SystemNodeV2
            type="WebServer"
            title="Monolith Server"
            tech="Next.js + PostgreSQL (Same Box)"
            status="healthy"
            cpuPercent={12}
            width={400}
            height={190}
            isMonolith={true}
          />
        </div>

        <HandDrawnAnnotation
          type="circle"
          x={310}
          y={690}
          width={460}
          height={250}
          text="Cheap Day 1 architecture ($12/mo)"
          color="#38bdf8"
          startFrame={40}
        />

        {/* Bottom Character: Junior Dev */}
        <div style={{ position: 'absolute', left: '80px', top: '1120px' }}>
          <TechDevActor role="junior_dev" label="Junior Dev" sublabel="Just launched v1.0" size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1180px' }}>
          <MemeDevQuote quote="It works on my machine! Ready for 10M users!" author="Junior Dev" variant="junior" />
        </div>

        {/* TikTok Caption Card */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #38bdf8', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "Day 1: Single monolith server. Web app and DB on one box. Fast, simple, and cheap."
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 2: 10,000 USERS — THE CRASH & 504 TIMEOUT (Frames 456 - 1060 | 15.2s - 35.4s)
          ========================================================= */}
      <Sequence from={456} durationInFrames={605}>
        {(() => {
          const actFrame = frame - 456;
          const isOverloaded = actFrame < 398; // 15.2s to 28.5s: 100% CPU crash

          return (
            <>
              {/* Metric HUD & AWS Bill */}
              <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
                <AWSBillingMeter cost={isOverloaded ? 420 : 1850} label="SERVER COST" isPanic={isOverloaded} />
                <div style={{ textAlign: 'right' }}>
                  <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800, letterSpacing: '0.05em' }}>ACTIVE USERS</div>
                  <div style={{ color: '#ef4444', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>10,000</div>
                  <div style={{ color: isOverloaded ? '#f87171' : '#34d399', fontSize: '18px', fontWeight: 800 }}>
                    {isOverloaded ? '980ms (504 TIMEOUT)' : '38ms Latency'}
                  </div>
                </div>
              </div>

              {isOverloaded ? (
                <>
                  <div style={{ position: 'absolute', left: '420px', top: '290px' }}>
                    <TechDevActor role="client_user" label="10k Users" sublabel="CRASHING" isStressed={true} size={240} />
                  </div>

                  <PacketConnection from={{ x: 540, y: 560 }} to={{ x: 540, y: 720 }} label="CONGESTED" speedFrames={8} isOverloaded={true} />

                  <div style={{ position: 'absolute', left: '340px', top: '720px' }}>
                    <SystemNodeV2
                      type="WebServer"
                      title="Monolith Server"
                      tech="CPU at 100% / Out of RAM"
                      status="overload"
                      cpuPercent={100}
                      width={400}
                      height={190}
                      isMonolith={true}
                    />
                  </div>

                  <HandDrawnAnnotation
                    type="cross"
                    x={330}
                    y={740}
                    width={420}
                    height={150}
                    text="SPOF: Web & DB fighting for RAM!"
                    color="#ef4444"
                    startFrame={20}
                  />

                  {/* On-call DevOps */}
                  <div style={{ position: 'absolute', left: '80px', top: '1120px' }}>
                    <TechDevActor role="devops_oncall" label="DevOps On-Call" sublabel="PAGERDUTY 3:00 AM" isStressed={true} size={350} />
                  </div>
                  <div style={{ position: 'absolute', left: '440px', top: '1180px' }}>
                    <MemeDevQuote quote="WHO PUSHED TO PROD ON FRIDAY 5 PM?!" author="On-Call DevOps" variant="panic" />
                  </div>
                </>
              ) : (
                <>
                  {/* Dedicated Web Tier */}
                  <div style={{ position: 'absolute', left: '120px', top: '640px' }}>
                    <SystemNodeV2 type="WebServer" title="Dedicated Web App" tech="Node.js API Container" status="healthy" cpuPercent={38} width={380} height={160} />
                  </div>

                  {/* Dedicated Database Tier */}
                  <div style={{ position: 'absolute', left: '580px', top: '640px' }}>
                    <SystemNodeV2 type="Database" title="Dedicated PostgreSQL" tech="Independent Storage Instance" status="healthy" cpuPercent={30} width={380} height={160} />
                  </div>

                  <PacketConnection from={{ x: 500, y: 720 }} to={{ x: 580, y: 720 }} label="SQL TCP" packetColor="#a855f7" speedFrames={16} />

                  {/* Senior Architect */}
                  <div style={{ position: 'absolute', left: '80px', top: '1120px' }}>
                    <TechDevActor role="senior_architect" label="Senior Architect" sublabel="Decoupled Tiers" size={350} />
                  </div>
                  <div style={{ position: 'absolute', left: '440px', top: '1180px' }}>
                    <MemeDevQuote quote="Rule #1: Separate compute from database storage." author="Senior Architect" variant="senior" />
                  </div>
                </>
              )}

              {/* TikTok Caption Card */}
              <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
                <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: `2.5px solid ${isOverloaded ? '#ef4444' : '#10b981'}`, borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
                  <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
                    {isOverloaded
                      ? '10,000 users hit at once! Server runs out of RAM. Complete 504 outage.'
                      : 'Fix: Decouple web app and database into independent tiers. Scale separately.'}
                  </div>
                </div>
              </div>
            </>
          );
        })()}
      </Sequence>
      {/* =========================================================
          ACT 3: 100,000 USERS — LOAD BALANCER (Frames 1061 - 1343 | 35.4s - 44.8s)
          ========================================================= */}
      <Sequence from={1061} durationInFrames={283}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <AWSBillingMeter cost={14800} label="AWS AUTO-SCALING" />
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800, letterSpacing: '0.05em' }}>ACTIVE USERS</div>
            <div style={{ color: '#38bdf8', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>100,000</div>
            <div style={{ color: '#34d399', fontSize: '18px', fontWeight: 800 }}>22ms Latency</div>
          </div>
        </div>

        {/* Load Balancer */}
        <div style={{ position: 'absolute', left: '360px', top: '420px' }}>
          <SystemNodeV2 type="LoadBalancer" title="Load Balancer" tech="Nginx / AWS ALB" status="healthy" cpuPercent={26} width={360} height={145} />
        </div>

        {/* 3 Horizontal Web Nodes */}
        <div style={{ position: 'absolute', left: '60px', top: '640px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 01" tech="Stateless" status="healthy" cpuPercent={34} width={300} height={125} />
        </div>
        <div style={{ position: 'absolute', left: '390px', top: '640px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 02" tech="Stateless" status="healthy" cpuPercent={36} width={300} height={125} />
        </div>
        <div style={{ position: 'absolute', left: '720px', top: '640px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 03" tech="Stateless" status="healthy" cpuPercent={38} width={300} height={125} />
        </div>

        {/* Database */}
        <div style={{ position: 'absolute', left: '360px', top: '830px' }}>
          <SystemNodeV2 type="Database" title="PostgreSQL Primary" tech="78% Read Bottleneck" status="warning" cpuPercent={78} width={360} height={145} />
        </div>

        {/* CTO Meme */}
        <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
          <TechDevActor role="cto_panic" label="CTO" sublabel="$14,800 AWS Bill" size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
          <MemeDevQuote quote="Jeff Bezos is laughing at our cloud bill right now!" author="CTO" variant="cto" />
        </div>

        <div style={{ position: 'absolute', left: '360px', top: '1000px' }}>
          <GitHubRepoBadge repo="nginx/nginx" stars="24.2k" topic="Reverse Proxy" />
        </div>

        {/* Caption */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #38bdf8', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "100,000 users: Load balancer distributes traffic across stateless servers. But DB is now choking on reads!"
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 4: 1,000,000 USERS — REDIS CACHE (Frames 1344 - 1667 | 44.8s - 55.6s)
          ========================================================= */}
      <Sequence from={1344} durationInFrames={324}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <AWSBillingMeter cost={32400} label="OPTIMIZED FLEET" />
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800, letterSpacing: '0.05em' }}>ACTIVE USERS</div>
            <div style={{ color: '#38bdf8', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>1,000,000</div>
            <div style={{ color: '#34d399', fontSize: '18px', fontWeight: 800 }}>6ms Latency</div>
          </div>
        </div>

        {/* Redis Cache Box */}
        <div style={{ position: 'absolute', left: '160px', top: '440px' }}>
          <SystemNodeV2 type="Cache" title="Redis Cache" tech="In-Memory RAM (Cache-Aside)" status="healthy" cpuPercent={18} width={360} height={145} />
        </div>
        <div style={{ position: 'absolute', left: '560px', top: '440px' }}>
          <SystemNodeV2 type="Database" title="Primary DB" tech="Writes Only (Low Load)" status="healthy" cpuPercent={24} width={360} height={145} />
        </div>

        {/* Read Replicas */}
        <div style={{ position: 'absolute', left: '360px', top: '650px' }}>
          <SystemNodeV2 type="Database" title="Read Replicas (x3)" tech="Async Read Fleet" scaleCount="x3" status="healthy" cpuPercent={20} width={360} height={145} />
        </div>

        <div style={{ position: 'absolute', left: '160px', top: '600px' }}>
          <GitHubRepoBadge repo="redis/redis" stars="68.4k" topic="In-Memory Cache" />
        </div>

        {/* Senior Architect */}
        <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
          <TechDevActor role="senior_architect" label="Senior Architect" sublabel="Smug & Relaxed" size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
          <MemeDevQuote quote="Told you 3 months ago: 85% of queries are identical. Cache it." author="Senior Architect" variant="senior" />
        </div>

        {/* Caption */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #10b981', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "1 Million Users: Redis caches 85% of reads in sub-millisecond RAM. Database is saved!"
            </div>
          </div>
        </div>
      </Sequence>

      {/* =========================================================
          ACT 5: 10,000,000 USERS — GLOBAL EDGE + SHARDING (Frames 1668 - 2200 | 55.6s - 73.3s)
          ========================================================= */}
      <Sequence from={1668} durationInFrames={532}>
        <div style={{ position: 'absolute', top: '230px', left: '60px', right: '60px', display: 'flex', justifyContent: 'space-between', zIndex: 90 }}>
          <AWSBillingMeter cost={84320} label="GLOBAL ENTERPRISE" />
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: '#94a3b8', fontSize: '15px', fontWeight: 800, letterSpacing: '0.05em' }}>ACTIVE USERS</div>
            <div style={{ color: '#38bdf8', fontSize: '44px', fontWeight: 900, fontFamily: 'monospace' }}>10,000,000</div>
            <div style={{ color: '#34d399', fontSize: '18px', fontWeight: 800 }}>4ms Latency (Global CDN)</div>
          </div>
        </div>

        {/* Global Edge CDN */}
        <div style={{ position: 'absolute', left: '120px', top: '430px' }}>
          <SystemNodeV2 type="CDN" title="Cloudflare CDN Edge" tech="Global Anycast (300+ Cities)" scaleCount="Edge" status="healthy" cpuPercent={15} width={400} height={145} />
        </div>
        <div style={{ position: 'absolute', left: '560px', top: '430px' }}>
          <SystemNodeV2 type="MessageQueue" title="Apache Kafka" tech="Async Event Streaming" status="healthy" cpuPercent={28} width={400} height={145} />
        </div>

        {/* Sharded DB */}
        <div style={{ position: 'absolute', left: '340px', top: '630px' }}>
          <SystemNodeV2 type="Database" title="Sharded Database" tech="User UUID Partitioned" scaleCount="x8 Shards" status="healthy" cpuPercent={30} width={400} height={145} />
        </div>

        <div style={{ position: 'absolute', left: '340px', top: '800px' }}>
          <GitHubRepoBadge repo="donnemartin/system-design-primer" stars="290k" topic="The Holy Bible" />
        </div>

        {/* Principal Architect */}
        <div style={{ position: 'absolute', left: '80px', top: '1100px' }}>
          <TechDevActor role="senior_architect" label="Principal Architect" sublabel="10M USERS READY" size={350} />
        </div>
        <div style={{ position: 'absolute', left: '440px', top: '1160px' }}>
          <MemeDevQuote quote="Zero Single Point of Failure. Sleep like a baby tonight!" author="Principal Architect" variant="senior" />
        </div>

        {/* Caption */}
        <div style={{ position: 'absolute', bottom: '120px', left: '50px', right: '50px', textAlign: 'center' }}>
          <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', border: '2.5px solid #a855f7', borderRadius: '20px', padding: '22px 28px', boxShadow: '0 12px 35px rgba(0,0,0,0.8)' }}>
            <div style={{ color: '#f8fafc', fontSize: '32px', fontWeight: 900, lineHeight: '1.35', textShadow: '0 2px 10px rgba(0,0,0,0.8)' }}>
              "10 Million Users: Global CDN, Kafka async processing, and Database Sharding. Architecture complete!"
            </div>
          </div>
        </div>

        {/* Grand Finale Climax Banner on Mobile (Frames 2080 - 2200 | 69.3s - 73.3s) */}
        {frame >= 2080 && (
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              transform: 'translate(-50%, -50%)',
              width: '900px',
              backgroundColor: 'rgba(15, 23, 42, 0.98)',
              border: '4px solid #10b981',
              borderRadius: '28px',
              padding: '30px 24px',
              boxShadow: '0 0 60px rgba(16, 185, 129, 0.7), 0 30px 60px rgba(0,0,0,0.95)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              textAlign: 'center',
              zIndex: 999,
            }}
          >
            <div style={{ fontSize: '56px', marginBottom: '10px' }}>🏆</div>
            <div style={{ color: '#34d399', fontSize: '38px', fontWeight: 900, letterSpacing: '0.02em', marginBottom: '8px' }}>
              ZERO SINGLE POINTS OF FAILURE
            </div>
            <div style={{ color: '#f8fafc', fontSize: '26px', fontWeight: 700 }}>
              10 Million Users Architecture Complete!
            </div>
          </div>
        )}
      </Sequence>
    </div>
  );
};
