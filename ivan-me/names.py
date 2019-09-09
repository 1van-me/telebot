class Person():
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    def person(self):
        print(self.name+str(self.age))
person=Person("Имя", 16)
person.person()

