data=["sdgg", "123"]
while True:
    answer=input("Введите команду: ")
    if answer=="логин":
        user=enter()
        if user==True:
            print("Вход выполнен")
    elif answer=="выход":
        exit()
    elif answer=="вход":
        newuser=[]
        while True:
            user=input("Введите имя пользователя: ")
            for i in data:
                if i [data]==user:
                    print("Неправильный логин или пароль ")
                elif answer=="выход":
                    exit()
                ex=True
            if ex==False:
                newuser.append(user)