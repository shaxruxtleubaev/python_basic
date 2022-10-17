n = int(input('До какой числы найти простые и составные числа?: '))
sostavnoy = []
prostoy = []
for i in range(1, n):
    score = 0
    for j in range(2, n):
        if i % j == 0:
            score += 1
            if score >= 2:
                sostavnoy.append(i)
            else:
                prostoy.append(j)
print(f'Составные числа: {set(sostavnoy)}')
print(f'Простые числа: {set(prostoy)}')























