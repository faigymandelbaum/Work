# I used instruction A

class Shopper:

    def __init__(self):
        self.__last_name = None
        self.__address = None
        self.__pref_transport_method = None

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_pref_transport_method(self):
        return self.__pref_transport_method        

    def set_last_name(self, lname):
        self.__last_name = lname  

    def set_address(self, address):
        self.__address = address 

    def set_pref_transport_method(self, method):
        self.__pref_transport_method = method
           



def trying_again():
    shopper1 = Shopper()
    last_name = input("Hi there, what is your last name? ")
    shopper1.set_last_name(last_name)
    address = input("What is your address? ")
    shopper1.set_address(address)
    
    add_items_to_shopping_list = True 
    shopping_list = []
    new_item = None
    while add_items_to_shopping_list:
        new_item = input("Enter the item to add to your shopping list: ")
        shopping_list.append(new_item)
        add_item = input("Do you have another item to add to your shopping list? Enter y or n")
        add_items_to_shopping_list = add_item == "y" #if the add_item is set to y, add_items_to_shopping_list will be True. If the user entered something else add_items_to_shopping_list will be False

    print("This is your shopping list: ")
    for list_item in shopping_list:
        print(list_item)

    fave_store = input("Now it's time to go to the store. Which store would you like to go to? ")
    store_address = input("What's the address of the store? ")
    is_usually_well_stocked = input("Is the store usually well stocked? Enter y or n ")
    pref_transport_method = input("What is your preferred method of transportation? ")
    shopper1.set_pref_transport_method(pref_transport_method)

    print("Here we go to " + fave_store + " via a " + shopper1.get_pref_transport_method() + " at the location " + store_address + "." )
    if is_usually_well_stocked:
        print("I'm hoping it'll be well stocked because usually it is " )
    else:
        print("I'm hoping it'll be well stocked because usually it is not" )


    item_found = None
    missing_items = []
    for list_item in shopping_list:
        item_found = input("Did you find " + list_item + "? Enter y or n")
        if item_found == "n":
            missing_items.append(list_item)
    
    if len(missing_items) > (len(shopping_list)/2): #more than half the list is missing from the store
        print("looks like the store is not well stocked today")
    else :
        print("we did alright picking out our items today")

    ready_to_pay = "n"
    while ready_to_pay == "n":
        ready_to_pay = input("Ready to pay? enter y or n ")

    print("Hooray, we're on our way back to the " , shopper1.get_last_name() , " residence at " + shopper1.get_address())

main() 

