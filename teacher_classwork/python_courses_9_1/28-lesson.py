#def -> 
"""def findSum():          #outer def  
    def find_list():    #inner def
        arr = list(range(1,6))
        return arr 
    return sum(find_list())   #call inerr def
app = findSum()               #call outer def 
print(app)

list_1 = [3,2,1] #x
list_2 = [1,2,3] #y
box_ = list(map(lambda x,y: x**y, list_1, list_2))
print(box_)

def lists(list_1,list_2):
    results = list()
    for i in range(len(list_1)):
        results.append(list_1[i]**list_2[i])
    return results 
print(lists(list_1,list_2))"""

"""try:
    import goslate
    import cowsay 
except ModuleNotFoundError:
    print('Не найдена модуль!')
finally:
    sheep = cowsay.cow('Привет!')
    t_rex = cowsay.trex('Brrrrrr!')
    citty = cowsay.kitty('Miau, Miau!')
    tux = cowsay.tux('Arctica!')"""

'''
print(input("Здравствуйте в IQ test созданный Шахрухом. Нажмите на Enter чтобы продолжить. "))
print("Вы можете узнать свой IQ ответив на следующие вопросы.")
print("В конце опроса выводиться ваш уровень IQ")
input("Вы готовы начать? ")
print()
print("Тогда начнем")
print()
score = 69
print("Первый вопрос: Какое число не вписывается в этот ряд? ")
print("4")
print("9")
print("2")
a1 = input("Ответ: ")
while a1:
    if a1 == "4":
        score += 6
        break
    elif a1 == "9":
        score += 4
        break
    elif a1 == "2":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Второй вопрос: Какой цвет не вписывается в этот ряд? ")
print("Зеленый")
print("Желтый")
print("Синий")
a2 = input("Ответ: ")
while a2:
    if a2 == "Зеленый":
        score += 6
        break
    elif a2 == "Желтый":
        score += 4
        break
    elif a2 == "Синий":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Третий вопрос: Какая страна не вписывается в этот ряд? ")
print("Бразилия")
print("Канада")
print("Мексика")
a3 = input("Ответ: ")
while a3:
    if a3 == "Бразилия":
        score += 6
        break
    elif a3 == "Канада":
        score += 4
        break
    elif a3 == "Мексика":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Четвертый вопрос: Какой город лишний? ")
print("Варшава")
print("Париж")
print("Иерусалим")
a4 = input("Ответ: ")
while a4:
    if a4 == "Варшава":
        score += 6
        break
    elif a4 == "Париж":
        score += 4
        break
    elif a4 == "Иерусалим":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Пятый вопрос: Какое слово лишнее? ")
print("Умный")
print("Смешной")
print("Спящий")
a5 = input("Ответ: ")
while a5:
    if a5 == "Умный":
        score += 6
        break
    elif a5 == "Смешной":
        score += 4
        break
    elif a5 == "Спящий":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Шестой вопрос: Какой металл не вписывается в этот ряд? ")
print("Серебро")
print("Медь")
print("Золото")
a6 = input("Ответ: ")
while a6:
    if a6 == "Серебро":
        score += 6
        break
    elif a6 == "Медь":
        score += 4
        break
    elif a6 == "Золото":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Седьмой вопрос: Какая профессия не вписывается в этот ряд? ")
print("Медсестра")
print("Костоправ")
print("Хирург")
a7 = input("Ответ: ")
while a7:
    if a7 == "Медсестра":
        score += 6
        break
    elif a7 == "Костоправ":
        score += 4
        break
    elif a7 == "Хирург":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Восьмой вопрос: Какая геометрическая фигура не вписывается в этот ряд? ")
print("Квадрат")
print("Круг")
print("Треугольник")
a8 = input("Ответ: ")
while a8:
    if a8 == "Квадрат":
        score += 6
        break
    elif a8 == "Круг":
        score += 4
        break
    elif a8 == "Треугольник":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Девятый вопрос: Какое животное не вписывается в этот ряд? ")
print("Кенгуру")
print("Коала")
print("Лев")
a9 = input("Ответ: ")
while a9:
    if a9 == "Кенгуру":
        score += 6
        break
    elif a9 == "Коала":
        score += 4
        break
    elif a9 == "Лев":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print("Десятый вопрос: Какая религия не вписывается в этот ряд? ")
print("Ислам")
print("Иудаизм")
print("Буддизм")
a10 = input("Ответ: ")
while a10:
    if a10 == "Ислам":
        score += 6
        break
    elif a10 == "Иудаизм":
        score += 4
        break
    elif a10 == "Буддизм":
        score += 2
        break
    else:
        score += 0
        break
print()
print()
print()
print("Опрос был окончен!")
print("Ваш IQ = ",score)
print(input("Спасибо что учавствовали в опросе. Чтобы закрыть программы нажмите на Enter."))
'''
import random 
import cowsay
numbers = [random.randint(1,50) for i in range(5)]

def find_summ(list):
    return sum(list)
result = find_summ(numbers)
#print(f'The list and summ are {numbers} and {result}')
summary = f'The list and summ are {numbers} and {result}'
#tux = cowsay.tux('Arctica!')

"""with open('results.txt', mode='a') as send_file:
    send_file.write(f'\n{summary}')
    send_file.write(f'\n{tux}')
    send_file.close()"""

answers_dict = dict()
answers_list = list()
with open('answers.txt', mode='r') as read_file:
    for i in read_file.read():
        answers_list.append(i)
    read_file.close()

str_list = "".join(answers_list)
answers_dict[0] = str_list[0:16]
answers_dict[1] = str_list[17:33]
answers_dict[2] = str_list[34:50]
answers_dict[3] = str_list[51:67]
answers_dict[4] = str_list[68:84]
print(answers_dict)