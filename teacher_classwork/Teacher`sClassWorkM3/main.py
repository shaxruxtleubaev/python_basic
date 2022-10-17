'''class Main():
    a = 5 
print(Main.a)

def main():
    a = 5 
    return a 
print(main())'''

#Класс делится на 3 -> Полиморфизм, Инкапсуляция, Наследование
"""class Main():

    app = [1,2,3,1,2,5,6,1]
    #Конструкторы
    def __init__(self,app):
        self.app = app
    def func(self):
        single = []
        for i in range(len(self)-1):
            if self[i] != self[i+1]:
                single.append(self[i])
        if self.count(self[-1]) < 2:
            single.append(self[-1])
        return single 
    a = func(app)
    with open('results.txt',mode='a') as file:
        file.write(f'\n{func(app)}')
        file.close()
"""
"""num = -50 
print(num.__add__(10))
print(num.__abs__())"""

"""class Animal:

    #Конструктор -> Характеристика
    def __init__(self,name,color,gender,age):
        
        self.name = name #Название
        self.color = color #Цвет
        self.gender = gender #Пол
        self.age = age #Возраст
    
    #Способности
    def isType(self):
        return f'{self.name} животное цвет {self.color} и возраст {self.age}'

    def isTakeFive(self):
        self.toys = ['Кости','Мяч','Палка']
        return f'{self.name} играет с {self.toys[1]}'"""

import math 
class Rectangle(object):

    def __init__(self, a,b):
        self.a = a 
        self.b = b 
 
    def square(self):
        S =  self.a * self.b
        return f'Площадь: {S}'
    
    def perimeter(self):
        P = 2*(self.a + self.b)
        return f'Периметр: {P}'

"""class Triangle(object):

    def __init__(self, a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
 
    def square(self):
        P = (self.a + self.b + self.c)/2
        S = math.sqrt(P*(P-self.a)*(P-self.b)*(P-self.c))
        return f'Площадь: {S}'
    
    def perimeter(self):
        P = (self.a + self.b + self.c)/2
        return f'Периметр: {P}'"""

class Triangle(Rectangle):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c  
        
    def square(self):
        P = (self.a + self.b + self.c)/2
        S = math.sqrt(P*(P-self.a)*(P-self.b)*(P-self.c))
        return f'Площадь: {S}'
    
    def perimeter(self):
        P = (self.a + self.b + self.c)/2
        return f'Периметр: {P}'
    
















