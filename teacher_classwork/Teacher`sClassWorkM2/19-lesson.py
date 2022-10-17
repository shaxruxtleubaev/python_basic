#1
"""box = []
for i in range(5):
    box.append('Азиза')
print(box)"""

#2
"""n = int(input('n: '))
box = list(range(n))
box_2 = ['Shaxzod' for i in range(n)]
print(box)
print(box_2)"""

#3
"""n = int(input('n: '))
mylist = [i for i in range(n)]
print(f'Список: {mylist} \nи длина списка {len(mylist)}')"""

#Заполняем список
"""box = []
for i in range(10):
    box.append(i)
print(box)
"""
#Находим четных чисел
"""try:
    odd_box = []
    for i in range(box):
        if box[i] % 2 != 0:
            odd_box.append(box[i])
    print(f'Нечетные числа: {odd_box}')
except TypeError:
    print('----------------------')
    generator_box = [i for i in range(10) if i % 2 != 0]
    print(generator_box)"""

"""import random 
box = [random.randint(-5,5) for i in range(5)]
print(box)
#print(f'{sorted(box)[::-1]}')
#box.reverse()
#print(box[::-1])
duplicate_box = []"""

# эквивалентно к set()
"""for i in box:
    if i not in duplicate_box:
        duplicate_box.append(i)
    else:
        print(box, end=' ')
print(f'\n{duplicate_box}')"""



"""for i in range(len(box)):
    if box[i] not in duplicate_box:
        duplicate_box.append(box[i])
print(f'Дубликаты: {duplicate_box} и длина его {len(duplicate_box)}')"""


#Ищем дублкаты
"""import random
box = [random.randint(-10,10) for i in range(10)]
duplicate_box = []
for i in range(len(box)):
    if box.count(box[i]) >= 2:
        duplicate_box.append(box[i])
print(f'До: {box} \nи дубликаты {duplicate_box} \nи количество дубликатов {len(duplicate_box)}')

#Удаляем дубликаты
remove_duplicate_box = []
for i in duplicate_box:
    if i not in remove_duplicate_box:
        remove_duplicate_box.append(i)
print(f'Вот список: {remove_duplicate_box}')

"""

#Указываем форму таблицы
n = int(input('n: '))
m = int(input('m: '))
print(f'Таблица: {n}x{m}')

#Заполняем таблицу
#1-версия если у вас всегда квадрат то есть 5x5 3x3 10x10
"""row = []
for i in range(n):
    row.append([0]*n)"""

#2-версия если у вас таблица в виде прямоугольника
row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

#Делаем операцию в лице заменителя
"""for i in range(len(row)):
    for j in range(len(column)):
        if i == j:
            row[i][j] = 5
        if i > j:
            row[i][j] = 4
        if i < j:
            row[i][j] = 3"""

for i in range(len(row)):
    for j in range(len(column)):
        if i <= n or j <= m:
            row[i][j] = 5
        if i == 0 or j == 0 :
            row[i][j] = 0
        if i == 3 or j == 3:
            row[i][j] = 0
#Попробуем найти сумму столбцов
for i in range(len(row)):
    summa = 0
    for j in range(len(column)):
        summa += row[i][j]

#Выводим результат
for i in row:
    print(i)

print(f'И сумма: {summa}')