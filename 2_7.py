digit1, digit2 = map(int, input().split())
array = []
for i in range(digit1):
    array.append([])
    for j in range(0, digit2):
        array[i].append(i*j)
print(array)
