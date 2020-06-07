from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

from pathlib import Path

# Entities seem to initialize upon import so:
from amb.src.entities import *

import os
import re

db_name = "amb.db"
path = Path(__file__).parent.absolute()

# Remember to turn echo off when stable
def initialize(db_path=path, db_name=db_name):
    """[Sets up local database for entities.]

    :param db_path: [Path where database should be inserted], defaults to Path.cwd()
    :type db_path: [Path], optional
    :param db_name: [Name of database to use. Defaults to amb], defaults to "amb.db"
    :type db_name: str, optional
    :return: [Returns base and engine]
    :rtype: [declarative_base, sqlalchemy engine]
    """
    # db_path = os.path.dirname(os.path.realpath(__file__))
    print(Path.cwd())
    base = declarative_base()
    db_path = str(db_path)
    db_path = db_path.replace("\\", "//")
    engine = create_engine(f"sqlite:///{db_path}/{db_name}")
    # engine = EngineSingletonContainer()
    # conn = engine.connect()
    create_db_if_non_existant(engine)
    base.metadata.create_all(bind=engine)
    # amb_engine = engine
    return base, engine


def create_db_if_non_existant(engine):
    """[Creates database if it doesn't exist. Checks for engine url. Database utilized is local]

    :param engine: [description]
    :type engine: [type]
    """
    if not database_exists(engine.url):
        try:
            print("db did not exist. Creating...")
            create_database(engine.url)
            print("DB created. Generating tables...")
            base.metadata.create_all(bind=engine)
            print("Tables successfully generated")
        except Exception as err:
            print(f"Could not create missing database: Error code: \n {err}")


base, amb_engine = initialize()

if __name__ == "__main__":
    Path(__file__).parent.absolute()
