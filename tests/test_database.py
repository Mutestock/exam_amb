import unittest
from amb.src.connection.db_management import initialize, create_all
from amb.src.entities.track import Track
from amb.src.entities.configuration import Configuration
from amb.src.entities.random_interval import RandomInterval
from amb.src.entities.random_volume import RandomVolume
from amb.src.entities.playlist import Playlist
from amb.src.entities.user import User

from pathlib import Path
import os


def db_decorator(func):
    def wrapper(*args, **kwargs):
        check_path = Path.cwd()
        file_path = Path(f"{check_path}/temp_test_db.db")
        base, engine = initialize(db_path=check_path, db_name="temp_test_db.db")
        func(*args, **kwargs, engine=engine, base=base)
        Path.unlink(file_path)
        return

    return wrapper


class TestConnection(unittest.TestCase):

    check_path = Path.cwd()
    file_path = Path(f"{check_path}/temp_test_db.db")
    initialize(db_path=check_path, db_name="temp_test_db.db")

    def test_initialize(self):
        check_path = Path.cwd()
        file_path = Path(f"{check_path}/temp_test_db.db")
        initialize(db_path=check_path, db_name="temp_test_db.db")
        self.assertTrue(file_path.is_file())
        Path.unlink(file_path)

    @db_decorator
    def test_table_basic_creation(self, engine=None, base=None):
        create_all(engine)
        res = engine.execute("SELECT * FROM Track")
        self.assertIsNotNone(res)
