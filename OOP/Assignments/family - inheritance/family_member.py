class FamilyMember:
    def __init__(self, f_name, l_name, age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age

    def babysit(self):
        return "Looking after the children, making sure they are happy, stimulated and occupied, fed and sleeping with love and warmth. "

    def __str__(self):
        return "{} {} is {} years old.".format(self.first_name, self.last_name, self.age)        