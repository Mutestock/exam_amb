from amb.src.audio_handling.ieffect_controller import IEffectController
import zope
import pygame
import random
from amb.definitions import AUDIO_DIR
import time
from amb.src.entities.configuration import Configuration


@zope.interface.implementer(IEffectController)
class EffectController:
    def __init__(self, track_list):
        self.__track_list = track_list
        self.__channels = len(track_list) * 2
        pygame.mixer.init(channels=self.__channels)

    def play_all(self):
        for track in self.__track_list:
            self.load_track(track)
            interval = self.control_interval(track)
            fade_in = self.control_fade(track)
            volume = self.control_volume(track)
            duration = track.duration
        (
            lambda _interval, _fade_in, _volume, _duration: play_single(
                _interval, _fade_in, _volume, duration
            )
        )(interval, fade_in, volume, duration)

    def play_single(self, interval, fade_in, volume, duration):
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
            pygame.mixer.music.play(loops=interval)

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
        track_path = f"{AUDIO_DIR}/{track.genre}/{track.name}.{track.extension}"
        pygame.mixer.music.load(track_path)


if __name__ == "__main__":
    level8 = Track(
        name="Level8",
        genre="forest",
        duration=12,
        extension="ogg",
        configuration=Configuration(random_interval=[2, 13], random_volume=[55, 75]),
    )
    track_list = [level8]
    ec = EffectController(track_list)
    ec.play_all()
