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

student1 = Student("Arpita",90)
student1.display()
student1.calculate_grade()
student2 = Student("Parth",80)
student2.display()
student2.calculate_grade()