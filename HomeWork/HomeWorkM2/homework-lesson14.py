import time
import random

print('1.')
for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=' ')
print()
time.sleep(2)

print('2.')
a = int(input('Введите температуру в градусе: '))
print(f'Если температура по цельсию будет равна {a} то температура по фаренгейту будет равен {(9/5)*a+32}')
print(f'Если температура по фаренгейту будет равна {a} то температура по цельсий будет равен {(a-32)*(5/9)}')
print()
time.sleep(2)

print('3.')
a = random.randint(1, 10)
print(f'Компьютер задал число. Вы должны угадать')
answer = int(input('Напишите число: '))
for i in range(1,10):
    if answer == a:
        print('Вы угадали!')
        break
    else:
        print(f'Вы не угадали! Заданное число было {a}')
        break
print()
time.sleep(2)

print('4.')
l = '*'
j = '*'
for i in range(6):
    print(i*l)
for k in range(4, 0, -1):
    print(k*j)
print()
time.sleep(2)

print('5.')  #взял с интернета немного изменив код
h = input("Введите слово: ")
for k in range(len(h) - 1, -1, -1):
  print(h[k], end="")
print()
time.sleep(2)

print('6.')
for i in range(0, 7, 3):
    if i+3 == 3 and i+6 == 6:
        print(0, 1, 2, 4, 5,)
    else:
        continue
print()
time.sleep(2)

print('7.')  #подсказку взял с интернета
a1 = a2 = 1
print(a1, a2, end=' ')
for i in range(2, 9):
    a1, a2 = a2, a1 + a2
    print(a2, end=' ')
print()
time.sleep(2)

print('8.')
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    elif i % 5 == 0:
        i = 'Гудение'
    elif i % 3 == 0:
        i = 'Шипение'
    print(i)
print()








