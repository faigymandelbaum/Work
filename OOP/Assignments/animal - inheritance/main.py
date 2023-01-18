from horse import Horse
from rabbit import Rabbit

def main():
    my_horse = Horse('white')
    print (my_horse.color)
    print (my_horse.walk())

    my_rabbit = Rabbit('grey')
    print (my_rabbit.has_tail)
    print (my_rabbit.walk())

if __name__ == "__main__":
    main()    