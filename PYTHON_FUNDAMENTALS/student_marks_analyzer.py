students = {
    "Arpita": [78, 85, 90],
    "Rahul": [65, 72, 68],
    "Priya": [92, 88, 95]
}

top_Student = ""
highest_average = 0
for key,value in students.items():
    average = sum(value)/len(value)
    print(key,average)

    if average > highest_average:
        highest_average = average
        top_Student = key

print("TOP STUDENT :",top_Student)
print("HIGHEST AVERAGE :",highest_average)

