# Remediation and Validation Playbook

## Unauthorized BSSID / SSID impersonation indicator
**Impact:** potential unauthorized infrastructure, policy bypass, or adversary-in-the-middle exposure.

**Remediation:** validate device ownership; trace switch/controller registration where applicable; isolate or remove unapproved hardware; update inventory only after formal approval.

**Validation evidence:** controller inventory, physical validation, approved change record, and a follow-up observation showing that only approved BSSIDs advertise the corporate SSID.

## Encryption downgrade
**Impact:** reduced confidentiality/integrity guarantees and possible policy non-compliance.

**Remediation:** restore the approved WPA2-Enterprise/WPA3 configuration and remove legacy security profiles.

**Validation evidence:** configuration export plus subsequent observation matching the baseline.

## PMF drift
**Impact:** reduced protection for management frames.

**Remediation:** enable PMF according to device/client compatibility policy.

**Validation evidence:** controller configuration and a follow-up observation showing PMF enabled.

## Closure criteria
A finding is closed only when the original control check passes, ownership/evidence is documented, and no unapproved exception remains. Exceptions should have an owner, business rationale, compensating controls, and expiry date.
