"""# list -> [] -> list()
# tuple -> () -> tuple()

app = [1,2,3,4,5]
print(app, type(app))

box = (1,2,3,4,5)
print(box, type(box))

list_1 = []
for i in range(10):
    list_1.append(i)
print(list_1)

tuple_1 = ()
for i in range(10):
    tuple_1.insert(i)
print(tuple_1)

#С помощью итератора (list)
#С помощью итератора (tuple)

list_2 = [i for i in range(10)]
print(list_2)
tuple_2 = tuple((i for i in range(10)))
print(tuple_2)
"""

"""box = []
n = int(input('n: '))
for i in range(n):
    box.append(i)
print(box)
print(box[5])
print(box.index(5))
#print(box.index(3))
names = ['Sultan','Atabek','Shoxrux']
print(names.index('Sultan'))
print(names[0])
"""

#19
"""import random
box = []
n = int(input('n: '))
for i in range(n):
    box.append(i)
print(box)

k = random.randint(0,n-1)
print(k)
box_2 = []
for i in range(len(box)):
    if box[0] < k and k < box[n-1]:
        box_2.append(box[i])
    else:
        box_2.append(0)
        break
print(box_2)
"""
#21
#Версия Шахруха
"""n = int(input('n: '))
g = [i for i in range(1, n+1)]
print(g)

k = int(input('k: '))
l = int(input('l: '))

box = [i for i in range(1, n) if 1 <= k and k <= l and l <= n]
print(box[k-1:l])
print(f'Среднее арифметическое: {int(sum(box[k-1:l])/len(box[k-1:l]))}')
"""

"""#Общая
n = int(input('n: '))
k = int(input('k: '))
l = int(input('l: '))

#Заполняем список от 1 до n
box = []
for i in range(n):
    box.append(i)

score = list()
numbers = []
#Находим сре ариф значение
for i in range(len(box)):
    if box[i] >= k and box[i] <= l:
        numbers.append(box[i])

summ = sum(numbers)
len_ = len(numbers)
print(f'Среднее арифметическое число: {int(summ/len_)}')
"""

#27
"""
import random 
#box = [random.randint(-15,15) for i in range(6)]
box = [1,-10,2,-32,5,-1,7]
print(box)

even_box = list()
for i in range(len(box)):
    if box[i]*box[i+1] < 0:
        even_box.append(0)
    else:
        print(box[i+1])
        break
print(even_box)
        
"""    
#29
"""box = [i for i in range(10) if i % 2 != 0]
print(f'Список: {box} и максимум это {max(box)}')
print(f'Список: {box} и минимум это  {min(box)}')
"""

box = tuple([i for i in range(10) if i % 2 != 0])
for i in range(len(box)):
    for j in range(len(box)):
        print(box[i])
