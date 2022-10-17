import random

print('1.')
boz = [random.randint(-100, 100) for i in range(2)]
print(boz)
print()

print('2.')
box = []
for i in range(1):
    box.append(input('Введите что нибудь: '))
print(box)
print()

print('3.')
qwe = ['something', 2, True]
print(qwe)
a = input('Введите что нибудь: ')
b = int(input('Введите индекс, куда нужно добавить значение: '))
for i in range(1):
    qwe.insert(b, a)
print(qwe)
print()

print('4.')
iop = [random.randint(0, 77) for i in range(5)]
print(iop)
for i in range(len(iop)):
    iop.append(random.randint(1, 77))
print(iop)
c = int(input('Введите индекс которого нужно удалить: '))
iop.pop(c)
print(iop)
m = int(input('Введите значение которого нужно удалить: '))
iop.remove(m)
print(iop)
print()

print('5.')
nt = []
for i in range(10):
    nt.append(i)
print(nt)
nt.clear()
nt = [random.randint(1, 77) for i in range(10)]
print(nt)
print()

print('6.')
ho = [i for i in range(1, 31)]
print(ho)
a = []
b = []
for i in range(len(ho)):
    if ho[i] % 2 == 0:
        a.append(i)
    else:
        b.append(i)
print(f'Нечетные числа: {a}')
print(f'Четные числа: {b}')
print()

print('7.')
N = int(input('N: '))
M = int(input('M: '))
row = []
for i in range(N):
    column = []
    for j in range(M):
        column.append(0)
    row.append(column)
for i in row:
    print(i)
print()

print('8.')
N = int(input('N: '))
M = int(input('M: '))
score = 0
row = []
for i in range(N):
    column = []
    for j in range(M):
        column.append(0)
        score += 1
    row.append(column)
for i in row:
    print(i)
print(f'Сумма строк = {score}')
print()

print('9.')
tee = (1, 2, 3, 4, 5)
print(tee)
print()

print('10.')
ki = (1, 3, 5, 3, 7)
print(ki)
print(f'Число 3 повторяется {ki.count(3)} раза')
print()

print('11.')
dictionary = {1: 'Шахрух', 2: 'Тлеубаев', 3: '15 лет'}
print(dictionary)
print()

print('12.')
mou = {0:'World', 1:'Hello'}
print(mou)
print(mou.keys())
print()

print('13.')
sett = {1, 3, 5, 7, 9}
print(sett)
sett.add(input('Введите что нибудь для добавления к set: '))
print(sett)
print()

print('14.')
set_1 = {1, 2, 3, 4, 5, 6, 7}
set_2 = {3, 4, 5, 6, 8, 9, 11}
print(set_1)
print(set_2)
print(f'Все одинаковые значения в этих множествах это: {set_1.intersection(set_2)}')
print()

print('15.')
a = {1}
b = {1}
c = {1}
for i in range(10):
    a.add(random.randint(1, 10))
    b.add(random.randint(1, 10))
    c.add(random.randint(1, 10))
print(a)
print(b)
print(c)
print(f'Разница первого множества от второго множества это: {a.difference(b)}')
print(f'Разница первого множества от тертьего множества это: {a.difference(c)}')
print()

print('16.')
spisok = [random.randint(1, 30) for i in range(4)]
kortej = (2, 29, 4, 7)
mnojestvo = {random.randint(1, 30) for i in range(4)}
print(spisok)
print(kortej)
print(mnojestvo)
a = mnojestvo.union(set(spisok))
b = a.union(set(kortej))
print(b)
print()

























