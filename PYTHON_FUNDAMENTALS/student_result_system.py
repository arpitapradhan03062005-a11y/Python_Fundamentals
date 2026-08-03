students = {
    "Arpita": [85, 78, 92],
    "Rahul": [65, 72, 68],
    "Priya": [92, 88, 95],
    "Aman": [35, 42, 38]
}

top_student = ""
highest_average = 0

for key,value in students.items():

    print(key)

    total = sum(value)
    print("Total : ",total)

    average = sum(value)/len(value)
    print("Average : ",average)

    if average >= 90:
        print("Grade : A")
        print("Result : PASS")
    elif average >= 80:
        print("Grade : B")
        print("Result : PASS")
    elif average >= 70:
        print("Grade : C")
        print("Result : PASS")
    elif average >= 60:
        print("Grade : D")
        print("Result : PASS")
    else:
        print("Result : FAIL")

    if average > highest_average:
        highest_average = average
        top_student = key

print("Top Student :",top_student)
print("Highest Marks :",highest_average)
    

