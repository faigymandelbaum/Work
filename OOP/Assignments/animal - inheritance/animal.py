class Animal:

    def __init__(self, clr, has_a_tail):
        self.color = clr
        self.has_tail = has_a_tail
        self.allowed_foods = []

    def walk(self):
        return "Walking on 4 legs "  

    @property
    def allowed_foods(self):
        return self._allowed_foods

    @allowed_foods.setter
    def allowed_foods(self, value):
        self._allowed_foods = value          