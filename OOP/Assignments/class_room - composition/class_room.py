class Classroom:

    def __init__(self, list_students, teacher):
        self.teacher = teacher
        self.students = list_students  

    def __str__(self):
       s =  "welcome to our classroom."
       s += "\nTeacher: " + str(self.teacher)
       s+= "\nStudents:\n"
       for student in self.students:
            s+= student.first_name + " " + student.last_name + " Mark: " + student.mark + "\n"

       return s