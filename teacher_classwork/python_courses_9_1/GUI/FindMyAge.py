import tkinter 
from tkinter import ttk
from tkinter import messagebox

class App(tkinter.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title('Find My Age')
        self.geometry('640x480')
        self.resizable(False, False)
        self.configure(bg='#273043')

        """ OLD DATA - Год Рождения """
        self.old_info = ttk.Label(
            self,
            text='Год рождения',
            font=('Poppins 20'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.old_info.place(x=60,y=40) 

        self.old_year = ttk.Label(
            self,
            text='Год',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.old_year.place(x=30,y=100)

        self.old_year_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.old_year_entry.place(x=90, y=100)

        self.old_month = ttk.Label(
            self,
            text='Месяц',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.old_month.place(x=30,y=150)

        self.old_month_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.old_month_entry.place(x=90, y=150)

        self.old_day = ttk.Label(
            self,
            text='День',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.old_day.place(x=30,y=200)

        self.old_day_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.old_day_entry.place(x=90, y=200)

        """ New Data - Текущяя дата """

        self.new_info = ttk.Label(
            self,
            text='Текущяя дата',
            font=('Poppins 20'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.new_info.place(x=400,y=40) 

        self.new_year = ttk.Label(
            self,
            text='Год',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.new_year.place(x=370,y=100)

        self.new_year_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.new_year_entry.place(x=430, y=100)

        self.new_month = ttk.Label(
            self,
            text='Месяц',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.new_month.place(x=370,y=150)

        self.new_month_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.new_month_entry.place(x=430, y=150)

        self.new_day = ttk.Label(
            self,
            text='День',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.new_day.place(x=370,y=200)

        self.new_day_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.new_day_entry.place(x=430, y=200)

        """ Result - Результат """

        self.result_info = ttk.Label(
            self,
            text='Ваш возраст',
            font=('Poppins 20'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.result_info.place(x=210,y=260) 

        self.result_year = ttk.Label(
            self,
            text='Год',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.result_year.place(x=180,y=320)

        self.result_year_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.result_year_entry.place(x=240, y=320)

        self.result_month = ttk.Label(
            self,
            text='Месяц',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.result_month.place(x=180,y=370)

        self.result_month_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.result_month_entry.place(x=240, y=370)

        self.result_day = ttk.Label(
            self,
            text='День',
            font=('Poppins 10'),
            background='#273043',
            foreground='#EFF6EE'
        )
        self.result_day.place(x=180,y=420)

        self.result_day_entry = ttk.Entry(
            self,
            width=10,
            font=('Poppins 10')
        )
        self.result_day_entry.place(x=240, y=420)

        """ Buttons - Кнопки """

        self.button_operation = ttk.Button(
            self,
            text='Операция'
        )
        self.button_operation['command'] = self.operation_all_commands
        self.button_operation.place(x=500, y=420)

        self.button_clear = ttk.Button(
            self,
            text='Очистить'
        )
        self.button_clear['command'] = self.clear_all_commands
        self.button_clear.place(x=400, y=420)
    
    def clear_all_commands(self):

        self.old_year_entry.delete(0, tkinter.END)
        self.old_month_entry.delete(0, tkinter.END)
        self.old_day_entry.delete(0, tkinter.END)

        self.new_year_entry.delete(0, tkinter.END)
        self.new_month_entry.delete(0, tkinter.END)
        self.new_day_entry.delete(0, tkinter.END)

        self.result_year_entry.delete(0, tkinter.END)
        self.result_month_entry.delete(0, tkinter.END)
        self.result_day_entry.delete(0, tkinter.END)

    def checkError(self):

        if self.old_year_entry.get() == "" or self.old_month_entry.get() == "" or \
            self.old_day_entry.get() == "" or self.new_year_entry.get() == "" or \
                self.new_month_entry.get() == "" or self.new_day_entry.get() == "":
                messagebox.showerror('ОШИБКА',message='Вы забыли заполнить!')
                return -1

    def operation_all_commands(self):

        value = self.checkError()
        if value == -1:
            return 
        else:
            old_year = int(self.old_year_entry.get())
            old_month = int(self.old_month_entry.get())
            old_day= int(self.old_day_entry.get())

            new_year = int(self.new_year_entry.get())
            new_month = int(self.new_month_entry.get()) 
            new_day = int(self.new_day_entry.get())

            months = [31,28,31,30,31,30,31,31,30,31,30,31]
            if old_day > new_day:
                new_month -= 1
                new_day += months[old_month-1]

            if old_month > new_month:
                new_year -= 1
                new_month += 12 

            calculate_year = abs(old_year-new_year)
            calculate_month = abs(old_month-new_month) 
            calculate_day   = abs(old_day - new_day)

            self.result_year_entry.insert(0, calculate_year)
            self.result_month_entry.insert(0, calculate_month)
            self.result_day_entry.insert(0, calculate_day)

if __name__ == '__main__':

    app = App()
    app.mainloop()
