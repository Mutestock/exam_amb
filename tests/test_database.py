import unittest
from amb.src.connection.db_management import initialize
from amb.src.entities.track import Track
from amb.src.entities.configuration import Configuration
from amb.src.entities.random_interval import RandomInterval
from amb.src.entities.random_volume import RandomVolume
from amb.src.entities.playlist import Playlist
from amb.src.entities.user import User
from amb.src.facades.track_facade import *
from pathlib import Path
import os


def db_decorator(func):
    """[Simple decorator which acts as a before each / after each database creation and dropping]

    :param func: [function to wrap around]
    :type func: [Function]
    """

    def wrapper(*args, **kwargs):
        check_path = Path.cwd()
        file_path = Path(f"{check_path}/temp_test_db.db")
        base, engine = initialize(db_path=check_path, db_name="temp_test_db.db")
        func(*args, **kwargs, engine=engine, base=base)
        #Path.unlink(file_path)
        return

    return wrapper


class TestConnection(unittest.TestCase):


    def test_initialize(self):
        check_path = Path.cwd()
        file_path = Path(f"{check_path}/temp_test_db.db")
        initialize(db_path=check_path, db_name="temp_test_db.db")
        self.assertTrue(file_path.is_file())
        Path.unlink(file_path)

    @db_decorator
    def test_table_basic_creation(self, engine=None, base=None):
        base.metadata.create_all(bind=engine)
        # create_all(engine)
        res = engine.execute("SELECT * FROM Track")
        self.assertIsNotNone(res)

    #### Entity relation tests ####

    @db_decorator
    def test_track_basic_creation(self, engine=None, base=None):

        c = Configuration(
            mono_stereo="stereo",
            interval=14,
            volume=100,
            fade_beginning=0,
            fade_end=0, 
        )
        create(c, engine=engine)
        t = Track(
            name="John Kirk",
            genre="Forest",
            duration=12,
            extension=19,
            configuration=c,
        )
        t.db_name = t.name
        t.db_genre = t.genre
        t.db_extension = t.extension
        print(f"Engine: {engine}")
        
        create(t, engine=engine)
        #t_read = read(1, engine=engine)
        all = read_all(Track, engine=engine)
        print(all)


    #@db_decorator
    #def test_configuration_basic_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_track_configuration_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_configuration_random_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_playlist_track_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_playlist_track_configuration_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_track_create(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_track_create(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_user_playlist_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_user_playlist_track_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_user_playlist_track_configuration_creation(self, engine=None, base=None):
    #    pass
#
    #@db_decorator
    #def test_full_creation(self, engine=None, base=None):
    #    pass
#
    #####
#