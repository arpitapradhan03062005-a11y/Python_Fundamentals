class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def total_salary(self):
        print("Total salary :",self.salary)

class Manager(Employee):

    def __init__(self, name, salary,bonous):
        super().__init__(name, salary)
        self.bonous = bonous

    def total_salary(self):
        print("Total salary :", self.salary + self.bonous)

print("Employee :")
name = input("Enter name :")
salary = int(input("Enter salary :"))
emp = Employee(name,salary)
emp.total_salary()

print("Manager :")
name = input("Enter name :")
salary = int(input("Enter salary :"))
bonous = int(input("Enter bonous :"))
manager = Manager(name,salary,bonous)
manager.total_salary()