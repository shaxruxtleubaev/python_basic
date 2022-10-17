
print('Case1')
a=int(input('Введите целое число в диапазоне 1-7: '))
if a==1:
	print('Понедельник')
elif a==2:
	print('Вторник')
elif a==3:
	print('Среда')
elif a==4:
	print('Четверг')
elif a==5:
	print('Пятница')
elif a==6:
	print('Суббота')
elif a==7:
	print('Воскресенье')
print()

print('Case2')
K=int(input('Введите целое число в диапазоне 1-5: '))
if K==1:
	print('Плохо')
elif K==2:
	print('Неудовлетворительно')
elif K==3:
	print('Удовлетворительно')
elif K==4:
	print('Хорошо')
elif K==5:
	print('Отлично')
else:
	print('ошибка')
print()

print('Case3')
nomer = int(input('Введите целое число месяца в диапазоне 1-12: '))
if nomer == 1 or nomer == 2 or nomer == 12: 
	print('Зима')
elif nomer == 3 or nomer == 4 or nomer == 5:
	print('Весна')
elif nomer == 6 or nomer == 7 or nomer == 8:
	print('Лето')
elif nomer == 9 or nomer == 10 or nomer == 11:
	print('Осень')
else:
	print('ошибка')
print()

print('Case4')
nomer = int(input('Введите целое число месяца в диапазоне 1-12: '))
if nomer == 1 or nomer == 3 or nomer == 5 or nomer == 7 or nomer == 8 or nomer == 10 or nomer == 12: 
	print('В этом месяце 31 дней')
elif nomer == 2:
	print('В этом месяце 28 дней')
elif nomer == 4 or nomer == 6 or nomer == 9 or nomer == 11:
	print('В этом месяце 30 дней')
else:
	print('ошибка')
print()

print('Case5')
A = int(input('Введите вещественное число: '))
B = int(input('Введите вещественное число не равное 0: '))
N = int(input('Выберите один из следующих действии: 1 - сложение, 2 - вычитание, 3 - умножение и 4 - деление: '))
if N == 1:
	print('Сложение чисел =',A+B)
elif N == 2:
	print('Вычитание чисел =',A-B)
elif N == 3:
	print('Умножение чисел =',A*B)
elif N == 4:
	print('Деление чисел =',A/B)
else:
	print('ошибка')
print()

print('Case6')
print('Выберите один из следующих меров длины для действия: 1-дециметр, 2-километр, 3-метр, 4-миллиметр, 5-сантиметр')
a = int(input('Выберите меру длины: '))
b = int(input('Введите длину: '))
if a == 1:
	print(b,'дм =',b/100,'метров')
elif a == 2:
	print(b,'км =',b*1000,'метров')
elif a == 3:
	print(b,'м = ',b,'метров')
elif a == 4:
	print(b,'мм =',b/1000,'метров')
elif a == 5:
	print(b,'см =',b/100,'метров')
else:
	print('ошибка')
print()

print('Case7')
print('Выберите один из следующих меров массы для действия: 1-килограмм, 2-миллиграмм, 3-грамм, 4-тонна, 5-центнер')
a = int(input('Выберите меру массы: '))
b = int(input('Введите массу: '))
if a == 1:
	print(b,'кг =',b,'кг')
elif a == 2:
	print(b,'мг =',b/1000000,'кг')
elif a == 3:
	print(b,'грамм = ',b/1000,'кг')
elif a == 4:
	print(b,'т =',b*1000,'кг')
elif a == 5:
	print(b,'цт =',b*100,'кг')
else:
	print('ошибка')
print()

print('Case8')  #это не я сделал
D = int(input('Введите день определенного месяца: '))
M = int(input('Введите номер определенного месяца: '))
if D != 1:
	D-=1
else:
	if M==1 or M==2 or M==4 or M==6 or M==8 or M==9 or M==11:
		D = 31
	elif M == 3:
		D = 28
	else:
		D = 30
	M -= 1
	if M == 0:
		M = 12
print(D,M)
print()
 
print('Case9')   #это не я сделал
d = int(input('Введите день определенного месяца: '))
m = int(input('Введите номер определенного месяца: '))
if m in [1, 3, 5, 7, 8, 10]:
    if d == 31:
        print(str(1) + ' ' + str(m + 1))
    else:
        print(str(d + 1) + ' ' + str(m))
elif m == 12:
    if d == 31:
        print(str(1) + ' ' + str(1))
    else:
        print(str(d + 1) + ' ' + str(m))
elif m == 2:
    if d == 28:
        print(str(1) + ' ' + str(m + 1))
    else:
        print(str(d + 1) + ' ' + str(m))  
else:
    if d == 30:
        print(str(1) + ' ' + str(m + 1))
    else:
        print(str(d + 1) + ' ' + str(m))
print()

print('Case10')
print('Робот сейчас в направлении к северу. Дайте ему новое направление: С - север, З - запад, Ю - юг, В - восток.')
N = input('Введите направление: ')
if N == 'С':
	print('Робот будет продолжать идти на север')
elif N == 'З':
	print('Робот направляется на запад')
elif N == 'Ю':
	print('Робот направляется на юг')
elif N == 'В':
	print('Робот направляется на восток')
else:
	print('Ошибка при вводе команды')
print()

print('Case11')
print('Локатор направлен на север. Дайте ему новое направление: 1 -поворот налево, -1 -поворот направо, 2 -поворот на 180градус. ')
a = int(input('Введите первый поворот: '))
b = int(input('Введите введите второй поворот после первого: '))
if a==1 and b==1:
	print('Локатор смотрит на юг')
elif a==1 and b==-1:
	print('Локатор смотрит на север')
elif a==1 and b==2:
	print('Локатор смотрит на восток')
elif a==-1 and b==-1:
	print('Локатор смотрит на юг')
elif a==-1 and b==1:
	print('Локатор смотрит на север')
elif a==-1 and b==2:
	print('Локатор смотрит на запад')
elif a==2 and b==2:
	print('Локатор смотрит на север')
elif a==2 and b==-1:
	print('Локатор смотрит на запад')
elif a==2 and b==1:
	print('Локатор смотрит на восток')
else:
	print('Ошибка при вводе')
print()

print('Case12')
Pi = 3.14
print('Выберите одну из следующих значении круга: 1 -радиус, 2 -диаметр, 3 -длина, 4 -площадь круга')
a = int(input('Введите ответ: '))
b = int(input('Введите значение ответа: '))
R = None
D = None
L = None
S = None
if a == 1:
	R = b
	D = 2*R
	L = 2*Pi*R
	S = Pi*pow(R,2)
	print('R =',R,'D =',D,'L =',L,'S =',S)
elif a == 2:
	D = b
	R = D/2
	L = 2*Pi*R
	S = Pi*pow(R,2)
	print('R =',R,'D =',D,'L =',L,'S =',S)
elif a == 3:
	L = b
	R = L/(2*Pi)
	D = 2*R
	S = Pi*pow(R,2)
	print('R =',R,'D =',D,'L =',L,'S =',S)
elif a == 4:
	S = b
	R = pow(S/Pi,0.5)
	D = 2*R
	L = 2*Pi*R
	print('R =',R,'D =',D,'L =',L,'S =',S)
else:
	print('Ошибка при вводе')
print()

print('Case13')
print('Выберите один из следующих элементов равнобедренного прямоугольного треугольника: 1 -катет a, 2-гипотенуза, 3 -высота h (опущенная на гипотенузу), 4 -площадь')
s = int(input('Введите ответ: '))
z = int(input('Введите целое значение для элемента: '))
a = None
c = None
h = None
S = None
if s == 1:
	a = z
	c = a*pow(2,0.5)
	h = c/2
	S = c*h/2
	print('a =',a,'c = ',c,'h =',h,'S =',S)
elif s == 2:
	c = z
	a = c/pow(2,0.5)
	h = c/2
	S = c*h/2
elif s == 3:
	h = z
	c = h*2
	a = c/pow(2,0.5)
	S = c*h/2
	print('a =',a,'c = ',c,'h =',h,'S =',S)
elif s == 4:
	S = z
	print('c*h =',S*2,'S =',S,'a = c/2**0.5')
else:
	print('Ошибка при вводе')
print()

print('Case14')
print('Выберите один из элементов равностороннего треугольника: 1 -сторона а, 2 -радиус R1 вписанной окружности, 3 -радиус R2 описанной окружности, 4 -площадь S' )
x = int(input('Выберите элемент равностороннего треугольника: '))
y = int(input('Дайте значение для выбранного элемента: '))
a = None
R1 = None
R2 = None
S = None
if x == 1:
	a = y
	R1 = (a*pow(3,0.5))/6
	R2 = 2*R1
	S = (pow(a,2)*pow(3,0.5))/4
	print('a =',a,'R1 =',R1,'R2 =',R2,'S =',S)
elif x == 2:
	R1 = y
	a = R1/(pow(3,0.5)/6)
	R2 = 2*R1
	S = (pow(a,2)*pow(3,0.5))/4
	print('a =',a,'R1 =',R1,'R2 =',R2,'S =',S)
elif x == 3:
	R2 = y
	R1 = R2/2
	a = R1/(pow(3,0.5)/6)
	S = (pow(a,2)*pow(3,0.5))/4
	print('a =',a,'R1 =',R1,'R2 =',R2,'S =',S)
elif x == 4:
	S = y
	a = (S/(pow(3,0.5)/4))**0.5
	R1 = (a*pow(3,0.5))/6
	R2 = R1*2
	print('a =',a,'R1 =',R1,'R2 =',R2,'S =',S)
else:
	print('Ошибка при вводе')
print()

print('Case15')
print('Выберите один из следующих мастей карты: 1 -пики, 2 -трефы, 3 -бубны, 4 -червы')
M = int(input('Введите ответ: '))
print('Теперь введите достоинству карты в диапазоне 6-10 или же выберите один из следующих: 11 -валет, 12 -дама, 13 -король, 14 -туз')
N = int(input('Введите ответ: '))
if M==1 and N==6:
	print('6 пики')
elif M==1 and N==7:
	print('7 пики')
elif M==1 and N==8:
	print('8 пики')
elif M==1 and N==9:
	print('9 пики')
elif M==1 and N==10:
	print('10 пики')
elif M==1 and N==11:
	print('валет пики')
elif M==1 and N==12:
	print('дама пики')
elif M==1 and N==13:
	print('король пики')
elif M==1 and N==14:
	print('туз пики')
elif M==2 and N==6:
	print('6 трефы')
elif M==2 and N==7:
	print('7 трефы')
elif M==2 and N==8:
	print('8 трефы')
elif M==2 and N==9:
	print('9 трефы')
elif M==2 and N==10:
	print('10 трефы')
elif M==2 and N==11:
	print('валет трефы')
elif M==2 and N==12:
	print('дама трефы')
elif M==2 and N==13:
	print('король трефы')
elif M==2 and N==14:
	print('туз трефы')
elif M==3 and N==6:
	print('6 бубны')
elif M==3 and N==7:
	print('7 бубны')
elif M==3 and N==8:
	print('8 бубны')
elif M==3 and N==9:
	print('9 бубны')
elif M==3 and N==10:
	print('10 бубны')
elif M==3 and N==11:
	print('валет бубны')
elif M==3 and N==12:
	print('дама бубны')
elif M==3 and N==13:
	print('король бубны')
elif M==3 and N==14:
	print('туз бубны')
elif M==4 and N==6:
	print('6 червы')
elif M==4 and N==7:
	print('7 червы')
elif M==4 and N==8:
	print('8 червы')
elif M==4 and N==9:
	print('9 червы')
elif M==4 and N==10:
	print('10 червы')
elif M==4 and N==11:
	print('валет червы')
elif M==4 and N==12:
	print('дама червы')
elif M==4 and N==13:
	print('король червы')
elif M==4 and N==14:
	print('туз червы')
print()

print('Case16')
a = int(input('Введте возраст в диапазоне 20-69: '))
if a >= 20 and a <= 69:
	if a == 20:
		print('Двадцать лет')
	if a == 21:
		print('Двадцать один год ')
	if a == 22:
		print('Двадцать два года ')
	if a == 23:
		print('Двадцать три года ')	
	if a == 24:
		print('Двадцать четыре года ')
	if a == 25:
		print('Двадцать четыре года ')
	if a == 26:
		print('Двадцать шесть года ')
	if a == 27:
		print('Двадцать семь года ')
	if a == 28:
		print('Двадцать восемь года ')
	if a == 29:
		print('Двадцать девять года ')
	if a == 30:
		print('Тридцать лет ')
	if a == 31:
		print('Тридцать один год ')
	if a == 32:
		print('Тридцать два года ')
	if a == 33:
		print('Тридцать три года ')
	if a == 34:
		print('Тридцать четыре года ')
	if a == 35:
		print('Тридцать пять года ')
	if a == 36:
		print('Тридцать шесть года ')
	if a == 37:
		print('Тридцать семь года ')
	if a == 38:
		print('Тридцать восемь года ')
	if a == 39:
		print('Тридцать девять года ')
	if a == 40:
		print('Сорок лет ')
	if a == 41:
		print('Сорок один год ')
	if a == 42:
		print('Сорок два года ')
	if a == 43:
		print('Сорок три года ')
	if a == 44:
		print('Сорок четыре года ')
	if a == 45:
		print('Сорок пять года ')
	if a == 46:
		print('Сорок шесть года ')
	if a == 47:
		print('Сорок семь года ')
	if a == 48:
		print('Сорок восемь года ')
	if a == 49:
		print('Сорок девять года ')
	if a == 50:
		print('Пятьдесят лет ')
	if a == 51:
		print('Пятьдесят один год ')
	if a == 52:
		print('Пятьдесят два года ')
	if a == 53:
		print('Пятьдесят три года ')
	if a == 54:
		print('Пятьдесят четыре года ')
	if a == 55:
		print('Пятьдесят пять года ')
	if a == 56:
		print('Пятьдесят шесть года ')
	if a == 57:
		print('Пятьдесят семь года ')
	if a == 58:
		print('Пятьдесят восемь года ')
	if a == 59:
		print('Пятьдесят девять года ')
	if a == 60:
		print('Шестьдесят лет ')
	if a == 61:
		print('Шестьдесят один год ')
	if a == 62:
		print('Шестьдесят два года ')
	if a == 63:
		print('Шестьдесят три года ')
	if a == 64:
		print('Шестьдесят четыре года ')
	if a == 65:
		print('Шестьдесят пять года ')
	if a == 66:
		print('Шестьдесят шесть года ')
	if a == 67:
		print('Шестьдесят семь года ')
	if a == 68:
		print('Шестьдесят восемь года ')
	if a == 69:
		print('Шестьдесят девять года ')
print()












