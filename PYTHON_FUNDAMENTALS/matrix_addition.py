matrix1 = [
    [1,2],
    [3,4]
]

matrix2 = [
    [5,6],
    [7,8]
]

m1 = []
for row in matrix1:
    for num in row:
        m1.append(num)
print(m1)

m2 = []
for row in matrix2:
    for num in row:
        m2.append(num)
print(m2)

result = []
for i in m1:
    for j in m2:
        if m1.index(i) == m2.index(j):
            result.append(i+j)

print(result)



