# from amb.src.connection.db_management import base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from amb.src.connection.engine_creation import main_base as base, main_engine


# Many to many?

association_table = Table(
    "association",
    base.metadata,
    Column("playlist_id", Integer, ForeignKey("playlist.id")),
    Column("track_id", Integer, ForeignKey("track.id")),
)


class Playlist(base):
    def __init__(self, track_list, name):
        self.__track_list = track_list
        self.__name = name

    __tablename__ = "playlist"
    id = Column("id", Integer, primary_key=True)
    db_name = Column("name", String, unique=True)
    db_track = relationship("Track", secondary=association_table)
    user_id = Column(Integer, ForeignKey("user.id"))

    @property
    def track_list(self):
        return self.__track_list

    @track_list.setter
    def track_list(self, value):
        self.__track_list = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


base.metadata.create_all(bind=main_engine)
