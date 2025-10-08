#Basics on classes and objects 

class Student:
    def __init__(self, name: str, age: int, grade: float):
        self.name = name 
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
#Add students to a course
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        #creating a list for students 
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

#Creating students 
student1 = Student("Izzy", 22, 91)
student2 = Student("Mia", 20, 75)
student3 = Student("Suzie", 23, 80)

#Creating course
course = Course("Science", 2)

#Adding students 
course.add_students(student1)
course.add_students(student2)
#This one will bot be added beacuse max_students is 2
course.add_students(student3)

#Targeting names, grades, ages in list 
print(course.students[0].grade)

#Returns False 
print(course.add_students(student3))

#Printing average grade 
print(course.get_average_grade())

