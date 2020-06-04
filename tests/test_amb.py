from amb import __version__
import unittest

# Rename
class TestAmbience(unittest.TestCase):
    def test_version(self):
        self.assertEquals(__version__, "0.2.0")
