from zope.interface import implementer
from amb.src.facades.ientity_facade import IEntityFacade
from sqlalchemy.orm import sessionmaker
from amb.src.utilities.decorators import session_handler
from amb.src.connection.db_management import initialize


# global engine_out

#
#
#
#

# @implementer(IEntityFacade)
# class TrackFacade:
#    def __init__(self, engine):
#        self.__engine = engine


@session_handler()
def create(self, entity, engine=None):
    """[Track CRUD creation.]
    :param entity: [Track entity]
    :type entity: [Track object]
    :return: [Same entity as parametre]
    :rtype: [Track object]
    """
    return entity


@session_handler()
def read(self, search, engine=None):
    """[Track CRUD read.]
    :param search: [Query identifier]
    :type search: [str]
    :return: [Found found object]
    :rtype: [Track object]
    """
    return search


@session_handler()
def read_all(self, search, engine=None):
    """[Track CRUD read_all.]
    :param entity_type: [Entity object type]
    :type entity_type: [Object]
    :return: [List of all track entities from database]
    :rtype: [list]
    """
    return search


@session_handler()
def update(self, entity, engine=None):
    """[Track CRUD update]
    :param entity: [Track entity object]
    :type entity: [Track object]
    :return: [Same entity as parametre]
    :rtype: [Track object]
    """
    return entity


@session_handler()
def delete(self, search, engine=None):
    """[Track CRUD delete]
    :param engine: [Engine to use. Either define one in this function or use the session_handler decorator]
    :type engine: [SqlAlchemy engine object]
    :param search: [Search query]
    :type search: [str]
    :return: [Same Track object, which is no longer in the database]
    :rtype: [Track object]
    """
    return search
