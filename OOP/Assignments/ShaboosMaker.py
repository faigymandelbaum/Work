
class ShabbosMaker:

    # class attributes:
    name = "Faigy"
    say = "L'choved Shabbos Kodesh"

    def __init__(self, cleaning_time, bathing_time, help):
        self.time1 = cleaning_time
        self.time2 = bathing_time
        self.help = help

    def clean_house(self, cleaning_suplies):
        print(self.name , "is cleaning the house " , self.time1 , "before Shabbos, with ", cleaning_suplies, '.' self.say) 

    def cook_food(self, food_list):
        for food in food_list:
           print("The ", self.help, "is cooking ", food, "while saying ", self.say, "!") 
        print ("With the ", self.help, "'s help, The whole Shabbos is cooked!!!")   

    def take_baths(self, soap):
        print(self.name, "is showering her kids with ", soap, ' ', self.time2, "before Shabbos.")    

# create an instance of seamstress

def main():
    my_shabbos_maker = ShabbosMaker("a day ", "3 hours", "seminary girl")
    my_shabbos_maker.clean_house("fantastic") 
    my_shabbos_maker.cook_food(['fish', 'cholent', 'soup', 'chicken', 'kugel', 'dessert']) 
    my_shabbos_maker.take_baths("kef shampoo")
    print("Now we are all ready: " + my_shabbos_maker.say)   

if __name__ == "__main__":
    main() 