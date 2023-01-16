def set_settings(temp, spin_speed, cycle):
    print ('My temperature is ' + str(temp))
    print ('My spinspeed is ' + str(spin_speed))
    print ('My cycle type is ' + cycle)

def soak(door_is_locked):
    if door_is_locked == True:
        print ("I'm soaking!") 
    else:
        print("Close door") 

def agitate(detergent):
    print ("Scrubbing with " + detergent)

def rinse():
    print("Rinsing")

def wash_laundry(temp, speed, cycle, door_is_locked, detergent):
    set_settings(temp, speed, cycle)
    soak(door_is_locked)
    agitate(detergent)
    rinse()

wash_laundry(30, 700, 'cottons', True, 'persil')    



         