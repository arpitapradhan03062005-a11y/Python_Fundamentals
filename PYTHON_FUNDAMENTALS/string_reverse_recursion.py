def reverse_string(text):
    if len(text) == 0:
        return ""
    else:
        return text[-1] + reverse_string(text[:-1])

text = input("Enter text :")
print(reverse_string(text))
