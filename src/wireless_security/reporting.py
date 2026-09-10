from __future__ import annotations

from collections import Counter
from .engine import posture_score
from .models import Finding


def render_markdown(findings: list[Finding]) -> str:
    counts = Counter(f.severity for f in findings)
    lines = [
        "# Wireless Security Assessment",
        "",
        f"Posture score: **{posture_score(findings)}/100**",
        "",
        f"Findings: {len(findings)} | Critical: {counts['critical']} | High: {counts['high']} | Medium: {counts['medium']} | Low: {counts['low']}",
        "",
    ]
    for f in sorted(findings, key=lambda x: (-( {'critical':4,'high':3,'medium':2,'low':1}[x.severity]), x.asset, x.title)):
        lines += [
            f"## {f.finding_id} — {f.title}",
            "",
            f"- Asset: `{f.asset}`",
            f"- Severity: **{f.severity.upper()}**",
            f"- Evidence: {'; '.join(f.evidence)}",
            f"- Remediation: {f.remediation}",
            f"- Validation: {f.validation}",
        ]
        if f.mitre_attack:
            lines.append(f"- MITRE ATT&CK context: {', '.join(f.mitre_attack)}")
        lines.append("")
    return "\n".join(lines)
