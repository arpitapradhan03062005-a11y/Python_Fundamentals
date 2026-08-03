with open("data.txt", "w") as file:
    file.write("Python is easy.\n")
    file.write("I am learning Python.\n")
    file.write("Python is useful.\n")

with open("data.txt", "r") as file:
    count = 0
    for line in file:
        count += 1

print(count)    