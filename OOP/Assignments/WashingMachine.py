
class WashingMachine:

    prerequisite = "water_pipe"

    def __init__(self, temp, spin_speed, cycle_type, door_is_locked, detergent):
        self.temp = temp
        self.speed = spin_speed
        self.cycle = cycle_type
        self.door_locked = door_is_locked
        self.detergent = detergent

    def soak(self):
        if self.door_locked == True:
            print ("I'm soaking")    
        else:
            print ("Close door")

    def show_settings(self):
        print ('My temperature is ' + str(self.temp))
        print ('My spinspeed is ' + str(self.speed))
        print ('My cycle type is ' + self.cycle)

    def agitate(self):
        print ("Scrubbing with " + self.detergent)

    def rinse(self):
        print("Rinsing")

    def wash_laundry(self):
        self.show_settings()
        self.soak()
        self.agitate()
        self.rinse() 

my_washing_machine = WashingMachine(30, 600, "cottons", True, "ariel")

my_broken_washing_machune = WashingMachine(60, 0, "wool", False, "Persil Gel")

my_washing_machine.wash_laundry()


        