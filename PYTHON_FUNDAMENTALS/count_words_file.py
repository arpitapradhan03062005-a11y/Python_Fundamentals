with open("data.txt", "w") as file:
    file.write("Python is easy.\n")
    file.write("I am learning Python.\n")

with open("data.txt", "r") as file:
    count = 0
    words = []
    for line in file:
        words = line.split()
    
        for word in words:
            count += 1

    print(count)