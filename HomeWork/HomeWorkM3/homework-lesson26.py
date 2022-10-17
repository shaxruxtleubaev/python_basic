import random

print('Proc2-----------------------------------------------------------------------------')
def Power234(A, B, C, D):
    for i in range(3):
        print(pow(A, 2), pow(A, 3), pow(A, 4))
        print(pow(B, 2), pow(B, 3), pow(B, 4))
        print(pow(C, 2), pow(C, 3), pow(C, 4))
        print(pow(D, 2), pow(D, 3), pow(D, 4))
        break
    return A, B, C, D
print(Power234(2, 3, 4, 5))
print()

print('Proc4-----------------------------------------------------------------------------')
a = int(input('a: '))
a1 = int(input('a1: '))
a2 = int(input('a2: '))
def TrianglePS(int):
    P = 3 * int
    S = pow(int, 2) * pow(3, 0.5) / 4
    return P, S
print(TrianglePS(a))
print(TrianglePS(a1))
print(TrianglePS(a2))
print()

print('Proc6-----------------------------------------------------------------------------')
C1 = []
C2 = []
C3 = []
C4 = []
C5 = []
K1 = int(input('K1: '))
K2 = int(input('K2: '))
K3 = int(input('K3: '))
K4 = int(input('K4: '))
K5 = int(input('K5: '))
def DigitCountSum(int, list):
    for i in range(int):
        list.append(i)
    S = sum(list)
    return list, S
print(DigitCountSum(K1, C1))
print(DigitCountSum(K2, C2))
print(DigitCountSum(K3, C3))
print(DigitCountSum(K4, C4))
print(DigitCountSum(K5, C5))
print()

print('Proc8-----------------------------------------------------------------------------')
K = int(input('K: '))
D = int(input('D in range 0-9: '))
def AddRightDigit(K, D):
    D1 = K+D
    D2 = K + D1
    return D1, D2
print(AddRightDigit(K, D))
print()

print('Дом задания!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()

print('1.---------------------------------------------------------------------')
x = int(input('x: '))
y = int(input('y: '))
def numbers(x, y):
    a = x + y
    return f'{x} + {y} = {a}'
print(numbers(x, y))
print()

print('2.---------------------------------------------------------------------')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
def raznost(x, y, z):
    p = x - y - z
    return f'{x} - {y} - {z} = {p}'
print(raznost(x, y, z))

# a = 5                              #Альтернатива на анонимном функции
# b = 3
# c = 1
# minus_2 = lambda: a - b - c
# print(minus_2())
#
# minus_3 = lambda a, b, c: a - b - c
# print(minus_3(5, 3, 1))
print()

print('3.---------------------------------------------------------------------')
box = [random.randint(1, 10) for i in range(random.randint(5, 25))]
print(box)
def count_box(list):
    countt = len(list)
    return countt
print(count_box(box))
print()

print('4.---------------------------------------------------------------------')
box = [random.randint(1, 10) for i in range(random.randint(1, 10))]
print(box)
def summ_box(list):
    summ = sum(box)
    return summ
print(summ_box(box))
print()

print('5.---------------------------------------------------------------------')
box = [random.randint(1, 10) for i in range(random.randint(5, 15))]
box.sort()
print(box)
def cont_box(list):
    bin = []
    for i in range(len(list)-1):
        if box.count(box[i]) >= 2:
            bin.append(list[i])
    return bin
print(f'Повторяющиеся элементы = {cont_box(box)}')
print()

print('6.---------------------------------------------------------------------')
def dict(**kwargs):
    return kwargs
print(dict(name='Shakhrukh', surname='Tleubaev'))
print()

print('7.---------------------------------------------------------------------')
def args(*args):
    return args
print(args(1, 2, 3, 4, 5, 6, 7, 8))
print()

print('8.---------------------------------------------------------------------')
a = int(input('Enter even number a: '))
b = int(input('Enter even number b: '))
if a % 2 == 0 and b % 2 == 0:
    find_sum_numbers = lambda a, b: a+b
    print(f'{a} + {b} = {find_sum_numbers(a, b)}')
else:
    print('There are odd number')
print()

print('9.---------------------------------------------------------------------')
a = int(input('Enter odd number a: '))
b = int(input('Enter odd number b: '))
if a % 2 != 0 and b % 2 != 0:
    find_sum_numbers = lambda a, b: a+b
    print(f'{a} + {b} = {find_sum_numbers(a, b)}')
else:
    print('There are even number')
print()

print('10.---------------------------------------------------------------------')
n = int(input('n: '))
sostavnoy = []
prostoy = []
for i in range(1, n):
    score = 0
    for j in range(2, n):
        if i % j == 0:
            score += 1
            if score >= 2:
                sostavnoy.append(i)
            else:
                prostoy.append(j)
print(f'Составные числа: {set(sostavnoy)}')
print(f'Простые числа: {set(prostoy)}')

def summ(list):
    x = sum(list)
    return x
print(f'Сумма простых чисел: {summ(prostoy)}')
print(f'Сумма составных чисел: {summ(sostavnoy)}')
print()








































