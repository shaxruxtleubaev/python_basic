'''
a = 0
b = 20
while a < b:
    a += 5
    print(a)
print()

a = 0
b = 20
c = 0
while a < b:
    a += 1
    c += a
    print(c)
print()

a = 0
b = 20
c = 1
while a < b:
    a += 1
    c *= a
    print(c)
print('----------------------------------------------------------------------------------------------------------------')

print('For1(While)')
K = int(input('Введите число: '))
N = int(input('Введите целое число >0: '))
a = 0
while a < N:
    a += 1
    print(K, end=' ')
print()

print('For2(While)')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое число В>A: '))
A1 = A-1
N = 0
while A1 < B:
    N += 1
    A1 += 1
    print(A1, end=' ')
print(f'Кол-во = {N}')
print()

print('For3(While)')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое число В>A: '))
N = 0
while B > A+1:
    N += 1
    B -= 1
    print(B, end=' ')
print(f'Кол-во = {N}')
print()

print('For4(While)')
cost = int(input('Введите цену 1 кг конфета: '))
A = 1
B = 10
while A < B:
    A += 1
    print(f'{A} кг конфет = {cost*A}')
print()

print('For5(While)')
cost = int(input('Введите цену 1 кг конфета: '))
A = 0
B = 10
while A < B:
    A += 1
    print(f'{A/10} кг конфет = {(cost*A)/10}')
print()

print('For6(While)')
cost = int(input('Введите цену 1 кг конфета: '))
A = 10
B = 20
while A < B:
    A += 2
    print(f'{A/10} кг конфет = {(cost*A)/10}')
print()

print('For7(While)')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое число В>A: '))
q = A
while q < B:
    q += 1
    A += q
    print(A)
print()

print('For8(While)')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое число В>A: '))
q = A
while q < B:
    q += 1
    A *= q
    print(A)
print()
'''






