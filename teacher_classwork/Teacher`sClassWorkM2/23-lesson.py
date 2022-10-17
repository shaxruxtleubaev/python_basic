"""
#dict -> Словарь
#set  -> Множество 

#dict -> key and value (ключ и значение)

#dict() -> {}
names = dict()
print(f'{names} и {type(names)}')
names[0] = 'Шохрух'
names[1] = 'Шахзод'
print(f'{names}')
print(f'Я ищу человека по именем {names[0]}')

name = {
    0 : 'Шохрух',
    1 : 'Шахзод'
}
print(f'{name}')
print(f'Я ищу человека по именем {name[1]}')

surnames = {
    'Кенжебаев': 0,
    'Муртазаев': 3
}
print(surnames['Муртазаев'])


humans = {
    'Расул': ('Футбол','Python','Музыка')
}
print('Чем интересуется Расул и его интересы {}'.format(humans['Расул']))


box = ('Алишер','Отегенов')
print(box, type(box))

#Методы
names = {
    0 : 'Шохрух',
    1 : 'Шахзод'
}
"""
"""print(names[1])     #устаревший метод
print(names.get(1)) #Более актуальный метод
print(names.keys())
print(names.values())
print(names.items())
print(names.pop(0))

"""
"""for key,value in names.items():
    print(key, ':', value)"""

"""keys = (0,1,2,3)
values = ['Исмаил','Жасур','Алибек','Хурлиман']
#zip -> 
names = {k:v for k,v in zip(keys,values)}
print(names)"""

"""
box = {}
score = 0
score_total = []
for k in range(1,11):
    box[k] = k*10
    score += box[k]
score_total.append(score)
print(box)
print(score_total)

app = {
    0 : 10,
    1 : 20
}
app[2] = 30
print(app)
"""

"""user = {
    'first_name': 'Исмаил',
    'last_name' : 'Уразбаев',
    'age'       : 15
}
user_options = {
    'nationality' : 'Karakalpak',
    'addres'      : 'Nukus',
    'phone'       : '123456789'
}
user.update(user_options)
key = input('Введите ключ: ')
isFind = 0
for k,v in user.items():
    if key in k:
        isFind += 1 
if isFind == 1:
    print(f'Ключ найден')
elif isFind == 0:
    print('Ключ не найден')"""

"""box = dict()
for i in range(1,16):
    box[i] = i**2 
print(box)
print(len(box))
"""

"""registration_side = {}

#user-1
registration_side['first_name'] = ['Алибек','Жасур']
registration_side['second_name'] = ['Казахбаев','Алламбергенов']
registration_side['age']        = [15,17] 

print(registration_side)"""

"""users = {}

first_names = list()
second_names = list()
ages = list()


for i in range(2):
    first_name = input('Напишите ваше имя: ')
    second_name = input('Напиште вашу фамилию: ')
    age = int(input('Укажите возраст: '))
    first_names.append(first_name)
    second_names.append(second_name)
    ages.append(age)

users['first_name'] = first_names
users['second_name'] = second_names
users['age'] = ages

for k,v in users.items():
    print(k, ':', v)

key = input('Ключ: ')
if key in users.items():
    print(key)
"""

numbers = [1,2,3,4,5]
print(numbers[0], numbers.index(3))


