# Wireless Security Engineering Lab

A defensive wireless-security project for evaluating enterprise Wi-Fi posture from **synthetic, passive observation data**. The lab demonstrates asset authorization checks, encryption-policy validation, rogue-access-point indicators, configuration drift detection, risk scoring, remediation tracking, and evidence-based revalidation without targeting real networks.

## Why this project exists

Wireless risk is not limited to weak passwords. Security teams must distinguish authorized infrastructure from lookalike SSIDs, detect legacy encryption, identify configuration drift, and validate that remediation actually removed the exposure. This project models that workflow as code.

## Architecture

```text
synthetic observations + authorized AP inventory
                  |
                  v
        normalization / validation
                  |
                  v
     wireless posture analyzer
       |      |       |      |
       |      |       |      +--> signal/location anomaly
       |      |       +---------> encryption-policy drift
       |      +-----------------> BSSID authorization
       +------------------------> SSID impersonation indicator
                  |
                  v
         scored security findings
                  |
                  v
        remediation + revalidation
```

## Controls implemented

| Control | What it detects | Risk |
|---|---|---|
| Authorized BSSID | Observed AP not present in approved inventory | High |
| SSID impersonation | Known corporate SSID advertised by an unknown BSSID | Critical |
| Encryption baseline | Open/WEP/WPA1 or policy downgrade | Critical–High |
| Management-frame policy | Missing PMF where required | Medium |
| Location drift | Authorized AP observed outside expected zone | Medium |
| Configuration drift | Approved AP differs from baseline security mode | High |

## Repository structure

```text
src/wireless_analyzer.py          posture and risk engine
data/authorized_aps.json          synthetic approved inventory
data/observations.json            synthetic passive observations
tests/test_wireless_analyzer.py   unit tests
docs/methodology.md               assessment methodology
docs/remediation-validation.md    closure/retest workflow
reports/example-findings.md       recruiter-readable sample output
.github/workflows/ci.yml          automated unit testing
```

## Run locally

```bash
python -m unittest discover -s tests -v
python src/wireless_analyzer.py data/authorized_aps.json data/observations.json
```

The analyzer uses only the Python standard library.

## Finding model

Each finding contains a control ID, severity, SSID, BSSID, evidence, recommended action, and validation requirement. The project intentionally avoids active attack automation, credential capture, deauthentication, cracking, or production targeting.

## Security engineering workflow

1. Define an approved wireless baseline.
2. Ingest passive observations from a controlled/synthetic source.
3. Normalize SSID, BSSID, encryption, PMF, channel, and location metadata.
4. Evaluate each observation against approved state.
5. Prioritize findings by business/security impact.
6. Record corrective action.
7. Re-run the same deterministic checks as closure evidence.

## ATT&CK context

Wireless impersonation and unauthorized infrastructure can facilitate credential-access or adversary-in-the-middle scenarios. ATT&CK is used here only for defensive threat-context mapping; the repository contains no offensive execution guidance.

## Skills demonstrated

- Wireless security engineering
- Security control validation
- Python automation
- Asset/inventory reconciliation
- Risk scoring and evidence handling
- Detection-oriented reasoning
- Remediation verification
- Unit testing and CI

## Limitations

This is a portfolio lab using synthetic observations. Signal strength alone cannot prove malicious intent, and production wireless investigations require approved sensors, RF context, physical validation, change records, and organizational authorization.

## Roadmap

- Add normalized JSON report export
- Add channel-policy and 6 GHz baseline checks
- Add approved exception handling with expiry dates
- Add trend metrics for recurring configuration drift
- Add optional visualization layer for finding summaries

## Ethical scope

Use only with systems and telemetry you own or are explicitly authorized to assess. No real credentials, customer information, employer data, or production identifiers are included.