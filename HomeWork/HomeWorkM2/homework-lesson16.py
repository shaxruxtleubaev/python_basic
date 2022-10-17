'''
print('First task')
number = 0
while number < 98:
    number += 7
    print(number, end=' ')
print()

print('Second task')
number = 1
while number < 512:
    number *= 2
    print(number, end=' ')
print()

print('Third task')
N = int(input('Enter natural number >0: '))
y = 0
while y < N:
    y += 1
    a = pow(y,2)
    print(f'{y}^2 = {a}')
print()

print('Fourth task')
range = int(input('Enter range: '))
r = 1
g = 0
while r < range:
    r += 2
    g += r
print(f'Sum of all odd numbers = {g+1}')
print()

y = 0
while y < range:
    y += 1
    if y % 5 == 0:
        print(f'The number multiple to 5 is = {y}')
print()

h = 0
while h < range:
    h += 1
    if h % 3 == 0 and h % 10 == 0:
        print(f'The number multiple to 3 and 10 is = {h}')
print()

j = 0
while j < range:
    j += 1
    if j % 4 == 0 or j % 6 == 0:
        print(f'The number multiple to 4 or 6 is = {j}')
print()

print('Fifth task')
contribution = 1000                                                #contribution
cont  = 1000
R = int(input('Enter a percent between 0 and 25: '))               #percent for every months
total = 1100                                                       #total after some months
K = 0                                                              #months
S = None                                                           #total count of contribution
percent = (cont*R)/100
while contribution < total:
    contribution += percent
    K += 1
S = contribution
print(f'After {K} months, count of contribution surpasses {total}')
print(f'Finally count of contribution is {S}')
print()

print('Sixth task')
distance = 10                                    #km
dist = 10
final_distance = 200
p = int(input('Enter a percent between 0 and 50: '))
Sum = None
k = 0
perc_of_dist = (distance * p)/100
while distance < final_distance:
    distance += perc_of_dist+distance
    k += 1
Sum = distance
print(f'After {k} days sportsman surpasses 200 km')
print(f'Summary of passed distance is {Sum}')
print()
'''

print('1.')
a = int(input('Введите положительное целое число: '))
h = 0
while h < a:
    h += 1
    g = pow(h, 2)
    print(f'{h}^2 = {g}')
print()

print('2.')
t = int(input('Введите положительное целое число: '))
k = 0
while k < t:
    k += 1
    if t % k == 0 and k != 1:
        print(f'Наименьший делитель числа {t} это {k}')
        break
print()

print('3.')
n = 2
i = 1
while n >= 2**i:
    i += 1
print((i-1), 2**(i-1))
print()

print('4.')
distance = int(input('Введите сколько км пробежал спортсмен в первый день: '))
dist = distance
final_distance = int(input('Введите общее расстояние: '))
p = 10           #   %
Sum = None
k = 0
perc_of_dist = (distance * p)/100
while distance < final_distance:
    distance += perc_of_dist+distance
    k += 1
Sum = distance
print(f'After {k} days sportsman surpasses {final_distance} km')
print(f'Summary of passed distance is {Sum} km')
print()

print('5.')
x = int(input('Введите объем вклада (рублей): '))
x_2 = x
p = int(input('Введите на сколько % увеличивается объем вклада: '))
y = int(input(f'Введите объем вклада который должен составлять через несколько лет {x} рублей: '))
year = 0
while x < y:
    year += 1
    percenty = (x*p)/100
    x += percenty
print(f'Через {year} лет изначальный вклад {x_2} рублей достигнет {y} рублей')
print(f'Итог: {int(x//1)} рублей')
print()

print('6.')
c = int(input('Введите целое неотрицательное число: '))
m = 0
while c != 0:
    m += 1
print(m)




