from amb.src.connection.engine_creation import main_base as base, main_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class RandomVolume(base):
    def __init__(self, random_min, random_max):
        self.__random_min = random_min
        self.__random_max = random_max

    __tablename__ = "random_volume"
    id = Column(Integer, primary_key=True)
    db_random_min = Column("random_min", Integer)
    db_random_max = Column("random_max", Integer)
    db_configuration_id = Column(Integer, ForeignKey("configuration.id"))

    @property
    def random_min(self):
        return self.__random_min

    @random_min.setter
    def random_min(self, value):
        self.__random_min = value

    @property
    def random_max(self):
        return self.__random_max

    @random_max.setter
    def random_max(self, value):
        self.__random_max = value


base.metadata.create_all(bind=main_engine)
