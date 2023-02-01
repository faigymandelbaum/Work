from camp import Camp
import decimal
from datetime import datetime

def main():

    our_camp = Camp("Integralytic", 20)

    menu_choice = None
    while menu_choice != 0:
        menu_choice = get_menu_choice()

        if menu_choice == 1: #add counselor
            first_name = input("Please enter first name: ")
            last_name = input("Please enter last name: ")
            salary = input("Please enter the counselor's salary: ")
            hire_date = datetime.now().date
            our_camp.add_counselor(first_name, last_name, salary) 
            

        elif menu_choice == 2: #add bunk
            bunk_name = input("Please enter a bunk name: ")
            counselor_fname = input("Please Enter the counselor's first name: ")
            counselor_lname = input("Please Enter the counselor's last name: ")
            our_camp.add_bunk(bunk_name, counselor_fname, counselor_lname)
            
        
        elif menu_choice == 3: #add camper
            first_name = input("Please enter first name: ")
            last_name = input("Please enter last name: ")
            dob = input("Please enter the date of birth in this format: yyyy-mm-dd. ")
            our_camp.add_camper(first_name, last_name, dob)
            
                           
        elif menu_choice == 4: #add an allergy
            first_name = input("Please enter first name: ")
            last_name = input("Please enter last name: ")
            allergy = input("Enter an allergy: ") 
            our_camp.add_allergy(first_name, last_name, allergy)
            
              
        elif menu_choice == 5: #assign camper to bunk
            first_name = input("Please enter first name: ")
            last_name = input("Please enter last name: ")
            bunk_name = input("Enter a bunk name: ") 
            our_camp.place_camper(first_name, last_name, bunk_name)
            
        elif menu_choice == 6: #
            print (our_camp)   
        elif menu_choice == 0:
            return "Ending Application!"
                
def get_menu_choice():
    menu = "\n1. Add A Counselor"
    menu +=	"\n2. Add a Bunk" 
    menu +=	"\n3. Add a Camper" 
    menu +=	"\n4. Add an Allergy"
    menu +=	"\n5. Assign a Camper to a Bunk"
    menu +=	"\n6. Display Camp data"
    menu +=	"\n0. Exit Application"

    choice = input(menu + "\nPlease enter 1-6 (or 0 to exit): ")
    return int(choice)

if __name__ == "__main__":
    main()