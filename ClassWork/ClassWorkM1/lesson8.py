import random
import time
number  = random.randint(1,5)
print(f'Компьютер задал число. Вы должны угадать.')
time.sleep(3)
score = 0
answer = int(input('Напишите число: '))
for i in range(5):
    if number == answer:
	    time.sleep(3)
	    print('Вы угадали!')
	    score+=1
	    print(f'У вас {score} очко')
	    break
    else:
	    print(f'Вы ошиблись. Заданное число = {number}')
	    print(f'У вас {score} очко')
