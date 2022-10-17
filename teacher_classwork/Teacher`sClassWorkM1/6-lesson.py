"""a = int(input('a: '))
b = int(input('b: '))
if a > b:
	print(True)
elif a < b:
	print(False)
else:
	print(f'Оба равны!')
"""
"""print('-----Добро пожаловать!-----')
num_1 = int(input('num_1: '))
num_2 = int(input('num_2: '))
operation = input('Выберите операцию: ')

if operation == '+':
	print(f'{num_1}+{num_2}={num_1+num_2}')
if operation == '-':
	print(num_1,'-',num_2,'=',num_1-num_2)
if operation == '*':
	pass 

"""

#39 Begin
""" 
A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = pow(B,2)-4*A*C
print(f'D : {D}')
x_1 = (-B + pow(D,0.5))/(2*A) #(-5+3)/4
x_2 = (-B - pow(D,0.5))/(2*A) #(-5-3)/4
print(f'x_1 = {x_1}')
print(f'x_2 = {x_2}')
"""
#33 Boolean
"""a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

#Разносторонний треугольник
if a > 0 and b > 0 and c > 0:
	if a != b != c:
		print('Разносторонний треугольник')
	elif a == b != c or a == c != b or b == c != a:
		print('Равнобедренный треугольник')
	elif a == b == c:
		print('Равносторонний треугольник')
else:
	print('Это не треугольник!')
"""
import math 
a = int(input('a: '))

print(f'Корень: {a**0.5}')
print(f'Корень: {pow(a,0.5)}')
print(f'Корень: {math.sqrt(a)}')

print(f'Степень: {a**2}')
print(f'Степень: {pow(a,2)}')