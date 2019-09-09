from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config

Config.set('graphics','resizable', 0)
Config.set('graphics','width', 400)
Config.set('graphics','height', 500)


def enter():
    while True:
        answer=input("Введите имя пользователя и пароль: ")
        answer=answer.split(' ')
        if answer in data:
            print("Вы авторизованы ")
            return True
        else:
            print("Такого пользователя не существует ") 
        break


data=[["sdgg", "123"], ["qwerty", "123"]]

while True:
    answer=input("Введите команду: ")
    if answer=="вход":
        user=enter()
        if user==True:
            print("Вход выполнен")
    elif answer=="выход":
        exit()
    elif answer=="регистрация":
        newuser=[]
        while True:
            user=input("Введите имя пользователя: ")
            for i in data:
                if i[0]==user:
                    print("Неправильный логин или пароль ")
                elif answer=="выход":
                    exit()
                elif i[0]!=user:
                    answer=input("Введите пароль: ")
                    if answer=="выход":
                        exit()
                ex=True
            if ex==False:
                newuser.append(user)
  
    while True:    #заказы
        if answer=="заказ":
            class User():
                def make_order(self, product_name, length, weigh):
                    return [product_name, int(length), int(weigh)]
            class Fabric():
                def craft_order(self, length, weigh, p_n):
                    print("Fabric create "+p_n+ " weigh"+str(length))
                    return [p_n, length, weigh]

            class Transport(): 
                def send_order(self, p_n, length, weigth):
                    if length<30:
                        kurer = Kurer(product_name, length, weigh)
                        kurer.dostavka()
                    elif 30<length<300:
                        gruz = Gruz(product_name, length, weigh)
                        gruz.dostavka()
                    elif length>300:
                        fly = Fly(product_name, length, weigh)
                        fly.dostavka()


            class Kurer(Transport):
                def __init__(self, product_name, length, weigth):
                    self.product_name = product_name
                    self.length = length
                    self.weigh = weigh
                def dostavka(self):
                    print('курьер доставил: ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")


            class Gruz(Transport):
                def __init__(self, product_name, length, weigth):
                    self.product_name = product_name
                    self.length = length
                    self.weigh = weigh
                def dostavka(self):
                    print('грузовик доставил: ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")

            class Fly(Transport):
                def __init__(self, product_name, length, weigth):
                    self.product_name = product_name
                    self.length = length
                    self.weigh = weigh
                def dostavka(self):
                    print('самолёт доставил: ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")

            if answer=="выход":
                exit()    
            product_name=input("Введите наименование товара: ")
            length=int(input("Введите растояние: "))
            weigh=int(input("Введите вес: "))    
            user = User()
            user.make_order(product_name, length, weigh)
            trans = Transport()
            trans.send_order(product_name, length, weigh)
            exit()
 
    while True:    #Калькулятор
        if answer=="калькулятор":
            a=float(input("Введите число: "))
            print(a)
            b=float(input("Введите второе число: "))
            znack=input("Введите знак: ")
            if znack=="+":
                print(a+b) 
                break
            elif znack=="-":
                print(a-b)
                break
            elif znack=="*":
                print(a*b)
                break
            elif znack=="/":
                print(a/b)
                break

    while True:
        if answer=="калькулятор1":
            class CalculatorApp(App):
                def update_label(self):
                    self.label.text=self.formula
                def add_number(self, instance):
                    if self.formula=='0':
                        self.formula=""
                    self.formula+=str(instance.text)
                    self.update_label()
                def add_operation(self, instance):
                    # if self(instance, text)=="x":
                    #     self.formula+="+"
                    # else:
                    self.formula+=str(instance.text)
                    self.update_label()
                def culc_result(self, insance):
                    self.label.text=str(eval(self.label.text))
                    self.formula='0'
                def build(self):
                    self.formula='0'
                    boxlayout=BoxLayout(orientation='vertical', padding=25)
                    gridlayout=GridLayout(cols=4, spacing=3, size_hint=(1,.6))
                    self.label=Label(text='0', font_size=40, halign='right', valign='center', size_hint=(0,.4))
                    self.label.bind(size=self.label.setter('text_size'))
                    boxlayout.add_widget(self.label)
                    gridlayout.add_widget(Button(text='7',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='8',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='9',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='0',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='6',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='5',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='4',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='3',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='2',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='1',on_press=self.add_number))
                    gridlayout.add_widget(Button(text='+',on_press=self.add_operation))
                    gridlayout.add_widget(Button(text='-',on_press=self.add_operation))
                    gridlayout.add_widget(Button(text='*',on_press=self.add_operation))
                    gridlayout.add_widget(Button(text='/',on_press=self.add_operation))
                    gridlayout.add_widget(Button(text='=',on_press=self.culc_result))
                    boxlayout.add_widget(gridlayout)
                    return boxlayout

if __name__=="__main__":
    CalculatorApp().run()         

    while True:    #читать
        if answer=="читать":
            f=open("45.txt", "o")
            for line in f:
                user=line.split(' ')
                print(user)
    
    else:
        print("Такой команды не существует")
        exit()





    