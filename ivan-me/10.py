login=123
pas=456
while True:
    answer=input("Введите имя пользователя: ")
    answer=answer.split(' ')
    if answer==login:
        print("Вы авторизованы")
    else:
        print("Такого пользователя не существует")

