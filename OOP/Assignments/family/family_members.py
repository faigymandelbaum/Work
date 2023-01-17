class FamilyMember:

    def __init__(self, fname, age, is_parent):
        self.first_name = fname
        self.age = age
        self.is_parent = is_parent

    @property
    def is_parent(self):
        return self._is_parent

    @is_parent.setter
    def is_parent(self, value):
        if self.age > 20 and value == True:
            self._is_parent = value
        else:
            self._is_parent = False


