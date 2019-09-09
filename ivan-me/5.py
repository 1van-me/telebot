lists=[["Коля", 14],["Дэни", 16],["Максим", 15]]
children=input("Введите имя и возраст ученика: ")
children=children.split(' ')
print(children) 
lists.append(children)
print(lists)
