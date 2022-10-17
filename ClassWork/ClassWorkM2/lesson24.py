import random

'''box = {1, 2, 3, 4, 5}             # -> set
box_1 = [1, 2, 3, 4, 5]           # -> list
box_2 = (1, 2, 3, 4, 5)           # -> tuple
box_3 = {0:1, 1:2, 2:3, 3:4, 4:5} # -> dict
# print(box, type(box))
import random
box = {1}
for i in range(10):
    box.add(random.randint(1,10))
print(box)

print({1,1,1,1,2,2,2,3,3,3})'''

'''box = {1, 2, 3, 4, 5}
box_2 = {6, 7, 8, 9, 10}
box.update(box_2)
print(box)

box.pop()     # Удаляет первый элемент
print(box)
box.remove(5) # Удаляет по значеню (Значение должно быть внутри set)
print(box)
box.discard(2) # Удаляет по значению (Значение необязательно быть внутри set,если его нет, то ничего не будет )
print(box)'''

# Различные команды
'''
numbers =  {1, 2, 3, 4, 5}
box = {2, 3, 4, 5, 6}

print(numbers.union(box))
print(numbers.intersection(box))
print(numbers.difference(box))
print(box.difference(numbers))
'''

print('1.-----------------------------------------------------------------------------')
n = int(input('n: '))
box = [random.randint(1, 10) for i in range(n)]
print(f'Box = {box}')
box_2 = tuple((random.randint(1, 10) for i in range(n)))
print(f'Box_2 = {box_2}')
print(set(box).difference(set(box_2)))
print(set(box_2).difference(set(box)))
print()

print('2.-----------------------------------------------------------------------------')
numbers = set()
for i in range(5):
    numbers.add(i**(5-i))
print(numbers, type(numbers)) 
print()

print('1.-----------------------------------------------------------------------------')
numbers_list = [random.randint(1, 10) for i in range(5)]
numbers_tuple = tuple(random.randint(1, 10) for i in range(5))
print(numbers_list)
print(numbers_tuple)
print(set(numbers_list).intersection(set(numbers_tuple)))
summa = sum(set(numbers_list).intersection(set(numbers_tuple)))
print(summa)
final_summa = {summa}
print(final_summa)
