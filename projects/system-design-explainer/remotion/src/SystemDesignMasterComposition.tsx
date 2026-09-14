import React from 'react';
import { Sequence, useCurrentFrame, interpolate } from 'remotion';
import { GridBlueprintBackground } from './components/GridBlueprintBackground';
import { EpisodeHeader } from './components/EpisodeHeader';
import { MetricHUD } from './components/MetricHUD';
import { StickmanActor } from './components/StickmanActor';
import { SystemNode } from './components/SystemNode';
import { PacketConnection } from './components/PacketConnection';
import { HandDrawnAnnotation } from './components/HandDrawnAnnotation';

export const SystemDesignMasterComposition: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <div
      style={{
        flex: 1,
        width: 1920,
        height: 1080,
        position: 'relative',
        backgroundColor: '#090d16',
        overflow: 'hidden',
      }}
    >
      {/* Blueprint Grid Background */}
      <GridBlueprintBackground />

      {/* Global Episode Header */}
      <EpisodeHeader
        episodeTitle="How to Scale an App from 1 to 10 Million Users"
        topicTag="SYSTEM DESIGN // ARCHITECTURE"
      />

      {/* =========================================================
          ACT 1: DAY 1 — THE SINGLE MONOLITH (Frames 0 - 300)
          ========================================================= */}
      <Sequence from={0} durationInFrames={300}>
        <MetricHUD
          levelTitle="LEVEL 1: SINGLE MONOLITH"
          userCount={interpolate(frame, [0, 200], [1, 100], { extrapolateRight: 'clamp' })}
          qps={5}
          latencyMs={8}
          statusText="ALL IN ONE"
        />

        {/* Client Stickman */}
        <div style={{ position: 'absolute', left: '180px', top: '480px' }}>
          <StickmanActor pose="mobile_user" label="Client App" sublabel="iOS / Android" />
        </div>

        {/* Single Monolith Server (Web + DB inside one machine) */}
        <div style={{ position: 'absolute', left: '600px', top: '460px' }}>
          <SystemNode
            type="WebServer"
            title="Monolith Server"
            tech="Web App + MySQL (Same Box)"
            status="healthy"
            cpuPercent={14}
            width={240}
            height={130}
          />
        </div>

        {/* Packet Connection */}
        <PacketConnection
          from={{ x: 270, y: 530 }}
          to={{ x: 600, y: 520 }}
          label="HTTPS GET"
          speedFrames={25}
        />

        {/* Annotation */}
        <HandDrawnAnnotation
          type="circle"
          x={580}
          y={440}
          width={280}
          height={170}
          text="Simple & cheap for Day 1"
          color="#38bdf8"
          startFrame={40}
        />
      </Sequence>

      {/* =========================================================
          ACT 2: THE CRASH & TIER SEPARATION (Frames 300 - 650)
          ========================================================= */}
      <Sequence from={300} durationInFrames={350}>
        {(() => {
          const actFrame = frame - 300;
          const isOverloaded = actFrame < 150;

          return (
            <>
              <MetricHUD
                levelTitle={isOverloaded ? "ALERT: RESOURCE EXHAUSTION" : "LEVEL 2: TIER SEPARATION"}
                userCount={interpolate(actFrame, [0, 100], [1000, 10000], { extrapolateRight: 'clamp' })}
                qps={1200}
                latencyMs={isOverloaded ? 980 : 38}
                isAlert={isOverloaded}
              />

              {/* Client Stickman */}
              <div style={{ position: 'absolute', left: '180px', top: '480px' }}>
                <StickmanActor
                  pose="mobile_user"
                  label="10,000 Users"
                  sublabel="High Concurrency"
                  isStressed={isOverloaded}
                />
              </div>

              {/* DevOps Engineer Panicking or Resolved */}
              <div style={{ position: 'absolute', left: '180px', top: '750px' }}>
                <StickmanActor
                  pose={isOverloaded ? "stressed_engineer" : "happy_engineer"}
                  label="DevOps On-Call"
                  sublabel={isOverloaded ? "PAGERDUTY ALARM" : "Architecture Fixed"}
                  isStressed={isOverloaded}
                  size={140}
                />
              </div>

              {isOverloaded ? (
                <>
                  {/* Overloaded Monolith */}
                  <div style={{ position: 'absolute', left: '600px', top: '460px' }}>
                    <SystemNode
                      type="WebServer"
                      title="Monolith Server"
                      tech="CPU at 100% / Out of RAM"
                      status="overload"
                      cpuPercent={100}
                      width={240}
                      height={130}
                    />
                  </div>
                  <PacketConnection
                    from={{ x: 270, y: 530 }}
                    to={{ x: 600, y: 520 }}
                    label="CONGESTED"
                    speedFrames={10}
                    isOverloaded={true}
                  />
                  <HandDrawnAnnotation
                    type="cross"
                    x={610}
                    y={470}
                    width={220}
                    height={110}
                    text="SPOF: Server & DB fight for RAM"
                    color="#ef4444"
                    startFrame={30}
                  />
                </>
              ) : (
                <>
                  {/* Dedicated Web Server */}
                  <div style={{ position: 'absolute', left: '550px', top: '460px' }}>
                    <SystemNode
                      type="WebServer"
                      title="Web App Server"
                      tech="Node.js / Express API"
                      status="healthy"
                      cpuPercent={42}
                      width={220}
                      height={120}
                    />
                  </div>

                  {/* Dedicated Database */}
                  <div style={{ position: 'absolute', left: '950px', top: '460px' }}>
                    <SystemNode
                      type="Database"
                      title="Database Tier"
                      tech="PostgreSQL (Dedicated Instance)"
                      status="healthy"
                      cpuPercent={35}
                      width={220}
                      height={120}
                    />
                  </div>

                  {/* Client -> Web Server */}
                  <PacketConnection
                    from={{ x: 270, y: 530 }}
                    to={{ x: 550, y: 520 }}
                    label="HTTPS API"
                    speedFrames={20}
                  />

                  {/* Web Server -> Database */}
                  <PacketConnection
                    from={{ x: 770, y: 520 }}
                    to={{ x: 950, y: 520 }}
                    label="SQL TCP"
                    speedFrames={18}
                    packetColor="#a855f7"
                  />

                  <HandDrawnAnnotation
                    type="circle"
                    x={930}
                    y={440}
                    width={260}
                    height={160}
                    text="Separate Compute from Storage!"
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
          ACT 3: 100,000 USERS — LOAD BALANCER & HORIZONTAL SCALE (Frames 650 - 1050)
          ========================================================= */}
      <Sequence from={650} durationInFrames={400}>
        {(() => {
          return (
            <>
              <MetricHUD
                levelTitle="LEVEL 3: HORIZONTAL WEB SCALE"
                userCount={100000}
                qps={15000}
                latencyMs={22}
                statusText="HIGH AVAILABILITY"
              />

              {/* Client Stickman */}
              <div style={{ position: 'absolute', left: '120px', top: '480px' }}>
                <StickmanActor pose="mobile_user" label="100,000 Users" sublabel="Global Traffic" />
              </div>

              {/* Load Balancer */}
              <div style={{ position: 'absolute', left: '420px', top: '460px' }}>
                <SystemNode
                  type="LoadBalancer"
                  title="Load Balancer"
                  tech="AWS ALB / Nginx"
                  status="healthy"
                  cpuPercent={28}
                  width={210}
                  height={120}
                />
              </div>

              {/* Cluster of 3 Web Servers */}
              <div style={{ position: 'absolute', left: '760px', top: '270px' }}>
                <SystemNode
                  type="WebServer"
                  title="Web Server 01"
                  tech="Stateless Container"
                  status="healthy"
                  cpuPercent={38}
                  width={200}
                  height={100}
                />
              </div>
              <div style={{ position: 'absolute', left: '760px', top: '470px' }}>
                <SystemNode
                  type="WebServer"
                  title="Web Server 02"
                  tech="Stateless Container"
                  status="healthy"
                  cpuPercent={41}
                  width={200}
                  height={100}
                />
              </div>
              <div style={{ position: 'absolute', left: '760px', top: '670px' }}>
                <SystemNode
                  type="WebServer"
                  title="Web Server 03"
                  tech="Stateless Container"
                  status="healthy"
                  cpuPercent={39}
                  width={200}
                  height={100}
                />
              </div>

              {/* Shared Database */}
              <div style={{ position: 'absolute', left: '1120px', top: '460px' }}>
                <SystemNode
                  type="Database"
                  title="PostgreSQL"
                  tech="Primary DB"
                  status="warning"
                  cpuPercent={78}
                  width={210}
                  height={120}
                />
              </div>

              {/* Packet Connections */}
              <PacketConnection from={{ x: 210, y: 530 }} to={{ x: 420, y: 520 }} label="HTTPS" speedFrames={15} />
              <PacketConnection from={{ x: 630, y: 490 }} to={{ x: 760, y: 320 }} speedFrames={18} />
              <PacketConnection from={{ x: 630, y: 520 }} to={{ x: 760, y: 520 }} speedFrames={18} />
              <PacketConnection from={{ x: 630, y: 550 }} to={{ x: 760, y: 720 }} speedFrames={18} />

              <PacketConnection from={{ x: 960, y: 320 }} to={{ x: 1120, y: 500 }} packetColor="#a855f7" speedFrames={20} />
              <PacketConnection from={{ x: 960, y: 520 }} to={{ x: 1120, y: 520 }} packetColor="#a855f7" speedFrames={20} />
              <PacketConnection from={{ x: 960, y: 720 }} to={{ x: 1120, y: 540 }} packetColor="#a855f7" speedFrames={20} />

              <HandDrawnAnnotation
                type="circle"
                x={1100}
                y={440}
                width={250}
                height={160}
                text="Next bottleneck: DB Read Heavy!"
                color="#f59e0b"
                startFrame={720}
              />
            </>
          );
        })()}
      </Sequence>

      {/* =========================================================
          ACT 4: 1,000,000 USERS — REDIS CACHE + READ REPLICAS (Frames 1050 - 1500)
          ========================================================= */}
      <Sequence from={1050} durationInFrames={450}>
        {(() => {
          return (
            <>
              <MetricHUD
                levelTitle="LEVEL 4: CACHE & READ REPLICAS"
                userCount={1000000}
                qps={65000}
                latencyMs={6}
                statusText="SUB-MS CACHE"
              />

              {/* Client Stickman */}
              <div style={{ position: 'absolute', left: '100px', top: '480px' }}>
                <StickmanActor pose="mobile_user" label="1 Million Users" sublabel="Heavy Read Loads" />
              </div>

              {/* Load Balancer */}
              <div style={{ position: 'absolute', left: '360px', top: '470px' }}>
                <SystemNode type="LoadBalancer" title="ALB Router" tech="Layer 7 Routing" width={190} height={110} />
              </div>

              {/* Web Servers Group */}
              <div style={{ position: 'absolute', left: '640px', top: '470px' }}>
                <SystemNode
                  type="WebServer"
                  title="App Fleet"
                  tech="Auto-Scaling Group"
                  scaleCount="x12 Nodes"
                  status="healthy"
                  cpuPercent={32}
                  width={210}
                  height={110}
                />
              </div>

              {/* Redis Cache Cluster (Top) */}
              <div style={{ position: 'absolute', left: '960px', top: '260px' }}>
                <SystemNode
                  type="Cache"
                  title="Redis Cluster"
                  tech="In-Memory RAM (Cache-Aside)"
                  status="healthy"
                  cpuPercent={22}
                  width={220}
                  height={115}
                />
              </div>

              {/* Primary DB (Writes Only) */}
              <div style={{ position: 'absolute', left: '960px', top: '460px' }}>
                <SystemNode
                  type="Database"
                  title="Primary DB"
                  tech="PostgreSQL (Master Writes)"
                  status="healthy"
                  cpuPercent={30}
                  width={220}
                  height={115}
                />
              </div>

              {/* Read Replica DBs (Reads Only) */}
              <div style={{ position: 'absolute', left: '960px', top: '660px' }}>
                <SystemNode
                  type="Database"
                  title="Read Replicas"
                  tech="Async Read Fleet (x3)"
                  scaleCount="x3"
                  status="healthy"
                  cpuPercent={26}
                  width={220}
                  height={115}
                />
              </div>

              {/* Connections */}
              <PacketConnection from={{ x: 190, y: 530 }} to={{ x: 360, y: 525 }} label="HTTPS" speedFrames={12} />
              <PacketConnection from={{ x: 550, y: 525 }} to={{ x: 640, y: 525 }} speedFrames={12} />

              {/* App Fleet -> Redis (Fast Sub-ms hit) */}
              <PacketConnection
                from={{ x: 850, y: 500 }}
                to={{ x: 960, y: 320 }}
                label="CACHE HIT (1ms)"
                packetColor="#10b981"
                speedFrames={10}
              />

              {/* App Fleet -> Primary (Writes) */}
              <PacketConnection
                from={{ x: 850, y: 525 }}
                to={{ x: 960, y: 520 }}
                label="WRITE ONLY"
                packetColor="#f59e0b"
                speedFrames={22}
              />

              {/* Primary -> Replica Sync */}
              <PacketConnection
                from={{ x: 1070, y: 575 }}
                to={{ x: 1070, y: 660 }}
                label="BINLOG REPLICATION"
                packetColor="#38bdf8"
                speedFrames={16}
              />

              <HandDrawnAnnotation
                type="circle"
                x={940}
                y={240}
                width={260}
                height={155}
                text="85%+ Traffic Served in RAM!"
                color="#10b981"
                startFrame={1120}
              />
            </>
          );
        })()}
      </Sequence>

      {/* =========================================================
          ACT 5: 10,000,000 USERS — ENTERPRISE GLOBAL SCALE (Frames 1500 - 2000)
          ========================================================= */}
      <Sequence from={1500} durationInFrames={500}>
        {(() => {
          return (
            <>
              <MetricHUD
                levelTitle="LEVEL 5: 10M GLOBAL SCALE"
                userCount={10000000}
                qps={280000}
                latencyMs={4}
                statusText="WORLDWIDE CDN + SHARDING"
              />

              {/* Global Clients Stickmen */}
              <div style={{ position: 'absolute', left: '60px', top: '350px' }}>
                <StickmanActor pose="mobile_user" label="US & EU Users" size={130} />
              </div>
              <div style={{ position: 'absolute', left: '60px', top: '620px' }}>
                <StickmanActor pose="mobile_user" label="Asia-Pac Users" size={130} />
              </div>

              {/* Global CDN Edge */}
              <div style={{ position: 'absolute', left: '260px', top: '470px' }}>
                <SystemNode
                  type="CDN"
                  title="Global CDN Edge"
                  tech="Cloudflare / 300+ PoPs"
                  scaleCount="Global"
                  status="healthy"
                  cpuPercent={18}
                  width={210}
                  height={115}
                />
              </div>

              {/* Load Balancer */}
              <div style={{ position: 'absolute', left: '530px', top: '470px' }}>
                <SystemNode
                  type="LoadBalancer"
                  title="Anycast DNS + ALB"
                  tech="Multi-Region Traffic"
                  status="healthy"
                  cpuPercent={24}
                  width={200}
                  height={115}
                />
              </div>

              {/* Microservices Cluster */}
              <div style={{ position: 'absolute', left: '800px', top: '470px' }}>
                <SystemNode
                  type="WebServer"
                  title="Microservices"
                  tech="Kubernetes (K8s) Cluster"
                  scaleCount="x150 Pods"
                  status="healthy"
                  cpuPercent={42}
                  width={210}
                  height={115}
                />
              </div>

              {/* Asynchronous Message Queue (Kafka) */}
              <div style={{ position: 'absolute', left: '1080px', top: '270px' }}>
                <SystemNode
                  type="MessageQueue"
                  title="Apache Kafka"
                  tech="Event Streaming Queue"
                  status="healthy"
                  cpuPercent={31}
                  width={210}
                  height={115}
                />
              </div>

              {/* Distributed Redis Cache */}
              <div style={{ position: 'absolute', left: '1080px', top: '470px' }}>
                <SystemNode
                  type="Cache"
                  title="Redis Global Cache"
                  tech="Multi-AZ In-Memory"
                  status="healthy"
                  cpuPercent={25}
                  width={210}
                  height={115}
                />
              </div>

              {/* Sharded Database Cluster */}
              <div style={{ position: 'absolute', left: '1080px', top: '670px' }}>
                <SystemNode
                  type="Database"
                  title="Sharded PostgreSQL"
                  tech="Partitioned by User UUID"
                  scaleCount="x8 Shards"
                  status="healthy"
                  cpuPercent={34}
                  width={210}
                  height={115}
                />
              </div>

              {/* Happy DevOps Architect celebrating */}
              <div style={{ position: 'absolute', left: '1420px', top: '460px' }}>
                <StickmanActor
                  pose="happy_engineer"
                  label="Principal Architect"
                  sublabel="10M USERS READY"
                  size={170}
                />
              </div>

              {/* Interconnected Packet Flows */}
              <PacketConnection from={{ x: 130, y: 400 }} to={{ x: 260, y: 520 }} speedFrames={10} />
              <PacketConnection from={{ x: 130, y: 670 }} to={{ x: 260, y: 540 }} speedFrames={10} />
              <PacketConnection from={{ x: 470, y: 527 }} to={{ x: 530, y: 527 }} label="EDGE CACHED" packetColor="#10b981" speedFrames={10} />
              <PacketConnection from={{ x: 730, y: 527 }} to={{ x: 800, y: 527 }} speedFrames={10} />

              {/* K8s to Kafka Async */}
              <PacketConnection from={{ x: 1010, y: 500 }} to={{ x: 1080, y: 330 }} label="ASYNC EVENT" packetColor="#f59e0b" speedFrames={12} />
              {/* K8s to Redis Cache */}
              <PacketConnection from={{ x: 1010, y: 527 }} to={{ x: 1080, y: 527 }} label="RAM GET" packetColor="#38bdf8" speedFrames={8} />
              {/* K8s to Sharded DB */}
              <PacketConnection from={{ x: 1010, y: 555 }} to={{ x: 1080, y: 725 }} label="SHARDED WRITE" packetColor="#a855f7" speedFrames={15} />

              <HandDrawnAnnotation
                type="circle"
                x={1390}
                y={430}
                width={240}
                height={230}
                text="Zero Single Point of Failure"
                color="#10b981"
                startFrame={1550}
              />
            </>
          );
        })()}
      </Sequence>
    </div>
  );
};
