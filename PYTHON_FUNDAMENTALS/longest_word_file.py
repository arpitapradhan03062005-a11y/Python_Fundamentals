with open("data.txt","w") as file:
    file.write("Python is powerful\n")
    file.write("Machine learning is interesting\n")
    file.write("Programming is useful\n")

with open("data.txt", "r") as file:
    longest_length = 0
    longest_word = ""
    for line in file:
        words = line.split(" ")
        for word in words:
            word = word.strip(".,?!")
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word


    print("Longest word :",longest_word)
    print("Length :",longest_length)