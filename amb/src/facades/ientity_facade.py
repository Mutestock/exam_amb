from zope.interface import Interface, Attribute


class IEntityFacade(Interface):

    """[Interface for all database interactions with entities]
    """

    def create(entity):
        """[Creates an entity in the database]

        :param entity: [Entity object]
        :type entity: [Object]
        """

    def read(id):
        """[Reads an entity from the database by id]

        :param id: [Entity id]
        :type id: [int]
        """

    def read_all():
        """[Read all entities of a given type]
        """

    def update(entity):
        """[Updates an entity in the database]

        :param entity: [Entity object]
        :type entity: [Object]
        """

    def delete(entity):
        """[Deletes an entity from the database]

        :param entity: [Entity object]
        :type entity: [Object]
        """
