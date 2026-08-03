def categorize(numbers):
    zero = []
    positive = []
    negative = []

    for num in numbers:
        if num == 0:
            zero.append(num)
        elif num < 0:
            negative.append(num)
        else:
            positive.append(num)

    print("ZEROS :",zero)
    print("NEGATIVE :",negative)
    print("POSITIVE :",positive)

numbers = [10, -5, 0, 7, -3, 0, 12, -8]
categorize(numbers)
