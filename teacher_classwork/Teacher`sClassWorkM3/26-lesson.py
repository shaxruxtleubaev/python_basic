#Функция -> Functions 
#print(), list(), split(), replace(), append()

#Функция -> Публичный и Приватный

#Публичная функ-я -> def -> definition 
#Приватная функ-я -> lambda 

"""def print_all():      #Функция создается
    print('Шахзод')   #Содержимое
print_all()           #Вывод 

def find_me():
    name = input('Напиши свое имя: ')
    print(name)
print(find_me())"""

"""def find_summ():
    for i in range(10):
        print(f'{i}')
#print(find_summ())    
find_summ() """

"""def find_summ():
    list_ = []
    score = 0
    for i in range(10):
        score = i 
    list_.append(score)
    return list_

number = find_summ()
print(f'Сумма от 0 до 10 {number}')"""

"""def print_all():
    print('Hello')
print_all()"""

"""#Функция -> Публичный (аргументом и без аргумента)
def total():    #без аргумента
    a = 5 
    b = 3 
    return a + b 
print(total())

def total_summ(a,b):     #с аргументом
    return a + b 
print(total_summ(5,3))"""

"""import random
def box_of_numbers(n):
    box = list()
    for i in range(n):
        box.append(random.randint(-100,100))
    return box
#print(box_of_numbers(50))
numbers = box_of_numbers(10)
print(numbers)"""
#print(sorted(numbers))

"""def sort_of_numbers(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list 
#print(sort_of_numbers(numbers))
box = [random.randint(-100,100) for i in range(20)]
print(box)
print(sort_of_numbers(box))

def summ_of_numbers(list):
    score = 0 
    for i in range(len(list)):
        score += list[i]
    return score 

print(summ_of_numbers(box))
"""

# * , ** 
# *args, **kwargs -> 
"""def numbers(a,b,c,d,e,f):
    return a,b,c,d,e,f 
print(numbers(1,2,3,4,5,6))

def numbers(*sanlar):
    return sanlar 
print(numbers(1,2,3,4,5,6))

def biography(**kwargs):
    return kwargs 
print(biography(name='Atabek',surname='Murtazaev'))

def auto():
    hello = dict()
    hello['name'] = 'Atabek'
    hello['surname'] = 'Murtazaev'
    return hello 
print(auto())"""

"""try:
    def numbers(list):
        list.append(10)
        return list 
    print(numbers(10))
except TypeError:
    print('Вы забыли аргумент!')
except AttributeError:
    print('Нельзя так делать!')
"""

#Приватная функция(Анонимная)
"""def sayHi():
    return 'Hello'
print(sayHi())

sayHi = lambda: 'Привет'
print(sayHi())

def find_sum_of_two_numbers(a,b):
    return a+b 
print(find_sum_of_two_numbers(10,15))

find_sum_numbers = lambda a,b: a+b
print(find_sum_numbers(30,25))"""

#1 
b = []
import random
def powerA3(a,b):
    for i in range(a):
        c = random.randint(1,5)
        b.append(pow(c,3))
    return b 
print(powerA3(5,b))

#3
import math 
a_mean = list()
g_mean = list()
def mean(x,y, a_mean, g_mean):
    a_mean.append((x+y)/2)
    g_mean.append(math.sqrt(x*y))
    return f'{a_mean} - {g_mean}'
print(mean(8,2,a_mean, g_mean))



