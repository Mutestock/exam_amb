import pygame

# Be aware that the mixer quits here


def get_audio_length(path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    duration = sound.get_length()
    pygame.mixer.quit()
    return duration
