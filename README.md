# Wireless Security Engineering Lab

A defensive wireless-security project for evaluating enterprise Wi-Fi posture from **synthetic, passive observation data and authorized configuration inventory**. The lab demonstrates asset authorization checks, encryption-policy validation, rogue-access-point indicators, configuration drift detection, management-plane review, lifecycle hygiene, risk scoring, remediation tracking, and evidence-based revalidation without targeting real networks.

## Why this project exists

Wireless risk is not limited to weak passwords. Security teams must distinguish authorized infrastructure from lookalike SSIDs, detect legacy or downgraded encryption, identify configuration drift, review segmentation and management-plane exposure, and validate that remediation actually removed the exposure. This project models that workflow as code.

## Architecture

```text
synthetic observations + authorized AP inventory
                  |
                  v
        normalization / validation
                  |
          +-------+-------+
          |               |
          v               v
 passive observation   configuration baseline
 analyzer              assessment engine
          |               |
          +-------+-------+
                  |
                  v
         scored security findings
                  |
                  v
        remediation + revalidation
```

The hardening layer in `src/wireless_security/` adds immutable validated domain models, duplicate-BSSID rejection, deterministic finding IDs, evidence-preserving findings, bounded posture scoring, Markdown reporting, and a reusable CLI. This complements the existing observation-oriented analyzer rather than replacing it.

## Controls implemented

| Control | What it detects | Risk |
|---|---|---|
| Authorized BSSID | Observed AP not present in approved inventory | High |
| SSID impersonation | Known corporate SSID advertised by an unknown BSSID | Critical |
| Encryption baseline | Legacy/open modes, WPA2-PSK use, or policy downgrade | Critical–Medium |
| WPS policy | Wi-Fi Protected Setup enabled | High |
| Management-frame policy | PMF not required where expected | Medium |
| Guest segmentation | Guest WLAN without client isolation | High |
| Management-plane exposure | Administrative interface reachable from user WLAN context | High |
| Firmware lifecycle | Firmware age beyond defined baseline | Medium |
| Ownership | Wireless asset has no accountable owner | Low |
| Location/configuration drift | Approved AP differs from expected state | High–Medium |

## Repository structure

```text
src/wireless_analyzer.py             passive observation posture engine
src/wireless_security/models.py      validated configuration domain model
src/wireless_security/engine.py      deterministic baseline control engine
src/wireless_security/reporting.py   posture scoring and Markdown reporting
src/wireless_security/cli.py         inventory assessment CLI
data/authorized_aps.json             synthetic approved inventory
data/observations.json               synthetic passive observations
data/synthetic_access_points.json    synthetic configuration inventory
tests/                               observation and configuration unit tests
docs/ARCHITECTURE.md                 hardened engine architecture
docs/METHODOLOGY.md                  assessment and revalidation methodology
docs/remediation-validation.md       closure/retest workflow
reports/                              example and generated reports
.github/workflows/ci.yml             compile, unit-test, and smoke-test checks
```

## Run locally

```bash
python -m unittest discover -s tests -v
python src/wireless_analyzer.py data/authorized_aps.json data/observations.json
python -m src.wireless_security.cli data/synthetic_access_points.json --output reports/generated-baseline.md
```

The assessment code uses only the Python standard library.

## Finding model

Each hardened configuration finding contains a deterministic finding ID, severity, affected wireless asset, evidence, recommended action, explicit validation requirement, and optional ATT&CK context. The project intentionally avoids active attack automation, credential capture, deauthentication, cracking, packet injection, or production targeting.

## Security engineering workflow

1. Define an approved wireless baseline.
2. Ingest passive observations and/or authorized configuration inventory.
3. Validate schema, uniqueness, ownership, security mode, PMF, WPS, segmentation, management-plane placement, and lifecycle attributes.
4. Evaluate observations and configurations against deterministic controls.
5. Prioritize findings by security impact.
6. Record corrective action and accountable ownership.
7. Re-run the same checks against fresh data as closure evidence.
8. Retain before/after reports for auditability.

## MITRE ATT&CK context

Mappings are used only for defensive threat-model context and do not imply exploitation or compromise. Relevant contextual mappings include:

- **T1557 — Adversary-in-the-Middle** for insecure wireless authentication/encryption scenarios.
- **T1498 — Network Denial of Service** as context for management-frame protection and resilience controls.

## CI/CD security checks

The GitHub Actions workflow is intentionally least-privilege (`contents: read`) and performs:

- Python source compilation
- full unit-test discovery
- configuration-baseline CLI smoke test
- generated report existence/content validation

CI status should be treated as authoritative only after the workflow for the relevant commit completes.

## Skills demonstrated

- Wireless security engineering
- Defensive configuration assessment
- Python security automation
- Asset/inventory reconciliation
- Deterministic risk scoring and evidence handling
- Detection-oriented reasoning
- Remediation and closure validation
- Unit testing and CI/CD quality gates
- Threat-model mapping with MITRE ATT&CK

## Limitations

This is a portfolio lab using synthetic data. Signal strength alone cannot prove malicious intent, and a configuration finding does not prove exploitability or compromise. Production wireless investigations require approved sensors/controllers, RF context, physical validation, change records, organizational authorization, and vendor-specific telemetry.

## Roadmap

- Add normalized JSON report export
- Add channel-policy and 6 GHz baseline checks
- Add approved exception handling with expiry dates
- Add trend metrics for recurring configuration drift
- Add vendor-neutral adapter interfaces for authorized controller exports
- Add optional visualization of posture trends

## Ethical scope

Use only with systems and telemetry you own or are explicitly authorized to assess. No real credentials, customer information, employer/client data, production identifiers, exploit payloads, or offensive wireless automation are included.
