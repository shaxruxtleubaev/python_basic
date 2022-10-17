import random

print('Proc10-----------------------------------------------------------------------------')
A = int(input('Введите значение число A: '))
B = int(input('Введите значение число B: '))
C = int(input('Введите значение число C: '))
D = int(input('Введите значение число D: '))
print(A, B, C, D)

def Swap(A, B, C, D):
    A, B = B, A
    C, D = D, C
    B, C = C, B
    return A, B, C, D
print(f'После изменении значении: {Swap(A, B, C, D)}')
print()

print('Proc12-----------------------------------------------------------------------------')
def SortInc3(A, B, C):
    box = [A, B, C]
    box.sort()
    for i in range(len(box)):
        print(box[i], end=' ')

A = int(input('Введите значение число A: '))
B = int(input('Введите значение число B: '))
C = int(input('Введите значение число C: '))
print(f'До сортировки: {A, B, C}')
print(f'После сортировки: ')
SortInc3(A, B, C)
print()

A1 = int(input('Введите значение число A1: '))
B1 = int(input('Введите значение число B1: '))
C1 = int(input('Введите значение число C1: '))
print(f'До сортировки: {A1, B1, C1}')
print(f'После сортировки: ')
SortInc3(A1, B1, C1)
print()

A2 = int(input('Введите значение число A2: '))
B2 = int(input('Введите значение число B2: '))
C2 = int(input('Введите значение число C2: '))
print(f'До сортировки: {A2, B2, C2}')
print(f'После сортировки: ')
SortInc3(A2, B2, C2)
print()

print('Proc14-----------------------------------------------------------------------------')
def ShiftRight3(A, B, C):
    A, C = C, A
    B, C = C, B
    return A, B, C

A = int(input('Введите значение число A: '))
B = int(input('Введите значение число B: '))
C = int(input('Введите значение число C: '))
print(f'После правого циклического сдвига: {ShiftRight3(A, B, C)}')
print()
A1 = int(input('Введите значение число A1: '))
B1 = int(input('Введите значение число B1: '))
C1 = int(input('Введите значение число C1: '))
print(f'После правого циклического сдвига: {ShiftRight3(A1, B1, C1)}')
print()
A2 = int(input('Введите значение число A2: '))
B2 = int(input('Введите значение число B2: '))
C2 = int(input('Введите значение число C2: '))
print(f'После правого циклического сдвига: {ShiftRight3(A2, B2, C2)}')
print()

print('Proc16-----------------------------------------------------------------------------')
def sign(x, y):
    score_x = None
    score_y = None
    if x < 0:
        score_x = -1
    elif x == 0:
        score_x = 0
    elif x > 0:
        score_x = 1
    else:
        print('Ошибка при вводе! ')
    if y < 0:
        score_y = -1
    elif y == 0:
        score_y = 0
    elif y > 0:
        score_y = 1
    else:
        print('Ошибка при вводе! ')
    return score_x + score_y

A = int(input('Введите значение число A: '))
B = int(input('Введите значение число B: '))
print(sign(A, B))
print()

print('Proc18-----------------------------------------------------------------------------')
def Circle(R):
    S = 3.14 * pow(R, 2)
    return f'Площадь круга с радиусом {int(R)} = {S}'

R1 = float(input('Введите значение радиуса окружности R1: '))
print(Circle(R1))
R2 = float(input('Введите значение радиуса окружности R2: '))
print(Circle(R2))
print()

print('Proc20-----------------------------------------------------------------------------')
def TriangleP(a, h):
    b = (a/2)**2 + h**2
    P = 2*b +a
    return f'Периметр равнобедренного треугольника со стороной а = {int(a)} и высотой = {int(h)} это = {int(P)}'

a1 = float(input('Введите сторону а равнобедренного треугольника: '))
h1 = float(input('Введите высоту равнобедренного треугольника: '))
print(TriangleP(a1, h1))
print()
a2 = float(input('Введите сторону а равнобедренного треугольника: '))
h2 = float(input('Введите высоту равнобедренного треугольника: '))
print(TriangleP(a2, h2))
print()
a3 = float(input('Введите сторону а равнобедренного треугольника: '))
h3 = float(input('Введите высоту равнобедренного треугольника: '))
print(TriangleP(a3, h3))
print()

print('Proc22-----------------------------------------------------------------------------')
def Calc(A, B, Op):
    if Op == 1:
        return A - B
    if Op == 2:
        return A * B
    if Op == 3:
        return A / B
    else:
        return A + B

A1 = float(input('Введите значение A1: '))
B1 = float(input('Введите значение B1: '))
Op1 = int(input('Введите целым параметр Op1: 1 - вычитание, 2 - умножение, 3 - деление, остальные значения - сложение: '))
N1 = Calc(A1, B1, Op1)
print(f'N1 = {N1}')
print()
A2 = float(input('Введите значение A2: '))
B2 = float(input('Введите значение B2: '))
Op2 = int(input('Введите целым параметр Op2: 1 - вычитание, 2 - умножение, 3 - деление, остальные значения - сложение: '))
N2 = Calc(A2, B2, Op2)
print(f'N2 = {N2}')
print()
A3 = float(input('Введите значение A3: '))
B3 = float(input('Введите значение B3: '))
Op3 = int(input('Введите целым параметр Op3: 1 - вычитание, 2 - умножение, 3 - деление, остальные значения - сложение: '))
N3 = Calc(A3, B3, Op3)
print(f'N3 = {N3}')
print()

print('Proc24-----------------------------------------------------------------------------')
box = [random.randint(1, 30) for i in range(10)]
print(box)
def Even(K):
    score = []
    for i in range(len(box)):
        if K[i] % 2 == 0:
            score.append(True)
        elif K[i] != 0:
            score.append(False)
    return f'Кол-во четных чисел = {score.count(True)}'
print(Even(box))
print()

print('Proc26-----------------------------------------------------------------------------')
box = [random.randint(24, 30) for i in range(10)]
print(box)
def IsPower5(K):
    score = []
    for i in range(len(box)):
        if pow(K[i], 0.5) == 5:
            score.append(True)
        else:
            score.append(False)
    return f'Кол-во степеней числа 5 = {score.count(True)}'
print(IsPower5(box))
print()

print('Proc28-----------------------------------------------------------------------------')
box = [random.randint(2, 50) for i in range(10)]
print(box)
sostavnoy = []
prostoy = []
def IsPrime(N):
    for i in range(1, 50):
        score = 0
        for j in range(2, 50):
            if i % j == 0:
                score += 1
                if score >= 2:
                    sostavnoy.append(i)
                else:
                    prostoy.append(j)
    score_2 = 0
    for l in range(len(N)):
        if N[l] in prostoy:
            score_2 += 1
    return f'Кол во простых чисел = {score_2}'
print(IsPrime(box))
print()

print('Proc30-----------------------------------------------------------------------------')

print('Proc32-----------------------------------------------------------------------------')
def DefToRoad(D):
    R = (D * 3.14) / 180
    return f'{D} градусов будет {R} радиан'
D1 = int(input('Введите градус D1 (0 < D1 < 360): '))
print(DefToRoad(D1))
D2 = int(input('Введите градус D2 (0 < D2 < 360): '))
print(DefToRoad(D2))
D3 = int(input('Введите градус D3 (0 < D3 < 360): '))
print(DefToRoad(D3))
D4 = int(input('Введите градус D4 (0 < D4 < 360): '))
print(DefToRoad(D4))
D5 = int(input('Введите градус D5 (0 < D5 < 360): '))
print(DefToRoad(D5))
print()

print('Proc34-----------------------------------------------------------------------------')
def Fact(N):
    score = 1
    for i in range(1, N):
        score *= i
    return score
N = int(input('Введите число N > 0 чтобы найти его факториал: '))
print(f'Факториал числа {N} = {Fact(N)}')
print()

print('Proc36-----------------------------------------------------------------------------')
def Fib(N):
    A, B = 1, 1
    for i in range(N-2):
        A, B = B, A + B
    return B
N1 = int(input('Введите N1-й элемент последовательности фибоначчи: '))
print(Fib(N1))
N2 = int(input('Введите N2-й элемент последовательности фибоначчи: '))
print(Fib(N2))
N3 = int(input('Введите N3-й элемент последовательности фибоначчи: '))
print(Fib(N3))
N4 = int(input('Введите N4-й элемент последовательности фибоначчи: '))
print(Fib(N4))
N5 = int(input('Введите N5-й элемент последовательности фибоначчи: '))
print(Fib(N5))
print()






































