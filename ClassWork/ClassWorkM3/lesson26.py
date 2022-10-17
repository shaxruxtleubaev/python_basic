import random

# Функция -> Functions

# Функция -> Публичный и Приватный

# def print_all():      # Функция создается
#     print('Шахзод')   # Содрежимое
# print_all()           # Вывод
#
# def find_me():
#     name = input('Напиши своё имя: ')
#     print(name)
# print(find_me())

# def total():        # Без аргумента
#     a = 5
#     b = 3
#     return a + b
# print(total())
#
# def total_summ(a, b):  # С аргументом
#     return a + b
# print(total_summ(5, 3))
'''
import random

def box_of_numbers(n):
    box = list()
    for i in range(n):
        box.append(random.randint(-100, 100))
    return box
#print(box_of_numbers(50))
numbers = box_of_numbers(10)
print(numbers)
#print(sorted(numbers))

def sort_of_numbers(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list
#print(sort_of_numbers(numbers))
box = [random.randint(-100, 100) for i in range(20)]
print(box)
print(sort_of_numbers(box))

def summ_of_numbers(list):
    score = 0
    for i in range(len(list)):
        score += list[i]
    return score
print(summ_of_numbers(box))'''

'''print('1.-----------------------------------------------------------------------')
def funkcia(list):
    name = input('Name: ')
    surname = input('Surname: ')
    third_name = input('Third name: ')
    a = [name, surname, third_name]
    return a
print(funkcia(list))

print('2.-----------------------------------------------------------------------')
def sth(list):
    box = list()
    for i in range(3):
        box.append(random.randint(1, 100))
    print(box)
    return sum(box)
print(sth(list))
print()

print('3.-----------------------------------------------------------------------')
def total():
    box = list(random.randint(1, 50) for i in range(10))
    print(box)
    box_2 = list()
    for i in range(len(box)):
        if box[i] % 2 == 0:
            box_2.append(box[i])
    return box_2
print(total())

print('4.-----------------------------------------------------------------------')
def qwe(list):
    box_x = [random.randint(1, 50) for i in range(10)]
    print(box_x)
    box_y = list()
    for i in range(len(box_x)):
        if box_x[i] % 5 == 0 or box_x[i] % 6 == 0:
            box_y.append(box_x[i])
    return box_y
print(qwe(list))'''

# *args, **kwargs ->
'''def numbers(a, b, c, d, e, f):
    return a, b, c, d, e, f
print(numbers(1, 2, 3, 4, 5, 6))

def numbers(*sanlar):
    return sanlar
print(numbers(1, 2, 3, 4, 5, 6))

def biography(**kwargs):
    return kwargs
print(biography(name='Shaxrux', surname='Murtazaev'))

def auto():
    hello = dict()
    hello['name'] = 'Shaxrux'
    hello['surname'] = 'Tleubaev'
    return hello
print(auto())'''

'''try:
    def numbers(list):
        list.append(10)
        return list
    print(numbers())
except TypeError:
    print('Вы забыли аргумент')
except AttributeError:
    print('Нельзя так делать!')'''


# Приватная функция(Анонимная)
'''def sayHi():
    return 'Hello'


print(sayHi())

sayHi = lambda: 'Привет'
print(sayHi())


def find_sum_of_two_numbers(a, b):
    return a + b


print(find_sum_of_two_numbers(10, 15))

find_sum_numbers = lambda a, b: a + b
print(find_sum_numbers(30, 25))
'''



























