print() # Отступ

# Логин, пароль
login = "nikita" # Логин
password = 12345678 # Пароль

userLogin = input("Логин: ") # Ввод логина
userPassword = int(input("Пароль: ")) # Ввод пароля

if userLogin == login: # Если введенный логин = логину
    if userPassword == password: # Если введенный пароль = паролю
        print("Вы вошли") # Вывод текста
    else:
        print("Неверный пароль.") # Вывод текста
else:
    print("Указанного вами пользователя не существует.") # Вывод текста