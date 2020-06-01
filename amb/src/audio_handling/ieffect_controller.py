from zope.interface import Interface, Attribute


class IAudioController(Interface):
    """[Interface for audio controller]

    :param Interface: [Zope Interface]
    :type Interface: [zope.interface.interface.InterfaceClass]
    """

    example = Attribute("This is a placeholder")

    def control_stereo_mono():
        """[Controller for stereo and mono]
        """

    def control_volume():
        """[Controller for volume, herein random, single]
        """

    def control_interval():
        """[Controller for interval, herein random, loop, single]
        """
