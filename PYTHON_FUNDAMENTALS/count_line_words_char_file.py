with open("data.txt", "w") as file:
    file.write("Python is easy\n")
    file.write("I am learning Python\n")

with open("data.txt", "r") as file:
    line_count = 0
    word_count = 0
    char_count = 0
    words = []
    char = []

    for line in file:
        line_count += 1
        words = line.split(" ")
        print(words)
        for word in words:
            char = list(word.strip())
            print(char)
            char_count += len(char)
        word_count += len(words)

print("Lines :",line_count)
print("Words :",word_count)
print("Characters :",char_count)



