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
        print('курьер доставил ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")


class Gruz(Transport):
    def __init__(self, product_name, length, weigth):
        self.product_name = product_name
        self.length = length
        self.weigh = weigh
    def dostavka(self):
        print('грузовик доставил ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")


class Fly(Transport):
    def __init__(self, product_name, length, weigth):
        self.product_name = product_name
        self.length = length
        self.weigh = weigh
    def dostavka(self):
        print('самолёт доставил ' + self.product_name + '; ' + "На расстояние: " + str(length) +'; '+"Весом: " + str(weigh)+";")

class money(Fly, Gruz, Kurer):
    def __init__(self, product_name, length, weigth):
        print("Стоимость: " + length*weigth)

product_name=input("Введите наименование товара: ")
length=int(input("Введите растояние: "))
weigh=int(input("Введите вес: "))    
user = User()
user.make_order(product_name, length, weigh)
trans = Transport()
trans.send_order(product_name, length, weigh)
#kurer = Kurer(product_name, length, weigh)
#kurer.dostavka()
fabric = Fabric()
#fabric.craft_order(43, 23,'eat')
