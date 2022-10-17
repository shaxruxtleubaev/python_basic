import random
import tkinter
from tkinter import ttk


print('1.')
print('Существует 4 типа данных: string, integer, boolean, float. String - это строка, Integer - это целые числа, Boolean - это правда или ложь, Float - это нецелые числа')
print()

print('2.')
a = ((23+17)/2)%5
print(a)
print(type(a))
print()

print('3.')
print('print лишь выводит то что было написано внутри него, а return выводит результат функции и т.д.')
print()

print('4.')
a = int(input('Введите целое двухзначное число: '))
print(f'Сумма двузначного числа {a} = {(a//10) + (a%10)}')
print()

print('5.')
q = float(input('Введите любое число: '))
w = float(input('Введите любое число: '))
if q > w:
    print(f'{q} > {w}')
elif q < w:
    print(f'{q} < {w}')
elif q == w:
    print(f'{q} == {w}')
print()

print('6.')
for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')
print()

print('7.')
for i in range(6):
    if i != 3 and i != 6:
        print(i)
print()

print('8.')
for i in range(10):
    print('Я новичок', end=' ')
print()

print('9.')
even = []
odd = []
for i in range(20):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print()

print('10.')
box = 0
for i in range(1, 20):
    if i in range(5,15):
        box += i
print(box)
print()

print('11.')
for i in range(1, 11):
    print(f'{i / 10} - {i * 10} кг')
print()

print('12.')
a = 1
for i in range(1, 10):
    a *= i
    print(a)
print()

print('13.')
a = [random.randint(-10, 10) for i in range(5)]
print(a)
a.insert(3, 0)
print(a)
print()

print('14.')
a = [random.randint(1, 10) for i in range(5)]
print(a)
print(f'Сумма чисел списка  = {sum(a)}')
print()

print('15.')
a = [random.randint(-10, 10) for i in range(5)]
print(a)
a.sort()
print(f'Наибольшее число в списке = {a[-1]}')
print(f'Наименьшее число в списке = {a[0]}')
print()

print('16.')
a = [random.randint(-10, 10) for i in range(random.randint(0, 3))]
print(a)
if len(a) > 0:
    print('Список не пуст')
if len(a) == 0:
    print('Список пуст')
print()

print('17.')
t = ('A', 'd', 'wef')
print(t)
f = ''.join(t)
print(f)

print('18.')
dictionary = {
    'name':'Shakhrukh',
    'surname':'Tleubaev',
    'age':'15'
}
print(dictionary)
n = input('Введите любое слово, чтобы проверить, такой ключ есть или нет в данном словаре: ')
if n in dictionary.keys():
    print('Да, оно есть в словаре')
else:
    print('Нет, такой ключ нет в словаре')
print()

print('19.')
m = [random.randint(-20, 30) for i in range(10)]
print(set(m))
print(type(set(m)))
print()

print('20.')
def maximum(list):
    list.sort()
    return list[-1], list[-2]
m = [random.randint(-20, 30) for i in range(10)]
print(m)
print(maximum(m))
print()

print('21.')
def multiple(list):
    a = 1
    for i in range(len(list)):
        a *= list[i]
    return a
m = [random.randint(1, 7) for i in range(5)]
print(m)
print(multiple(m))
print()

print('22.')
def student(name, surname, age):
    return f'Имя: {name}, Фамилия: {surname}, Возраст: {age}'
name = input('Введите имя студента: ')
surname = input('Введите фамилию студента: ')
age = input('Введите возраст студента: ')
print(student(name, surname, age))
print()

print('23.')
class Home():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def student1(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}'

    def student2(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}'
print()

print('24.')
class App(tkinter.Tk):
    
    def __init__(self):
        super(App, self).__init__()
        self.title('Task 24')
        self.geometry('800x600')

if __name__ == '__main__':
    app = App()
    app.mainloop()
print()

print('25.')
window = tkinter.Tk()
window.geometry('800x600')
window.title('Task 25')
window.configure(bg='black')

text = ttk.Label(
    window,
    text='Exemple',
    font='Helvetica 35',
    foreground='white',
    background='black',
)
text.pack()
window.mainloop()
print()






