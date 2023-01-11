
class Hummingbird:
    species="Costa's Hummingbird"

    def __init__(self, color, age):
        #instance attributes
        self.color=color
        self.age=age

    def survive_cold_temp(self, normal_heart_rate, survive_heart_rate=50):
        if normal_heart_rate > 500 and normal_heart_rate < 900:
            print("I'm in tupor mode")
            return survive_heart_rate
        else:
            print("heart rate entered not valid")
    
    def __str__(self):
        if self.color =="purple":
            gender="male"
        else:
            gender="female"
        description= "I'm a {} year old {} Costa Hummingbird".format(self.age, gender)
        return description

def main():
    hummingbird_1 = Hummingbird("purple", 5)
    hummingbird_1.survive_cold_temp(678)
    print(hummingbird_1)

if __name__ == "__main__":
    main()
        





