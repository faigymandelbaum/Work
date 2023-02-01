from person import Person
import decimal
import datetime

class Counselor(Person):

    def __init__(self, first_name, last_name, salary:decimal, hire_date = datetime.datetime.now().date()):
        super().__init__(first_name, last_name)
        self.hire_date = hire_date
        self.salary = salary

    def __str__(self):
        return super().__str__() + "\nHire date: " + str(self.hire_date) + "\nSalary: " + str(self.salary) 

        
# my_counselor = Counselor('Esti', "Herman", 789)
# print (my_counselor)  

