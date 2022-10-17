'''def findSum():                        #outer def
    def find_list():                  #inner def
        arr = list(range(1, 6))
        return arr                    #call inner def
    return sum(find_list())           #call outer def
app = findSum()
print(app)

list_1 = [3, 2, 1]  #x
list_2 = [1, 2, 3]  #y
box_ = list(map(lambda x, y: x**y, list_1, list_2))
print(box_)

def lists(list_1, list_2):
    results = list()
    for i in range(len(list_1)):
        results.append(list_1[i]**list_2[i])
    return results
print(lists(list_1, list_2))
'''
'''import cowsay
cowsay.ghostbusters('HI GHOSTBUSTERS')

try:
    import cowsay
except:
    ModuleNotFoundError
finally:
    sheep = cowsay.cow('Muuu')
    t_rex = cowsay.trex('Brrrrrr!')'''

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
print(answers_dict)'''



















