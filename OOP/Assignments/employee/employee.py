class Employee:

    def __init__(self, emp_name, dept):
        self.name = emp_name
        self.department = dept

    @property
    def name(self):
        return self._name.upper()

    @name.setter
    def name(self, value):
        if value.isdigit():
            self._name = ""
        else:
            self._name = value        

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value     


