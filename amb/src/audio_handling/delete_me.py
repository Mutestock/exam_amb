
import pygame
from amb.src.entities.track import Track
from amb.src.entities.configuration import Configuration
from pathlib import Path
from amb.definitions import AUDIO_DIR

if __name__ == "__main__":

    pygame.mixer.init()
    pygame.mixer.set_num_channels(10)
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
    level8.channel=1
    serenity.channel=2

    #track_path = Path(f"{AUDIO_DIR}\{track.genre}\{track.name}.{track.extension}")
    #if not Path.is_file(Path(track_path)):
    #    raise FileNotFoundError()
    #print(track_path)
    p1 = str(Path(f"{AUDIO_DIR}\{level8.genre}\{level8.name}.{level8.extension}"))
    if not Path.is_file(Path(p1)):
        raise FileNotFoundError()
    print(p1)
    ch = pygame.mixer.Channel(0).play(pygame.mixer.Sound(p1))
