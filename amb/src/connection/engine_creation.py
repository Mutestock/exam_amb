from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path


db_name = "amb.db"
path = Path(__file__).parent.absolute()


def amb_engine_creation(db_path=path, db_name="amb.db"):
    base = declarative_base()
    db_path = str(db_path)
    db_path = db_path.replace("\\", "//")
    engine = create_engine(f"sqlite:///{db_path}/{db_name}")
    base.metadata.create_all(bind=engine)
    return base, engine


main_base, main_engine = amb_engine_creation()
