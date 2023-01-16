from employee import Employee

def main():
    employee1 = Employee('Avi', 'engineering')
    print("employee's name: " + employee1.name)
    print("employee's department: " + employee1.department)

    
    name_entered = input("Enter a new employee name: ")
    employee1.name = name_entered
   
    dept_entered = input("Enter a new department: ")
    employee1.department  = dept_entered

    print ("My new name is: " + employee1.name)
    print ("My new dept is: " + employee1.department)

main()    
