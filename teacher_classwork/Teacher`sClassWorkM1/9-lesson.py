#36 - boolean 

#Расположение 
"""x_1 = int(input('x_1: '))
y_1 = int(input('y_1: '))

#Координаты фигуры
x_2 = int(input('x_2: '))
y_2 = int(input('y_2: '))"""

"""if (x_1 == x_2) or (y_1 == y_2):
	print('Ладья так может!')
else:
	print('Ладья так не может!')"""

"""if abs(x_1-x_2) == 1 and abs(y_1-y_2)==1:
	print('Король так может')
elif abs(x_1-x_2) == 1 and abs(y_1-y_2)==0:
	print('Король так может')
elif abs(x_1-x_2) == 0 and abs(y_1-y_2)==1:
	print('Король так может')
else:
	print('Король так не может')"""

"""if abs(x_1-x_2) == abs(y_1-y_2):
	print('Слон так может ходить!')
if abs(x_1-x_2) != abs(y_1-y_2):
	print('Слон так не может ходить!')"""

"""if (abs(x_1-x_2)==1 and abs(y_1-y_2)==2):
	print('Слон так может ходить')
elif (abs(x_1-x_2)==2 and abs(y_1-y_2)==1):
	print('Слон так может ходить')
else:
	print('Слон так не может ходить!')"""

"""n = int(input('n: '))
if n >= 20 and n <= 69:
	if n == 20:
		print('Двадцать лет')
	if n == 32:
		print('Тридцать два года')
	if n == 41:
		print('Сорок один ')"""

#Циклы -> Loops 
"""
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')"""

# <5 <=5 

"""for start in range(0,5,1):
	print('Hello')

#Нельзя
for start in range(, 10,1)
for start in range(,,1)

#Можно
for start in range(10)
for start in range(1,10)

#range(start, stop, step)"""

#Инкремент -> прибавить единицу 
"""index = 5
for i in range(index,10):
	print(i)"""

"""for i in range(1, 51,1):
	if i % 2 == 1:
		print(i, end=' ')"""

"""score = 0 
for i in range(1,6):
	score += i
print(score)"""

total = 10000
wishes = input('Хотите что-нибудь покупать? ')
if wishes == 'Yes' or wishes == 'yes':
	print('Выберите продукт. ')
	things = int(input('Введите сумму: '))
	quantity = int(input('Сколько вещей вы хотите покупать? '))
	for i in range(quantity):
		if things*quantity <= total:
			if things == 3000:
				total -= things
		else:
			print('У вас недостаточно средств!')
			break
elif wishes == 'No' or wishes == 'no': 
	print('Определитесь уже!') 
print(f'У вас осталось: {total}сум')