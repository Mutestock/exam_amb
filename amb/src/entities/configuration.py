from amb.src.connection.db_management import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Configuration(base):
    def __init__(
        self,
        mono_stereo="stereo",
        interval=0,
        volume=100,
        fade_beginning=0,
        fade_end=0,
        random_interval=[],
        random_volume=[],
    ):
        self.__mono_stereo = mono_stereo
        self.__interval = interval
        self.__volume = volume
        self.__fade_beginning = fade_beginning
        self.__fade_end = fade_end
        self.__random_interval = random_interval
        self.__random_volume = random_volume
        self.__switch = "off"

    __tablename__ = "configuration"
    id = Column("id", Integer, primary_key=True)
    db_mono_stereo = Column("mono_stereo", String)
    db_interval = Column("interval", Integer)
    db_volume = Column("volume", Integer)
    db_fade_beginning = Column("fade_beginning", Integer)
    db_fade_end = Column("fade_end", Integer)
    db_track_id = Column(Integer, ForeignKey("track.id"))
    #db_random_interval = relationship(
    #    "RandomInterval", uselist=False, backref="configuration"
    #)
    #db_random_volume = relationship(
    #    "RandomVolume", uselist=False, backref="configuration"
    #)

    # random_interval=Column(Integer)
    # random_volume=Column(Integer)

    @property
    def mono_stereo(self):
        return self.__mono_stereo

    @mono_stereo.setter
    def mono_stereo(self, value):
        self.__mono_stereo = value

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        self.__interval = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def fade_beginning(self):
        return self.__fade_beginning

    @fade_beginning.setter
    def fade_beginning(self, value):
        self.__fade_beginning = value

    @property
    def fade_end(self):
        return self.__fade_end

    @fade_end.setter
    def fade_end(self, value):
        self.__fade_end = value

    # Too many/few arguments exception
    @property
    def random_volume(self):
        return self.__random_volume

    @random_volume.setter
    def random_volume(self, value):
        if len(value) == 2:
            self.__random_volume = value
        else:
            raise ValueError(
                f"random_volume setter takes a list containing exactly 2 elements{len(value)}"
            )

    # Too many/few arguments exception
    @property
    def random_interval(self):
        return self.__random_interval

    @random_interval.setter
    def random_interval(self, value):
        if len(value) == 1:
            self.__random_interval = value
        else:
            raise ValueError(
                f"random_interval setter takes a list containing exactly 2 elements{len(value)}"
            )
