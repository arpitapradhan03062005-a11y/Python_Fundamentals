def remove_duplicates(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
print(remove_duplicates(numbers))