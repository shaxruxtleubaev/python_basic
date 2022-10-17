
print('1.')
print('Всего 4 типа данных')
print()

print('2.')
name = 12 
print(type(name))
print()

print('3.')
a = int(input('a: '))
b = int(input('b: '))
S = a*b
P = 2*(a+b)
print('S =',S)
print('P =',P)
print()

print('4.')
print('Медод type() определяет состав переменного')
print()

print('5.')
s = pow(8,3)
print('8**3 =',s)
print()

print('6.')
q = pow(64,1/3)
print(q)
print()

print('7.')
r = pow(16,1/4) + pow(625,1/4)
print(r)
print()

print('8.')
a = int(input('Введите целое двузначное число: '))
w = a//10
e = a%10
g = w-e
print(g)

print('9.')
n = int(input('Введите любое целое число: '))
m = int(input('Введите любое целое число: '))
print(n-m)
print()

print('10.')
a = 256/4
print(f'{a}')
print()

print('1-variant')
a = int(input('Введите любое целое число а: '))
b = int(input('Введите любое целое число b: '))
if a > b:
    print(b)
elif a < b:
    print(a)
elif a == b:
    print('a = b')
else:
    print('Error')
print()

print('2-variant')
a = int(input('Введите любое целое число а: '))
b = int(input('Введите любое целое число b: '))
if (a+b) > 15:
    print(True)
elif (a+b) <= 15:
    print(False)
else:
    print('Error')
print()

print('3-variant')
a = int(input('Введите любое целое число а: '))
b = int(input('Введите любое целое число b: '))
if a > b:
    a,b = b,a
print('a =',a)
print('b =',b)
print()

print('4-variant')
a = int(input('Введите целое двузначное число: '))
if a % 2 == 0:
    print(True)
else:
    print(False)
print()

print('5-variant')
l = int(input('Введите целое трехзначное число: '))
if l % 5 == 0:
    print(True)
else:
    print(False)
print()

print('6-variant')
s = int(input('Введите любое целое число: '))
d = int(input('Введите любое целое число: '))
score = 0
if (s*d) > 10:
    score += 1
else:
    score += 0
print(score,'очко') 
print()

print('7-variant')
k = int(input('Введите количество проведенных занятий: '))
l = int(input('Введите количество посещенных занятий: '))
if (l*100)/k < 75:
    print('Вы не сможете сдать экзамен')
elif (l*100)/k >= 75:
    print('Вы сможете сдавать экзамен')
else:
    print('Error')
print()

print('8-variant')
a = int(input('Введите возраст первого человека: '))
b = int(input('Введите возраст второго человека: '))
c = int(input('Введите возраст третьего человека: '))
if a > b > c:
    print(f'Старший: {a}, Младший: {c}')
elif a > c > b:
    print(f'Старший: {a}, Младший: {b}')
elif b > a > c:
    print(f'Старший: {b}, Младший: {c}')
elif b > c > a:
    print(f'Старший: {b}, Младший: {a}')
elif c > b > a:
    print(f'Старший: {c}, Младший: {a}')
elif c > a > b:
    print(f'Старший: {c}, Младший: {b}')
else:
    print('Error')
print()

print('9-variant')
w = int(input('Введите целое положительное четырехзначное число: '))
if w == 1000:
    print('Это наименьшее четырехзначное число')
else:
    print('Это не наименьшее четырехзначное число')
print()

print('10-variant')
god = int(input('Введите целое положительное число года: '))
if god == 300 or god == 1300 or god==1900:
	print('365 дней')
elif god == 1200 or god == 2000:
	print('366 дней')
elif god%4 == 0:
	print('366 дней')
else:
	print('365 дней')
print()
