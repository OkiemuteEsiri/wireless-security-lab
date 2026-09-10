from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

_ALLOWED_SECURITY = {"OPEN", "WEP", "WPA2-PSK", "WPA2-ENT", "WPA3-SAE", "WPA3-ENT"}


@dataclass(frozen=True)
class AccessPoint:
    ssid: str
    bssid: str
    security: str
    wps_enabled: bool
    pmf_required: bool
    management_vlan: str
    guest_isolation: bool
    admin_interface_exposed: bool
    owner: str
    firmware_age_days: int

    def __post_init__(self) -> None:
        if not self.ssid.strip():
            raise ValueError("ssid must not be empty")
        if self.security not in _ALLOWED_SECURITY:
            raise ValueError(f"unsupported security mode: {self.security}")
        if self.firmware_age_days < 0:
            raise ValueError("firmware_age_days must be non-negative")


@dataclass(frozen=True)
class Finding:
    finding_id: str
    title: str
    severity: str
    asset: str
    evidence: Tuple[str, ...]
    remediation: str
    validation: str
    mitre_attack: Tuple[str, ...] = ()
