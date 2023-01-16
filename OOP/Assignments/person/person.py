class Person:

    def __init__(self, firstname, lastname):
        self.__first_name = firstname
        self.__last_name = lastname

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, fname):
        self.__first_name = fname.title()

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, lname):
        self.__last_name = lname.title()
        
                    


