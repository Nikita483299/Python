"""
Если а больше б то:
    вывести да (то есть а больше чем б)
Дополнительное условие, а меньше чем б:
    если (а + 1) меньше чем б:
        вывести а + 1 (сумму)
    вывести нет (то есть а не меньше чем б)
Иначе:
    вывести а = б (11 = 6)
"""


print()

a = 11
b = 6

if a > b:
    print(a > b)
elif a < b:
    if (a + 1) < b:
        print(a + 1)
    print(a < b)
else:
    print(a, "=", b)