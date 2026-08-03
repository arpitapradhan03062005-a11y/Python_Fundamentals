students = {
    "Arpita": [85, 78, 92],
    "Rahul": [65, 72, 68],
    "Priya": [92, 88, 95],
    "Aman": [35, 42, 38],
    "Neha": [78, 82, 80]
}

top_student = ""
highest_average = 0
pass_count = 0
fail_count = 0

for key,value in students.items():
    print(key)
    average = sum(value)/len(value)
    print("Total :",average)
    if average >= 90:
        print("Grade : A")
        print("Result : PASS")
        pass_count += 1
    elif average >= 80:
        print("Grade : B")
        print("Result : PASS")
        pass_count += 1
    elif average >= 70:
        print("Grade : C")
        print("Result : PASS")
        pass_count += 1
    elif average >= 60:
        print("Grade : D")
        print("Result : PASS")
        pass_count += 1
    else:
        print("Result : FAIL")
        fail_count += 1


    if average > highest_average:
        highest_average = average
        top_student = key 

print("Top Student :",top_student)
print("Highest average :",highest_average)

print("Passed :",pass_count)
print("Failed :",fail_count)



