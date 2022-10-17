#33
"""x = float(input('x кг конфет: '))
a = float(input('Стоимость: '))
y = float(input('y кг конфет: '))

b = (a*y)/x
print(f'Стоимость: {b} руб.')"""

#34
"""x = int(input('x кг(ш) : '))
a = int(input('цена (ш): '))
y = int(input('y кг(и) : '))
b = int(input('цена (и): '))

step_1 = (a/x)
step_2 = (b/y)

print(f'Разница: {int(step_1/step_2)}')"""

#35
"""v = int(input('Скорость лодки: '))
u_1 = int(input('Скорость реки: '))
t_1 = int(input('Время(озеро): '))
t_2 = int(input('Время(река): '))

S_1 = v*t_1
S_2 = (v-u_1)*t_2

print(f'Путь(озеро): {S_1}км')
print(f'Путь(река):  {S_2}км')"""

"""#36
a = int(input('a: '))
b = int(input('b: '))
"""

#13 Integer
"""num = int(input('num: '))

a = num // 100 
b = num // 10 % 10
c = num % 10

total = (b*100)+(c*10)+a
print(f'Итог: {total}')

"""
"""
import random 
import time 
number = random.randint(1,5)
print(f'Компьютер задал число. Вы должны угадать')
time.sleep(1)
score = 0 
answer = int(input('Напишите число: '))
for i in range(5):
	if number == answer:
		time.sleep(1)
		print('Вы угадали!')
		score += 1 
		print(f'У вас {score} очко')
		break
	else:
		time.sleep(1)
		print(f'Вы ошиблись! Число {number}')
		print(f'У вас {score} очко')
		break
	"""

"""#19
sekund = int(input('Секунд: '))
minut  = sekund // 60 
ostatok = sekund % 60
print(f'Минута: {minut}:{ostatok}')"""

"""#24
k = int(input('День: '))
n = 1 

otvet = (((k+n)-2)%7)+1
if otvet == 1:
	print('Понедельник')
if otvet == 2:
	print('Вторник')
if k % 7 == 3:
	print('Среда')"""


#35
x_1 = int(input('x_1: '))
y_1 = int(input('y_1: '))
x_2 = int(input('x_2: '))
y_2 = int(input('y_2: '))

if (x_1+y_1) % 2  == (x_2+y_2) % 2 :
	print(f'Даны поля имеют одинаковый цвет')
else:
	print(f'Даны поля не имеют одинаковый цвет')