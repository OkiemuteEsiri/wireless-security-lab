# Example Wireless Security Findings

> Synthetic portfolio output. No production network data is represented.

## Executive summary
The sample dataset produces several high-priority control failures: a corporate SSID advertised from an unrecognized BSSID, legacy encryption on a guest AP, and security-profile drift on an authorized corporate AP. The highest priority is to validate the unknown infrastructure and restore approved encryption settings.

## Priority findings

| ID | Severity | Scenario | Recommended action |
|---|---|---|---|
| WIFI-002 | Critical | Corporate SSID from unknown BSSID | Validate ownership and isolate/remove if unauthorized |
| WIFI-003 | Critical | WEP observed | Migrate to approved modern encryption |
| WIFI-004 | High | Authorized AP encryption drift | Restore approved security profile |
| WIFI-005 | Medium | PMF requirement not met | Enable PMF and revalidate |
| WIFI-006 | Medium | Authorized AP location mismatch | Reconcile change/physical inventory |

## Validation plan
Re-run the analyzer after corrective action. Closure requires the exact failed control to pass and supporting inventory/configuration evidence to be recorded.
