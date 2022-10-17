
print('1.----------------------------------------------------------')
dictionary = {'Name': 'Shaxrux', 'Surname': 'Tleubaev', 'Age': 15}
print(dictionary)
# for k,v in dictionary.items():
#     print(k, ':', v)
print()

print('2.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe.keys())
print()

print('3.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe.values())
print()

print('4.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe.items())
# for i in qwe.items():
#     print(qwe)
#     break
print()

print('5.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
score = 0
for i in range(1, n+1):
    qwe[i] = i 
    score += 1
print(qwe)
print(f'Кол-во ключей = {score}')
print()

print('6.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe)
print(f'Сумма значении = {sum(qwe.values())}')
print()

print('7.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe)
for i in qwe.items():
    print(qwe.values())
    break
print()

print('8.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe)
for i in qwe.items():
    print(qwe.keys())
    break
print()

print('9.----------------------------------------------------------')
n = int(input('Введите количество словарей: '))
qwe = {}
for i in range(1, n+1):
    qwe[i] = i 
print(qwe)
for i in qwe.items():
    print(qwe)
    break
print()



