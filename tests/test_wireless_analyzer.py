import unittest
from src.wireless_analyzer import analyze, summarize


class WirelessAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.authorized = [{"ssid":"Corp-Secure","bssid":"aa:bb:cc:00:00:01","encryption":"WPA3-ENTERPRISE","pmf_required":True,"location":"HQ-1F"}]

    def test_clean_baseline_has_no_findings(self):
        obs = [{"ssid":"Corp-Secure","bssid":"aa:bb:cc:00:00:01","encryption":"WPA3-ENTERPRISE","pmf":True,"location":"HQ-1F"}]
        self.assertEqual(analyze(self.authorized, obs), [])

    def test_unknown_bssid_on_corporate_ssid_is_critical(self):
        obs = [{"ssid":"Corp-Secure","bssid":"de:ad:be:ef:00:01","encryption":"WPA2","pmf":False,"location":"HQ-Lobby"}]
        findings = analyze(self.authorized, obs)
        self.assertTrue(any(f.control_id == "WIFI-002" and f.severity == "critical" for f in findings))

    def test_legacy_encryption_is_critical(self):
        obs = [{"ssid":"Other","bssid":"00:11:22:33:44:55","encryption":"WEP","pmf":False,"location":"Lab"}]
        findings = analyze(self.authorized, obs)
        self.assertTrue(any(f.control_id == "WIFI-003" for f in findings))

    def test_summary_counts_by_severity(self):
        obs = [{"ssid":"Corp-Secure","bssid":"de:ad:be:ef:00:01","encryption":"WEP","pmf":False,"location":"HQ-Lobby"}]
        summary = summarize(analyze(self.authorized, obs))
        self.assertGreaterEqual(summary["critical"], 2)


if __name__ == "__main__":
    unittest.main()
