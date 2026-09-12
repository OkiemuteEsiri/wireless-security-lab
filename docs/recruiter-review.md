# Recruiter / Technical Review Guide

This guide provides a short path through the strongest evidence in this wireless-security flagship without requiring a reviewer to inspect every file.

## Five-minute review path

1. **Start with `README.md`** — problem statement, architecture, controls, limitations, safety boundaries, and roadmap.
2. **Review `src/wireless_security/engine.py`** — deterministic defensive control evaluation and finding generation.
3. **Review `src/wireless_security/models.py`** — validated domain model and fail-closed input handling.
4. **Review `src/wireless_security/reporting.py`** — posture scoring and analyst-facing reporting.
5. **Inspect `data/` and `reports/`** — fictional inputs and example assessment output.
6. **Inspect `tests/` and `.github/workflows/ci.yml`** — automated validation and quality controls.
7. **Read `docs/METHODOLOGY.md` and `docs/control-validation-matrix.md`** — assessment logic, evidence standards, remediation, and revalidation.

## Capability-to-evidence map

| Capability | Evidence in repository |
|---|---|
| Wireless security engineering | Baseline controls for encryption, PMF, WPS, segmentation, management-plane placement, firmware and ownership |
| Defensive security automation | Deterministic Python assessment engine and CLI |
| Asset/inventory reconciliation | Approved AP inventory compared with passive observations and configuration state |
| Risk communication | Severity classification, posture scoring, prioritized findings and Markdown reporting |
| Evidence handling | Findings preserve affected asset, observed condition, recommendation and validation requirement |
| Remediation governance | Defined corrective-action and fresh-evidence revalidation lifecycle |
| Testing discipline | Unit tests covering observation/configuration analysis and validation behavior |
| CI/CD quality | Least-privilege GitHub Actions workflow for compile, test and smoke validation |
| Threat-informed defense | MITRE ATT&CK context used only to explain defensive relevance |

## What this project is designed to demonstrate

A reviewer should be able to answer the following questions from the repository:

- How is an authorized wireless baseline represented and validated?
- How does the project distinguish approved infrastructure from configuration drift or suspicious observations?
- Which wireless control failures receive the highest priority and why?
- How are evidence quality and false-positive risk handled?
- What must be observed before a finding is considered technically remediated?
- How are ATT&CK mappings prevented from becoming unsupported compromise claims?
- Which safety boundaries keep the project defensive and reproducible?

## Security boundaries

The project uses synthetic data and offline analysis. It does not perform packet injection, deauthentication, credential capture, cracking, exploitation, bypass testing, or production targeting. ATT&CK mappings are threat-model context rather than evidence of an intrusion.

## CI interpretation

A workflow definition is not evidence that a particular revision passed. CI should be described as green only after the GitHub Actions result for the exact commit under review has completed successfully.
