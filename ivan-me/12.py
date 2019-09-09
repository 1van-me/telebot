spisok=[["qwerty", "12345"]]
while True:
    answer=input("Введите команду: ")
    if answer=="войти":
        user=enter(spisok)
        if user==True:
            print:("Вход выполнен")
        elif user==False:
            print:("Ошибка входа")
    elif answer=="выход":
        exit()
    elif answer=="вход":
        newuser=[]