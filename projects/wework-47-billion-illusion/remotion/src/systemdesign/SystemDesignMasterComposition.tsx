import React from 'react';
import { Sequence, useCurrentFrame, interpolate } from 'remotion';
import { TechStudioBackground } from './components/TechStudioBackground';
import { EpisodeHeader } from './components/EpisodeHeader';
import { MetricHUD } from './components/MetricHUD';
import { AWSBillingMeter } from './components/AWSBillingMeter';
import { GitHubRepoBadge } from './components/GitHubRepoBadge';
import { MemeDevQuote } from './components/MemeDevQuotes';
import { TechDevActor } from './components/TechDevActor';
import { SystemNodeV2 } from './components/SystemNodeV2';
import { PacketConnection } from './components/PacketConnection';
import { HandDrawnAnnotation } from './components/HandDrawnAnnotation';

export const SystemDesignMasterComposition: React.FC = () => {
  const frame = useCurrentFrame();

  // Screen shake on Act 2 crash (Comedic Timing & Shock Value)
  // Crash occurs exactly from 15.2s to 28.5s (Frames 456 to 854)
  const isAct2Crash = frame >= 456 && frame < 854;
  const cameraShakeX = isAct2Crash ? Math.sin(frame * 2.4) * 5 : 0;
  const cameraShakeY = isAct2Crash ? Math.cos(frame * 2.8) * 4 : 0;

  return (
    <div
      style={{
        flex: 1,
        width: 1920,
        height: 1080,
        position: 'relative',
        backgroundColor: '#070b14',
        overflow: 'hidden',
        transform: `translate(${cameraShakeX}px, ${cameraShakeY}px)`,
        fontFamily: 'Inter, system-ui, sans-serif',
      }}
    >
      {/* Dynamic Technical Studio Background */}
      <TechStudioBackground isAlert={isAct2Crash} />

      {/* Global Episode Header */}
      <EpisodeHeader
        episodeTitle="How to Scale an App from 1 to 10 Million Users"
        topicTag="SYSTEM DESIGN // ARCHITECTURE"
      />

      {/* Emergency Red Flashing Strobe Vignette on Act 2 Crash */}
      {isAct2Crash && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            boxShadow: `inset 0 0 ${100 + Math.sin(frame * 0.8) * 60}px rgba(239, 68, 68, 0.55)`,
            pointerEvents: 'none',
            zIndex: 999,
          }}
        />
      )}

      {/* =========================================================
          ACT 1: DAY 1 — THE SINGLE MONOLITH (Frames 0 - 455 | 0.0s - 15.2s)
          ========================================================= */}
      <Sequence from={0} durationInFrames={456}>
        {/* Top Right: Metrics & AWS Cost */}
        <div style={{ position: 'absolute', top: '35px', right: '50px', display: 'flex', gap: '16px', alignItems: 'flex-start', zIndex: 100 }}>
          <AWSBillingMeter cost={12} label="EC2 T4G.MICRO" />
          <MetricHUD
            levelTitle="LEVEL 1: SINGLE MONOLITH"
            userCount={interpolate(frame, [0, 300], [1, 100], { extrapolateRight: 'clamp' })}
            qps={5}
            latencyMs={8}
            statusText="ALL IN ONE"
          />
        </div>

        {/* Client User holding smartphone */}
        <div style={{ position: 'absolute', left: '160px', top: '360px' }}>
          <TechDevActor role="client_user" label="Client App" sublabel="iOS / Android" size={300} />
        </div>

        {/* Monolith Server with Web + DB Internal Cards */}
        <div style={{ position: 'absolute', left: '600px', top: '380px' }}>
          <SystemNodeV2
            type="WebServer"
            title="Monolith Server"
            tech="Next.js + PostgreSQL (Same Box)"
            status="healthy"
            cpuPercent={14}
            width={380}
            height={190}
            isMonolith={true}
          />
        </div>

        {/* Packet Connection */}
        <PacketConnection from={{ x: 320, y: 475 }} to={{ x: 600, y: 475 }} label="HTTPS GET" speedFrames={25} />

        <HandDrawnAnnotation
          type="circle"
          x={580}
          y={350}
          width={420}
          height={245}
          text="Cheap & simple for Day 1 ($12/mo)"
          color="#38bdf8"
          startFrame={40}
        />

        {/* Junior Dev Character + Meme */}
        <div style={{ position: 'absolute', left: '1160px', top: '360px' }}>
          <TechDevActor role="junior_dev" label="Junior Dev" sublabel="Pushed v1.0 to main" size={330} />
        </div>
        <div style={{ position: 'absolute', left: '1420px', top: '310px' }}>
          <MemeDevQuote quote="Works fine on my machine! Ready for 10 million users!" author="Junior Dev" variant="junior" />
        </div>
      </Sequence>

      {/* =========================================================
          ACT 2: THE CRASH & TIER SEPARATION (Frames 456 - 1060 | 15.2s - 35.4s)
          ========================================================= */}
      <Sequence from={456} durationInFrames={605}>
        {(() => {
          const actFrame = frame - 456;
          const isOverloaded = actFrame < 398; // 15.2s to 28.5s: 100% CPU crash

          return (
            <>
              {/* Top Right Metrics */}
              <div style={{ position: 'absolute', top: '35px', right: '50px', display: 'flex', gap: '16px', alignItems: 'flex-start', zIndex: 100 }}>
                <AWSBillingMeter cost={isOverloaded ? 420 : 1850} label="SERVER COST" isPanic={isOverloaded} />
                <MetricHUD
                  levelTitle={isOverloaded ? "ALERT: RESOURCE EXHAUSTION" : "LEVEL 2: TIER SEPARATION"}
                  userCount={interpolate(actFrame, [0, 180], [1000, 10000], { extrapolateRight: 'clamp' })}
                  qps={1200}
                  latencyMs={isOverloaded ? 980 : 38}
                  isAlert={isOverloaded}
                />
              </div>

              {/* Client User */}
              <div style={{ position: 'absolute', left: '160px', top: '360px' }}>
                <TechDevActor
                  role="client_user"
                  label="10,000 Users"
                  sublabel="Traffic Surge"
                  isStressed={isOverloaded}
                  size={300}
                />
              </div>

              {isOverloaded ? (
                <>
                  <div style={{ position: 'absolute', left: '600px', top: '380px' }}>
                    <SystemNodeV2
                      type="WebServer"
                      title="Monolith Server"
                      tech="CPU at 100% / Out of RAM"
                      status="overload"
                      cpuPercent={100}
                      width={380}
                      height={190}
                      isMonolith={true}
                    />
                  </div>
                  <PacketConnection from={{ x: 320, y: 475 }} to={{ x: 600, y: 475 }} label="CONGESTED" speedFrames={10} isOverloaded={true} />
                  <HandDrawnAnnotation
                    type="cross"
                    x={610}
                    y={390}
                    width={360}
                    height={165}
                    text="SPOF: Web & DB fighting for RAM!"
                    color="#ef4444"
                    startFrame={25}
                  />

                  {/* DevOps On-Call Panicking */}
                  <div style={{ position: 'absolute', left: '1160px', top: '360px' }}>
                    <TechDevActor role="devops_oncall" label="On-Call DevOps" sublabel="PAGERDUTY 3:00 AM" isStressed={true} size={330} />
                  </div>
                  <div style={{ position: 'absolute', left: '1420px', top: '310px' }}>
                    <MemeDevQuote quote="WHO THE HELL PUSHED TO PROD ON FRIDAY 5 PM?!" author="On-Call DevOps" variant="panic" />
                  </div>
                </>
              ) : (
                <>
                  {/* Dedicated Web Tier */}
                  <div style={{ position: 'absolute', left: '520px', top: '380px' }}>
                    <SystemNodeV2 type="WebServer" title="Dedicated Web App" tech="Node.js API Container" status="healthy" cpuPercent={42} width={300} height={160} />
                  </div>

                  {/* Dedicated Database Tier */}
                  <div style={{ position: 'absolute', left: '950px', top: '380px' }}>
                    <SystemNodeV2 type="Database" title="Dedicated PostgreSQL" tech="Independent Storage Instance" status="healthy" cpuPercent={32} width={300} height={160} />
                  </div>

                  <PacketConnection from={{ x: 320, y: 460 }} to={{ x: 520, y: 460 }} label="HTTPS API" speedFrames={20} />
                  <PacketConnection from={{ x: 820, y: 460 }} to={{ x: 950, y: 460 }} label="SQL TCP" speedFrames={18} packetColor="#a855f7" />

                  {/* Senior Architect Quote */}
                  <div style={{ position: 'absolute', left: '1360px', top: '360px' }}>
                    <TechDevActor role="senior_architect" label="Senior Architect" sublabel="Problem Solved" size={320} />
                  </div>
                  <div style={{ position: 'absolute', left: '1540px', top: '280px' }}>
                    <MemeDevQuote quote="Rule #1: Separate Compute from Database." author="Senior Architect" variant="senior" />
                  </div>

                  <HandDrawnAnnotation
                    type="circle"
                    x={930}
                    y={360}
                    width={340}
                    height={200}
                    text="Dedicated compute & I/O!"
                    color="#10b981"
                    startFrame={170}
                  />
                </>
              )}
            </>
          );
        })()}
      </Sequence>

      {/* =========================================================
          ACT 3: 100,000 USERS — LOAD BALANCER (Frames 1061 - 1343 | 35.4s - 44.8s)
          ========================================================= */}
      <Sequence from={1061} durationInFrames={283}>
        <div style={{ position: 'absolute', top: '35px', right: '50px', display: 'flex', gap: '16px', alignItems: 'flex-start', zIndex: 100 }}>
          <AWSBillingMeter cost={14800} label="AWS AUTO-SCALING" />
          <MetricHUD
            levelTitle="LEVEL 3: HORIZONTAL WEB SCALE"
            userCount={100000}
            qps={15000}
            latencyMs={22}
            statusText="HIGH AVAILABILITY"
          />
        </div>

        {/* Client */}
        <div style={{ position: 'absolute', left: '80px', top: '380px' }}>
          <TechDevActor role="client_user" label="100,000 Users" sublabel="Global Requests" size={280} />
        </div>

        {/* Load Balancer */}
        <div style={{ position: 'absolute', left: '380px', top: '410px' }}>
          <SystemNodeV2 type="LoadBalancer" title="Load Balancer" tech="Nginx / AWS ALB" status="healthy" cpuPercent={26} width={280} height={150} />
        </div>

        {/* 3 Stateless Web Servers */}
        <div style={{ position: 'absolute', left: '760px', top: '180px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 01" tech="Stateless Container" status="healthy" cpuPercent={36} width={250} height={125} />
        </div>
        <div style={{ position: 'absolute', left: '760px', top: '410px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 02" tech="Stateless Container" status="healthy" cpuPercent={40} width={250} height={125} />
        </div>
        <div style={{ position: 'absolute', left: '760px', top: '640px' }}>
          <SystemNodeV2 type="WebServer" title="Web Node 03" tech="Stateless Container" status="healthy" cpuPercent={38} width={250} height={125} />
        </div>

        {/* Shared Database choking */}
        <div style={{ position: 'absolute', left: '1140px', top: '410px' }}>
          <SystemNodeV2 type="Database" title="PostgreSQL" tech="Primary (78% Read Choke)" status="warning" cpuPercent={78} width={280} height={150} />
        </div>

        {/* Packet Connections */}
        <PacketConnection from={{ x: 230, y: 480 }} to={{ x: 380, y: 480 }} label="HTTPS" speedFrames={15} />
        <PacketConnection from={{ x: 660, y: 450 }} to={{ x: 760, y: 240 }} speedFrames={18} />
        <PacketConnection from={{ x: 660, y: 485 }} to={{ x: 760, y: 470 }} speedFrames={18} />
        <PacketConnection from={{ x: 660, y: 520 }} to={{ x: 760, y: 700 }} speedFrames={18} />

        <PacketConnection from={{ x: 1010, y: 240 }} to={{ x: 1140, y: 460 }} packetColor="#a855f7" speedFrames={20} />
        <PacketConnection from={{ x: 1010, y: 470 }} to={{ x: 1140, y: 485 }} packetColor="#a855f7" speedFrames={20} />
        <PacketConnection from={{ x: 1010, y: 700 }} to={{ x: 1140, y: 510 }} packetColor="#a855f7" speedFrames={20} />

        {/* CTO Crying Meme */}
        <div style={{ position: 'absolute', left: '1480px', top: '380px' }}>
          <TechDevActor role="cto_panic" label="CTO" sublabel="$14.8k AWS invoice" size={310} />
        </div>
        <div style={{ position: 'absolute', left: '1540px', top: '280px' }}>
          <MemeDevQuote quote="Jeff Bezos is laughing at our cloud invoice right now." author="CTO" variant="cto" />
        </div>

        {/* GitHub Badge for Nginx */}
        <div style={{ position: 'absolute', left: '380px', top: '600px' }}>
          <GitHubRepoBadge repo="nginx/nginx" stars="24.2k" topic="Reverse Proxy" />
        </div>
      </Sequence>

      {/* =========================================================
          ACT 4: 1,000,000 USERS — REDIS CACHE (Frames 1344 - 1667 | 44.8s - 55.6s)
          ========================================================= */}
      <Sequence from={1344} durationInFrames={324}>
        <div style={{ position: 'absolute', top: '35px', right: '50px', display: 'flex', gap: '16px', alignItems: 'flex-start', zIndex: 100 }}>
          <AWSBillingMeter cost={32400} label="OPTIMIZED FLEET" />
          <MetricHUD
            levelTitle="LEVEL 4: CACHE & READ REPLICAS"
            userCount={1000000}
            qps={65000}
            latencyMs={6}
            statusText="SUB-MS CACHE"
          />
        </div>

        {/* Client */}
        <div style={{ position: 'absolute', left: '60px', top: '380px' }}>
          <TechDevActor role="client_user" label="1M Users" sublabel="85% Reads" size={270} />
        </div>

        {/* ALB */}
        <div style={{ position: 'absolute', left: '330px', top: '400px' }}>
          <SystemNodeV2 type="LoadBalancer" title="ALB Router" tech="Layer 7 Traffic" width={240} height={140} />
        </div>

        {/* App Fleet */}
        <div style={{ position: 'absolute', left: '620px', top: '400px' }}>
          <SystemNodeV2 type="WebServer" title="App Fleet" tech="Auto-Scaling Cluster" scaleCount="x12 Nodes" status="healthy" cpuPercent={30} width={260} height={140} />
        </div>

        {/* Redis Cache Cluster */}
        <div style={{ position: 'absolute', left: '980px', top: '170px' }}>
          <SystemNodeV2 type="Cache" title="Redis Cache" tech="In-Memory RAM (Cache-Aside)" status="healthy" cpuPercent={20} width={280} height={145} />
        </div>

        {/* Primary DB */}
        <div style={{ position: 'absolute', left: '980px', top: '400px' }}>
          <SystemNodeV2 type="Database" title="Primary DB" tech="PostgreSQL (Writes Only)" status="healthy" cpuPercent={28} width={280} height={145} />
        </div>

        {/* Read Replicas */}
        <div style={{ position: 'absolute', left: '980px', top: '640px' }}>
          <SystemNodeV2 type="Database" title="Read Replicas" tech="Async Read Fleet (x3)" scaleCount="x3" status="healthy" cpuPercent={24} width={280} height={145} />
        </div>

        {/* Connections */}
        <PacketConnection from={{ x: 210, y: 470 }} to={{ x: 330, y: 470 }} speedFrames={12} />
        <PacketConnection from={{ x: 570, y: 470 }} to={{ x: 620, y: 470 }} speedFrames={12} />
        <PacketConnection from={{ x: 880, y: 440 }} to={{ x: 980, y: 240 }} label="CACHE HIT (1ms)" packetColor="#10b981" speedFrames={10} />
        <PacketConnection from={{ x: 880, y: 470 }} to={{ x: 980, y: 470 }} label="WRITE ONLY" packetColor="#f59e0b" speedFrames={22} />
        <PacketConnection from={{ x: 1120, y: 545 }} to={{ x: 1120, y: 640 }} label="BINLOG REPLICATION" packetColor="#38bdf8" speedFrames={16} />

        {/* GitHub Badge for Redis */}
        <div style={{ position: 'absolute', left: '980px', top: '95px' }}>
          <GitHubRepoBadge repo="redis/redis" stars="68.4k" topic="In-Memory Speed" />
        </div>

        {/* Senior Architect Meme */}
        <div style={{ position: 'absolute', left: '1380px', top: '380px' }}>
          <TechDevActor role="senior_architect" label="Senior Architect" sublabel="Smug & Relaxed" size={320} />
        </div>
        <div style={{ position: 'absolute', left: '1520px', top: '280px' }}>
          <MemeDevQuote quote="Told you 3 months ago: 85% of queries are identical. Cache it." author="Senior Architect" variant="senior" />
        </div>
      </Sequence>

      {/* =========================================================
          ACT 5: 10,000,000 USERS — GLOBAL SCALE (Frames 1668 - 2200 | 55.6s - 73.3s)
          ========================================================= */}
      <Sequence from={1668} durationInFrames={532}>
        <div style={{ position: 'absolute', top: '35px', right: '50px', display: 'flex', gap: '16px', alignItems: 'flex-start', zIndex: 100 }}>
          <AWSBillingMeter cost={84320} label="ENTERPRISE CLUSTER" />
          <MetricHUD
            levelTitle="LEVEL 5: 10M GLOBAL SCALE"
            userCount={10000000}
            qps={280000}
            latencyMs={4}
            statusText="WORLDWIDE CDN + SHARDING"
          />
        </div>

        {/* Clients */}
        <div style={{ position: 'absolute', left: '40px', top: '220px' }}>
          <TechDevActor role="client_user" label="US & EU Users" size={230} />
        </div>
        <div style={{ position: 'absolute', left: '40px', top: '550px' }}>
          <TechDevActor role="client_user" label="Asia-Pac Users" size={230} />
        </div>

        {/* Cloudflare CDN */}
        <div style={{ position: 'absolute', left: '260px', top: '410px' }}>
          <SystemNodeV2 type="CDN" title="Cloudflare CDN Edge" tech="300+ Cities Worldwide" scaleCount="Global" status="healthy" cpuPercent={18} width={270} height={145} />
        </div>

        {/* ALB */}
        <div style={{ position: 'absolute', left: '570px', top: '410px' }}>
          <SystemNodeV2 type="LoadBalancer" title="Anycast DNS + ALB" tech="Multi-Region Traffic" status="healthy" cpuPercent={24} width={260} height={145} />
        </div>

        {/* K8s Microservices */}
        <div style={{ position: 'absolute', left: '870px', top: '410px' }}>
          <SystemNodeV2 type="WebServer" title="K8s Microservices" tech="Auto-Scaling Fleet" scaleCount="x150 Pods" status="healthy" cpuPercent={42} width={270} height={145} />
        </div>

        {/* Kafka */}
        <div style={{ position: 'absolute', left: '1190px', top: '180px' }}>
          <SystemNodeV2 type="MessageQueue" title="Apache Kafka" tech="Event Streaming Queue" status="healthy" cpuPercent={31} width={270} height={145} />
        </div>

        {/* Redis Global Cache */}
        <div style={{ position: 'absolute', left: '1190px', top: '410px' }}>
          <SystemNodeV2 type="Cache" title="Redis Global Cache" tech="Multi-AZ In-Memory" status="healthy" cpuPercent={25} width={270} height={145} />
        </div>

        {/* Sharded DB */}
        <div style={{ position: 'absolute', left: '1190px', top: '640px' }}>
          <SystemNodeV2 type="Database" title="Sharded PostgreSQL" tech="Partitioned by User UUID" scaleCount="x8 Shards" status="healthy" cpuPercent={34} width={270} height={145} />
        </div>

        {/* Connections */}
        <PacketConnection from={{ x: 160, y: 310 }} to={{ x: 260, y: 470 }} speedFrames={10} />
        <PacketConnection from={{ x: 160, y: 640 }} to={{ x: 260, y: 500 }} speedFrames={10} />
        <PacketConnection from={{ x: 530, y: 480 }} to={{ x: 570, y: 480 }} label="EDGE CACHED" packetColor="#10b981" speedFrames={10} />
        <PacketConnection from={{ x: 830, y: 480 }} to={{ x: 870, y: 480 }} speedFrames={10} />
        <PacketConnection from={{ x: 1140, y: 440 }} to={{ x: 1190, y: 250 }} label="ASYNC EVENT" packetColor="#f59e0b" speedFrames={12} />
        <PacketConnection from={{ x: 1140, y: 480 }} to={{ x: 1190, y: 480 }} label="RAM GET" packetColor="#38bdf8" speedFrames={8} />
        <PacketConnection from={{ x: 1140, y: 520 }} to={{ x: 1190, y: 710 }} label="SHARDED WRITE" packetColor="#a855f7" speedFrames={15} />

        {/* GitHub Badge: Holy Bible */}
        <div style={{ position: 'absolute', left: '870px', top: '580px' }}>
          <GitHubRepoBadge repo="donnemartin/system-design-primer" stars="290k" topic="The Holy Bible" />
        </div>

        {/* Celebrating CTO / Architect */}
        <div style={{ position: 'absolute', left: '1530px', top: '380px' }}>
          <TechDevActor role="senior_architect" label="Principal Architect" sublabel="10M USERS READY" size={320} />
        </div>
        <div style={{ position: 'absolute', left: '1580px', top: '260px' }}>
          <MemeDevQuote quote="Zero Single Point of Failure. Sleep like a baby tonight!" author="Principal Architect" variant="senior" />
        </div>

        {/* Grand Finale Climax Banner (Frames 2080 - 2200 | 69.3s - 73.3s) */}
        {frame >= 2080 && (
          <div
            style={{
              position: 'absolute',
              bottom: '40px',
              left: '50%',
              transform: 'translateX(-50%)',
              backgroundColor: 'rgba(15, 23, 42, 0.95)',
              border: '3px solid #10b981',
              borderRadius: '24px',
              padding: '16px 40px',
              boxShadow: '0 0 50px rgba(16, 185, 129, 0.6), 0 20px 40px rgba(0,0,0,0.9)',
              display: 'flex',
              alignItems: 'center',
              gap: '16px',
              zIndex: 999,
              animation: 'pulse 1.5s infinite',
            }}
          >
            <span style={{ fontSize: '32px' }}>🏆</span>
            <div style={{ color: '#f0fdf4', fontSize: '26px', fontWeight: 900, letterSpacing: '0.05em' }}>
              ZERO SINGLE POINTS OF FAILURE // 10 MILLION USERS READY!
            </div>
          </div>
        )}
      </Sequence>
    </div>
  );
};
