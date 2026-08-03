students = {
    "Arpita": 85,
    "Rahul": 67,
    "Priya": 92,
    "Aman": 48
}
found = False
name = input("Enter Student name :")
for key,value in students.items():
    if name.lower() == key.lower():
        print(f"{key}'s marks : {value}")
        found = True
        break
if not found :
    print("Student not found!")
      