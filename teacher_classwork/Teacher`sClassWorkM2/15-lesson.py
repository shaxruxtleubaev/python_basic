#1
"""for i in range(1500, 2701):
 	if i % 7 == 0 and i % 5 == 0:
 		print(i)
"""

#2
"""c = int(input('Укажите градус по C: '))
if c:
	# c*(9/5)+n=F
	f = c*(9/5)+32 
	print('Градус по Цельсию {} -> {} по Фарангейту!'.format(c,f))
f = int(input('Укажите градус по Ф: '))
if f:
	c = (f-32)//(9/5)
	print('Градус по Цельсию {} -> {} по Фарангейту!'.format(f,c))
"""

#3
"""
import random 
answer = int(input('Enter the number between 1 and 4: '))

score = 0 #Очко
for i in range(4):
	number = random.randint(1,4) #Генератор случайных чисел
	if answer == number:
		score += 1 
		print(f'Correct! You have {score} points')
		answer = int(input('Enter the number between 1 and 9: '))
		if score == 2:
			break
	elif answer != number:
		print(f'Incorrect! You have {score} points')
		answer = int(input('Enter the number between 1 and 9: '))
"""

#5
"""word = input('word: ')
print('Length is {}->{}'.format(word, len(word)))
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
for i in range(len(word)-1,-1,-1):
	print(word[i], end='')
"""

#6
"""n = int(input('n: '))
a = 0 
b = 1
for i in range(0, n+1):
	a,b = b,a+b
	print('{}s fibonacci number -> {}'.format(i,a))"""


#4
"""symbol = '*'
for i in range(4):
	for j in range(4):
		if i >= j:
			print(symbol, end=' ')
	print()
for i in range(1):
	for j in range(5):
		if i == 0:
			print(symbol, end=' ')
	print()
for i in range(4):
	for j in range(4):
		if i <= j:
			print(symbol, end=' ')
	print()"""

#while -> пока 
"""start = 1
stop  = 11
for i in range(start,stop):
	print(i, end=' ')
print()
print('--------------------')

"""
"""start = 1 
stop  = 11 
while start <= stop:
	start += 1
	print(start, end=' ')"""

"""n = int(input('n: '))
isProcess = True 
while isProcess:
	n += 1
	if n == 10:
		isProcess = False
	print(n)"""

"""import time
isProcess = True 
a = int(input('a: '))
while isProcess:
	print(a)
	if a == 1000:
		isProcess = False
	a += 100"""

#31
k = int(input('k: '))
a = 2
for i in range(1,k+1): 
	for j in range(1, i+1):
		a_k = 2 + (1/a)
		a = a_k
	print(a_k)

"""score = 0
for i in range(5):
	for j in range(i):
		score += i
		print(i, end=' ')
	print()
print(score)"""












