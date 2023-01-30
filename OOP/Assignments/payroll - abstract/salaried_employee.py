from employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, first_name, last_name, weekly_salary) -> None:
        super().__init__(first_name, last_name)
        self.weekly_salary = weekly_salary

    def get_salary(self):
        return self.weekly_salary
