import random

lst = [[random.randint(-100, 100) for i in range(100)] for _ in range(100)]
lst2 = []
result = 1

for i in lst:
    for j in i:
        if j == result:
            lst2.append(j)

# дз, написать логику чтоб создавались списки и и записывались каждые однотипные елементы в его список