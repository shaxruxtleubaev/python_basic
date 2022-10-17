'''
box = 'Shax',
print(type(box))

# dict -> словарь
# set  -> множество
# dict -> key and value

# dict() -> {}
names = dict()
print(f'{names} и {type(names)}')
names[0] = 'Шохрух'
names[1] = 'Шахзод'
print(names)
print(f'Я ищу человека по именем {names[0]}')

surnames = {
    'Кенжебаев': 0,
    'Муртазаев': 3
}
print(surnames['Муртазаев'])

humans = {
    'Расул': ('Футбол', 'Python', 'Музыка')
}
print('Чем интересуется Расул и его интересы {}'.format(humans['Расул']))

box = ('Алишер','Отегенов')
print(box, type(box))

# Методы
names = {
    0: "Шохрух",
    1: "Шахзод"
}
print(names[1])     # устаревший метод
print(names.get(1)) # актуальный метод
print(names.keys())
print(names.values())
print(names.items())
print(names.pop(0))

for key, value in names.items():
    print(key, ':', value)

keys = (0, 1, 2, 3)
values = ['Исмаил', 'Жасур', "Алибек", "Хурлиман"]
names = {k:v for k,v in zip(keys,values)}
print(names)
'''

'''
N = 10
box = {}
score = 0
score_total = []
for k in range(1, N+1):
    box[k] = k*10
    score += box[k]
score_total.append(score)
print(box)
print(score)

app = {
    0: 10,
    1: 20
}
app[2] = 30
print(app)
'''
'''
user = {
    'first_name': 'Исмаил',
    'last_name' : 'Уразбаев',
    'age'       : 15
}
user_options= {
    'nationality' : 'Karakalpak',
    'adress'      : 'Nukus',
    'phone'       : '123 45 67'
}
user.update(user_options)
for k, v in user.items():
    print(f'{k} : {v}')
'''
'''
user = {
    'first_name': 'Исмаил',
    'last_name' : 'Уразбаев',
    'age'       : 15
}
score = 0
key = input('key: ')
for k,v in user.items():
    if key in k:
        score += 1
if score >= 1:
    print(True)
else:
    print(False)
'''
'''box = {}
for i in range(1, 16):
    box[i] = i**2
print(box)
print(len(box))'''
















