"""from main import Main

app = [1,2,3,1,2,5,6,1]
first_object = Main(app) #Вызов класса 
print(first_object.a)

print(dir(int))"""

"""from main import Animal as a

tiger = a('Тигр','Желтый','Мужчина',5)
dog   = a('Собака','хаски','мужчина',10)
print(tiger.isType())
print(f'{dog.isType()} играет с {dog.isTakeFive()}')
"""
from main import Rectangle 
from main import Triangle

rectangle = Rectangle(3,4)
print(rectangle.square())
print(rectangle.perimeter())

triangle = Triangle(3,4,5)
print(triangle.square())
print(triangle.perimeter())

#Наследование 
