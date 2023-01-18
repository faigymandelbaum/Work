from animal import Animal

class Horse(Animal):
    def __init__(self, clr):
        super(). __init__(clr, True)

    def walk(self):
        return super().walk() + "and gallopping."    