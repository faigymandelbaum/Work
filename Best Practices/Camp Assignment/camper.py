from person import Person
from allergy import Allergy
from datetime import datetime 


class Camper(Person):
    def __init__(self, f_name, l_name, date_of_birth:datetime):
        super().__init__(f_name, l_name)
        
        try:
            self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except:
            self.date_of_birth = datetime.strptime(date_of_birth, "%Y/%m/%d").date()

        self.allergies = []

    def add_allergy(self, allergy):
        all_allergies = [member.name for member in Allergy]
        if allergy.upper() in all_allergies:
            if Allergy[allergy.upper()] not in self.allergies:
                self.allergies.append(Allergy[allergy.upper()])
        else:
            raise Exception("Invalid Allergy")
    

    def get_age(self):
        return int(datetime.now().year - self.date_of_birth.year)

    def __str__(self):
        s = super().__str__()
        age = str(self.get_age()) 
        s += "\nDob: " + str(self.date_of_birth) + "\nAge: " + age
        if len(self.allergies) > 1:
            s += "\nAllergies: "
            for allergy in self.allergies:
                s += '\n' + str(allergy.name.lower())  

        return s

# camper = Camper('Faigy', 'Mandelbaum', '2000/06/07')
# camper.add_allergy('eggs')
# print (camper)


# print (camper.allergies)


