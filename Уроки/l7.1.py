dct = {
    'a': 34567,
    'b': 45678,
    'c': 654,
    'd': 45,
    'e': 'text'
}

arithmeticMean = 0

for i in dct.values():
    if type(i) == int:
        arithmeticMean += i
print(arithmeticMean / len(dct.values()))
# for i in dct.values():
#     if type(i) == int:
#         print(i)


