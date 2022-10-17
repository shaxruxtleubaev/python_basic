import random

print('Array30----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
abc = []
for i in range(len(box)-1):
    if box[i] > box[i+1]:
        abc.append(box[i])
print(f'Номера элементов которые больше числа с права = {abc} \nИх количество = {len(abc)}')
print()

print('Array31----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
abc = []
for i in range(len(box)-1):
    if box[i] > box[i-1]:
        abc.append(box[i])
print(f'Номера элементов которые больше числа слева = {abc} \nИх количество = {len(abc)}')
print()

print('Array32----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
local_min = []
for i in range(len(box)-1):
    if box[i] < box[i-1] and box[i] < box[i+1]:
        local_min.append(box[i])
        break
print(f'Первый локальный минимум = {local_min}')
print()

print('Array33----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
local_max = []
for i in range(len(box)-1):
    if box[i] > box[i-1] and box[i] > box[i+1]:
        local_max.append(box[i])
print(f'Последний локальный максимум = {local_max[-1]}')
print()

print('Array34----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
local_min = []
for i in range(len(box)-1):
    if box[i] < box[i-1] and box[i] < box[i+1]:
        local_min.append(box[i])
print(local_min)
print(f'Максимальный локальный минимум = {max(local_min)}')
print()

print('Array35----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
print(box)
local_max = []
for i in range(len(box)-1):
    if box[i] > box[i-1] and box[i] > box[i+1]:
        local_max.append(box[i])
print(local_max)
print(f'Минимальный локальных максимумов = {min(local_max)}')
print()

print('Array36----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
box = [random.randint(-10, 10) for i in range(N)]
bin_ = []
print(box)
for i in range(len(box)-1):
    if box[i] > box[i-1] and box[i] > box[i+1]:
        bin_.append(box[i])
    if box[i] < box[i-1] and box[i] < box[i+1]:
        bin_.append(box[i])
print(f'Локальные минимумы и локальные максимумы: {bin_}')
for i in range(len(bin_)):
    if len(bin_) >= 1:
        box.remove(bin_[i])
print(f'Числы который не входят в локальные минимумы и локальный максимумы: {box}')
print(f'Максимальный число который не входит в локальный минимум и локальный максимум: {max(box)}')
print()

print('Array37----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
xyz = [random.randint(-10, 10) for i in range(N)]
print(xyz)
k = 0
flag = True
for i in range(len(xyz)-1):
    if xyz[i-1] < xyz[i] :
        if flag:                    # Подсказку взял с интернета
            k += 1
            flag = False
    else:
        flag = True
print(f'Количество участков = {k}')
print()

print('Array38----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
xyz = [random.randint(-10, 10) for i in range(N)]
print(xyz)
k = 0
flag = True
for i in range(len(xyz)-1):
    if xyz[i] > xyz[i-1] :
        if flag:                   
            k += 1
            flag = False
    else:
        flag = True
print(f'Количество участков = {k}')
print()

print('Array39----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива N: '))
xyz = [random.randint(-10, 10) for i in range(N)]  # Думаю этот код с ошибками
print(xyz)
k = 0
flag = True
flag_2 = True
for i in range(len(xyz)-1):       
    if xyz[i-1] < xyz[i]:
        if flag:                    
            k += 1
            flag = False
    if xyz[i] > xyz[i+1]:
        if flag_2:                    
            k += 1
            flag_2 = False        
    else:
        flag = True
        flag_2 = True
print(f'Количество участков = {k}')
print()

print('Array40----------------------------------------------------------------------------------------')
R = int(input('Введите целое число R: '))
N = int(input('Введите размер массива: '))
box = [random.randint(-20, 30) for i in range(N)]
print(box)
qwe = []
for i in range(len(box)):
    qwe.append(abs(box[i]-R)) 
g = qwe.index(min(qwe))
print(f'Наиболее близкий число к {R}, это: {box[g]}')
print()

print('Array41----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(-20, 30) for i in range(N)]
print(f'Дано: {box}')
qwe = []
for i in range(len(box)-1):
    qwe.append(box[i]+box[i+1])
print(f'Сумма соседних элементов: {qwe}, максимальная сумма = {max(qwe)}')
g = qwe.index(max(qwe))
print(f'Две соседних элемента, сумма которых макимальна, это {box[g]} и {box[g+1]}')
print()

print('Array42----------------------------------------------------------------------------------------')
R = int(input('Введите число R: '))
N = int(input('Введите размер массива: '))
box = [random.randint(-20, 30) for i in range(N)]
print(f'Дано: {box}')
qwe = []
vbn = []
for i in range(len(box)-1):
    qwe.append(box[i]+box[i+1])
    vbn.append(abs(qwe[i]-R)) 
print(f'Сумма соседних чисел = {qwe}')
g = vbn.index(min(vbn))
print(f'Два соседних элемента массива, сумма которых наиболее близка к числу {R}, это {box[g]} и {box[g+1]}')
print()

print('Array43----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(1, 50) for i in range(N)]
box.sort()
print(f'Дано: {box}')
k = 0
for i in range(len(box)-1):
    if box[i] != box[i+1]:
        k += 1
    else:
        break
print(f'Количество различных элементов = {k}')
print()

print('Array44----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(1, 50) for i in range(N)]
box.sort()
print(f'Дано: {box}')
k = 0
for i in range(len(box)-1):
    if box[i] == box[i+1]:
        if box.count(box[i]) == 2:
            print(f'Две одинаковые элементы = {box[i]} и {box[i+1]}')
        else:
            print('В данном массиве нет одинаковых двух элементов! ')
            break
print()

print('Array45----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(-50, 50) for i in range(N)]
print(f'Дано: {box}')
asd = []
for i in range(len(box)-1):
    asd.append(abs(box[i]-box[i+1]))
print(f'Модули разности двух последовательных элементов: {asd}')
min_asd = asd.index(min(asd))
print(f'Номера двух ближайших элементов с наименьшим модулем разности это: {box[min_asd]} и {box[min_asd+1]}')
print()

print('Array46----------------------------------------------------------------------------------------')
R = int(input('Введите целое число R: '))
N = int(input('Введите размер массива: '))
box = [random.randint(-30, 30) for i in range(N)]
print(f'Дано: {box}')
ert = []
iop = []
for i in range(len(box)-1):
    ert.append(box[i] + box[i+1])
    iop.append(abs(ert[i]-R)) 
print(f'Сумма последовательных элементов: {ert}')
print(f'Минимальность чисел массива: {iop}')
dfg = iop.index(min(iop))
print(f'Два различных элемента, сумма которых наиболее близка к числу {R}, это: {box[dfg]} и {box[dfg+1]}')
print()

print('Array47----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(1, 30) for i in range(N)]
print(f'Дано: {box}')
k = 0
for i in range(len(sorted(box))-1):
    if box[i] != box[i+1]:
        k += 1
    else:
        break
print(f'Количество различных элементов = {k}')
print()

print('Array48----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(1, 25) for i in range(N)]
box.sort()
print(f'Дано: {box}')
k = []
for i in range(len(box)-1):
    k.append(box.count(box[i]))

if len(set(k)) > 1:
    print(f'Максимальное количество одинаковых элементов = {max(k)}')
else:
    print('В данном массиве нет одинаковых чисел')
print()

print('Array49----------------------------------------------------------------------------------------')
N = int(input('Введите размер массива: '))
box = [random.randint(1, N) for i in range(N)]
box_2 = [i for i in range(1, N+1)]
box.sort()
print(box)
k = 0
for i in range(len(box)-1):
    if box[i] == box_2[i] and box[-1] == box_2[-1]:
        k += 1
    if box[i] != box_2[i] or box[-1] != box_2[-1]:
        print(box[i])
        break
    if k == N-1:
        print(0)
print()

print('Array50----------------------------------------------------------------------------------------')





























