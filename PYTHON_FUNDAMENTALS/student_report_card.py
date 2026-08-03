class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :",self.name)
        print("Marks :",self.marks)

    def calculate_grade(self):
            if self.marks >= 90:
                print("Grade : A")
            elif self.marks >= 80 and self.marks <= 89:
                print("Grade : B")
            elif self.marks >= 70 and self.marks <= 79:
                print("Grade : C")
            elif self.marks >= 60 and self.marks <= 69:
                print("Grade : D")
            else:
                print("Grade : F")

s1 = Student("arpita",90)
s2 = Student("parth",80)
s3 = Student("aditya",70)
s4 = Student("parag",85)
s5 = Student("aditi",2)

students = [s1,s2,s3,s4,s5]

for student in students:
    student.display()
    student.calculate_grade()