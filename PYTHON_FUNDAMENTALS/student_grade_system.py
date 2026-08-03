

'''
90+ → A
75–89 → B
60–74 → C
40–59 → D
Below 40 → F
'''
def calculate_grade(key,value):
    
        if value >= 90:
            print(key," : A")
        elif value >= 75 and value <= 89:
            print(key," : B")
        elif value >= 60 and value <= 74:
            print(key," : C")
        elif value >= 40 and value <= 59:
            print(key," : D")
        else:
            print(key," : F")

students = {
    "Arpita": 85,
    "Rahul": 67,
    "Priya": 92,
    "Aman": 48
}

for key,value in students.items():
     calculate_grade(key,value)
