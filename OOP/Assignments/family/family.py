class Family:

    def __init__(self, last_name, home_address, famous_for, family_members):
        self.last_name = last_name
        self.home_address = home_address
        self.famous_for = famous_for
        self.family_members = family_members

    def __str__(self):
        f = "Family {} lives in {}. \nThey are famous for {}!".format(self.last_name, self.home_address, self.famous_for)
        f += "\nThere family members are:"
        for member in self.family_members:
            if member.is_parent == True:
                f += "\nparent: {} is {} years old.".format(member.first_name, member.age)
            else:
                f += "\nchild: {} is {} years old.".format(member.first_name, member.age)
 
        return f   

