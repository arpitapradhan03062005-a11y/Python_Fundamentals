def is_palindrome(str):
    reversed = ""
    for char in str:
        reversed = char + reversed

    if str == reversed :
        print("PALINDROME")
    else:
        print("NOT PALINDROME")

str = "Arpiipra"
is_palindrome(str.lower())