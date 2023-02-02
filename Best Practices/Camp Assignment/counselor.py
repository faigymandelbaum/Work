from person import Person
import decimal
from datetime import datetime

class Counselor(Person):

    def __init__(self, first_name, last_name, salary:decimal, hire_date:datetime):
        super().__init__(first_name, last_name)
        try:
            self.hire_date = datetime.strptime(hire_date, "%Y-%m-%d").date()
        except:
            self.hire_date = datetime.strptime(hire_date, "%Y/%m/%d").date()
        self.salary = salary

    def __str__(self):
        return super().__str__() + "\nHire date: " + str(self.hire_date) + "\nSalary: " + str(self.salary) 

        
# my_counselor = Counselor('Esti', "Herman", 789)
# print (my_counselor)  

