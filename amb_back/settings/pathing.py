import os
import getpass
import configparser
import sys


def setup_track_path():
    """
    Track audio is played via. path stored in DB rather than media file itself.
    This function determines the path dynamically based on operative system and current host
    Can be turned off in configuration.ini
    """
    pseudo_switch = {
        "win32": __win_pathing,
        "darwin": __mac_pathing,
        "linux": __linux_pathing,
        'aix' : raise NotImplementedError("aix os is not supported"),
        "cygwin": raise NotImplementedError("cygwin os is not supported")
    }
    pseudo_switch.get(sys.platform)()


def __win_pathing():
    """
    Automatically sets track path for Win OS. Can be turned off in configuration.ini
    """
    conf = configparser.ConfigParser()
    conf.read("./settings/configuration.ini")
    with open("./settings/configuration.ini", "w") as conf:
        global_configuration.write(conf)
    return f"C://Users/{getpass.getuser()}/Documents/amb_tracks"


def __mac_pathing():
    """
    Automatically sets track path for Mac OS. Can be turned off in configuration.ini
    """
    raise NotImplementedError


def __linux_pathing():
    """
    Automatically sets track path for Linux. Can be turned off in configuration.ini
    Destributions not taken into consideration. Default is Ubuntu. 
    If you're not using Ubuntu, then you'll have to turn 'LinuxAutomaticTrackPathing' to false in configuration.ini
    """
    raise NotImplementedError
