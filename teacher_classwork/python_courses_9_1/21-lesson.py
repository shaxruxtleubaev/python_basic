#2
"""numbers = [] #хранилище чисел 
print(f'В списке {numbers}')
n = int(input('n: ')) #любое число

for i in range(n):
    numbers.append(2**i)
print(numbers)"""

#4
"""n = int(input('n: '))
a = int(input('a: '))
d = int(input('d: '))

numbers = []
for i in range(n):
    numbers.append(a*(d**i))
print(numbers)"""

#6
"""a = 4 
b = 7 
numbers = [a,b]
print(f'Изначально: {numbers}')
n = int(input('n: '))
summa = 0
for i in range(n):
    c = a + b 
    a = b 
    b = c
    numbers.append(c)
print(f'После: {numbers}')"""

#8
"""A = []
n = int(input('n: '))
for i in range(n+1):
    if i % 2 != 0:
        A.append(i)
print(A)"""

#10
"""import random 
#генератор
numbers = [random.randint(1,11) for i in range(10)]
print(numbers)

odd_numbers = []    #Список для нечетных чисел
even_numbers = []   #Список для четных чисел

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    if numbers[i] % 2 != 0:
        odd_numbers.append(numbers[i])

a = sorted(odd_numbers)[::-1]
b = sorted(even_numbers)
numbers.clear()
numbers.extend([*b, *a])
print(numbers)"""

#12
"""arr = []
for i in range(1,11):
    arr.append(2*i)
print(arr)

even_numbers = []   #Список для четных чисел
for i in range(len(arr)//2):
    even_numbers.append(arr[i])
print(even_numbers)"""

#16
"""box = []
n = int(input('n: '))
for i in range(n+1):
    box.append(i)
    box.append(n-i)
print(box)
"""

for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print(num)

