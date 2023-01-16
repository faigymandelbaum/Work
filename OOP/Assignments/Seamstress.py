
class Seamstress:

    # class attributes:

    hand = "hand"
    sewing_machine = "singer" # every seamstress in Israel has a singer sewing_machine.

    def __init__(self, experience, talent, specialty):
        self.experience = experience
        self.talent = talent
        self.specialty = specialty

    def cut_material(self, cutting_tool, fabric):
        print("I'm cutting the fabric called " + fabric +  " with my " + cutting_tool + " in my " + self.hand) 

    def take_measurements(self, measuring_tool):
        print("Now I'm taking measurements with a " + measuring_tool) 

    def sew_garment(self, requested_garment_type):
        print("I'm sewing a " + requested_garment_type + " with my " + self.sewing_machine + " sewing machine.") 

    def __str__(self):
        description = "HI I'm a seamstress. I have " + self.experience +" experience. "
        if self.talent == True:
            description += "I've got talent"
        else :
            description += " I've got no talent. "
        description += " My speciality is " + self.specialty + '.'
        return description      

# create an instance of seamstress

def main():
    rivky_berlin = Seamstress("6 years", True, "gowns")
    rivky_berlin.take_measurements("measuring stick") 
    rivky_berlin.cut_material("scissors", "crushed velvet") 
    rivky_berlin.sew_garment("gown")
    print("This is my experience: " + rivky_berlin.experience) 
    print (rivky_berlin)


chava_kurman = Seamstress("10 years ", True, "baby things") 
chava_kurman.take_measurements("measuring stick") 
print(chava_kurman)  

if __name__ == "__main__":
    main()                 