print('№12')
start = int(input('start: '))
stop = int(input('stop: '))
step = int(input('step: '))
g = start*2
for i in range(start, stop, step):
    g = g - i 
print(g)
print()

