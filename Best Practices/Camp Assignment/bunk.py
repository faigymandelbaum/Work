from camper import Camper
from counselor import Counselor


class Bunk:

    def __init__(self, bunk_name:str, counselor:Counselor):
        self.bunk_name = bunk_name
        self.counselor = counselor
        self.campers = []

    def add_camper(self, camper):
        camper_exists = False
        for c in self.campers:
            if camper.first_name == c.first_name and camper.last_name == c.last_name:
                camper_exists = True
                print ("{} {} is already in bunk {}.".format(camper.first_name, camper.last_name, self.bunk_name))
        else:
            if not camper_exists:
                self.campers.append(camper)
            

    def __str__(self):
        s = "Bunk name: {} \nCounselor: {} \nCampers: ".format(self.bunk_name, str(self.counselor))
        for camper in self.campers:
            s += "\n* {}".format(str(camper))
        return s

counselor = Counselor('Rivky', 'Green', 789, '2015-02-05')
camper1 = Camper('Ruchi', 'Blau', '2003-02-05')
camper2 = Camper('Esti', 'Black', '2005-02-05')
camper3 = Camper('Malky', 'Black', '2005-02-05')
camper4 = Camper('Malky', 'Black', '2005-02-05')
my_bunk = Bunk('A', counselor)
my_bunk.add_camper(camper1)  
my_bunk.add_camper(camper2)
my_bunk.add_camper(camper3)
my_bunk.add_camper(camper4)
 
print (my_bunk)   