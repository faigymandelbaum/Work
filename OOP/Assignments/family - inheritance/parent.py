from family_member import FamilyMember

class Parent(FamilyMember):
    def __init__(self, f_name, l_name, age):
        super().__init__(f_name, l_name, age)

    def babysit(self):
        return super().babysit() + "Cleanes up the house."    