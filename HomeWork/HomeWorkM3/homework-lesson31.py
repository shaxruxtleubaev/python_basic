import tkinter

window = tkinter.Tk()
window.title('СКОЛЬКО МНЕ ЛЕТ')
window.geometry('800x600')
window.resizable(False, False)
window.configure(background='#252422')

old_title = tkinter.Label(
    window,
    text='Когда вы родились?',
    background='#252422',
    foreground='white'
)
old_title.place(x=20, y=0)
######################################################333

def total():
    year_old = old_year_entry.get()
    year_now = now_year_entry.get()
    tot_y = int(year_now) - int(year_old)

    month_old = old_month_entry.get()
    month_now = now_month_entry.get()
    tot_m = int(month_now) - int(month_old)
    if tot_m < 0:
        tot_y -= 1

    day_old = old_day_entry.get()
    day_now = now_day_entry.get()
    tot_d = int(day_now) - int(day_old)
    if tot_d < 0:
        tot_m -= 1

    finally_year = total_year_entry.insert(0, tot_y)
    if tot_m < 0:
        finally_month = total_month_entry.insert(0,12-abs(tot_m))
    if tot_m > 0:
        finally_month = total_month_entry.insert(0,abs(tot_m))      
    finally_day = total_day_entry.insert(0, abs(tot_d))

    return finally_year, finally_month, finally_day

def clean():

    a = total_day_entry.delete(0,tkinter.END)
    b = total_month_entry.delete(0,tkinter.END)
    c = total_year_entry.delete(0,tkinter.END)
    d = old_day_entry.delete(0,tkinter.END)
    e = old_month_entry.delete(0,tkinter.END)
    f = old_year_entry.delete(0,tkinter.END)
    g = now_day_entry.delete(0,tkinter.END)
    h = now_month_entry.delete(0,tkinter.END)
    i = now_year_entry.delete(0,tkinter.END)
  
old_year = tkinter.Label(
    window,
    text='Год',
    background='#252422',
    foreground='white'    
)
old_year.place(x=20,y=30)

old_year_entry = tkinter.Entry(
    window
)
old_year_entry.place(x=80,y=30)

old_month = tkinter.Label(
    window,
    text='Месяц',
    background='#252422',
    foreground='white'
)
old_month.place(x=20,y=50)

old_month_entry = tkinter.Entry(
    window
)
old_month_entry.place(x=80,y=50)

old_day = tkinter.Label(
    window,
    text='День',
    background='#252422',
    foreground='white'    
)
old_day.place(x=20,y=70)

old_day_entry = tkinter.Entry(
    window
)
old_day_entry.place(x=80,y=70)
#################################################################################

now_title = tkinter.Label(
    window,
    text='Какое сейчас время?',
    background='#252422',
    foreground='white'
)
now_title.place(x=500, y=0)

now_year = tkinter.Label(
    window,
    text='Год',
    background='#252422',
    foreground='white'     
)
now_year.place(x=500,y=30)

now_year_entry= tkinter.Entry(
    window
)
now_year_entry.place(x=560,y=30)

now_month = tkinter.Label(
    window,
    text='Месяц',
    background='#252422',
    foreground='white'     
)
now_month.place(x=500,y=50)

now_month_entry = tkinter.Entry(
    window
)
now_month_entry.place(x=560,y=50)

now_day = tkinter.Label(
    window,
    text='День',
    background='#252422',
    foreground='white'
)
now_day.place(x=500,y=70)

now_day_entry = tkinter.Entry(
    window
)
now_day_entry.place(x=560,y=70)
#######################################################33333

solve_button = tkinter.Button(
    window, 
    width='10',
    text='Вычислить',
    font=('Roboto',13),
    background='#8ac926',
    foreground='white'   ,
    command=total
)
solve_button.place(x=300,y=20)

clear_button = tkinter.Button(
    window,
    width='10',
    text='Очистить',
    font=('Roboto',13),
    background='#d90429',
    foreground='white',  
    command=clean      
)
clear_button.place(x=300,y=70)
########################################################################

cont = tkinter.Label(
    window,
    text='Ваш возраст!',
    font='Roboto',
    background='#252422',
    foreground='white'
)
cont.place(x=300, y=150)

total_year = tkinter.Label(
    window,
    text='Год',
    background='#252422',
    foreground='white'    
)
total_year.place(x=250,y=200)

total_year_entry = tkinter.Entry(
    window
)
total_year_entry.place(x=310,y=200)

total_month = tkinter.Label(
    window,
    text='Месяц',
    background='#252422',
    foreground='white'      
)
total_month.place(x=250,y=220)

total_month_entry = tkinter.Entry(
    window
)
total_month_entry.place(x=310,y=220)

total_day = tkinter.Label(
    window,
    text='День',
    background='#252422',
    foreground='white'     
)
total_day.place(x=250, y=240)

total_day_entry = tkinter.Entry(
    window
)
total_day_entry.place(x=310,y=240)

warning = tkinter.Label(
    window,
    text='Внимание! Вам нужно запольнить в ячейках, с вопросами  "Когда вы родились?"  и  "Какое сейчас время?"',
    background='#252422',
    foreground='white' 
)
warning.place(x=30, y=500)

warning_2 = tkinter.Label(
    window,
    text='Чтобы узнать результат, нажмите на кнопку  "Вычислить".  Нажмите на кнопку  "Очистить"  чтобы заново начать вычисление',
    background='#252422',
    foreground='white'
)
warning_2.place(x=30,y=520)
window.mainloop()