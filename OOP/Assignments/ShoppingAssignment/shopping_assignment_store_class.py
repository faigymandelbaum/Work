class Store:

    def __init__(self):
        self.__store_name = None
        self.__store_location = None
        self.__well_stocked = None

    def get_store_name(self):
        return self.__store_name

    def get_store_location(self):
        return self.__store_location

    def get_if_store_well_stocked(self):
        return self.__well_stocked 

    def set_store_name(self, fave_store):
        self.__store_name = fave_store

    def set_store_location(self, store_address):
        self.__store_location = store_address

    def set_if_store_well_stocked(self, well_stocked):
        self.__well_stocked = well_stocked           



def just_trying():
    store = Store()
    last_name = input("Hi there, what is your last name? ")
    address = input("What is your address? ")
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
    store.set_store_name(fave_store)

    store_address = input("What's the address of the store? ")
    store.set_store_location(store_address)

    is_usually_well_stocked = input("Is the store usually well stocked? Enter y or n ")
    store.set_if_store_well_stocked(is_usually_well_stocked)

    pref_transport_method = input("What is your preferred method of transportation? ") #bus, car, walk etc

    print("Here we go to " + store.get_store_name() + " via a " + pref_transport_method + " at the location " + store.get_store_location() + "." )
    if store.get_if_store_well_stocked == 'y':
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

    print("Hooray, we're on our way back to the " +last_name + " residence at " + address)  

main()          