# Assessment Methodology

## Scope
This lab is designed for owned or explicitly authorized environments. Input data is synthetic and represents passive wireless observations only.

## Workflow
1. Establish the authorized AP inventory and expected security profile.
2. Normalize SSID, BSSID, encryption, PMF, channel, and location metadata.
3. Compare observations against approved state.
4. Classify deviations by security impact and confidence.
5. Investigate ownership/change records before declaring malicious activity.
6. Record remediation ownership and target date.
7. Re-run the same checks after remediation and preserve evidence.

## Risk model
- **Critical:** known corporate SSID on unknown infrastructure; legacy/open encryption.
- **High:** unauthorized infrastructure or encryption downgrade.
- **Medium:** PMF or expected-location drift.
- **Low:** informational hygiene issues only.

## Evidence quality
A single observation is not sufficient to prove malicious activity. Corroborate with controller inventory, switch-port data, physical inspection, NAC records, and approved change records where available.

## Safe-lab constraints
The project intentionally excludes credential capture, packet injection, deauthentication, cracking, exploitation, or guidance for bypassing access controls.
