'''import tkinter as tk
from tkinter import ttk
import math


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Triangle')
        self.geometry('640x480')
        self.resizable(False, False)
        self.configure(bg='#457b9d')
    

        self.title = tk.Label(
            self,
            text='ТРЕУГОЛЬНИК',
            font='Roboto 15',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.title.pack()


        self.a_label = tk.Label(
            self,
            text='A:',
            font='Roboto 20',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.a_label.place(x=40, y=60)


        self.b_label = tk.Label(
            self,
            text='B:',
            font='Roboto 20',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.b_label.place(x=40, y=120)


        self.c_label = tk.Label(
            self,
            text='C:',
            font='Roboto 20',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.c_label.place(x=40, y=180)    


        self.entry_a = tk.Entry(
            self,
            width=5,
            font=('Roboto 15')
        )
        self.entry_a.place(x=85, y=65)


        self.entry_b = tk.Entry(
            self,
            width=5,
            font=('Roboto 15')
        )
        self.entry_b.place(x=85, y=125)


        self.entry_c = tk.Entry(
            self,
            width=5,
            font=('Roboto 15')
        )
        self.entry_c.place(x=85, y=185)


        self.p_label = tk.Label(
            self,
            text='P:',
            font='Roboto 20',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.p_label.place(x=400, y=55)


        self.s_label = tk.Label(
            self,
            text='S:',
            font='Roboto 20',
            background='#457b9d',
            foreground='#f1faee'
        )
        self.s_label.place(x=400, y=110)


        self.entry_p = tk.Entry(
            self,
            width=5,
            font=('Roboto 15')
        )
        self.entry_p.place(x=450, y=60)


        self.entry_s = tk.Entry(
            self,
            width=5,
            font=('Roboto 15')
        )
        self.entry_s.place(x=450, y=115)


        self.operation_button = tk.Button(
            self,
            text='Вычислить',
            font='Intro'
        )
        self.operation_button.place(x=420, y=170)

        self.operation_button['command'] = self.operation
        self.operation_button.place(x=420, y=170)
    
    def operation(self):
        self.a = self.entry_a.get()
        self.b = self.entry_b.get()
        self.c = self.entry_c.get()

        self.p = float(self.a) + float(self.b) + float(self.c)
        self.entry_p.insert(0, self.p)

        #Равносторонний треугольник
        if self.a == self.b and self.b == self.c and self.a == self.c:
            self.s = (pow(float(self.a),2)*math.sqrt(3))/4
            self.entry_s.insert(0, self.s)
        
        #Разносторонний треугольник
        if self.a != self.b and self.b != self.c and self.a != self.c:
            self.s = math.sqrt((self.p/2)*((self.p/2)-float(self.a))\
                *((self.p/2)-float(self.b))*((self.p/2))-float(self.c))
            self.entry_s.insert(0, self.s)ы

        



if __name__ == '__main__':
    app = App()
    app.mainloop()


'''































