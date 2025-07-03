mtx = [[8, 3, 2, 3, 3],
       [1, 9, 8, 7, 1],
       [6, 6, 4, 9, 4],
       [9, 10, 4, 8, 3],
       [4, 7, 6, 2, 4]]
mtx2 = [[8, 1, 5, 1, 2],
        [1, 10, 10, 2, 1],
        [3, 8, 9, 5, 3],
        [6, 4, 4, 2, 10],
        [10, 3, 2, 2, 8]]
mtx3 = []

for i, j in zip(mtx, mtx2):
    row_result = []
    for row, row2 in zip(i, j):
        row_result.append(row + row2)
    mtx3.append(row_result)
print (mtx3)

max_el = 0
min_el = mtx3[0][0]

for i in mtx3:
    for j in i:
        if max_el < j:
            max_el = j
        
        if min_el > j:
            min_el = j

print(max_el, min_el) # закинуть в еще 1 матрицу
# вычеслить среднее арифметичное последней матрицы