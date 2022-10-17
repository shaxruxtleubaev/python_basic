#Характеристика машины
class Cars:
    #Конструктор 
    def __init__(self, name, color, types, driver):
        #Создаем переменные 
        self.name = name 
        self.color = color 
        self.types = types
        self.driver = driver  
    #Скорость машины
    def cars_speed(self):
        #Скорость 
        self.all_cars = []
        self.types = f'The car {self.name} is coming with driver {self.driver}'
        self.all_cars.append(self.types)
        return self.all_cars
    #Данные о водителе
    #def drivers_info(self):
    #   self.driver_information = {}
    #    self.driver_information['name'] = self.driver 
    #    self.driver_information['types'] = self.types 
    #    return self.driver_information 
    def drivers_matches(self,driver_name):
        self.cars_speed = {
            driver_name : self.cars_speed(),
        }
        return self.cars_speed 

first_player = Cars('audi','white','sport car','Alibek')
second_player = Cars('bmw','black','sport car','Ismail')
#print(first_player.drivers_matches('Alibek'))
#print(second_player.drivers_matches('Ismail'))

#Наследование 
class Parent:
    def __init__(self, name, age, isWork, isStudy):
        self.name = name 
        self.age = age 
        self.isWork = isWork 
        self.isStudy = isStudy  
    def leavemessage(self):
        return f'Hi {self.name} your age is {self.age} and you are working\
            is {self.isWork} or studying is {self.isStudy}!'
father = Parent('Father',43,True,False)
#print(father.leavemessage())
class Child(Parent):
    def __init__(self,name,age,isWork,isStudy):
        super().__init__(name,age,isWork,isStudy)
    def isPlay(self):
        return f'Child is {self.name} and playing with guitar'
daughter = Child('Daughter',15,False,True)
#print(daughter.leavemessage())
#print(daughter.isPlay())
class Numbers:

    def __iter__(self):
        self.number = 1 
        return self 
    
    def __next__(self):
        if self.number <= 5:
            x = self.number 
            self.number += 2 
            return x 
        else:
            raise StopIteration

first_number = Numbers()
first_iter = iter(first_number)

print(next(first_iter))
print(next(first_iter))
print(next(first_iter))
print(next(first_iter))
print(next(first_iter))








