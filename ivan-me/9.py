lists=[["Коля", 14],["Максим", 16],["Дима", 15]]
while True:
    child=input("Введите имя и возраст:")
    if child=="exit":
        break
    else:
        child=child.split(' ')
        lists.append(child)
while True:
    number=input("Ввидите номер ученика: ")
    if number=="end":
        if int(number)<= len(lists):
            print ("Имя" + lists[-1+int(number)][0])
            print ("Возраст" + lists[-1+int(nomber)][0])
        else:
            print("не верное число")
    else:
        print("конец") 
    break