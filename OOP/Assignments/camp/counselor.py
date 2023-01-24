from person import Person
class Counselor(Person):

    def __init__(self, hire_date, salary, first_name, last_name):
        super().__init__(first_name, last_name)
        self.hire_date = hire_date
        self.salary = salary

    def __str__(self):
        return  "{0} {1} was hired {2}. {0}'s salary: {3}".format(self.first_name, self.last_name, self.hire_date, self.salary) 
