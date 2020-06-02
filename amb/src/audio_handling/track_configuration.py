from tempfile import NamedTemporaryFile


def modified_track_wav(track):
    """[Modifies wav in accordance with track configuration]

    :param track: [Track object. Contains information like name, duration, genre]
    :type track: [<class 'track.Track'>]
    """
    _apply_fade(track)
    _apply_stereo_mono(track)


def _apply_fade(track):
    _fade_error_check(track)


def _apply_mono_mono_stereo(track):
    _stereo_mono_error_check(track)


def _fade_error_check(track):
    f_end = track.configuration.fade_end
    f_begin = track.configuration.fade_beginning

    if f_end > 100:
        raise ValueError("fade_end was higher than 100 in apply attenpt")
    elif f_end < 0:
        raise ValueError("fade_end was lower than 0 in apply attempt")
    elif f_begin > 100:
        raise ValueError("fade_beginning was higher than 100 in apply attenpt")
    elif f_begin < 0:
        raise ValueError("fade_beginning was lower than 0 in apply attempt")
    elif (f_begin - f_end) < 0:
        raise ValueError(
            "fade_beginning - f_end can not be lower than zero, as it would cover more than the entire track's duration"
        )


def _stereo_mono_error_check(track):
    mono_stereo = track.configuration.mono_stereo
    if mono_stereo == "mono":
        pass
    elif mono_stereo == "stereo":
        pass
    elif mono_stereo == "None":
        raise ValueError("mono_stereo was none on apply attempt")
    else:
        raise ValueError(
            f"mono_stereo illegal value: {track.configuration.mono_stereo}"
        )
