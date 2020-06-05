from zope.interface import implementer
from ientity_facade import IEntityFacade
from sqlalchemy.orm import sessionmaker
from amb.src.utilities.decorators import session_handler


@implementer(IEntityFacade)
class TrackFacade:
    def __init__(self, engine):
        self.__engine = engine

    @session_handler(engine=engine)
    def create(self, entity):
        """[Track CRUD creation.]

        :param entity: [Track entity]
        :type entity: [Track object]
        :return: [Same entity as parametre]
        :rtype: [Track object]
        """
        return entity

    @session_handler(engine=engine)
    def read(self, search):
        """[Track CRUD read.]

        :param search: [Query identifier]
        :type search: [str]
        :return: [Found found object]
        :rtype: [Track object]
        """
        return search

    @session_handler(engine=engine)
    def read_all(self, entity_type):
        """[Track CRUD read_all.]

        :param entity_type: [Entity object type]
        :type entity_type: [Object]
        :return: [List of all track entities from database]
        :rtype: [list]
        """
        return entity_type

    @session_handler(engine=engine)
    def update(self, entity):
        """[Track CRUD update]

        :param entity: [Track entity object]
        :type entity: [Track object]
        :return: [Same entity as parametre]
        :rtype: [Track object]
        """
        return entity

    @session_handler(engine=engine)
    def delete(self, search):
        """[Track CRUD delete]

        :param search: [Search query]
        :type search: [str]
        :return: [Same Track object, which is no longer in the database]
        :rtype: [Track object]
        """
        return search
