class Track:
    def __init__(self, name, genre, duration, configuration):
        self.__name = name
        self.__genre = genre
        self.__duration = duration
        self.__configuration = configuration
        if not "switch" in self.__configuration:
            self.__configuration["switch"] = "Off"

    #To do: Tags

    @staticmethod
    def get_property_count():
        """[Returns amount of object properties]

        :return: [Amount of variabes]
        :rtype: [int]
        """
        return 5

    @staticmethod
    def get_track_attribute_name_by_index(index):
        return ["mono_stereo", "Interval", "Volume"][index - 1]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        self.__configuration = value
