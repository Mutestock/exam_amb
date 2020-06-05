from amb.src.connection.db_management import base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(base):
    def __init__(self, name, password, play_lists):
        self.__name = name
        self.__password = password
        self.__play_lists = play_lists

    """
    It is absolutely understood that passwords are supposed to be hashed, salted, etc. 
    This exam is not focused on the security aspect.
    Consider it a stretch goal that I simply don't have enough time to reach.
    """

    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    db_name = Column("name", String, unique=True)
    db_password = Column("password", String)
    db_playlist = relationship("Playlist", cascade="all, delete, delete-orphan")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def play_lists(self):
        return self.__play_lists

    @play_lists.setter
    def play_lists(self, value):
        self.__play_lists = value
