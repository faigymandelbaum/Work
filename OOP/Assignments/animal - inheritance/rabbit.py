from animal import Animal

class Rabbit(Animal):
    def __init__(self, clr):
        super().__init__(clr, True)

    def walk(self):
        return "Walking on 2 legs." 

    def eat(self, food):
        if food in self.allowed_foods:
            return ("eating {}.".format(food))  
        else:
            raise Exception("Food not allowed!")         