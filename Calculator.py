import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry('480x360')
window.resizable(False, False)
window.title('Calculator')
window.configure(bg='#353535')

entry = tkinter.Entry(
    window,
    width=23,
    font=('Impact', 30),
    background='#353535',
    foreground='White'
)
entry.place(x=0, y=0)

answer = tkinter.Label(
    window,
    text='3563532545',
    width=23,
    font=('Impact', 30),
    background='#353535',
    foreground='White'
)
answer.place(x=0, y=55)





window.mainloop()