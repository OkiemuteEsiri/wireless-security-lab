from __future__ import annotations

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

SEVERITY_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}


@dataclass(frozen=True)
class Finding:
    control_id: str
    severity: str
    ssid: str
    bssid: str
    evidence: str
    remediation: str
    validation: str


def load_json(path: str | Path) -> list[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("Expected a JSON list")
    return data


def index_authorized(authorized: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(ap["bssid"]).lower(): ap for ap in authorized}


def analyze(authorized: list[dict[str, Any]], observations: list[dict[str, Any]]) -> list[Finding]:
    baseline = index_authorized(authorized)
    approved_ssids = {str(ap["ssid"]) for ap in authorized}
    findings: list[Finding] = []

    for obs in observations:
        bssid = str(obs["bssid"]).lower()
        ssid = str(obs["ssid"])
        encryption = str(obs.get("encryption", "unknown")).upper()
        pmf = bool(obs.get("pmf", False))
        location = str(obs.get("location", "unknown"))
        approved = baseline.get(bssid)

        if approved is None:
            severity = "critical" if ssid in approved_ssids else "high"
            findings.append(Finding(
                "WIFI-001", severity, ssid, bssid,
                "Observed BSSID is absent from the authorized inventory.",
                "Validate ownership and remove, isolate, or formally authorize the device.",
                "Re-scan and confirm the BSSID is absent or appears in an approved inventory entry."
            ))

        if ssid in approved_ssids and approved is None:
            findings.append(Finding(
                "WIFI-002", "critical", ssid, bssid,
                "Corporate SSID is advertised by an unrecognized BSSID.",
                "Investigate as an impersonation indicator and validate physical/network ownership.",
                "Confirm only approved BSSIDs advertise the corporate SSID."
            ))

        if encryption in {"OPEN", "WEP", "WPA", "WPA1"}:
            findings.append(Finding(
                "WIFI-003", "critical", ssid, bssid,
                f"Observed legacy or insecure encryption mode: {encryption}.",
                "Migrate to the organization's approved WPA2-Enterprise/WPA3 policy.",
                "Confirm subsequent observations report only approved encryption modes."
            ))

        if approved:
            expected_encryption = str(approved.get("encryption", "")).upper()
            if expected_encryption and encryption != expected_encryption:
                findings.append(Finding(
                    "WIFI-004", "high", ssid, bssid,
                    f"Encryption drift: observed {encryption}, expected {expected_encryption}.",
                    "Restore the approved security profile or document a time-bounded exception.",
                    "Re-observe the AP and match encryption to the approved baseline."
                ))

            if bool(approved.get("pmf_required", False)) and not pmf:
                findings.append(Finding(
                    "WIFI-005", "medium", ssid, bssid,
                    "Protected Management Frames are required by baseline but not observed.",
                    "Enable PMF according to the approved wireless profile.",
                    "Confirm PMF is enabled in both controller configuration and subsequent observation."
                ))

            expected_location = str(approved.get("location", ""))
            if expected_location and location != expected_location:
                findings.append(Finding(
                    "WIFI-006", "medium", ssid, bssid,
                    f"Location drift: observed {location}, expected {expected_location}.",
                    "Validate asset movement against change records and update or correct placement.",
                    "Confirm physical inventory and observation location agree."
                ))

    return sorted(findings, key=lambda item: SEVERITY_ORDER[item.severity], reverse=True)


def summarize(findings: list[Finding]) -> dict[str, int]:
    summary = {level: 0 for level in SEVERITY_ORDER}
    for finding in findings:
        summary[finding.severity] += 1
    return summary


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python src/wireless_analyzer.py <authorized.json> <observations.json>")
        return 2
    findings = analyze(load_json(sys.argv[1]), load_json(sys.argv[2]))
    print(json.dumps({"summary": summarize(findings), "findings": [asdict(f) for f in findings]}, indent=2))
    return 1 if any(f.severity in {"high", "critical"} for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
