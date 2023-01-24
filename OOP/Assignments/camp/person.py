class Person:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name