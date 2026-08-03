def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            print(f"{target} found at index {i}")


numbers = [10, 25, 30, 45, 50]
target = 30
search(numbers,target)