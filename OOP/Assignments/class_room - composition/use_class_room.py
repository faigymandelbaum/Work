from teacher import Teacher
from class_room import Classroom
from student import Student

def main():
    my_fave_teacher = Teacher("Esti Donnebaum", "support")

    student1 = Student("Elisheva", "Friedman", "B")
    student2 = Student("Batsheva", "Cohen", "A")

    students = [student1, student2]

    my_class_room  = Classroom(my_fave_teacher, students)
    print (my_class_room)

    teacher_say_hi(my_class_room)

def teacher_say_hi(classroom1):
    print("Hi, from {}.".format(classroom1.teacher.name))

if __name__ == '__main__':
    main()    

    