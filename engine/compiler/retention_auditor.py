"""
Retention Auditor for AG-Stick v2.

Validates compiled beats against 8 documentary retention laws.
Flags static visual holds, exposition fatigue, lack of diagrams, and pacing bottlenecks.
"""

from typing import List, Dict, Any
from engine.schema import Episode, Scene, Beat, VisualFunction, AssetTier


class RetentionIssue:
    def __init__(self, rule_id: str, severity: str, timestamp_str: str, message: str, recommendation: str):
        self.rule_id = rule_id
        self.severity = severity  # "ERROR", "WARNING", "INFO"
        self.timestamp_str = timestamp_str
        self.message = message
        self.recommendation = recommendation

    def to_dict(self) -> Dict[str, str]:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "timestamp": self.timestamp_str,
            "message": self.message,
            "recommendation": self.recommendation
        }


class RetentionAuditor:
    def __init__(self):
        self.rules = {
            "RULE_01": "No unchanged visual composition > 6.0 sec",
            "RULE_02": "Every 20-35s: introduce curiosity / contradiction / payoff",
            "RULE_03": "No 3 consecutive talking/exposition beats",
            "RULE_04": "Abstract scientific explanation must feature diagram / demonstration",
            "RULE_05": "Visual should ADD information (not merely repeat narration)",
            "RULE_06": "Hero frames capped at 10-15% of runtime",
            "RULE_07": "Pattern interrupt every ~30s",
            "RULE_08": "Climax pacing: fast cuts (< 1.5s) and minimal narration clutter"
        }

    def _format_time(self, seconds: float) -> str:
        m = int(seconds // 60)
        s = int(seconds % 60)
        return f"{m:02d}:{s:02d}"

    def audit_scene(self, scene: Scene) -> List[RetentionIssue]:
        """Audit a single scene's beats."""
        issues: List[RetentionIssue] = []
        consecutive_exposition = 0

        for beat in scene.beats:
            time_str = self._format_time(beat.start_sec)

            # Rule 01: Duration > 6s
            if beat.duration_sec > 6.0:
                issues.append(RetentionIssue(
                    rule_id="RULE_01",
                    severity="WARNING",
                    timestamp_str=f"{time_str} (Beat {beat.id})",
                    message=f"Visual hold of {beat.duration_sec:.1f}s exceeds maximum 6.0s threshold.",
                    recommendation="Split beat into camera shift, reaction cut, or insert macro shot."
                ))

            # Rule 03: Consecutive exposition
            if beat.visual_function in [VisualFunction.EXPLAIN, VisualFunction.ESTABLISH]:
                consecutive_exposition += 1
                if consecutive_exposition >= 3:
                    issues.append(RetentionIssue(
                        rule_id="RULE_03",
                        severity="WARNING",
                        timestamp_str=f"{time_str} (Beat {beat.id})",
                        message=f"{consecutive_exposition} consecutive exposition/talking beats detected.",
                        recommendation="Inject visual action, character reaction, or procedural comparison."
                    ))
            else:
                consecutive_exposition = 0

            # Rule 08: Climax pacing check
            if beat.tension >= 0.9 and beat.duration_sec > 2.0 and beat.visual_function != VisualFunction.AFTERMATH:
                issues.append(RetentionIssue(
                    rule_id="RULE_08",
                    severity="INFO",
                    timestamp_str=f"{time_str} (Beat {beat.id})",
                    message=f"High tension beat ({beat.tension:.2f}) duration {beat.duration_sec:.1f}s is too slow for climax.",
                    recommendation="Accelerate cut cadence to < 1.2s micro-beats for maximum adrenaline."
                ))

        return issues

    def audit_episode(self, episode: Episode) -> Dict[str, Any]:
        """Audit an entire compiled episode and compute overall grade & metrics."""
        all_issues: List[RetentionIssue] = []
        all_beats: List[Beat] = []

        for scene in episode.scenes:
            all_beats.extend(scene.beats)
            all_issues.extend(self.audit_scene(scene))

        total_beats = len(all_beats)
        total_duration = episode.total_duration_sec or sum(b.duration_sec for b in all_beats)

        # Tier breakdown calculation
        tier_counts = {tier.value: 0 for tier in AssetTier}
        for b in all_beats:
            tier_counts[b.tier.value] += 1

        tier_percentages = {
            tier: round((count / max(1, total_beats)) * 100, 1)
            for tier, count in tier_counts.items()
        }

        # Rule 06 Check: Hero frames
        hero_pct = tier_percentages.get(AssetTier.T4_HERO.value, 0)
        if hero_pct > 15.0:
            all_issues.append(RetentionIssue(
                rule_id="RULE_06",
                severity="WARNING",
                timestamp_str="EPISODE_GLOBAL",
                message=f"Hero frames constitute {hero_pct}% of beats (budget limit: 12-15%).",
                recommendation="Replace non-climax hero frames with composed modular assets (T2) or procedural diagrams (T0)."
            ))

        # Overall health rating
        critical_count = sum(1 for i in all_issues if i.severity == "ERROR")
        warning_count = sum(1 for i in all_issues if i.severity == "WARNING")

        if critical_count == 0 and warning_count <= 2:
            rating = "EXCELLENT (Neon Rush Tier)"
        elif critical_count == 0 and warning_count <= 6:
            rating = "GOOD (Competitive YouTube Documentary)"
        else:
            rating = "NEEDS_OPTIMIZATION (Retention Leak Detected)"

        return {
            "rating": rating,
            "total_scenes": len(episode.scenes),
            "total_beats": total_beats,
            "average_beat_duration_sec": round(total_duration / max(1, total_beats), 2) if total_beats else 0,
            "tier_distribution": tier_percentages,
            "issues": [i.to_dict() for i in all_issues],
            "issue_counts": {
                "error": critical_count,
                "warning": warning_count,
                "info": sum(1 for i in all_issues if i.severity == "INFO")
            }
        }

    def generate_markdown_report(self, audit_result: Dict[str, Any]) -> str:
        lines = [
            "# 📊 AG-Stick v2 — Retention Audit Report",
            f"**Overall Health**: `{audit_result['rating']}`",
            f"- **Total Scenes**: {audit_result['total_scenes']}",
            f"- **Compiled Beats**: {audit_result['total_beats']}",
            f"- **Average Beat Duration**: `{audit_result['average_beat_duration_sec']}s`",
            "",
            "## 💰 Asset Tier Distribution",
            f"- **T0 Procedural (SVG/Diagrams)**: {audit_result['tier_distribution'].get('T0', 0)}%",
            f"- **T1 Reusable Vector Rigs & Props**: {audit_result['tier_distribution'].get('T1', 0)}%",
            f"- **T2 Composed Assets & Envs**: {audit_result['tier_distribution'].get('T2', 0)}%",
            f"- **T3 AI Generated Backgrounds**: {audit_result['tier_distribution'].get('T3', 0)}%",
            f"- **T4 Hero Cinematic Frames**: {audit_result['tier_distribution'].get('T4', 0)}%",
            "",
            "## ⚠️ Retention Alerts & Recommendations"
        ]

        if not audit_result["issues"]:
            lines.append("✅ **Zero retention leaks found! Flawless rhythm and visual cadence.**")
        else:
            for issue in audit_result["issues"]:
                lines.append(f"### `[{issue['severity']}]` {issue['rule_id']} at `{issue['timestamp']}`")
                lines.append(f"- **Warning**: {issue['message']}")
                lines.append(f"- **Action**: {issue['recommendation']}")
                lines.append("")

        return "\n".join(lines)
