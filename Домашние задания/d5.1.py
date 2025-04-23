# Найти сумму елементов и поделить на их кол-во
# Список создать свой
# Задача написать свою логику

lst = [87389210, 98423032, 3489720, 4832940932]

summ = 0
quantity = 0

for i in lst:
    quantity += 1
    summ += i

arithmeticMean = summ / quantity
     
print("Кол-во елементов:", quantity)
print("Сумма елементов:", summ)

print("Среднее арифметичное:", arithmeticMean)