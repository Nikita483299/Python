
lst = [2, 'hsdjkfh34235', 4589, '8ghw89g4h2', 'sjhjdk']
lst2 = []

for i in lst:
    if type(i) == str:
        for j in i: # Работает только с строкой, с int не работает
            if j.isdigit(): # отдает да или нет (если в елементе есть число (даже в списке) )
                lst2.append(j)

print(lst2)

