#4
"""cost = 1000 
for i in range(1, 11):
	print('{}kg sweet is {}'.format(i, cost*i))"""
#13
# 11 - 12 + 13 - 14 + 15 ..... 

#13
"""score = 0
n = int(input('n: '))
for i in range(11, n+1):
	score += (i/10-(i+1)/10)
	print(score)"""

#6
"""cost = float(input('Price: '))
for i in range(12, 21):
	if i % 2 == 0:
		print('{} kg sweet is {}'.format(i/10, cost*(i/10)))
"""

#23
"""n = int(input('n: '))
x = int(input('x: '))
factorial = 1
score = 0

for i in range(1, n+1):
	factorial = factorial * i
	if i % 2 != 0:
		score += (pow(-1,(i-1)/2)*pow(x,i))/(factorial)
		print(score)
"""

#5
"""cost = float(input('Price: ')) #Цена
for i in range(1, 11):
	print('{} kg konfet is {}'.format(i/10, (i/10)*cost))"""

#7
"""score = 0 
a = int(input('a: '))
b = int(input('b: '))
for i in range(a,b):
	score = score + i
print(score)
"""

#9
"""score = 0 
a = int(input('a: '))
b = int(input('b: '))
for i in range(a,b):
	score = score + (pow(i,2))
	print(score)"""

#Nested loops 
for i in range(3):
	for j in range(2):
		print(j)