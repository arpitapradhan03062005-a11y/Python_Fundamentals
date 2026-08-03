def function(numbers):
    # Remove duplicates
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)

    # Find smallest and second smallest
    smallest = unique[0]
    second_smallest = unique[0]

    for num in unique:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num > smallest and num < second_smallest:
            second_smallest = num
    return second_smallest

numbers = [45, 12, 78, 3, 89, 12, 34]
print(function(numbers))