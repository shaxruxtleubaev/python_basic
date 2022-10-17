import os
import pyfiglet

a = input('Enter something that you wanna change: ')

def CoolText(text):

    #Экземпляр Figlet с настройками шрифта под наклоном
    cool_text = pyfiglet.Figlet(font='slant')

    #Очистить терминал окна
    os.system('cls')

    #Установка терминала по заданному размеру
    os.system('mode con: cols=75 lines=30')
    return str(cool_text.renderText(text))

if __name__ == '__main__':

    new_text_is = CoolText(a)
    print(new_text_is)