import unittest

# from amb.src.audio_handling.audio_basic import TrackRunner
from amb.src.entities.track import Track

# Deprecated
# Make audio downlaoder as a 'before all' in tests. Delete it at after an 'after all'
# class TestAudioController(unittest.TestCase):
# def test_track_runner_processing_eof(self):
#    t = TrackRunner(
#        [
#            Track(
#                "wind",
#                "forest",
#                12,
#                {
#                    "mono_stereo": "Mono",
#                    "interval": "Random 23 - 40",
#                    "volume": "100%",
#                },
#            ),
#            Track(
#                "river",
#                "forest",
#                9,
#                {"mono_stereo": "Stereo", "interval": "Loop", "volume": "14-50%"},
#            ),
#        ]
#    )
# t.play_all()
# t.stop_all()

# def test_play_all_alt(self):
#    t = TrackRunner(
#        [
#            Track(
#                "wind",
#                "forest",
#                12,
#                {
#                    "mono_stereo": "Mono",
#                    "interval": "Random 23 - 40",
#                    "volume": "100%",
#                },
#            ),
#            Track(
#                "river",
#                "forest",
#                9,
#                {"mono_stereo": "Stereo", "interval": "Loop", "volume": "14-50%"},
#            ),
#        ]
#    )
#    t.play_all_alt()
