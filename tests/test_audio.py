import unittest

# Make audio downlaoder as a 'before all' in tests. Delete it at after an 'after all'
class TestAudioController(unittest.TestCase):
    def test_extract_from_numpy():
        from amb.src.audio_handling import _extract_from_numpy
