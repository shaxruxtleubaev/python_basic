print('Integer1')
L = int(input('Введите число для сантиметра: ')) #сантиметр
metr = L/100
print('Расстояние = ',metr,'метров')
print()

print('Integer2')
M = int(input('Введите число для кг: ')) #кг
T = M/1000
print('Масса = ',T,'тонна')
print()

print('Integer3')
Bayt = int(input('Введите число для Байта: '))
Kilobayt = Bayt/1024
print('Размер файла = ',Kilobayt,'КБ')
print()

print('Integer4')
A = int(input('Введите число A для длины: '))
B = int(input('Введите число B которое меньше чем A: '))
Max_amount_otrezki = A//B
print('Максимальное кол-во отрезков',B,'в',A,'равен',Max_amount_otrezki)
print()

print('Integer5')
A = int(input('Введите число A для  длины: '))
B = int(input('Введите число B которое меньше чем A: '))
Nezanyataya_chast = A%B
print('Незянатая часть = ',Nezanyataya_chast)
print()

print('Integer6')
a = int(input('Введите двузначное число: '))
levaya_sifra = a//10
pravaya_sifra = a%10
print('Значение левого числа = ',levaya_sifra)
print('Значение правого числа = ',pravaya_sifra)
print()

print('Integer7')
a = int(input('Введите двузначное число: '))
print('Сумма данного числа = ',a+a)
print('Произведение данного числа = ',a*a)
print()

print('Integer8')
a = int(input('Введите двузначное число: '))
levaya_sifra = a//10
pravaya_sifra = a%10
print('Переставление данного числа = ',str(pravaya_sifra)+str(levaya_sifra))
print()

print('Integer9')
a = int(input('Введите трехзначное число: '))
pervaya_sifra = a//100
print('Первая цифра данного числа = ',pervaya_sifra)
print()

print('Integer10')
a = int(input('Введите трехзначное число: '))
b = a%100
poslednaya_sifra = b%10
srednaya_sifra = b//10
print('Последняя цифра данного = ',poslednaya_sifra)
print('Средняя цифра данного = ',srednaya_sifra)
print()

print('Integer11')
a = int(input('Введите трехзначное число: '))
print('Сумма данного числа = ',a+a)
print('Произведение данного числа  = ',a*a)
print()

print('Integer12')
a = int(input('Введите трехзначное число: '))
print('Первое число данного = ',a//100)
print('Второе число данного = ',(a%100)//10)
print('Третье число данного = ',(a%100)%10)
print()

print('Integer13')
a = int(input('Введите трехзначное число: '))
vicherknutoe_chislo = a//100
ostatok = a%100
poluchennoe_chislo = str(ostatok)+str(vicherknutoe_chislo)
print('Полученное число = ',poluchennoe_chislo)
print()

print('Integer14')
a = int(input('Введите трехзначное число: '))
tretye_chislo = (a%100)%10
vtoroye_chislo = (a%100)//10
pervoye_chislo = a//100
print('Результат данного числа = ',str(tretye_chislo)+str(pervoye_chislo)+str(vtoroye_chislo))
print()

print('Integer15')
a = int(input('Введите трехзначное число: '))
tretye_chislo = (a%100)%10
vtoroye_chislo = (a%100)//10
pervoye_chislo = a//100
print('Результат = ',str(vtoroye_chislo)+str(pervoye_chislo)+str(tretye_chislo))
print()

print('Integer16')
a = int(input('Введите трехзначное число: '))
tretye_chislo = (a%100)%10
vtoroye_chislo = (a%100)//10
pervoye_chislo = a//100
print('Ответ = ',str(pervoye_chislo)+str(tretye_chislo)+str(vtoroye_chislo))
print()

print('Integer17')
a = int(input('Введите число которое больше чем 999: '))
deleniye_nacelo = a//100
vzyatie_ostatki_deleniya = a%100
print('Деление нацело = ',deleniye_nacelo)
print('Деление взятия остатков = ',vzyatie_ostatki_deleniya)
print()

print('Integer18')
a = int(input('Введите число которое больше чем 999: '))
deleniye_nacelo = a//1000
vzyatie_ostatki_deleniya = a%1000
print('Деление нацело = ',deleniye_nacelo)
print('Деление взятия остатков = ',vzyatie_ostatki_deleniya)
print()

print('Integer 19')
N = int(input('Введите целое число секунда: '))
minute = N/60
print(f'С начало суток прошло {minute} минута')
print()

print('Integer20')
N = int(input('Введите целое число секунда больше чем 3600: '))
hour = (N/60)/60
print('С начало суток прошло',hour,'часов')
print()

print('Integer21')
N = int(input('Введите целое число секунда больше чем 3600: '))
seconds = N%60
print('Количество пройденных секунд с последнего минута = ',seconds)
print()

print('Integer22')
N = int(input('Введите целое число секунда больше чем 3600: '))
seconds = (N%3600)
print('Количество пройденных секунд с последнего часа = ',seconds)
print()

print('Integer23')
N = int(input('Введите целое число секунда больше чем 3600: '))
seconds = (N%3600)/60
print('Количество пройденных минут с последнего часа = ',seconds)
print()

print('Integer24')
K = int(input('Введите любое число дня года в диапазоне 1-365: '))
N = 1
otvet = (((K+N)-2)%7)+1
if otvet == 1:
	print('Понедельник')
elif otvet == 2:
	print('Вторник')
elif otvet == 3:
	print('Среда')
elif otvet == 4:
	print('Четверг')
elif otvet == 5:
	print('Пянтница')
elif otvet == 6:
	print('Суббота')
else:
	print('Воскресенье')
print()

print('Integer25')
K = int(input('Введите любое число дня года в диапазоне 1-365: '))
N = 4
otvet = (((K+N)-2)%7)+1
if otvet == 1:
	print('Понедельник')
elif otvet == 2:
	print('Вторник')
elif otvet == 3:
	print('Среда')
elif otvet == 4:
	print('Четверг')
elif otvet == 5:
	print('Пянтница')
elif otvet == 6:
	print('Суббота')
else:
	print('Воскресенье')
print()

print('Integer26')
K = int(input('Введите любое число дня года в диапазоне 1-365: '))
N = 2
otvet = (((K+N)-2)%7)+1
if otvet == 1:
	print('Понедельник')
elif otvet == 2:
	print('Вторник')
elif otvet == 3:
	print('Среда')
elif otvet == 4:
	print('Четверг')
elif otvet == 5:
	print('Пянтница')
elif otvet == 6:
	print('Суббота')
else:
	print('Воскресенье')
print()

print('Integer27')
K = int(input('Введите любое число дня года в диапазоне 1-365: '))
N = 6
otvet = (((K+N)-2)%7)+1
if otvet == 1:
	print('Понедельник')
elif otvet == 2:
	print('Вторник')
elif otvet == 3:
	print('Среда')
elif otvet == 4:
	print('Четверг')
elif otvet == 5:
	print('Пянтница')
elif otvet == 6:
	print('Суббота')
else:
	print('Воскресенье')
print()

print('Integer28')
K = int(input('Введите любое число дня года в диапазоне 1-365: '))
N = int(input('Введите любое число дня недели в диапазоне 1-7: '))
otvet = (((K+N)-2)%7)+1
if otvet == 1:
	print('Понедельник')
elif otvet == 2:
	print('Вторник')
elif otvet == 3:
	print('Среда')
elif otvet == 4:
	print('Четверг')
elif otvet == 5:
	print('Пянтница')
elif otvet == 6:
	print('Суббота')
else:
	print('Воскресенье')
print()

print('Integer29')
A = int(input('Введите число A: '))
B = int(input('Введите число B: '))
C = int(input('Введите число C: '))
razmer_pryamougolnika = A*B
razmer_kvadrata = C**2
kol_vo_kvadratov_vnutri_pryamougolnika = razmer_pryamougolnika//razmer_kvadrata
S_nezanyatoy_chast_pryamougolnika = razmer_pryamougolnika%razmer_kvadrata
print('Количество квадратов размещенных на прямоугольнике = ',kol_vo_kvadratov_vnutri_pryamougolnika)
print('Площадь незанятой части прямоугольника = ',S_nezanyatoy_chast_pryamougolnika)
print()

print('Integer30')
god = int(input('Введите год: '))
znacheniye_stoletiya = ((god*20)/1901)//1
print('Номер столетия = ',znacheniye_stoletiya)
print()
#-------------------------------------------------------------------------------

print('Boolean1')
A = int(input('Введите любое число: '))
if A >= 0:
	print(True)
else:
	print(False)
print()

print('Boolean2')
A = int(input('Введите любое число: '))
B = A%2
if B != 0:
	print('True')
else:
	print('False')
print()

print('Boolean3')
A = int(input('Введите любое число: '))
B = A%2
if B == 0:
	print('True')
else:
	print('False')
print()

print('Boolean4')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
if A>2 and B<=3:
	print('True')
else:
	print('False')
print()

print('Boolean5')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
if A>=0 or B<-2:
	print('True')
else:
	print('False')
print()

print('Boolean6')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A<B<C:
	print(True)
else:
	print(False)
print()

print('Boolean7')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A<B<C or A>B>C:
	print('True')
else:
	print('False')
print()

print('Boolean8')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = A%2
D = B%2
if C and D != 0:
	print(True)
else:
	print(False)
print()

print('Boolean9')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = A%2
D = B%2
if C or D != 0:
	print(True)
else:
	print(False)
print()

print('Boolean10')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = A%2
D = B%2
if C != 0 and D == 0 or C == 0 and D != 0:
	print(True)
else:
	print(False)
print()

print('Boolean11')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = A%2
D = B%2
if C != 0 and D != 0 or C == 0 and D == 0:
	print(True)
else:
	print(False)
print()

print('Boolean12')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A > 0 and B > 0 and C > 0:
	print(True)
else:
	print(False)
print()

print('Boolean13')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A > 0 or B > 0 or C > 0:
	print(True)
else:
	print(False)
print()

print('Boolean14')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A>0 and B<0 and C<0 or A<0 and B>0 and C<0 or A<0 and B<0 and C>0:
	print(True)
else:
	print(False)
print()

print('Boolean15')
A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
C = int(input('Введите целое число C: '))
if A>0 and B>0 and C<0 or A>0 and B<0 and C>0 or A<0 and B>0 and C>0:
	print(True)
else:
	print(False)
print()

print('Boolean16')
A = int(input('Введите целое положительное число : '))
B = A%2
if A>9 and A<100 and B == 0:
	print(True)
else:
	print(False)
print()

print('Boolean17')
A = int(input('Введите целое положительное число : '))
B = A%2
if A>99 and A<1000 and B != 0:
	print(True)
else:
	print(False)
print()

print('Boolean18')
A = int(input('Введите любое число A: '))
B = int(input('Введите любое число B: '))
C = int(input('Введите любое число C: '))
if A==B or A==C or B==C:
	print(True)
else:
	print(False)
print()

print('Boolean19')
A = int(input('Введите любое число A: '))
B = int(input('Введите любое число B: '))
C = int(input('Введите любое число C: '))
if A==(-B) or A==(-C) or B==(-A) or B==(-C) or C==(-A) or C==(-B):
	print(True)
else:
	print(False)
print()

print('Boolean20')
a = int(input('Введите трехзначное число: '))
a1 = a//100
a2 = (a%100)//10
a3 = (a%100)%10
if a1 != a2 != a3:
	print(True)
else:
	print(False)
print()

print('Boolean21')
a = int(input('Введите трехзначное число: '))
a1 = a//100
a2 = (a%100)//10
a3 = (a%100)%10
if a3 == (a2+1) and a2 == (a1+1):
	print(True)
else:
	print(False)
print()

print('Boolean22')
a = int(input('Введите трехзначное число: '))
a1 = a//100
a2 = (a%100)//10
a3 = (a%100)%10
if a3==(a2+1) and a2==(a1+1) or a2==(a1-1) and a3==(a2-1):
	print(True)
else:
	print(False)
print()

print('Boolean23')
a = int(input('Введите четырехзначное число: '))
a1 = a//1000
a2 = (a%1000)//100
a3 = ((a%1000)%100)//10
a4 = ((a%1000)%100)%10
if a1 == a2 == a3 == a4:
	print(True)
else:
	print(False)
print()

print('Boolean24')
A = int(input('Введите любое число A не равное 0: '))
B = int(input('Введите любое число B: '))
C = int(input('Введите любое число C: '))
D = pow(B,2)-4*A*C
if D >= 0:
	print(True)
else:
	print(False)
print()

print('Boolean25')
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x<0 and y>0:
	print(True)
else:
	print(False)
print()

print('Boolean26')
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x>0 and y<0:
	print(True)
else:
	print(False)
print()

print('Boolean27')
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x<0 and y>0 or x<0 and y<0:
	print(True)
else:
	print(False)
print()

print('Boolean28')
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x<0 and y<0 or x>0 and y>0:
	print(True)
else:
	print(False)
print()

print('Boolean29')
x = int(input('Введите значение x: '))    #2
y = int(input('Введите значение y: '))    #3
x1 = int(input('Введите значение x1: '))  #1
y1 = int(input('Введите значение y1: '))  #4
x2 = int(input('Введите значение x2: '))  #6
y2 = int(input('Введите значение y2: '))  #1
if x2>x>x1 and y2<y<y1:
	print(True)
else:
	print(False)
print()

print('Boolean30')
a = int(input('Введите любые целые положительное число a: '))
b = int(input('Введите любые целые положительное число b: '))
c = int(input('Введите любые целые положительное число c: '))
if a==b==c:
	print(True)
else:
	print(False)
print()

print('Boolean31')
a = int(input('Введите любые целые положительное число a: '))
b = int(input('Введите любые целые положительное число b: '))
c = int(input('Введите любые целые положительное число c: '))
if a==b!=c or a!=b==c or a==c!=b:
	print(True)
else:
	print(False)
print()

print('Boolean32')
a = int(input('Введите любые целые положительное число a: '))
b = int(input('Введите любые целые положительное число b: '))
c = int(input('Введите любые целые положительное число c: '))
if pow(a,2)+pow(b,2) == pow(c,2):
	print(True)
else:
	print(False)
print()

print('Boolean33')
a = int(input('Введите любые целые положительное число a: '))
b = int(input('Введите любые целые положительное число b: '))
c = int(input('Введите любые целые положительное число c: '))
if a+b>c or a+c>b or b+c>a:
	print(True)
else:
	print(False)
print()

print('Boolean34')
x = int(input('Введите целое число в диапазона 1-8 x: '))
y = int(input('Введите целое число в диапазона 1-8 y: '))
x1 = x%2
y1 = y%2
if x==1 and y==1 or x1==0 and y1==0:
	print(True)
else:
	print(False)
print()

print('Boolean35')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if (((x1+y1)%2)==((x2+y2)%2)):
	print(True)
else:
	print(False)
print()

print('Boolean36')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if x1==x2 or y1==y2:
	print(True)
else:
	print(False)
print()

print('Boolean37')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if (abs(x1-x2) and abs(y1-y2)) <=1:
	print(True)
else:
	print(False)
print()

print('Boolean38')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if abs(x1-x2)==abs(y1-y2):
	print(True)
else:
	print(False)
print()

print('Boolean39')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if x1==x2 or y1==y2 or abs(x1-x2)==abs(y1-y2):
	print(True)
else:
	print(False)
print()

print('Boolean40')
x1 = int(input('Введите целое число в диапазона 1-8 x1: '))
y1 = int(input('Введите целое число в диапазона 1-8 y1: '))
x2 = int(input('Введите целое число в диапазона 1-8 x2: '))
y2 = int(input('Введите целое число в диапазона 1-8 y2: '))
if (abs(x1-x2)==1) and (abs(y1-y2)==2) or (abs(x1-x2)==2) and (abs(y1-y2)==1):
	print(True)
else:
	print(False)
print()