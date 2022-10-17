# Итератор
n = int(input('n: '))
box = []
for i in range(n):
    box.append(i)
print(box)

#Генератор
box_2 = list(range(n))
print(box_2)

box_3 = [i for i in range(n)]
print(box_3)






























