from animal import Animal
from horse import Horse
from rabbit import Rabbit
import random
def main():
    my_animal = get_random_animal()
    is_rabbit = isinstance(my_animal, Rabbit)
    if is_rabbit:
        my_animal.eat("carrots")
    else:
        my_animal.walk()
    is_animal = isinstance(my_animal, Animal)
    animal_type = type(my_animal)
    print("is rabbit")
    print(isinstance(my_animal, Rabbit))
    print(type(my_animal) == Rabbit)
    print("is horse")
    print(isinstance(my_animal, Horse))
    print(type(my_animal) == Horse)
    print("is animal")
    print(isinstance(my_animal, Animal))
    print(type(my_animal) == Animal)
def get_random_animal() -> Animal:
    my_horse = Horse("white")
    my_rabbit = Rabbit("grey")
    my_animals = [my_horse, my_rabbit]
    return random.choice(my_animals)
if __name__ == "__main__":
    main()