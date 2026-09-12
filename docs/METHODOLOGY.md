# Wireless Security Assessment Methodology

## Purpose and scope

This project models a defensive enterprise wireless-security review using only synthetic passive observations and authorized configuration inventory. It is intended for owned or explicitly authorized environments and evaluates control posture, configuration drift, governance, and remediation evidence. It does **not** attempt to prove exploitability or compromise.

## Assessment workflow

1. Establish the authorized access-point inventory and expected security baseline.
2. Validate input completeness, uniqueness, and required ownership/context fields.
3. Normalize SSID, BSSID, authentication/encryption, PMF, WPS, channel, location, management-plane, segmentation, firmware, and ownership metadata.
4. Compare passive observations and approved configuration against expected state.
5. Classify deviations by security impact, confidence, and affected control family.
6. Corroborate suspicious observations with controller inventory, switch-port data, NAC records, physical validation, and approved change records where available.
7. Assign remediation ownership and document the intended corrective control.
8. Re-run the same deterministic checks against fresh observations/configuration after remediation.
9. Preserve before/after evidence and validation results for auditability.

## Control sequence

The assessment evaluates the following control families:

- authorized infrastructure and BSSID ownership;
- corporate SSID impersonation indicators;
- authentication and encryption baseline;
- WPS exposure;
- protected management frames (PMF);
- guest WLAN client isolation and segmentation;
- wireless management-plane placement;
- firmware lifecycle hygiene;
- accountable asset ownership;
- expected location and configuration drift.

## Severity model

- **Critical** — direct systemic exposure such as obsolete/open encryption or a known corporate SSID advertised by unknown infrastructure.
- **High** — material control weakness with practical abuse potential, including unauthorized infrastructure, encryption downgrade, exposed management plane, or missing guest isolation.
- **Medium** — defense-in-depth, lifecycle, authentication-design, PMF, or location-drift weakness requiring planned remediation.
- **Low** — governance or inventory hygiene weakness with limited immediate exploitability.

Severity communicates control impact; it is not a probability-of-compromise claim.

## Evidence quality

A single passive observation is not sufficient to prove malicious activity. Evidence confidence improves when observations are corroborated with authorized enterprise sources such as:

- wireless-controller inventory;
- switch-port or network-access-control records;
- approved change records;
- physical inspection;
- configuration exports;
- representative client-connectivity validation after a change.

The lab keeps raw synthetic evidence alongside normalized findings so that conclusions remain reviewable.

## Remediation and revalidation

A finding is not considered closed merely because a ticket is completed. Closure requires fresh evidence showing that the stated control objective is satisfied. The expected workflow is:

1. record the corrective action and owner;
2. implement the approved change;
3. collect new authorized observation/configuration evidence;
4. re-run the same assessment logic;
5. verify the original condition no longer triggers;
6. validate representative connectivity where the change can affect clients;
7. retain before/after evidence and the validation outcome.

Risk acceptance, if used in a real environment, should remain separate from technical closure and should have an accountable owner, rationale, approval, and review/expiry date.

## MITRE ATT&CK usage

ATT&CK mappings are included only where they improve defensive threat context. They do not imply that a technique was observed, exploited, reproduced, or attributed. Contextual mappings used by this project include:

- **T1557 — Adversary-in-the-Middle** for insecure wireless authentication/encryption and impersonation-related risk context.
- **T1498 — Network Denial of Service** as resilience context for management-frame protection and wireless availability controls.

## Safe-lab constraints

The project intentionally excludes credential capture, packet injection, deauthentication, cracking, exploitation, access-control bypass instructions, or production targeting. All included data is fictional/synthetic and designed for reproducible defensive analysis.
