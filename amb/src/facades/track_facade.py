from zope.interface import implementer
from ientity_facade import IEntityFacade
from sqlalchemy.orm import sessionmaker
from amb.src.utilities.decorators import session_handler


@implementer(IEntityFacade)
class TrackFacade:
    def __init__(self, engine):
        self.__engine = engine
        self.__sessionmaker = sessionmaker(bind=engine)

    @session_handler(engine=engine)
    def create(self, entity):
        return entity

    @session_handler(engine=engine)
    def read(self, id):
        sessionk

    @session_handler(engine=engine)
    def read_all(self):
        raise NotImplementedError

    @session_handler(engine=engine)
    def update(self, entity):
        raise NotImplementedError

    @session_handler(engine=engine)
    def delete(self, entity):
        raise NotImplementedError
