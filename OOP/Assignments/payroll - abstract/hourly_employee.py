from employee import Employee

class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, hourly_rate, hours_worked_this_week) -> None:
        super().__init__(first_name, last_name)
        self.hourly_rate = hourly_rate
        self.hours_worked_this_week = hours_worked_this_week

    def get_salary(self):
        salary = self.hourly_rate * self.hours_worked_this_week
        return salary

