
from rectangle import Rectangle

def main():

    small_rectangle = Rectangle(5, 2)

    small_rectangle.length = input("put in length: ")
    small_rectangle.width = input("put in width: ")

    print (small_rectangle.length * small_rectangle.width)

main()    