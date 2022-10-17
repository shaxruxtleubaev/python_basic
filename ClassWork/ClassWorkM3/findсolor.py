import tkinter
from tkinter import ttk
import time

class App(tkinter.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title('Find Color')
        self.configure(background='#495057')
        self.geometry('640x480')
        self.resizable(False, False)
        self.colorText = tkinter.StringVar()          #Данные

        #Виджеты:
        self.game_title = ttk.Label(
            self,
            text='Угадай название цвета!',
            font='Poppins 20',
            background='#495057',
            foreground='white'
        )
        self.game_title.pack()

        self.game_start = ttk.Button(
            self,
            text='Начинать'
        )
        self.game_start.place(x=280, y=80)

        self.watch_text = ttk.Label(
            self,
            text='ВРЕМЯ',
            font='Poppins 15',
            background='#495057',
            foreground='white'
        )
        self.watch_text.place(x=40, y=150)

        self.score_text = ttk.Label(
            self,
            text='ОЧКО',
            font='Poppins 15',
            background='#495057',
            foreground='white'
        )
        self.score_text.place(x=470, y=150)

if __name__ == '__main__':
    app = App()
    app.mainloop()


































