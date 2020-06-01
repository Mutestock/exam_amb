from ieffect_controller import IEffectController
import zope


@zope.interface.implementer(IEffectController)
class AudioController:
    def __init__(self):
        pass

    def control_mono_stereo():
        raise NotImplementedError

    def _stereo():
        raise NotImplementedError

    def _mono():
        raise NotImplementedError

    def control_volume():
        raise NotImplementedError

    def _volume_random():
        raise NotImplementedError

    def _volume_single():
        raise NotImplementedError

    def _volume_mute():
        raise NotImplementedError

    def control_interval():
        raise NotImplementedError

    def _interval_random():
        raise NotImplementedError

    def _interval_loop():
        raise NotImplementedError

    def _interval_single():
        raise NotImplementedError
