import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkinter import Menu
import sys

class App(tk.Tk):

    def __init__(self):
        super(App,self).__init__()
        self.title('Quadrilateral')
        self.geometry('800x600')
        self.resizable(False, False)
        self.configure(bg='#778da9')

        self.a = ttk.Label(
            self,
            text='A:',
            foreground='white',
            background='#778da9',
            font='Intro 30'
        )
        self.a.place(x=20, y=50)

        self.a_entry = ttk.Entry(
            self,
            width=3,
            font='Intro 25'
        )
        self.a_entry.place(x=80, y=50)

        self.b = ttk.Label(
            self,
            text='B:',
            foreground='white',
            background='#778da9',
            font='Intro 30',            
        )
        self.b.place(x=20, y=110)

        self.b_entry = ttk.Entry(
            self,
            width=3,
            font='Intro 25'
        )
        self.b_entry.place(x=80, y=110)

        self.c = ttk.Label(
            self,
            text='C:',
            foreground='white',
            background='#778da9',
            font='Intro 30',                   
        )
        self.c.place(x=20, y=170)

        self.c_entry = ttk.Entry(
            self,
            width=3,
            font='Intro 25'
        )
        self.c_entry.place(x=80, y=170)

        self.d = ttk.Label(
            self,
            text='D:',
            foreground='white',
            background='#778da9',
            font='Intro 30',                   
        )
        self.d.place(x=20, y=230)

        self.d_entry = ttk.Entry(
            self,
            width=3,
            font='Intro 25'
        )
        self.d_entry.place(x=80, y=230)

        self.p = ttk.Label(
            self,
            text='P:',
            foreground='white',
            background='#778da9',
            font='Intro 30',   
        )
        self.p.place(x=200, y=90)

        self.p_entry = ttk.Entry(
            self,
            width=5,
            font='Intro 30'
        )
        self.p_entry.place(x=250, y=90)

        self.s = ttk.Label(
            self,
            text='S:',
            foreground='white',
            background='#778da9',
            font='Intro 30',   
        )
        self.s.place(x=200, y=160)
        
        self.s_entry = ttk.Entry(
            self,
            width=5,
            font='Intro 30'
        )
        self.s_entry.place(x=250, y=160)

        self.operation_button = tk.Button(
            self,
            text='Вычислить',
            width=10,
            font='Intro 15',
            foreground='White',
            background='#38b000'
        )
        self.operation_button['command'] = self.operation
        self.operation_button.place(x=550, y=100)

        self.clear_button = tk.Button(
            self,
            text='Очистить',
            width=10,
            font='Intro 15',
            foreground='White',
            background='#e5383b'
        )
        self.clear_button.place(x=550, y=150)
        self.clear_button['command'] = self.clear

        self.warning = ttk.Label(
            self,
            text='При вводе информации, вам нужно ввести величину стороны квадрата или прямоугольника.',
            foreground='white',
            background='#778da9',
            font='Intro 10', 
        )
        self.warning.place(x=30, y=530)

        self.warning_2 = ttk.Label(
            self,
            text='В ином случае программа не сработает',
            foreground='white',
            background='#778da9',
            font='Intro 10', 
        )
        self.warning_2.place(x=30, y=550)       

    def check_error(self):
        if self.a_entry.get() == "" or self.b_entry.get() == "" \
            or self.c_entry.get() == "" or self.d_entry.get() == "":
                messagebox.showerror('ОШИБКА',message='Вы забыли заполнить!')
                return -1

    def operation(self):

        value = self.check_error()
        if value == -1:
            return 
        else:
            self.A = float(self.a_entry.get())
            self.B = float(self.b_entry.get())
            self.C = float(self.c_entry.get())
            self.D = float(self.d_entry.get())

            self.P = float(self.A) + float(self.B) + float(self.C) + float(self.D)
            self.p_entry.insert(0, self.P)

            
            #Равносторонний четырехугольник
            if self.A == self.B and self.A == self.C and self.A == self.D and self.B == self.C and self.B == self.D and self.C == self.D:
                    self.S = pow(float(self.A), 2)
                    self.s_entry.insert(0, self.S)
                
            #Прямоугольник
            if self.A == self.B and self.C == self.D:
                self.S = self.A * self.C
            if self.A == self.C and self.B == self.D:
                self.S = self.A * self.B
            if self.A == self.D and self.B == self.C:
                self.S = self.A * self.B
            self.s_entry.insert(0, self.S)
    
    def clear(self):
        self.a_1 = self.a_entry.delete(0, tk.END)
        self.a_2 = self.b_entry.delete(0, tk.END)
        self.a_3 = self.c_entry.delete(0, tk.END)
        self.a_4 = self.d_entry.delete(0, tk.END)
        self.a_5 = self.p_entry.delete(0, tk.END)
        self.a_6 = self.s_entry.delete(0, tk.END)
    
if __name__ == '__main__':
	window = App()
	window.mainloop()


































