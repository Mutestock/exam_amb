class Playlist:
    def __init__(self, track_list, name):
        self.__track_list = track_list
        self.__name = name

    @property
    def track_list(self):
        return self.__track_list

    @track_list.setter
    def track_list(self, value):
        self.__track_list = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
