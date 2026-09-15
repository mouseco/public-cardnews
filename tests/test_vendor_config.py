from pathlib import Path
import unittest

class VendorConfigTests(unittest.TestCase):
    def test_restricted_sandbox_and_explicit_binary(self):
        s = (Path(__file__).resolve().parents[1] / 'vendor/baoyu-codex-imagegen/src/spawn.ts').read_text()
        self.assertIn('"workspace-write"', s)
        self.assertIn('process.env.CODEX_BIN || "codex"', s)

if __name__ == '__main__':
    unittest.main()
