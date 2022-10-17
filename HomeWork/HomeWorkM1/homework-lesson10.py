print('№1')
god_s = int(input('Введите год службы: '))
zarplata = int(input('Введите зарплату (в сумах): '))
if god_s >= 5:
    print('Ваш 5% бонус =',(5*god_s)/100,'млн')
else:
    print('Вам не зачисляется бонус')
print()

print('№2')
a = int(input('Введите значения а: '))
b = int(input('Введите значение b: '))
if a == b:
    print('Это квадрат')
else:
    print('Это не квадрат')
print()

print('№3')
s = int(input('Сколько продуктов вы купили: '))
stoimost = s*100
skidka = (stoimost*10)/100
if s > 10:
    print('Стоимость вашей покупки с учетом 10% скидки =',stoimost-skidka,'сумов')
else:
    print('Стоимость вашей покупки =',stoimost)
print()

print('№4')
a = int(input('Введите ваши оценки в диапазоне 1-100: '))
if a < 25:
    print('Ваша оценка F')
elif 25 <= a and a < 45:
    print('Ваша оценка E')
elif 45 <= a and a < 50:
    print('Ваша оценка D')
elif 50 <= a and a < 60:
    print('Ваша оценка C')
elif 60 <= a and a < 80:
    print('Ваша оценкаа B')
elif a >= 80 and a <= 100:
    print('Ваша оценка A')
else:
    raise ValueError('Error!')
print()

print('№5')
a = int(input('Введите число месяца в диапазоне 1-12: '))
if a == 1:
    print('Январь, 31 дней')
elif a == 2:
    print('Февраль, 28 дней')
elif a == 3:
    print('Март, 31 дней')
elif a == 4:
    print('Апрель, 30 дней')
elif a == 5:
    print('Май, 31 дней')
elif a == 6:
    print('Июнь, 30 дней')
elif a == 7:
    print('Июль, 31 дней')
elif a == 8:
    print('Август, 31 дней')
elif a == 9:
    print('Сентябрь, 30 дней')
elif a == 10:
    print('Октябрь, 31 дней')
elif a == 11:
    print('Ноябрь, 30 дней')
elif a == 12:
    print('Декабрь, 31 дней')
else:
    print('Ошибка при вводе')
print()

print('№6')
x = int(input('Введите любое целое число: '))
if x%7 == 0:
    print('Число 7 делится на заданное число')
else:
    print('Число 7 не делится на заданное число')
print()

print('№7')
c = int(input('Введите количество дней в библиотеке: '))
if c <= 5:
    print('Ваша плата =',2*c)
elif c >= 6 and c <=10:
    print('Ваша плата =',3*c)
elif c >= 11 and c < 15:
    print('Ваша плата =',4*c)
elif c >= 15:
    print('Ваша плата =',5*с)
else:
    print('Ошибка при вводе')
print()

print('1.')
A = int(input('Введите значение А: '))
B = int(input('Введите значение В, больше чем А: '))
N = B-A
for i in range(A,B+1):
    print(i)
print('Кол-во =',N+1)
print()

print('2.')
a = int(input('Введите вещественное число цена 1 кг конфет: '))
for i in range(1,11):
    print(i*a)
print()

print('3.')
a = int(input('Введите вещественное число: '))
for i in range(12, 21, 2):
    i = (i/10)*a
    print(i)
print()

print('4.')
A = int(input('Введите целое значение А: '))
B = int(input('Введите целое значение В, больше чем А: '))
factorial = 1
for i in range(A,B+1):
    factorial *= i
print(f'{factorial}')
print()

print('5.')
N = int(input('Введите целое вещественное число больше 0: '))
s = 0
for i in range(1,N+1):
    i = 1/i
    s = s+i
print(s)
print()

print('6.')
n = int(input('Введите целое цисло >0: ')) 
score = 1
for i in range(11,n*10): 
	score = (score * i)/10
print(f'Тотал: {score}')
print()

print('7.')
N = int(input('Введите целое число > 0: '))
a = 0
for i in range(1,2*N,2):
    a = a+i
print(f'N2 = {a}')
print()

print('8.')
A = int(input('Введите целое вещественное число: '))
N = int(input('Введите целое число > 0: '))
s = None
for i in range(1,N+1):
    s = pow(A,i)
    print(s)
print()

print('9.') #не смог сделать

print('10.') #не смог сделать
