class User:
    def __init__(self, name, password, play_lists):
        self.__name = name
        self.__pasword = password
        self.__play_lists = play_lists

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def play_lists(self):
        return self.__play_lists

    @play_lists.setter
    def play_lists(self, value):
        self.__play_lists = value
