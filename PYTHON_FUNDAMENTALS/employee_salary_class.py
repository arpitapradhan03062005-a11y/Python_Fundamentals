class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)

    def annual_salary(self):
        print("Annual Salary :",self.salary * 12)

name = input("Enter name :")
salary = int(input("Enter salary :"))
object = Employee(name,salary)
object.annual_salary()