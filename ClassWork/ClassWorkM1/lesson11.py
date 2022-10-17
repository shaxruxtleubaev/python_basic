print('Hello')

"""for index in range(10):
	print('Hello')"""

"""score = 0
for i in range(3):
	name = input('Enter your name: ')
	score = score + 1 
print(f'Счет: {score}')"""


import random 

"""score = 0 
for i in range(5):
	number = random.randint(1,10)
	if number == 3:
		score += 5
	if number == 2:
		score += 3
	print(f'Число: {number}')
print(f'number: {score}')"""

"""n = int(input('n: ')) #Разряд -> маниси
score = 0 
N = int(input('N: ')) #Число -> сан

for i in range(n):
	score += pow(N+i,2) #100
	print(f'Общая сумма: {score}')"""

"""n = int(input('n: ')) #Разряд -> маниси
score = 1
for i in range(11,n): #range -> integer
	print(i/10, end=' ')
	score = (score * i)/10
print(f'Тотал: {score}')"""



"""N = int(input('N: '))
factorial = 1 
summa = 0
for i in range(1,N+1):
	factorial = factorial * i 
	summa += (1/factorial)
	print(f'{i}!={factorial}')
print(f'Сумма: {1+summa}')"""


x = int(input('x: '))
factorial = 1
score = 0

"""for i in range(1, x+1):
	factorial *= (2*i)+1 
	print(f'{i}!={factorial}')"""

# x = 3 -> 1,2,3
# 1,2,3,4 ... x
# 1,3,5,7,9 ... x

for i in range(1, x+1):
	factorial *= i
	if i % 2 != 0:
		score += factorial
print(f'Тотал: {score}')
		
		 