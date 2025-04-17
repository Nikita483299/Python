lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Список от 1 до 10 и буква t

count_p = 0
count_n_p = 0

for i in lst:
    if i % 2 == 0:
        count_p += 1
    else:
        count_n_p += 1

print("Кол-во парных чисел:", count_p)
print("Кол-во непарных чисел:", count_n_p)