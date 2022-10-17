#Список -> List -> Tizim 
# 2 -> ===   [] -> list()

"""box = []
print(box)
print(type(box))

box_2 = list()
print(box_2)
print(type(box_2))"""

from tracemalloc import start


fruits = ['apple','banana','orange','cherry']
"""print(fruits)
print(fruits[0])
print(fruits[2])
#print(fruits[4])
print(fruits[-2])"""

peoples = ['Жасур','Расул',['Шохрух','Шахзод']]
"""print(peoples)
print(peoples[2][1])"""

queues = ['Азиза']
print(f'Очередь: {queues}')

#Методы
"""queues.append('Шохрух')
print(f'Очередь: {queues}')

queues.insert(0, 'Расул')
print(f'Очередь: {queues}')

queues.extend(['Шахзод','Бауыржан'])
print(f'Очередь: {queues}')
print(f'В очереди {len(queues)} людей.')

queues.pop(0)
print(f'Очередь: {queues}')
print(f'В очереди {len(queues)} людей.')

queues.remove('Бауыржан')
print(f'Очередь: {queues}')
print(f'В очереди {len(queues)} людей.')
"""

numbers = [
    1,2,3,
    4,5,6
]
"""print(numbers)
numbers.append(7)
numbers.append(7)
numbers.append(7)
numbers.append(7)
numbers.append(7)
print(numbers)
numbers.clear()
print(numbers)"""



#[start:stop:step]
"""fruits = ['apple','banana','orange','cherry']
print(f'Изначально: {fruits}')
fruits.reverse()
print(f'Сейчас: {fruits}')"""

# str -> list
"""name = input('Напиши свое имя: ').split()
print(name)
print(type(name))"""

# list -> str 
"""names = ['Азиза']
print(names)
print(type(names))

str_names = ''.join(names)
print(str_names)
print(type(str_names))"""

"""name = '   Жасур'
print(name)
print(name.strip())

name = 'Бауыржан'.replace('а','e')
print(name)"""

names = [
    'Азиза',
    'Жасур',
    'Бауыржан'
]
"""print(names)
old_names = ' '.join(names)
print(old_names)
print(old_names.replace(' ',','))
box = [old_names]
print(box)"""

"""start = 1
stop = 10
while start <= stop:
    print(pow(start,3))
    start +=1"""

"""t = int(input('t: '))
k = 0
while k < t:
    k += 1
    if t % k == 0 and k != 1:
        print(f'Наименьший делитель числа {t} это {k}')
        break"""

x = int(input('x: '))
y = int(input('y: '))
day = 0
isProcess = True

while isProcess:
    if x <= y:
        x *= 1.1
        print(f'{x}km')
        isProcess = False
    day += 1
    print(f'Понадобилось {day} дней.')
