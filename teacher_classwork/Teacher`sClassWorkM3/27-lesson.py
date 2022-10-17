#1
"""def summ():
    a = 5 
    b = 3 
    return a + b 
print(f'Сумма: {summ()}')

def summ(a,b):
    return a + b 
print(f'Сумма: {summ(5,3)}')
#print(), append(), """

#2
"""def minus():
    a = 5
    b = 3
    c = 1 
    return a - b - c 
print(minus())

def minus_1(a,b,c):
    return a - b - c
print(minus_1(5,3,1))"""

"""#Приватная функция
a = 5 
b = 3 
c = 1
minus_2 = lambda: a-b-c
print(minus_2())

minus_3 = lambda a,b,c:a-b-c
print(minus_3(5,3,1))"""

"""def numbers():
    a = [4,6,23,435,457]
    return len(a)
print(numbers())"""

"""def new_len(*args):
    len_ = 0 
    for i in range(len(args)):
        len_ += 1 
    print(len_) 
new_len(1,5,2)"""

"""def summ():
    a = [3,5,6,7,9]
    return sum(a)
print(summ())"""

"""def new_sum(args):
    score = 0 
    for i in range(len(args)):
        score += args[i]
    return score 
a = [3,5,6,7,9]
print(new_sum(a))"""
import random
#box = [random.randint(1,10) for i in range(random.randint(5,15))]
#box.sort()
#print(box)
"""def count_box(list):
    mean = []
    for i in range(len(list)-1):
        if box.count(box[i]) >= 2:
            mean.append(list[i])
    return mean 
print(count_box(box))"""
"""box = [2, 4, 6, 6, 6, 7, 8, 9, 10]
print(box)
def count_box(list):
    duplicates = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j] and list[i] not in duplicates:
                duplicates.append(list[i])
    return duplicates 
print(count_box(box))"""

#map, filter 



"""list_ = [1,2,3,4,5]
words = ['a','b','c','d','e']
print(sum(list_))
app = list(map(len, list_))

words_ = list(map(str.upper, words))
print(app)
print(words_)"""

def words(vowels):
    return vowels.upper()

names = ['atabek','hello']
words_ = list(map(words, names))
print(words_)

def sum_of_numbers(numbers):
    score = 0
    for i in range(1,6):
        score += 1
    return score 

"""numbers = [1,2,3,4,5]
numbers_ = list(map(sum_of_numbers, numbers))
print(numbers_)

app = list(map(lambda n: len(numbers), numbers))
print(app)"""

#[1,2,3,4,5]
#[5,4,3,2,1]
#[1^5, 2^4, 3^3, 4^2, 5^1]

def square(list_1, list_2):
    score = [] 
    for i in range(len(list_1)):
        score.append(list_1[i]**list_2[i])
    return score 
print(square([1,2,3,4,5], [5,4,3,2,1]))

app = lambda x: [x for i in range(5) if i % 2 ]
print(app(10))

"""x = int(input('x: ')) 
y = int(input('y: '))
if x > y: print(x)
if x < y: print(y)"""

numbers_ = list(map(lambda x: [x for i in range(1,21) if i % 2 == 0], list(range(1,21))))
print(numbers_)