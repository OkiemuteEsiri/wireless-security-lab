import unittest

from src.wireless_security.engine import assess_devices, posture_score
from src.wireless_security.models import AccessPoint


def ap(**overrides):
    values = dict(ssid="Corp-Secure", bssid="02:00:00:00:00:01", security="WPA3-ENT", wps_enabled=False, pmf_required=True, management_vlan="mgmt-10", guest_isolation=True, admin_interface_exposed=False, owner="Network Security", firmware_age_days=60)
    values.update(overrides)
    return AccessPoint(**values)


class WirelessAssessmentTests(unittest.TestCase):
    def test_secure_baseline_has_no_findings(self):
        self.assertEqual([], assess_devices([ap()]))

    def test_legacy_security_is_critical(self):
        findings = assess_devices([ap(security="WEP")])
        self.assertTrue(any(f.severity == "critical" for f in findings))

    def test_wps_is_high(self):
        findings = assess_devices([ap(wps_enabled=True)])
        self.assertTrue(any("Protected Setup" in f.title and f.severity == "high" for f in findings))

    def test_guest_isolation_control(self):
        findings = assess_devices([ap(ssid="Guest-WiFi", guest_isolation=False)])
        self.assertTrue(any("client isolation" in f.title for f in findings))

    def test_duplicate_bssid_rejected(self):
        with self.assertRaises(ValueError):
            assess_devices([ap(), ap()])

    def test_invalid_security_rejected(self):
        with self.assertRaises(ValueError):
            ap(security="UNKNOWN")

    def test_negative_firmware_age_rejected(self):
        with self.assertRaises(ValueError):
            ap(firmware_age_days=-1)

    def test_score_is_bounded(self):
        findings = assess_devices([ap(security="WEP", wps_enabled=True, pmf_required=False, admin_interface_exposed=True, owner="", firmware_age_days=900)])
        self.assertGreaterEqual(posture_score(findings), 0)
        self.assertLessEqual(posture_score(findings), 100)


if __name__ == "__main__":
    unittest.main()
