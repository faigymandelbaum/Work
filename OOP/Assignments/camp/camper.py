from person import Person
from enum import Enum

class Camper(Person):
    def __init__(self,birth_date):
        self.date_of_birth = birth_date
        self.allergies = []

    def add_allergy(self, string):
        self.allergies.append(Enum(string))

    def get_age(self):
        return

    def __str__(self):
        return


