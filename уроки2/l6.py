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

a = len(mtx)

for row, row2 in zip(mtx, mtx2):
    row_result = []
    for i, y in zip(row, row2):
        row_result.append(i/y)
    mtx3.append(row_result)

print(mtx3)