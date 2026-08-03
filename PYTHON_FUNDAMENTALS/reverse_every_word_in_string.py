text = "Python is easy"

words = text.split()


r = ""

for word in words:
    reversed = ""
    for char in word:
        reversed = char + reversed
    r = r + reversed + " "

print(r)