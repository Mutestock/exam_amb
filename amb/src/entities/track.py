from amb.definitions import AUDIO_DIR
from amb.src.connection.engine_creation import main_base as base, main_engine
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship

# from amb.src.entities import configuration


class Track(base):
    def __init__(self, name, genre, duration, configuration, extension="wav"):
        self.__name = name
        self.__genre = genre
        self.__duration = duration
        self.__extension = extension
        self.__configuration = configuration
        self.__path = f"{AUDIO_DIR}/{self.__genre}/{self.__name}.{self.__extension}"

    __tablename__ = "track"
    id = Column("id", Integer, primary_key=True)
    db_name = Column("name", String, unique=True)
    db_genre = Column("genre", String)
    db_duration = Column("duration", Integer)
    db_extension = Column("extension", String)
    db_configuration = relationship(
        "Configuration",
        uselist=False,
        backref="track",
        cascade="all, delete, delete-orphan",
    )

    # To do: Tags

    def associate_database_variables(self):
        self.db_name = self.__name
        self.db_genre = self.__genre
        self.db_duration = self.__duration
        self.db_extension = self.__extension
        self.db_configuration = self.__configuration

    @staticmethod
    def get_property_count():
        """[Returns amount of object properties]

        :return: [Amount of variabes]
        :rtype: [int]
        """
        return 5

    @staticmethod
    def get_track_attribute_name_by_index(index):
        return ["mono_stereo", "Interval", "Volume"][index - 1]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        self.__configuration = value

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        self.__extension = value

    @property
    def path(self):
        return self.__path


base.metadata.create_all(bind=main_engine)
