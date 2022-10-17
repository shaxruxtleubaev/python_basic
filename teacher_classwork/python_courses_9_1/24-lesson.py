#set -> множество 

box = {1,2,3,4,5} # -> set
box_1 = [1,2,3,4,5] # -> list
box_2 = (1,2,3,4,5) # -> tuple 
box_3 = {0:1, 1:2, 2:3, 3:4, 4:5} # -> dictionary 
box = {1,2,3,4,5,1,2,3}
#print(box, type(box))

"""#print(box, type(box))
import random 
box = {1}
for i in range(10):
    box.add(random.randint(1,10))
print(box)
print({1,1,1,1,2,3,3,2})

box = {1,2,3,4,5}
box_2 = {6,7,8,9,10}
box.update(box_2)
print(box)
box.pop()
box.update({1,2,3,4,5})
#print(box)
box.discard(2)
print(box)

#Различные команды
numbers = {1,2,3,4,5}
box = {2,3,4,5,6}

print(numbers.union(box)) 
print(numbers.intersection(box))
print(numbers.difference(box))
print(box.difference(numbers))"""

#Dictionary ->key and value 
"""
names = dict()
names[0] = 'Азиз'
names[1] = 'Султан'
print(names, type(names))

names_1 = {
    0 : 'Азиз',
    1 : 'Султан'
}
print(names_1, type(names_1))
"""
"""box = {}
for i in range(10):
    box[i] = i**i
print(box)

print(box.keys())
print(box.values())
print(box.items())

for i in box.keys():
    print(i)
print()
for i in box.values():
    print(i)
print()
for i,j in box.items():
    print(i, ':', j)"""

"""user_1 = {
    'first_name': 'Азиз',
    'last_name' : 'Медетбаев',
    'age'       : 23 
}
user_2 = {
    'first_name': 'Султан',
    'last_name' : 'Сагынбаев',
    'age'       : 18 
}
first_names = []
last_names  = []
ages        = []
for i in range(3):
    first_name = input('Enter your first name: ')
    last_name  = input('Enter your last name: ')
    age = int(input('Enter your age: '))

    first_names.append(first_name)
    last_names.append(last_name)
    ages.append(age)
#print(first_names, last_names, ages)

users = {}
users['first_name'] = first_names
users['last_name'] = last_names
users['age'] = ages 

#Поиск 
search = input('Enter your key: ')
search_field = list()
for i in users.items():
    search_field.append(users[search])
    break
print(f'Ключ {search} и -> {search_field}')
"""

import random
numbers = {0}
for i in range(10):
    numbers.add(random.randint(1,10))
#print(numbers)

"""box = {1,2,3,4,5}
box.add(6)
box.update({7,8,9,10,1,2,3})
box.pop()       #birinshi sandi oshirdi 
box.remove(2)   #2shi element index arqali
box.discard(3)  #3shi 

numbers_1 = {1,2,3,4,5}
numbers_2 = {2,3,4,5,6}
print(numbers_1.union(numbers_2))
print(numbers_1.intersection(numbers_2))
print(numbers_1.difference(numbers_2))
print(numbers_2.difference(numbers_1))"""
'''
import random 
numbers_list =  [random.randint(1,10) for i in range(6)]
numbers_tuple = tuple((random.randint(1,10) for i in range(6)))
print(numbers_list)
print(numbers_tuple)

set_list = set(numbers_list)
set_tuple = set(numbers_tuple)

difference_list_tuple = set_list.difference(set_tuple)
print(f'Список: {list(difference_list_tuple)}')'''

'''numbers=list()
for i in range(5):
    numbers.append(i**(5-i))
print(set(numbers),type(numbers))'''