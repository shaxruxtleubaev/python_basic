'''a = int(input('a: '))
b = int(input('b: '))
if a > b:
	print(True)
elif a < b:
	print(False)
else:
	print(f'Оба равны!')
'''

print('-----Добро пожаловать-----')
num_1 = int(input('num_1: '))
num_2 = int(input('num_2: '))
operation = input('Выберите операцию: ')
if operation == '+':
    print(f'{num_1}+{num_2}={num_1+num_2}')
elif operation == "-":
    print(f'{num_1}-{num_2}={num_1-num_2}')
elif operation == '*':
	print(f'{num_1}*{num_2}={num_1*num_2}')
elif operation == "/":
	print(f'{num_1}/{num_2}={num_1/num_2}')
elif operation == '**2':
	print(f'{num_1}**{num_2}={num_1**num_2}')
elif operation == '//':
	print(f'{num_1}//{num_2}={num_1//num_2}')
elif operation == '%':
	print(f'{num_1}%{num_2}={num_1%num_2}')
else:
	print(f'Nothing')

'''if operation = '*':
	pass'''               # pass = пропуск кода
                











