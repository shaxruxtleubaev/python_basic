print('If1')
a = int(input('Введите целое число: '))
if a>0:
	a+=1
	print(a)
elif a<0:
	print(a)
else:
	print(a)
print()

print('If2')
a = int(input('Введите целое число: '))
if a>0:
    a+=1
    print(a)
elif a<0:
	a-=2
	print(a)
else:
	print(a)
print()

print('If3')
a = int(input('Введите целое число: '))
if a > 0:
	a += 1
	print(a)
elif a<0:
	a-=2
	print(a)
else:
	a += 10
	print(a)
print()

print('If4')
a = int(input('Введите целое число a: '))
b = int(input('Введите целое число b: '))
c = int(input('Введите целое число c: '))
print((a > 0) + (b > 0) + (c > 0),'положительных чисел')
print()

print('If5')
a = int(input('Введите целое число a: '))
b = int(input('Введите целое число b: '))
c = int(input('Введите целое число c: '))
print((a > 0) + (b > 0) + (c > 0),'положительных чисел')
print((a < 0) + (b < 0) + (c < 0),'отрицательных чисел')
print()

print('If6')
A = int(input('Введите любое число A: '))
B = int(input('Введите любое число B: '))
if A>B:
	print(A)
elif A<B:
	print(B)
else:
	print('Equal')
print()

print('If7')
a1 = int(input('Введите числа a1: '))
a2 = int(input('Введите числа a2: '))
if a1<a2:
	print(1)
elif a2<a1:
	print(2)
print()

print('If8')
a1 = int(input('Введите числа a1: '))
a2 = int(input('Введите числа a2: '))
if a1>a2:
	print(a1)
	print(a2)
elif a1<a2:
	print(a2)
	print(a1)
else:
	print(None)
print()

print('If9')
A = input('Введите число A: ')
B = input('Введите число B: ')
if A<B:
	pass
elif A>B:
	A,B=B,A
print('A = ',A)
print('B = ',B)
print()

print('If10')
A = int(input('Введите целое число A:'))
B = int(input('Введите целое число B:'))
if A!=B:
	A=A+B
	B=A
elif A==B:
	A=0
	B=0
print(A,B)
print()

print('If11')
A = int(input('Введите целое число A:'))
B = int(input('Введите целое число B:'))
if A!=B:
	if A>B:
		B=A
	elif A<B:
		A=B
elif A==B:
	A=0
	B=0
print(A,B)
print()

print('If12')
num1 = int(input('Введите любое число: '))
num2 = int(input('Введите любое число: '))
num3 = int(input('Введите любое число: '))
if num1<=num2 and num1<=num3:
	print('Наим-шее число = ',num1)
elif num2<=num1 and num2<=num3:
	print('Наим-шее число = ',num2)
elif num3<=num1 and num1<=num2:
	print('Наим-шее число = ',num3)
print()

print('If13')
num1 = int(input('Введите любое число: '))
num2 = int(input('Введите любое число: '))
num3 = int(input('Введите любое число: '))
if num2>num1>num3 or num3>num1>num2:
	print('Ср число = ',num1)
elif num1>num2>num3 or num3>num2>num1:
	print('Ср число = ',num2)
elif num1>num3>num2 or num2>num3>num1:
	print('Ср число = ',num3)
print()

print('If 14')
num1 = int(input('Введите любое число: '))
num2 = int(input('Введите любое число: '))
num3 = int(input('Введите любое число: '))
menshe = None
bolshe = None
if num1<=num2 and num1<=num2:
	menshe = num1
if num1>=num2 and num1>=3:
	bolshe = num1
if num2<=num1 and num2<=num3:
	menshe = num2
if num2>=num1 and num2>=num3:
	bolshe = num2
if num3<=num1 and num3<=num2:
	menshe = num3
if num3>=num1 and num3>=num2:
	bolshe = num3
print('Наименьшее число = ',menshe)
print('Наибольшее число = ',bolshe)
print()

print('If15')
num1 = int(input('Введите любое число: '))
num2 = int(input('Введите любое число: '))
num3 = int(input('Введите любое число: '))
summa = None
if num1>num3 and num2>num3:
	summa = num1+num2
elif num2>num1 and num3>num1:
	summa = num2+num3
elif num3>num2 and num1>num2:
	summa = num1+num3
print('Сумма двух наибольших из них = ',summa)
print()

print('If16')
A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
C = int(input('Введите число C: '))
if A<B<C:
	A=A*2
	B=B*2
	C=C*2
	print('A =',A,'B =',B,'C =',C)
else:
	A=(-A)
	B=(-B)
	C=(-C)
	print('A =',A,'B =',B,'C =',C)
print()

print('If17')
A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
C = int(input('Введите число C: '))
if A>B>C or A<B<C:
	A=A*2
	B=B*2
	C=C*2
	print('A =',A,'B =',B,'C =',C)
else:
	A=(-A)
	B=(-B)
	C=(-C)
	print('A =',A,'B =',B,'C =',C)
print()

print('If18')
print('Введите 2 одинаковых, 1 отличающихся целых чисел')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a==b:
	print(3)
elif a==c:
	print(2)
elif b==c:
	print(1)
print()

print('If19')
print('Введите 3 одинаковых, 1 отличающихся целых чисел')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
if a==b==c:
	print(4)
elif a==b==d:
	print(3)
elif a==c==d:
	print(2)
elif b==c==d:
	print(1)
print()

print('If20')
A = int(input('Введите любое число A:'))
B = int(input('Введите любое число B:'))
C = int(input('Введите любое число C:'))
if abs(A-B)<abs(A-C):
	print(B)
	print('Расстояние = ',abs(A-B))
elif abs(A-B)>abs(A-C):
	print(C)
	print('Расстояние = ',abs(A-C))
print()

print('If21')
x = int(input('Введите целое число x:'))
y = int(input('Введите целое число y:'))
if x==0 and y==0:
	print(0)
elif x==0 and y!=0:
	print(1)
elif x!=0 and y==0:
	print(2)
elif x!=0 and y!=0:
	print(3)
print()

print('If22')
x = int(input('Введите целое число x:'))
y = int(input('Введите целое число y:'))
if x>0 and y>0:
	print('1 четверть')
elif x<0 and y>0:
	print('2 четверть')
elif x<0 and y<0:
	print('3 четверть')
elif x>0 and y<0:
	print('4 четверть')
print()

print('If23')
x1 = int(input('Введите целое число x1: ')) #1
x2 = int(input('Введите целое число y1: ')) #1
y1 = int(input('Введите целое число x2: ')) #1
y2 = int(input('Введите целое число y2: ')) #3
x3 = int(input('Введите целое число x3: ')) #4
y3 = int(input('Введите целое число y3: ')) #1
x4 = None
y4 = None
if x2==x3:
	x4=x1
if x3==x1:
	x4=x2
if x1==x2:
	x4=x3
if y2==y3:
	y4=y1
if y3==y1:
	y4=y2
if y1==y2:
	y4=y3
print('Координаты четвертой вершины x=',x4,'y=',y4)
print()

print('If24')

print('If25')
x = int(input('Введите вещественное число х: '))
f_x = None
if x<-2 or x>2:
	f_x = 2*x
else:
	f_x = -3*x
print('f(x) = ',f_x)
print()

print('If26')
x = int(input('Введите вещественное число х: '))
f_x = None
if x<=0:
	f_x = -x
elif 0<x<2:
	f_x = x**2
elif x>=2:
	f_x = 4
print('f(x) = ',f_x)
print()

print('If27')
x = int(input('Введите вещественное число х: '))
f_x = None
if x<0:
	f_x = 0
elif x%2 == 0:
	f_x = 1
else:
	f_x = -1
print('f(x) =',f_x)
print()

print('If28')
god = int(input('Введите целое положительное число года: '))
if god == 300 or god == 1300 or god==1900:
	print('365 дней')
elif god == 1200 or god == 2000:
	print('366 дней')
elif god%4 == 0:
	print('366 дней')
else:
	print('365 дней')
print()

print('If29')
a = int(input('Введите целое число: '))
if a<0 and a%2==0:
	print('Отрицательное четное число')
if a<0 and a%2!=0:
	print('Отрицательное нечетное число')
if a==0:
	print('Нулевое число')
if a>0 and a%2!=0:
	print('Положительное нечетное число')
if a>0 and a%2==0:
	print('Положительное четное число')
print()

print('If30')
a = int(input('Введите целое числов диапазоне 1-999: '))
if 0<a<10 and a%2==0:
	print('Четное однозначное число')
if 0<a<10 and a%2!=0:
	print('Нечетное однозначное число')
if 9<a<100 and a%2==0:
	print('Четное двузначное число')
if 9<a<100 and a%2!=0:
	print('Нечетное двузначное число')
if 99<a<1000 and a%2==0:
	print('Четное трехзначное число')
if 99<a<1000 and a%2!=0:
	print('Нечетное трехзначное число')
print()












