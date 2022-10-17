import tkinter 

window = tkinter.Tk()
window.title('СКОЛЬКО МНЕ ЛЕТ')
window.geometry('800x600')
window.resizable(False, False)

old_title = tkinter.Label(
    window,
    text='Когда родился(ась)?',
)
old_title.place(x=20, y=0)

old_year = tkinter.Label(
    window,
    text='Год'
)
old_year.place(x=20,y=20)

old_year_entry = tkinter.Entry(
    window
)
old_year_entry.place(x=60,y=20)

old_month = tkinter.Label(
    window,
    text='Месяц'
    
)
old_month.place(x=20,y=40)

old_month_entry = tkinter.Entry(
    window
)
old_month_entry.place(x=60,y=40)

window.mainloop()