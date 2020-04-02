class Track(object):
    def __init__(self, name, duration, mode, author, description, tags):
        self.__name = name
        self.__duration = duration
        self.__mode = mode
        self.__author = author
        self.__description = description
        self.__tags = tags

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.mode = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, value):
        self.__tags = value
