def testFunc():
    print("Использована функция testFunc()")

testFunc()

print()

def testFunction(a, b):
    print(a ** b) # ** это степень (а в степени б то есть а^b ответ этой степени будет)

testFunction(3, 2)

print()

def simple_func(name, age):
    print(f"name = {name}\nage = {age}")
simple_func('Tom', 12)
# Если на оборот то можно написать simple_func(name='Tom', age=12)