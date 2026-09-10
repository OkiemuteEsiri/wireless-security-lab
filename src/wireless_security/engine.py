from __future__ import annotations

import hashlib
from typing import Iterable, List

from .models import AccessPoint, Finding

SEVERITY_WEIGHT = {"critical": 25, "high": 15, "medium": 8, "low": 3}


def _id(asset: str, rule: str) -> str:
    digest = hashlib.sha256(f"{asset}|{rule}".encode()).hexdigest()[:10]
    return f"WIFI-{digest.upper()}"


def _finding(ap: AccessPoint, rule: str, title: str, severity: str, evidence: list[str], remediation: str, validation: str, mitre: tuple[str, ...] = ()) -> Finding:
    return Finding(_id(ap.bssid, rule), title, severity, ap.ssid, tuple(evidence), remediation, validation, mitre)


def assess_devices(devices: Iterable[AccessPoint]) -> List[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()
    for ap in devices:
        if ap.bssid in seen:
            raise ValueError(f"duplicate BSSID: {ap.bssid}")
        seen.add(ap.bssid)

        if ap.security in {"OPEN", "WEP"}:
            findings.append(_finding(ap, "legacy-security", "Insecure wireless authentication/encryption", "critical", [f"security={ap.security}"], "Migrate to WPA3-Enterprise where supported, otherwise WPA2-Enterprise with strong EAP and certificate validation.", "Confirm legacy SSID is removed and reassess negotiated security mode.", ("T1557 - Adversary-in-the-Middle",)))
        elif ap.security == "WPA2-PSK":
            findings.append(_finding(ap, "shared-psk", "Shared pre-shared key used", "medium", ["security=WPA2-PSK"], "Prefer enterprise authentication with unique identities; rotate any retained PSKs and separate guest access.", "Verify enterprise authentication or documented compensating controls."))

        if ap.wps_enabled:
            findings.append(_finding(ap, "wps", "Wi-Fi Protected Setup enabled", "high", ["wps_enabled=true"], "Disable WPS on managed access points.", "Confirm WPS is disabled in configuration and through authorized validation."))
        if not ap.pmf_required:
            findings.append(_finding(ap, "pmf", "Protected Management Frames not required", "medium", ["pmf_required=false"], "Require 802.11w/PMF where client compatibility permits.", "Confirm PMF is required and representative clients connect successfully.", ("T1498 - Network Denial of Service",)))
        if not ap.guest_isolation and "guest" in ap.ssid.lower():
            findings.append(_finding(ap, "guest-isolation", "Guest wireless network lacks client isolation", "high", ["guest_isolation=false", f"ssid={ap.ssid}"], "Enable client isolation and restrict guest-to-internal routing with explicit firewall policy.", "Validate east-west guest traffic is blocked and internal routes are inaccessible."))
        if ap.admin_interface_exposed:
            findings.append(_finding(ap, "admin-exposure", "Wireless management interface exposed to user WLAN", "high", ["admin_interface_exposed=true", f"management_vlan={ap.management_vlan}"], "Restrict management planes to dedicated administrative networks and strong identity controls.", "Verify management endpoints are unreachable from user and guest WLANs."))
        if not ap.owner.strip():
            findings.append(_finding(ap, "ownership", "Access point has no accountable owner", "low", ["owner is empty"], "Assign a technical/business owner and lifecycle responsibility.", "Confirm ownership appears in the authoritative inventory."))
        if ap.firmware_age_days > 365:
            findings.append(_finding(ap, "firmware", "Wireless firmware is stale", "medium", [f"firmware_age_days={ap.firmware_age_days}"], "Review vendor support status and apply an approved current firmware release.", "Confirm firmware version/date meets the organization's supported baseline."))
    return findings


def posture_score(findings: Iterable[Finding]) -> int:
    penalty = sum(SEVERITY_WEIGHT.get(f.severity, 0) for f in findings)
    return max(0, 100 - min(100, penalty))
