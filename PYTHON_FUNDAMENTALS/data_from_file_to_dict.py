with open("students.txt", "w") as file:
    file.write("Arpita:85\n")
    file.write("Rahul:67\n")
    file.write("Priya:92\n")
    file.write("Aman:78\n")

with open("students.txt","r") as file:
    items = []
    keys = []
    values = []
    dict = {}

    for line in file:
        items = line.split(":")
        for item in items:
            if items.index(item) % 2 == 0:
                keys.append(item)
            else:
                values.append(item)

    for key in keys:
        for value in values:
            if keys.index(key) == values.index(value):
                dict.update({ key : int(value.strip()) })
       
    print(dict)