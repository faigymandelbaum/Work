from asalaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee

def main():

    employee1 = SalariedEmployee('Avi', 'Gold', 678)
    employee2 = HourlyEmployee('Chayim', 'Mandel', 25, 30)
    employee3 = SalariedEmployee('Reuven', 'Halpern', 540)
    employee4 = HourlyEmployee('Yehudah', 'Gafni', 22, 24)
    employee5 = SalariedEmployee('Yosef', 'Rosen', 810)
    employee6 = HourlyEmployee('David', 'Rubin', 29, 45)

    employees = [employee1, employee2, employee3, employee4, employee5, employee6]

    for employee in employees:
        print(employee.full_name +': '+ str(employee.get_salary()))

if __name__ == "__main__":
    main()        