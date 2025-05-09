dct = {
    1: 2,
    2: 3,
    3: 4
}

dct2 = {}

for i in dct.values():
    if type(i) == int:
        dct2[i] = None

print(dct2)