class Student:
    def __init__(self):
        # private varibale or property in Python
        self.__id = -1
        self.__name = ""
        self.__address = ""
        self.__age = 0
        self.__registered_date = ""
        self.__completed = ""
        self.__completed_date = ""

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_registered_date(self, registered_date):
        self.__registered_date = registered_date

    def get_registered_date(self):
        return self.__registered_date

    def set_completed(self, completed):
        self.__completed = completed

    def get_completed(self):
        return self.__completed

    def set_completed_date(self, completed_date):
        self.__completed_date = completed_date

    def get_completed_date(self):
        return self.__completed_date
