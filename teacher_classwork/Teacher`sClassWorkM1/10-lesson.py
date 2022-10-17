#1 

"""number = 1 
print(number)
print(number+1)
print(number+2)
print(number+3)
print(number+4)
print(number+5)"""

#start = 0, stop = n, step = 1
#range(start, stop, step) -> Диапазон

"""number = 1
n = int(input('n: '))
for i in range(0,n,1):
	print(number+i)"""

"""start = int(input('start: '))
stop = int(input('stop: '))
step = int(input('step: '))
for i in range(start,stop,step):
	print(i, end=' ')"""



#5
"""start = 0
stop  = 41
step  = 4 

for i in range(start,stop,step):
	print(i)"""

"""start = 50
stop = 1 
step = -5
for i in range(start,stop,step):
	print(i)"""

"""start = 1
stop = 10
step = 1 

for i in range(start,stop,step):
	print(i, end=' ')
"""

"""start = 20
stop = 10
step = -2 

for i in range(start,stop,step):
	print(i, end=' ')"""

"""for i in range(0,20,2):
	print(i)"""

"""for i in range(1,30,2):
	print(i)"""
#print(1+2+3+4+5+6+7+8+9+10)
"""score = 0 
n = int(input('n: '))
for i in range(1,n,1):
	score = score + i
print(f'Сумма от {1} до {n} это {score}')"""
#print(score)

"""score = 10 
n = int(input('n: '))
for i in range(5,n,-1):
	score = score - i
	print(f'Разность от {5} до {n} это {score}')"""

"""score = 10 
for i in range(5,0,-1):
	score = score - i 
	print(score)"""


"""for i in range(1, 51):
	if i % 2 != 0:
		print(i, end=' ')
	if i % 2 == 0:
		print(i, end=' ')"""

# break -> стоп
# continue -> пропускает
# conditionals

"""for i in range(20):
	if i == 10:
		print('Жасур')
		break
	print(i)"""

"""for i in range(20):
	if i == 7:
		continue 
	print(i)"""

#1 от 50 
# 25 и 30

"""score = 0
for i in range(1, 51):
	if i >= 25 and i <= 30:
		score += i
print(f'Сумма: {score}')"""

#Факториал 

#5! = 120 
#5! = 1*2*3*4*5

factorial = 1
n = int(input('n: '))
for i in range(1,n+1):
	factorial *= i 
	print(f'{i}!={factorial}')
