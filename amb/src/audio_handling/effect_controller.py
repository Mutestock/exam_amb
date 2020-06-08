from amb.src.audio_handling.ieffect_controller import IEffectController
from amb.src.entities.track import Track
import zope
import pygame
import random
from amb.definitions import AUDIO_DIR
import time
from amb.src.entities.configuration import Configuration
from pathlib import Path
from time import sleep
import threading

# from amb.src.entities.configuration import Configuration
from amb.src.facades.track_facade import *

# Needs updates after database setup


@zope.interface.implementer(IEffectController)
class EffectController:
    def __init__(self, track_list):
        self.__track_list = track_list
        self.__channels = len(track_list) * 2
        pygame.mixer.init(channels=self.__channels)
        pygame.mixer.set_num_channels(self.__channels)

    def play_all(self):
        """[Plays all tracks from the list of tracks defined when instantiating the EffectController]
        """
        for track in self.__track_list:
            (lambda t: self.play_single(t))(track)

    def play_single(self, track):
        """[Plays the track in question. This the functionality used by the 'play_all' function. Checks for fades, intervals, loops, etc.]

        :param interval: [Integer]
        :type interval: [type]
        :param fade_in: [description]
        :type fade_in: [type]
        :param volume: [description]
        :type volume: [type]
        :param duration: [description]
        :type duration: [type]
        """

        if pygame.mixer.Channel(track.channel).get_busy():
            pygame.mixer.Channel(track.channel).stop()
            return

        c = read(Configuration, Configuration.db_track_id, track.id)

        interval = self.control_interval(c)
        fade_in = self.control_fade(c)
        volume = self.control_volume(c)
        duration = track.db_duration

        pygame.mixer.Channel(track.channel).set_volume(volume)

        repeatable = interval
        fade_in_modified = fade_in

        p = str(
            Path(f"{AUDIO_DIR}\{track.db_genre}\{track.db_name}.{track.db_extension}")
        )
        s = pygame.mixer.Sound(p)

        if fade_in != 0:
            fade_modified = (fade_in / 100) * duration
        if interval == "random":
            self.recursive_play(track, c, s)
        elif interval == "single":
            pygame.mixer.Channel(track.channel).play(s)
        else:
            # s.play()
            pygame.mixer.Channel(track.channel).play(s, loops=-1)

    # Needs extended database..
    def recursive_play(self, track, c, sound, first=False):
        r_interval = random.randint(c.db_random_interval_min, c.db_random_interval_max)
        # timer = None
        timer = None

        def r_play():
            global timer
            r_interval = random.randint(
                c.db_random_interval_min, c.db_random_interval_max
            )
            timer = threading.Timer(track.db_duration + r_interval, r_play)
            pygame.mixer.Channel(track.channel).play(sound)
            timer.start()

        timer = threading.Timer(r_interval, r_play)
        timer.start()

    def control_mono_stereo(self,):
        raise NotImplementedError

    def control_volume(self, c):
        volume = "0"
        try:
            if c.db_vol_random == True:
                volume = (
                    random.randint(c.db_random_interval_min, c.db_random_interval_max)
                    / 100
                )
            else:
                volume = float(c.db_volume) / 100
        except Exception as err:
            print(f"Failed to convert volume to float. Was {volume} Err: \n {err}")
        if volume > 1:
            raise ValueError(f"Volume can't be higher than 1. Was: {volume}")
        elif volume < 0:
            raise ValueError(f"Volume can't be lower than 0. Was {volume}")
        else:
            return volume

    def control_interval(self, c):
        interval = c.db_interval
        if interval == "loop":
            return "loop"
        elif interval == "single":
            return "single"
        elif interval == "random":
            return "random"
        else:
            raise ValueError(f"Illegal interval in control_interval: {interval}")

    def unload_all(self,):
        pygame.mixer.music.unload()

    def control_fade(self, c):
        fade_in = "0"
        try:
            fade_in = float(c.db_fade_beginning)
        except Exception as err:
            print(f"Failed to convert fade_in to float. Was {fade_in}")
        if fade_in > 100:
            raise ValueError(
                f"Fade in value must be lower than 100, but was was {fade_in}"
            )
        elif fade_in < 0:
            raise ValueError(f"Fade in value can't be negative. Was: {fade_in}")
        else:
            return fade_in

    def load_track(self, track):
        print("loading...")
        track_path = Path(
            f"{AUDIO_DIR}\{track.db_genre}\{track.db_name}.{track.db_extension}"
        )

        if not Path.is_file(Path(track_path)):
            print(f"failed track path: {track_path}")
            raise FileNotFoundError()
        pygame.mixer.music.load(str(track_path))
        # clock = pygame.time.Clock()
        # clock.tick(10)


if __name__ == "__main__":
    """
    For manual testing.
    Please note that without the sleep, then the program will exit and all sounds will end

    """
    level8 = Track(
        name="Level8",
        genre="forest",
        duration=12,
        extension="ogg",
        configuration=Configuration(
            interval="loop", random_interval=[2, 13], random_volume=[55, 75]
        ),
    )
    serenity = Track(
        name="KR-Serenity",
        genre="forest",
        duration=12,
        extension="ogg",
        configuration=Configuration(
            interval="loop", random_interval=[2, 13], random_volume=[55, 75]
        ),
    )
    level8.channel = 2
    serenity.channel = 4

    track_list = [level8, serenity]
    ec = EffectController(track_list)
    ec.play_all()
    time.sleep(500)
