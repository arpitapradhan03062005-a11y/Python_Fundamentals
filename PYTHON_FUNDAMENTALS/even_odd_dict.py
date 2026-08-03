numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_odd = {
    "even" : [],
    "odd" : []
}

for item in numbers:
    if item % 2 == 0:
        even_odd["even"].append(item)
    else:
        even_odd["odd"].append(item)

print(even_odd)
