from zope.interface import Interface, Attribute


class IEntityFacade(Interface):

    """[Interface for all database interactions with entities]
    """

    def create(entity):
        raise NotImplementedError

    def read(id):
        raise NotImplementedError

    def read_all():
        raise NotImplementedError

    def update(entity):
        raise NotImplementedError

    def delete(entity, search):
        raise NotImplementedError
