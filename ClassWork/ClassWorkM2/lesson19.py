import random
from itertools import count
#
# box = [random.randint(-5, 5) for i in range(5)]
# print(box)
# print(f'{sorted(box)[::-1]}')
# # box.reverse()
# print(box[::-1])


# # Ищем дубликаты
# box = [random.randint(-10, 10) for i in range(10)]
# dublicate_box = []
# for i in range(len(box)):
#     if box.count(box[i]) >= 2:
#         dublicate_box.append(box[i])
# print(f'До: {box} \nДубликаты {dublicate_box} \nКол-во дубликатов {len(dublicate_box)}')
#
# # Удаляем дубликаты
# remove_dublicate_box = []
# for i in dublicate_box:
#     if i not in remove_dublicate_box:
#         remove_dublicate_box.append(i)
# print(f'Список: {remove_dublicate_box}')




# Указываем форму таблицы
n = int(input('n: '))
m = int(input('m: '))
print(f'Таблица: {n}x{m}')

# Заполняем таблицу
# 1-версия если у вас квадрат то есть 5х5 6х6 8х8
# row = []
# for i in range(n):
#     row.append([0]*n)

# 2-версия если у вас в виде прямоугольника
row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

# Делаем операцию в виде заменителя
for i in range(len(row)):
    for j in range(len(column)):
        if i == j:
            row[i][j] = 5
        if i > j:
            row[i][j] = 4
        if i < j:
            row[i][j] = 3

#  Попробуем найти сумму столбцов
for i in range(len(row)):
    summa = 0
    for j in range(len(column)):
        summa += row[i][j]

# Выводим результат
for i in row:
    print(i)

print(f'И сумма {summa}')





















