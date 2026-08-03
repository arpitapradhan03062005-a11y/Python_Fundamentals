def remove_duplicates(numbers):
    unique = []
    duplicates = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
        elif num not in duplicates:
            duplicates.append(num)

    return duplicates

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
duplicates = remove_duplicates(numbers)
print(duplicates)

