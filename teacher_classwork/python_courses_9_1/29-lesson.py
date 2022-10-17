#1
"""box = []
a = lambda x: [box.append(x[len(x)-1-i]) for i in range(len(x))]
a("Python")
box_str = "".join(box)
with open('results.txt',mode='a') as file:
    file.write(f'\n{box_str}')
    file.close()"""
#2
"""import random
app = [random.randint(-10,10) for i in range(10)]
print(app)
single = []
single_1 = []
#Удаляем дубликаты версия - 1 
numbers = [single.append(i) for i in app if i not in single] 
print(single)
#Удаляем дубликаты версия - 2
for i in range(len(app)):
    if app[i] not in single_1:
        single_1.append(app[i])
print(single_1)"""
#Удаляем дубликаты версия - 3
"""def func(x):
    single = []
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            single.append(x[i])
    if x.count(x[-1]) < 2:
        single.append(x[-1])
    return single 
with open('results.txt',mode='a') as file:
    file.write(f'\n{func(app)}')
    file.close()"""

