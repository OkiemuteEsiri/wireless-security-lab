# Architecture

This project models a defensive wireless security posture assessment pipeline for authorized inventory data. It does not perform packet injection, credential capture, deauthentication, exploitation, or active targeting.

## Flow

1. **Inventory ingestion** — structured access-point attributes are loaded from synthetic or authorized sources.
2. **Validation** — domain models reject unsupported security modes, invalid ages, and duplicate BSSIDs.
3. **Control evaluation** — deterministic rules evaluate encryption/authentication, WPS, PMF, guest isolation, management-plane exposure, lifecycle ownership, and firmware age.
4. **Risk normalization** — findings use consistent severity labels and bounded posture scoring.
5. **Evidence preservation** — each finding records observed configuration evidence, remediation, and a validation condition.
6. **Reporting** — Markdown output supports recruiter review, remediation planning, and repeatable reassessment.

## Design principles

- Defensive-only: no offensive wireless actions are implemented.
- Deterministic: identical inputs produce identical finding IDs and results.
- Explainable: every rule emits evidence and a closure criterion.
- Fail-closed validation: malformed or duplicate inventory is rejected instead of silently accepted.
- Provider-neutral: the model is not tied to a specific WLAN vendor.

## Extension points

Future adapters can normalize authorized controller exports from platforms such as Cisco, Aruba, Meraki, or cloud-managed WLAN systems into the same `AccessPoint` model. Production integrations should add authentication isolation, pagination, retry controls, schema versioning, and secrets management without changing the assessment core.
