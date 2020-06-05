from sqlalchemy.orm import sessionmaker


def session_handler(engine):
    """[Resolves all basic database session queries]

    :param engine: [Sqlalchemy engine object to bind sessionmaker]
    :type engine: [Sqlalchemy engine object]
    """

    def func_decorator(func):
        def wrapper(*args, **kwargs):
            session = sessionmaker(bind=engine)()
            print(f"Args 0 = {args[0]} ")
            if func.__name__ == "create":
                entity = args[0]
                session.add(entity)
                session.commit(entity)
                func(*args, **kwargs)
            elif func.__name__ == "read":
                search = args[0]
                res = session.query(search)
                func(*args, **kwargs, search=res)
            elif func.__name__ == "read_all":
                entity_type = args[0]
                res = session.query(entity_type).all()
                func(*args, **kwargs, entity_type=res)
            elif func.__name__ == "update":
                entity = arg[0]
                session.commit(entity)
                func(*args, *kwargs, entity=entity)
            elif func.__name__ == "delete":
                search = args[0]
                session.query(search).delete()
                func(*args, *kwargs, entity=entity)
            session.close()
            return wrapper

        return func_decorator
