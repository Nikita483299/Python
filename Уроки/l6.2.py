
dct = { # Ключ(переменная) значение(значение переменной) типа a = 1
    'a': 1, # место = тут пишеться : а потом значнеие
    'b': 2,
    'c': 3,
    'd': 4
}

print("Список ключей")

print(dct.keys()) # Даст список с ключами

for i in dct.keys():
    print(i) # keys выводит только ключи (первое)

print("Значения")

print(dct.values()) # Даст список с значениями

for i in dct.values():
    print(i) # values выводит только значения (второе)

print()

for i in dct.items():
    print(i)

# Выдаст вот это (25, 26)
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)
# Выдает и ключи и значения (тип данных кортеж)