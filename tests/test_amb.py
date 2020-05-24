from amb import __version__
import unittest


class Tests(unittest.TestCase):
    def test_version(self):
        self.assertEquals(__version__, "0.1.0")
