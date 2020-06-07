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

# Needs updates after database setup

@zope.interface.implementer(IEffectController)
class EffectController:
    def __init__(self, track_list):
        self.__track_list = track_list
        self.__channels = len(track_list) * 2
        print(f"Channels: {self.__channels}")
        pygame.mixer.init(channels=self.__channels)
        pygame.mixer.set_num_channels(10)

    def play_all(self):
        """[Plays all tracks from the list of tracks defined when instantiating the EffectController]
        """
        for track in self.__track_list:
            self.load_track(track)
            (lambda t: self._play_single(t))(track)

    def _play_single(self, track):
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
        interval = self.control_interval(track)
        interval = self.control_interval(track)
        fade_in = self.control_fade(track)
        volume = self.control_volume(track)
        duration = track.duration

        repeatable = interval
        fade_in_modified = fade_in
        if fade_in != 0:
            fade_modified = (fade_in / 100) * duration
        if interval != -1 or interval != 1 and type(interval) == list:
            first = True
            while True:
                r0 = interval[0]
                r1 = interval[1]
                r_interval = random.randint(r0, r1)
                concat = r_interval
                if first == False:
                    concat = concat + pygame.music.get_length()
                time.sleep(concat)
                pygame.music.play(fade_ms=fade_modified)
        elif interval == 1:
            pygame.mixer.music.play(fade_ms=fade_modified)
        else:
            print("playing loops")
            #pygame.mixer.music.play(loops=interval)
            p = str(Path(f"{AUDIO_DIR}\{track.genre}\{track.name}.{track.extension}"))
            s = pygame.mixer.Sound(p)
            s.play()
            print(track.channel)
            pygame.mixer.Channel(track.channel).play(s, loops=interval)
    def control_mono_stereo(self,):
        raise NotImplementedError

    def _stereo(self,):
        raise NotImplementedError

    def _mono(self,):
        raise NotImplementedError

    def control_volume(self, track):
        volume = "0"
        try:
            volume = float(track.configuration.volume) / 100
        except Exception as err:
            print(f"Failed to convert volume to float. Was {volume} Err: \n {err}")
        if volume > 1:
            raise ValueError(f"Volume can't be higher than 1. Was: {volume}")
        elif volume < 0:
            raise ValueError(f"Volume can't be lower than 0. Was {volume}")
        else:
            return volume

    def _volume_random(self,):
        raise NotImplementedError

    def _volume_single(self,):
        raise NotImplementedError

    def _volume_mute(self,):
        raise NotImplementedError

    def control_interval(self, track):
        interval = track.configuration.interval
        if interval == "loop":
            return -1
        elif interval == "single":
            return 1
        elif interval == "random":
            return track.configuration.random_interval
        else:
            raise ValueError(
                f"Illegal interval in control_interval: {track.configuration.interval}"
            )

    def _interval_random(self,):
        raise NotImplementedError

    def _interval_loop(self,):
        raise NotImplementedError

    def _interval_single(self,):
        raise NotImplementedError

    def unload_all(self,):
        pygame.mixer.music.unload()

    def control_fade(self, track):
        fade_in = "0"
        try:
            fade_in = float(track.configuration.fade_beginning)
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
        track_path = Path(f"{AUDIO_DIR}\{track.genre}\{track.name}.{track.extension}")
        
        if not Path.is_file(Path(track_path)):
            print(f"failed track path: {track_path}")
            raise FileNotFoundError()
        print(track_path)
        pygame.mixer.music.load(str(track_path))
        #clock = pygame.time.Clock()
        #clock.tick(10)
        


if __name__ == "__main__":
    '''
    For manual testing.
    Please note that without the sleep, then the program will exit and all sounds will end

    '''
    level8 = Track(
        name="Level8",
        genre="forest",
        duration=12,
        extension="ogg",
        configuration=Configuration(interval="loop", random_interval=[2, 13], random_volume=[55, 75]),
    )
    serenity = Track(
        name="KR-Serenity",
        genre="forest",
        duration=12,
        extension="ogg",
        configuration=Configuration(interval="loop", random_interval=[2, 13], random_volume=[55, 75]),
    )
    level8.channel=2
    serenity.channel=4

    track_list = [level8, serenity]
    ec = EffectController(track_list)
    ec.play_all()
    time.sleep(500)
