class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("NAME :",self.name)
        print("SALARY :",self.salary)

class Manager(Employee):

    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department :",self.department)

object = Manager("Arpita",50000,"IT")
object.display()