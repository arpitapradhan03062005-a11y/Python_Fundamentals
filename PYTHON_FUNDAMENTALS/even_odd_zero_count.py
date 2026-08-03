def analyze(numbers):
    count_zero = 0
    count_even = 0
    count_odd = 0
    for num in numbers:

        if num == 0:
            count_zero += 1
        elif num % 2 == 0:
            count_even +=1
        else:
            count_odd += 1

    print("EVEN :",count_even)
    print("ODD :",count_odd,)
    print("ZERO :",count_zero)

numbers = [1,2,3,45,6,6,78,9,0,0]
analyze(numbers)
