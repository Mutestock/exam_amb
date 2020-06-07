from sqlalchemy.orm import sessionmaker
from amb.src.connection.db_management import initialize
import functools


def session_handler(engine=None):
    """[Resolves all basic database session queries]

    :param engine: [Sqlalchemy engine object to bind sessionmaker]
    :type engine: [Sqlalchemy engine object]
    """

    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, engine):
            print(engine)
            session = sessionmaker(bind=engine)()
            #print(f"Args 0 = {args[0]} ")
            if func.__name__ == "create":
                entity = args[0]
                session.add(entity)
                session.commit()
                func(*args, engine)
            elif func.__name__ == "read":
                search = args[0]
                res = session.query(search)
                func(*args, search=res)
            elif func.__name__ == "read_all":
                search = args[0]
                res = session.query(search).all()
                print(res)
                func(*args, search=res)
            elif func.__name__ == "update":
                entity = arg[0]
                session.commit()
                func(*args, entity=entity)
            elif func.__name__ == "delete":
                search = args[0]
                session.query(search).delete()
                func(*args, entity=entity)
            session.close()
            return

        return wrapper

    return func_decorator
