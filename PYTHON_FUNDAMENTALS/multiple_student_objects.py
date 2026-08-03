class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("arpita",90)
student2 = Student("parth",80)
student3 = Student("aditya",85)
student4 = Student("arpit",89)
student5 = Student("aditi",50)

students = [student1, student2, student3, student4, student5]

for student in students:
    print(student.name, ":", student.marks)

highest = students[0]

for student in students:
    if student.marks > highest.marks:
        highest = student

print("Top Student:", highest.name)
print("Highest Marks:", highest.marks)