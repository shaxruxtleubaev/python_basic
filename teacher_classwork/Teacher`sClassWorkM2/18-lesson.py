# Структура данных 
# List, dict, tuple, set 
# Типы данных 
# integer, string, boolean, float 

"""name = 'Alisheriewtuiweiiuqwi'
print(name)
print(name.replace('i','y'))
print(name.count('i'))
print(len(name))"""

#Итератор
"""n = int(input('n: '))
box = []
for i in range(n):
    box.append(i)
print(box)"""

#Генератор
"""box_2 = list(range(n))
print(box_2)

box_3 = [i for i in range(n)]
print(box_3)"""

"""from itertools import count
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(0,10))
print(numbers)
odd_box = []    #нечетный
even_box = []   #четный
duplicates_box = [] #количество дубликатов!
sorted_box = sorted(numbers)

summa = 0
for i in range(len(sorted_box)-1):
    summa += numbers[i] 
    if sorted_box[i] % 2 == 0 and sorted_box[i] != 0:
        odd_box.append(numbers[i])
    if sorted_box[i] % 2 != 0:
        even_box.append(sorted_box[i])

print(f'Четные числа: {odd_box} и их сумма {sum(odd_box)}')
print(f'Нечетные числа: {even_box} и их сумма {sum(even_box)}')
print(f'Сумма: {summa}')
print(duplicates_box)

"""

"""import random 
box_2 = [random.randint(-10,10) for i in range(100)]
print(f'До сортировки: {box_2}')

#Bubble sort -> Сортировка пузырком!
for i in range(len(box_2)):
    for j in range(len(box_2)-1):
        if box_2[j] > box_2[j+1]:
            box_2[j],box_2[j+1] = box_2[j+1], box_2[j]
print(f'После сортировки: {box_2}')"""
'''
box_2 = [i**4 for i in range(10)]
print(box_2)
box=list()
n=int(input('n: '))
for i in range(n):
    box.append(i)
print(box)
'''
'''n = int(input('n: '))
mylist = []
for i in range(n):
    mylist.append(n**2)
print(mylist)
for i in range(len(mylist)-1):
    if i % 3 == 0:
        print(mylist[i])
'''


n = int(input('n = '))
a = 0
b = 1
box = []
for i in range(n):
    a, b = b, a + b
    box.append(b)
print(box)








