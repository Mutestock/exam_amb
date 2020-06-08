from sqlalchemy.orm import sessionmaker
from amb.src.connection.db_management import initialize, amb_engine
import functools


"""[Resolves all basic database session queries]
:param engine: [Sqlalchemy engine object to bind sessionmaker]
:type engine: [Sqlalchemy engine object]
"""


def session_handler(func):
    def wrapper(*args, engine=amb_engine):
        session = sessionmaker(bind=engine)()
        print(args)
        # print(f"Args 0 = {args[0]} ")
        if func.__name__ == "create":
            entity = args[0]
            session.add(entity)
            session.commit()
            func(*args, engine)

        elif func.__name__ == "read":
            entity_class = args[0]
            modifier = args[1]
            search = args[2]
            res = session.query(entity_class).filter(modifier == search).first()
            return func(entity_class=entity_class, modifier=modifier, search=res)

        elif func.__name__ == "read_all":
            search = args[0]
            res = session.query(search).all()
            return func(search=res)

        elif func.__name__ == "update":
            entity = args[0]
            session.merge(entity)
            session.commit()
            func(entity=entity)

        elif func.__name__ == "delete":
            search = args[0]
            session.query(search).delete()
            func(*args, entity=entity)

        session.close()

    return wrapper
