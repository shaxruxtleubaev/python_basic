print('For1')
K = int(input('Введите целое число K: '))
N = int(input('Введите челое число больше 0: '))
for i in range(N):
    print(K,end=' ')
print()

print('For2')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое которое больше А: '))
N = 0
for i in range(A,B+1): 
    print(i,end=' ') 
    N = N+1
print('Кол-во =',N)

print('For3')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое которое больше А: '))
N = 0
for i in range(B-1,A,-1): 
    print(i,end=' ') 
    N = N+1
print('Кол-во =',N)

print('For4')
a = int(input('Введите вещественное число цена 1 кг конфет: '))
for i in range(1,11):
    print(i*a)
print()

print('For5')
a = int(input('Введите вещественное число цена 1 кг конфет: '))
for i in range(1, 11):
    print((i/10)*a)
print()

print('For6')
a = int(input('Введите вещественное число цена 1 кг: '))
for i in range(12, 21, 2):
    i = (i/10)*a
    print(i)
print()

print('For7')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое которое больше А: '))
score = 0
for i in range(A,B+1):
    score += i
print(score)
print()

print('For8')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое которое больше А: '))
score = 1
for i in range(A,B+1):
    score *= i
print(score)
print()

print('For9')
A = int(input('Введите целое число А: '))
B = int(input('Введите целое которое больше А: '))
score = 1
for i in range(A,B+1):
    score += pow(i,2)
print(score-1)
print()

print('For10')
N = int(input('Введите целое вещественное число больше 0: '))
s = 0
for i in range(1,N+1):
    i = 1/i
    s = s+i
print(s)
print()

print('For11')
N = int(input('Введите целое вещественное число больше 0: '))
s = None
d = 0
u = pow(2*N,2)
for i in range(0,N+1):
    s = pow(N+i,2)
    d += s
print('summa =',d+u)
print()

print('For12')
n = int(input('Введите целое цисло >0: ')) 
score = 1
for i in range(11,n*10): 
	score = (score * i)/10
print(f'Тотал: {score}')
print()

print('For13')   #Сделали в классе
N = int(input('Введите целое число N>0: '))
t = 1
for i in range(1,N+1):
    t += (i/10-(i+1)/10)
    print(t)

print('For14')
N = int(input('Введите целое число > 0: '))
a = 0
for i in range(1,2*N,2):
    a = a+i
print(f'N^2 = {a}')
print()

print('For15')
A = int(input('Введите целое вещественное число: '))
N = int(input('Введите целое число > 0: '))
s = None
for i in range(1,N+1):
    s = pow(A,i)
print(s)
print()

print('For16')
A = int(input('Введите целое вещественное число: '))
N = int(input('Введите целое число > 0: '))
sope = None
for i in range(N):
    sope = pow(A,i)
    print(sope)
print()

print('For17')
A = int(input('Введите целое вещественное число: '))
N = int(input('Введите целое число > 0: '))
sope = 0
for i in range(N+1):
    sope += (pow(A,i))
print(sope)
print()

print('For18')

print('For19')
N = int(input('Введите целое вещественное число >0: '))
scoree = 1
for i in range(1,N+1):
    scoree *= i
print(scoree)
print()

print('For20')
N = int(input('Введите целое вещественное число >0: '))
scoree = 1
ty = 0
for i in range(1,N+1):
    scoree *= i 
    ty += scoree
print(ty)
print()   

print('For21')
N = int(input('Введите целое вещественное число >0: '))
scoree = 1
sth = 1
for i in range(1,N+1):
    scoree *= i
    sth += (1/scoree)
    print(sth)
print()

print('For22')
X = int(input('Введите вещественное число X: '))
N = int(input('Введите целое вещественное число >0: '))
scoree = 1
sth = 1
for i in range(1,N+1):
    scoree *= i
    sth += pow(X,i)/scoree 
print(sth) 
print()

print('For23')     #Сделали в классе
n = int(input('n: '))
x = int(input('x: '))
factorial = 1
score = 0 
for i in range(1, n+1):
  factorial *= i 
  pow_x = pow(x, i)
  if i % 2 != 0:
    score += (pow(-1,i)*(pow_x))/(factorial)
    print(score)
print()

print('For24')

print('for25')

print('For26')

print('For27')

print('For28')

print('For29')
N = int(input('Введите целое число N>1: '))
A = int(input('Введите вещественное целое число А: '))
B = int(input('Введите вещественное целое число В>A: '))
for i in range(A,B+1,N):
    H = N
    print(f'Набор точек = {i}')
print(f'Длина отрезков = {N}')
print()

print('For30')
N = int(input('Введите целое число N>1: '))  #2
A = int(input('Введите вещественное целое число А: '))  #0
B = int(input('Введите вещественное целое число В>A: '))   #16
for i in range(A,B+1,N):
    H = N
    print(f'Набор точек = {i}')
    print(f'F({i}) = 1-sin({i})')
print(f'Длина отрезков = {N}')
print()

print('For31')

print('For32')

print('For33')

print('For34')

print('For35')

print('For36')
N = int(input('Введите целое положительное число N: '))
K = int(input('Введите целое положительное число K: '))
sth = 0
for i in range(1,N+1):
    sth += pow(i,K)
print(f'Total = {sth}')
print()

print('For37')
N = int(input('Введите целое вещественное число N>0: '))
sth = 0
for i in range(1,N+1):
    sth += pow(i,i)
print(f'Total = {sth}')
print()

print('For38')
N = int(input('Введите целое вещественное число N>0: '))
sth = N
por = 0
for i in range(2,N+1):
    sth -= 1
    iut = pow(i,sth) 
    por += iut
    out = pow(1,N)
    print(f'Total = {out+por}')
print()

print('For39')
A = int(input('Введите целое положительное число А: '))
B = int(input('Введите целое положительное число В>A: '))
inb = 0
for i in range(A,B+1):
    print(str(i)*i,end=' ')
print()

print('For40')
A = int(input('Введите целое положительное число А: '))
B = int(input('Введите целое положительное число В>A: '))
inb = 0
for i in range(A,B+1):
    inb += 1
    print(str(i)*inb)
print()
