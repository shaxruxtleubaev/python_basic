import tkinter 
from tkinter import ttk

class App(tkinter.Tk):               #Название приложений

    def __init__(self):              #Характеристика
        super(App, self).__init__()  #Наследуем все данные
        self.title('Find Color')     #Заголовок
        self.configure(background='#808D8E') #Задний фон
        self.geometry('640x480')            #Размер экрана
        self.resizable(False, False)        #Изменяемость

        self.colorText = tkinter.StringVar() #Данные 

        """Виджеты-Widgets"""
        #Заголовок игры
        self.game_title = ttk.Label(
            self,
            text='Угадай название цвета!',
            font=('Poppins 20'),
            background='#808D8E',
            foreground='white'
        )
        self.game_title.pack()
        
        #Запуск игры через кнопки
        self.game_start = ttk.Button(
            self,
            text='Начинать'
        )
        self.game_start.place(x=280,y=80)

        #Время
        self.watch_text = ttk.Label(
            self,
            text='ВРЕМЯ : ',
            font=('Poppins 15'),
            background='#808D8E',
            foreground='white'
        )
        self.watch_text.place(x=60, y=150)

        #Очко
        self.score_text = ttk.Label(
            self,
            text='ОЧКО : ',
            font=('Poppins 15'),
            background='#808D8E',
            foreground='white'
        )
        self.score_text.place(x=470, y=150)


if __name__ == '__main__':           #Если класс это главный
    app = App()                      #Класс
    app.mainloop()                   #Запуск