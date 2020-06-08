from amb.src.connection.engine_creation import main_base as base, main_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Configuration(base):
    def __init__(
        self,
        mono_stereo="stereo",
        interval="loop",
        volume=100,
        vol_random=False,
        fade_beginning=0,
        fade_end=0,
        random_interval_min=0,
        random_interval_max=10,
        random_volume_min=0,
        random_volume_max=100,
    ):
        self.__mono_stereo = mono_stereo
        self.__interval = interval
        self.__volume = volume
        self.__vol_random = vol_random
        self.__fade_beginning = fade_beginning
        self.__fade_end = fade_end
        self.__random_interval_max = random_interval_max
        self.__random_interval_min = random_interval_min
        self.__random_volume_max = random_volume_max
        self.__random_volume_min = random_volume_min

    __tablename__ = "configuration"
    id = Column("id", Integer, primary_key=True)
    db_mono_stereo = Column("mono_stereo", String)
    db_interval = Column("interval", String)
    db_volume = Column("volume", Integer)
    db_vol_random = Column("vol_random", Boolean)
    db_fade_beginning = Column("fade_beginning", Integer)
    db_fade_end = Column("fade_end", Integer)
    db_random_interval_max = Column("random_interval_max", Integer)
    db_random_interval_min = Column("random_interval_min", Integer)
    db_random_volume_max = Column("random_volume_max", Integer)
    db_random_volume_min = Column("random_volume_min", Integer)
    db_track_id = Column(Integer, ForeignKey("track.id"))

    def associate_database_variables(self):
        self.db_mono_stereo = self.__mono_stereo
        self.db_interval = self.__interval
        self.db_volume = self.__volume
        self.db_vol_random = self.__vol_random
        self.db_fade_beginning = self.__fade_beginning
        self.db_fade_end = self.__fade_end
        self.db_random_interval_max = self.__random_interval_max
        self.db_random_interval_min = self.__random_interval_min
        self.db_random_volume_max = self.__random_volume_max
        self.db_random_volume_min = self.__random_volume_min

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


base.metadata.create_all(bind=main_engine)
