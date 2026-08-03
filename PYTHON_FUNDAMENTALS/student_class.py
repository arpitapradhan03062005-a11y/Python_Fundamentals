class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :",self.name)
        print("Marks :",self.marks)

student1 = Student("Arpita",90)
student1.display()
student2 = Student("Parth",80)
student2.display()

