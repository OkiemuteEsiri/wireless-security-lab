# Wireless Control Validation Matrix

This matrix connects each major wireless control family to impact, acceptable remediation evidence, revalidation conditions, and defensive threat context.

| Control family | Example risk condition | Security impact | Minimum remediation evidence | Revalidation condition | ATT&CK / threat context |
|---|---|---|---|---|---|
| Authorized infrastructure | Observed BSSID absent from approved inventory | Unauthorized or unmanaged wireless presence | Ownership investigation, approved inventory correction or removal record | Fresh observation/configuration data shows only approved infrastructure for the assessed scope | T1557 context where impersonation or interception risk is relevant |
| Corporate SSID integrity | Known corporate SSID advertised by unknown BSSID | User trust could be redirected to unapproved infrastructure | Investigation outcome plus removal/containment or approved ownership evidence | Fresh observation confirms no unknown BSSID advertises the protected SSID | T1557 — Adversary-in-the-Middle context |
| Authentication / encryption | Open, legacy, or weaker-than-baseline mode | Confidentiality and authentication weakness | Approved configuration change showing required security mode | Fresh configuration inventory confirms baseline-compliant authentication/encryption | T1557 context |
| WPS | WPS enabled where prohibited | Increased attack surface and policy non-compliance | Configuration change disabling WPS | Fresh authorized configuration confirms WPS disabled | Defensive hardening context |
| Protected management frames | PMF optional/disabled where required | Reduced management-frame resilience | Configuration change requiring PMF where supported and approved | Fresh configuration plus representative client validation shows PMF policy is active | T1498 availability/resilience context |
| Guest segmentation | Guest WLAN lacks client isolation or required segmentation | Lateral exposure between untrusted clients or networks | Segmentation/client-isolation configuration and approved change evidence | Fresh configuration and authorized validation confirm isolation policy | Network-segmentation threat context |
| Management plane | Administrative interface reachable from user WLAN context | Administrative control surface exposed to lower-trust network | Management-plane relocation or access-control change | Fresh authorized configuration confirms management access is restricted to approved administrative paths | Privilege-boundary context |
| Firmware lifecycle | AP firmware exceeds defined lifecycle baseline | Known-vulnerability and supportability exposure | Upgrade record and resulting supported firmware version | Fresh inventory reports approved supported firmware | Vulnerability-management context |
| Ownership | AP has no accountable owner | Remediation and governance ambiguity | Named accountable owner in authoritative inventory | Fresh inventory contains valid ownership metadata | Governance control |
| Location/config drift | Approved AP differs from expected location or baseline | Potential unauthorized change, inventory error, or weakened control | Change record, physical validation, or corrected configuration | Fresh observation and inventory agree with approved state | Detection / change-governance context |

## Evidence quality levels

1. **Administrative evidence only** — ticket/comment states that work was completed. This is insufficient for technical closure.
2. **Configuration evidence** — approved configuration or inventory shows the intended change.
3. **Independent revalidation** — fresh evidence processed through the same assessment confirms the original condition is no longer present.
4. **Sustained validation** — repeated observations over an appropriate period show the control remains effective and drift has not recurred.

## Closure principle

Technical findings should close only when the security condition has been independently revalidated. Ticket closure, change approval, or risk acceptance alone does not demonstrate that the exposure is removed.

Where a real organization accepts residual risk, that exception should be governed separately with an accountable owner, rationale, approval, scope, and review/expiry date. An exception changes governance status; it does not change the underlying technical fact.

## ATT&CK interpretation

ATT&CK references in this repository explain how a control may relate to adversary behavior. They do not establish that exploitation, compromise, attribution, or a specific adversary technique actually occurred.
