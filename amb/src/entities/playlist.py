from amb.src.connection.db_management import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Playlist(base):
    def __init__(self, track_list, name):
        self.__track_list = track_list
        self.__name = name

    __tablename__ = "playlist"
    id = Column("id", Integer, primary_key=True)
    db_name = Column("name", String, unique=True)
    db_track = relationship("Track")
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
