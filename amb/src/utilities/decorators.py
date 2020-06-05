from sqlalchemy.orm import sessionmaker


def session_handler(engine):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            Session = sessionmaker(bind=engine)()
            print(f"Args 0 = {args[0]} ")
            if func.__name__ == "create":
                entity = func(*args, **kwargs)
                session.add(entity)
                session.commit(entity)
            elif func.__name__ == "read":
                pass
            elif func.__name__ == "read_all":
                pass
            elif func.__name__ == "update":
                pass
            elif func.__name__ == "delete":
                pass

            session.close()
            return wrapper

        return func_decorator
