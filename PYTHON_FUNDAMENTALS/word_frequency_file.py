with open("students.txt", "w") as file:
    file.write("python is easy\n")
    file.write("python is powerful\n")
    file.write("python is useful\n")

with open("students.txt","r") as file:
    words = []
    unique = []
    for line in file:
        words += line.split()
    print(words)

    #finding unique
    count = 0
    for word in words:
       if word not in unique:
           unique.append(word)
    print(unique)

    #finding frequuency
    for i in unique:
        count = 0
        for word in words:
            if i == word :
                count += 1
        print(i ,":", count)
