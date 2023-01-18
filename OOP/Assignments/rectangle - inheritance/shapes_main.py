from rectangle import Rectangle
from square import Square

def main():
    rect = Rectangle(9, 6)
    print("Rectangle's area: {}".format(rect.calculate_area()))

    square = Square(5)
    print("Square's area: {}".format(square.calculate_area()))

if __name__ == "__main__":
    main()
