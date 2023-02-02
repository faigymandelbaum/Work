from camp import Camp
import traceback
import logging

def main():

    our_camp = Camp("Integralytic", 20)

    menu_choice = None
    while menu_choice != 0:

        menu_choice = get_menu_choice()

        try: 

            if menu_choice == 1: #add counselor
                first_name = input("Please enter first name: ")
                last_name = input("Please enter last name: ")
                salary = input("Please enter the counselor's salary in numbers: ")
                try:
                    float(salary)
                except:
                    salary = input("Please re-enter the counselor's salary: ")
                    try:
                        float(salary)
                    except:    
                        print("Salary must be in numbers, youre returned to the main menu.")
                        logging.error(str(ve) + traceback.format_exc())
                        return None
                hire_date = input("Please Enter the counselor's hire date: ")        
                try:
                    our_camp.add_counselor(first_name, last_name, salary, hire_date) 
                    logging.info("Counselor Added Successfully.")
                except ValueError as ve:
                    print (str(ve))
                    logging.error(str(ve) + traceback.format_exc())
                    hire_date = input('The hire date was bad format, please re-enter(yyyy-mm-dd): ') 
                    try:
                        our_camp.add_counselor(first_name, last_name, salary, hire_date)
                        logging.info("Counselor Added Successfully.")
                    except:
                        logging.error(str(ve) + traceback.format_exc())
                        print('The date was wrong format, youre returned to the main menu.')
                        

            elif menu_choice == 2: #add bunk
                bunk_name = input("Please enter a bunk name: ")
                counselor_fname = input("Please Enter the counselor's first name: ")
                counselor_lname = input("Please Enter the counselor's last name: ")
                our_camp.add_bunk(bunk_name, counselor_fname, counselor_lname)
                logging.info("Bunk Added Successfully.")
                
            
            elif menu_choice == 3: #add camper
                first_name = input("Please enter first name: ")
                last_name = input("Please enter last name: ")
                dob = input("Please enter the date of birth in this format: yyyy-mm-dd. ")
                try:
                    our_camp.add_camper(first_name, last_name, dob)
                    logging.info("Camper Added Successfully.")
                except ValueError as ve:
                    print (str(ve))
                    logging.error(str(ve) + traceback.format_exc()) 
                    dob = input('The date of birth was bad format, please re-enter(yyyy-mm-dd): ') 
                    try:
                        our_camp.add_camper(first_name, last_name, dob)
                        logging.info("Camper Added Successfully.")
                    except:
                        print (str(ve))
                        logging.error(str(ve) + traceback.format_exc())                        
                        print('The date was wrong format, youre returned to the menu.')
                    
                            
            elif menu_choice == 4: #add an allergy
                first_name = input("Please enter first name: ")
                last_name = input("Please enter last name: ")
                allergy = input("Enter an allergy: ") 
                try:
                    our_camp.add_allergy(first_name, last_name, allergy)
                    logging.info("Allergy Added Successfully.")
                    
                except:
                    logging.error(traceback.format_exc())
                    allergy = input("Please enter a valid allergy: ")                    
                    try:
                        our_camp.add_allergy(first_name, last_name, allergy)
                        logging.info("Allergy Added Successfully.")
                    except:
                        print (str(ve))
                        logging.error(str(ve) + traceback.format_exc())
                        print('The allergy was not valid, youre returned to the main menu.')
                        
                
                        
                
            elif menu_choice == 5: #assign camper to bunk
                first_name = input("Please enter first name: ")
                last_name = input("Please enter last name: ")
                bunk_name = input("Enter a bunk name: ") 
                our_camp.place_camper(first_name, last_name, bunk_name)
                
            elif menu_choice == 6: #
                print (our_camp) 

            elif menu_choice == 0:
                print ("Ending program")

                logging.info("Ending Application!")


        except Exception as e:
            print (str(e))
            logging.error(traceback.format_exc() + '{}'.format(str(e)))



def get_menu_choice():
    menu = "\n1. Add A Counselor"
    menu +=	"\n2. Add a Bunk" 
    menu +=	"\n3. Add a Camper" 
    menu +=	"\n4. Add an Allergy"
    menu +=	"\n5. Assign a Camper to a Bunk"
    menu +=	"\n6. Display Camp data"
    menu +=	"\n0. Exit Application"

    choice = input(menu + "\nPlease enter 1-6 (or 0 to exit): ")
    try:
        return int(choice)
    except:
        print ('Invalid menu choice. Enter 1-6 (or 0 to exit): ')
        logging.error("Invalid menu choice.")
    


if __name__ == "__main__":
    main()