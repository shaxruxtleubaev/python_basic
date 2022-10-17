from itertools import count
import random
'''
print('1.')
box = []
a = lambda x: [box.append(x[len(x)-1-i]) for i in range(len(x))]
a('Python')
box_str = "".join(box)
with open('results.txt', mode='a') as file:
    file.write(f'\n{box_str}')
    file.close()
print()
'''
print('2.')
box = sorted([random.randint(1, 30) for i in range(10)])                                         
print(box)
'''def func(x):
    single = []
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            single.append(x[i])
    if x.count(x[-1]) < 2:
        single.append(x[-1])
    return single
with open('results.txt', mode='a') as file:
    file.write(f'\n{func(box)}')
    file.close()
print()'''

  
h = lambda x: [x[i] for i in range(len(x)-1) if x[i] != x[i+1] if x.count(x[-1]) < 2]
print(h(box))
# with open('results.txt', mode='a') as file:
#     file.write(f'\n{box}')
#     file.write(f'\n{h(box)}')
#     file.close()


'''
print('3.')
a = [i for i in range(1, 31)]
b = [2 for i in range(30)]
c = list(map(lambda x,y: x**y, a, b))
print(c)
print()


print('7.')
a = [random.randint(-10, 10) for i in range(7)]
print(a)
f = lambda n: sum(n)
print(f(a))
print()
'''








