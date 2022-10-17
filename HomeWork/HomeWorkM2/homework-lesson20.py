import random
from itertools import count

print('Array18-----------------------------------------------------------------------------')
A = [random.randint(1, 100) for i in range(11)]
print(A)
print(f'A10 = {A[10]}')
for i in range(len(A)):
    if A[i] < A[10]:
        print(f'Первое число меньше {A[10]} = {A[i]}')
        break
    else:
        print(0)
        break
print()

print('Array19-----------------------------------------------------------------------------')
A = [random.randint(1, 100) for i in range(10)]
c = []
print(A)
for i in range(len(A)):
    if A[0] < A[i] < A[9]:
        c.append(A[i])
if len(c) == 0:
    print(0)
else:
    print(f'Самое последнее число больше {A[0]} и меньше {A[9]} это {c[-1]}')
print()

print('Array20-----------------------------------------------------------------------------')
N = int(input('Введите целое значение размера массива N: '))
K = int(input(f'Введите целое число, которое больше 1 и меньше {N}: '))
L = int(input(f'Введите целое число, которое больше {K} и меньше {N}: '))
j = [i for i in range(1, N)]
print(j)
print()
massiv = [i for i in range(1, N) if 1 <= K and K <= L and L <= N]
print(massiv[K-1:L])
print(f'Сумма данного массива = {sum(massiv[K-1:L])}')
print()

print('Array21-----------------------------------------------------------------------------')
N = int(input('Введите целое значение размера массива N: '))
j = [i for i in range(1, N+1)]
print(j)
print()
K = int(input(f'Введите целое число, которое больше 1 и меньше {N}: '))
L = int(input(f'Введите целое число, которое больше {K} и меньше {N}: '))
print()
massiv = [i for i in range(1, N) if 1 <= K and K <= L and L <= N]
print(massiv[K-1:L])
print(f'Среднее арифметическое этого массива = {(sum(massiv[K-1:L]))/len(massiv[K-1:L])}')
print()

print('Array22-----------------------------------------------------------------------------')
N = int(input('Введите целое значение размера массива N: '))
j = [i for i in range(1, N+1)]
print(j)
print()
K = int(input(f'Введите целое число, которое больше 1 и меньше {N}: '))
L = int(input(f'Введите целое число, которое больше {K} и меньше {N}: '))
print()
a = sum(j[:K-1])
b = sum(j[L:N])
print(f'Сумма чисел кроме чисел между {K} и {L} = {a+b}')
print()

print('Array23-----------------------------------------------------------------------------')
N = int(input('Введите целое значение размера массива N: '))
j = [i for i in range(1, N+1)]
print(j)
print()
K = int(input(f'Введите целое число, которое больше 1 и меньше {N}: '))
L = int(input(f'Введите целое число, которое больше {K} и меньше {N}: '))
print()
a = sum(j[:K-1])
b = sum(j[L:N])
mid_arifmetic = (a+b)/(len(j[:K-1])+len(j[L:N]))
print(f'Среденне арифметическое чисел, кроме чисел между {K} и {L} это = {mid_arifmetic} ')
print()

print('1.')
n = 3
m = 3
print(f'Таблица: {n}x{m}')

row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

for i in range(len(row)):
    for j in range(len(column)):
        if i == 0 or j == 0:
            row[0][j] = 1
            row[1][j] = 2
            row[2][j] = 3

for i in row:
    print(i)
print()

print('3.')
n = 3
m = 3
print(f'Таблица: {n}x{m}')

row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

for i in range(len(row)):
    for j in range(len(column)):
        if i == 0 or j == 0:
            row[i][0] = 0
            row[i][1] = 1
            row[i][2] = 2

for i in row:
    print(i)
print()

print('4.')
n = 3
m = 3
print(f'Таблица: {n}x{m}')

row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

for i in range(len(row)):
    for j in range(len(column)):
        if i >= 0 or j >= 0:
            row[i][j] = 1
            row[1][1] = 2
            
for i in row:
    print(i)
print()

print('5.')
n = 3
m = 3
print(f'Таблица: {n}x{m}')

row = []
for i in range(n):
    column = []
    for j in range(m):
        column.append(0)
    row.append(column)

for i in range(len(row)):
    for j in range(len(column)):
        if i >= 0 or j >= 0:
            row[i][0] = 3
            row[i][1] = 2
            row[i][2] = 1
            
for i in row:
    print(i)
print()
















































