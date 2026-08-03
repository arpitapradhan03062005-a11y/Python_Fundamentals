from datetime import datetime 

birth_year = int(input("Enter you birth year :"))

current_year = datetime.now().year

age = current_year - birth_year

print("Your age is :",age)