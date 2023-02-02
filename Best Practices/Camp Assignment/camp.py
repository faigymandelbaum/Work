from person import Person
from counselor import Counselor
from camper import Camper
from bunk import Bunk
from allergy import Allergy
import an_logs
import logging

logging.basicConfig(filename= an_logs.LOG_FILE,
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class Camp:

    def __init__(self, camp_name:str, max_bunks:int):
        self.camp_name = camp_name
        self.max_bunks = max_bunks
        self.bunks = []
        self.num_bunks = 0
        self.persons = []

    def find_counselor(self, first_name, last_name):
        for person in self.persons:
            if isinstance(person, Counselor):
                if first_name == person.first_name and last_name == person.last_name:
                    return person

        return None

    def find_camper(self, first_name, last_name):
        for person in self.persons:
            if isinstance(person, Camper):
                if first_name == person.first_name and last_name == person.last_name:
                    return person
                
        return None

    def add_counselor(self, first_name, last_name, salary:float, hire_date): # Hire date is the cuurent date of the time that was assigned.
        counselor = self.find_counselor(first_name, last_name)
        if counselor == None:
            new_counselor = Counselor(first_name, last_name, salary, hire_date)
            self.persons.append(new_counselor)
            print ("Counselor added successfully.")
        else:
            raise Exception("Counselor already exists.")

        return None

    def add_camper(self, first_name, last_name, dob):
        camper = self.find_camper(first_name, last_name)
        if camper == None:
            new_camper = Camper(first_name, last_name, dob)
            self.persons.append(new_camper)
            print ("Camper added successfully.")
        else: 
            raise Exception("Camper already exists.")
            
        return None

    def add_bunk(self, bunk_name, counselor_fname, counselor_lname):
        bunk_counselor = self.find_counselor(counselor_fname, counselor_lname)
        if bunk_counselor == None:
            raise Exception("Counselor {} {} not found. Could not add bunk.".format(counselor_fname, counselor_lname))
        
        else:
            if self.num_bunks < self.max_bunks:
                new_bunk = Bunk(bunk_name, bunk_counselor)
                self.bunks.append(new_bunk)
                self.num_bunks += 1
                print ("Bunk {} added.".format(bunk_name))
            else:
                raise Exception('You have reached the max nummer of bunks. Cannot add bunks anymore.')

        return None

    def find_bunk(self, bunk_name):
        for bunk in self.bunks:
            if isinstance(bunk, Bunk):
                if bunk.bunk_name == bunk_name:
                    return bunk

        return None
            
    def place_camper(self, first_name, last_name, bunk_name):
        campers_bunk = self.find_bunk(bunk_name)
        camper = self.find_camper(first_name, last_name)
        if campers_bunk == None:
            raise Exception ("Bunk {} not found.".format(bunk_name))
        elif camper == None:
            raise Exception ("Camper {} {} not found.".format(first_name, last_name))    
        else:    
            campers_bunk.add_camper(camper)
            print ("Camper {} {} placed in bunk {}.".format(camper.first_name, camper.last_name, bunk_name))

        return None

    def add_allergy(self, first_name, last_name, allergy:str):
        camper = self.find_camper(first_name, last_name)
        if camper == None:
            print ("Camper {} {} not found.".format(first_name, last_name)) 
        else:
            camper.add_allergy(allergy)
            print ("Allergy added to camper.")

        return None

    def __str__(self):
        s = "Welcome to camp {}! \nOur camp has {} bunks.".format(self.camp_name, self.num_bunks)
        s += "\nOur bunks:"
        for bunk in self.bunks:
            s += "\n- {}".format(str(bunk))
 
        return s

# my_camp = Camp("B'nos", 3)


# a = my_camp.add_counselor('R', 'l', 9887)
# b = my_camp.add_counselor('A', 's', 9887)
# c = my_camp.add_counselor('A', 's', 9887)
# c = my_camp.add_counselor('Z', 's', 9887)
# c = my_camp.add_counselor('x', 'm', 9887)
# my_camp.add_bunk('g', 'R', 'l')
# my_camp.add_bunk('v', 'A', 's')
# my_camp.add_bunk('o', 'd', 'r')
# my_camp.add_bunk('k', 'Z', 's')
# my_camp.add_bunk('s', 'x', 'm')
# my_camp.add_camper('x', 'p', '2015-02-05')
# my_camp.add_camper('s', 't', '2012-02-05')
# my_camp.add_camper('w', 'r', '2014-02-05')
# my_camp.add_camper('d', 'h', '2016-02-05')
# my_camp.add_camper('c', 'f', '2014-02-05')
# print (my_camp.find_counselor('R', 'l'))
# print (my_camp.find_counselor('s', 'g'))
# print (my_camp.find_bunk('g'))
# print (my_camp.find_bunk('p'))
# my_camp.place_camper('x', 'p', 'g')
# my_camp.place_camper('s', 't', 'o')
# my_camp.place_camper('b', 'p', 'g')
# my_camp.place_camper('x', 'n', 'g')
# my_camp.add_allergy('x', 'p', 'milk')
# my_camp.add_allergy('x', 'p', 'mil')
# my_camp.add_allergy('x', 'u', 'milk')

# print (my_camp)

