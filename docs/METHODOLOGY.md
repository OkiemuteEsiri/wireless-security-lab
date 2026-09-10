# Assessment Methodology

## Scope

The assessment is designed for owned or explicitly authorized wireless infrastructure using inventory/configuration data. It evaluates configuration posture rather than attempting to prove exploitability.

## Control sequence

1. Validate inventory completeness and uniqueness.
2. Identify obsolete or weak authentication/encryption modes.
3. Check WPS exposure and management-frame protection.
4. Review guest segmentation and client isolation.
5. Review management-plane network placement.
6. Check ownership and firmware lifecycle hygiene.
7. Prioritize findings by severity and remediation dependency.
8. Re-run the same assessment after change implementation and retain before/after reports.

## Severity model

- **Critical** — configuration creates direct systemic exposure, such as obsolete wireless encryption.
- **High** — material control weakness with practical abuse potential or broad administrative impact.
- **Medium** — defense-in-depth, lifecycle, or authentication design weakness requiring planned remediation.
- **Low** — governance or inventory weakness with limited immediate exploitability.

## Validation workflow

A finding is not considered closed merely because a change ticket is completed. Closure requires the stated validation condition to be observed in fresh inventory/configuration data. Where a change can affect client compatibility, validation should include representative connectivity testing in an authorized test window.

## MITRE ATT&CK usage

ATT&CK mappings are included only where they improve defensive threat context. They do not imply that a technique was observed, exploited, or reproduced. Example contextual mappings include adversary-in-the-middle activity and network denial-of-service considerations around wireless management protections.
