students = {
    "Arpita": 85,
    "Rahul": 67,
    "Priya": 92
}

with open("students.txt", "w") as file:
    for key,value in students.items():
        file.write(f"{key}:{value}\n")
    
with open("students.txt", "r") as file:
    print(file.read())