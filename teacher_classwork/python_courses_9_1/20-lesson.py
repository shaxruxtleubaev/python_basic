import random
#1
"""numbers = list()
n = int(input('n: '))
for i in range(n):
    if i % 2 != 0:
        numbers.append(i)
print(numbers)"""

#3
"""a = int(input('a: '))
d = int(input('d: '))
n = int(input('n: '))
numbers = []
for i in range(n):
    numbers.append(a+(i*d))
print(numbers)"""

#7
"""box = [random.randint(1,20) for i in range(1,5)]
print(box)
box.reverse()
print(box)"""
#9
#Dizimdi toldirdiq
"""box = []
for i in range(1,20):
    box.append(i)
print(box)

even_box = [] #jup sanlar
#Jup sanlardi tabamiz
for i in range(len(box)):
    if box[i] % 2 == 0:
        even_box.append(box[i])
print(even_box[::-1])"""

"""box = [i for i in range(20) if 2 <= i and i % 2 == 0]
print(box)
box_2 = list(range(2,20,2))
print(box_2)"""

#11
"""box = [random.randint(1,10) for i in range(10)]
print(box)

#print(sorted(set(box)))
k = int(input('k: '))
k_box = []

for i in range(len(box)):
    #Нельзя if
    k_box.append(box[i]*k)
print(k_box)"""

"""print(11) #Версия Шохруха
K = int(input('K: '))
N = int(input('N: '))
box = [i for i in range(K, N+1, K)]
print(box)"""

"""n = int(input('n: '))
a = [i for i in range(1,n+1,2)][::-1]
print(a)"""

"""a = []
n = int(input('n: '))

taq_sanlar = []
jup_sanlar = []
#Список a размера n
for i in range(1,n+1):
    taq_sanlar.append((2*i)-1)
    jup_sanlar.append(2*i)

b = []
for i in range(len(taq_sanlar)//2):
    b.append(taq_sanlar[i])
print(b)

c = []
for i in range(len(jup_sanlar)//2):
    c.append(jup_sanlar[i])
print(c)
d = reversed(c)
a = [*b,*d]
print(a)"""

#Заполнили
"""n = int(input('n: '))
b = []
for i in range(1,n+1):
    if i <= 2:
        b.append(i)
    if i <= 2:
        b.append((n+1)-i)
print(b)
#Находим половину списка"""





