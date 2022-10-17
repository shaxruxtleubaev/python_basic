import random

'''class Main():
    a = 5
print(Main.a)

def Main():
    a = 5
    return a
print(main())
'''

#  Класс делится на 3 -> Полиформизм, Инкапсуляция, Наследование
'''
class Main():

    app = [1,2,3,1,2,5,6,1]
    # Конструкторы
    def __init__(self, app):
        self.app = app
    def func(self):
        single = []
        for i in range(len(self)-1):
            if self[i] != self[i+1]:
                single.append(self[i])
        if self.count(self[-1]) < 2:
            single.append(self[-1])
        return single
    a = func(app)'''

'''
class Animal:

    # Конструктор ->  Характеристика
    def __init__(self,name,color,gender,age):
        
        self.name = name        #Название
        self.color = color      #Цвет
        self.gender = gender    #Пол
        self.age = age          #Возраст
    
    #Способности
    def IsType(self):
        return f'{self.name} животное, цвет {self.color}, и возраст {self.age}'
    
    def IsTakeFive(self):
        self.toys = ['Кости', "Мяч", "Палка"]
        return f'{self.name} играет с {self.toys[1]}'
 '''   
















































