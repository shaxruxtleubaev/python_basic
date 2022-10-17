import random

print('1.-----------------------------------------------------------------------------')
a = [random.randint(1, 5) for i in range(5)]
print(a)
print()

print('2.-----------------------------------------------------------------------------')
n = int(input('n: '))
b = list(range(n))
print(b)
print()

print('3.-----------------------------------------------------------------------------')
y = int(input('Enter number: '))
box = list()
for i in range(y):
    box.append(i)
print(box)
print()

print('4.-----------------------------------------------------------------------------')
k = list(random.randint(1, 10) for i in range(random.randint(1, 10)))
print(k)
print(f'Длина списка = {len(k)}')
print()

print('5.-----------------------------------------------------------------------------')
f = list(random.randint(1, 15) for i in range(random.randint(1, 10)))
print(f)
print(f'Сумма списка = {sum(f)}')
print()

from math import prod
print('6.-----------------------------------------------------------------------------')
f = list(random.randint(1, 15) for i in range(random.randint(0, 5)))
print(f)
print(f'Произведение списка = {prod(f)}')
print()

print('7.-----------------------------------------------------------------------------')
v = [random.randint(1, 100) for i in range(random.randint(2, 12))]
print(f'До сортировки: {v}')
q = sorted(v)
print(f'После сортировки: {q}')
print()

print('8.-----------------------------------------------------------------------------')
x = [random.randint(1, 20) for i in range(random.randint(2, 10))]
print(f'До замены: {x}')
x.reverse()
print(f'После замены: {x}')
print()

print('9.-----------------------------------------------------------------------------')
w = list(random.randint(1, 20) for i in range(random.randint(2, 4)))
print(f'До добавления дубликации: {w}')
r = -1
for i in range(len(w)*5):
    r += 1
    w.append(w[r])
print(f'После добавления дубликации: {w}')
print()

print('10.-----------------------------------------------------------------------------')
c = [random.randint(1, 20) for i in range(random.randint(2, 10))]
print(f'До удаления дубликатов: {c}')
print(f'После удаления дубликатов: {set(c)}')







