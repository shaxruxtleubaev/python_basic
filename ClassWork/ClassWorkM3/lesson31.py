#CLI -> Command line interface
#GUI -> Graphical user Interface

import tkinter

#Создаем окно
window = tkinter.Tk()
window.geometry('720x480')
window.title('GUI')
window.configure(background='#001219')

text_field = tkinter.Label(
    window,
    text='My first programm!',
    font=('cursive',20),
    background='#001219',
    foreground='white'
)
text_field.pack()

def operation():

    request = entry_field.get()
    response = entry_field_1.insert(0, request)

def clean():

    request = entry_field.delete(0,tkinter.END)
    response = entry_field_1.delete(0,tkinter.END)

entry_field = tkinter.Entry(
    width=50,
    font=('Roboto',15)
)
entry_field.pack()

button_field = tkinter.Button(
    window, 
    text='Нажимай',
    font=('Roboto',15),
    background='#8ac926',
    foreground='white',
    command=operation
)
button_field.pack()

entry_field_1 = tkinter.Entry(
    width=50,
    font=('Roboto',15)
)
entry_field_1.pack()

button_clean = tkinter.Button(
    window, 
    text='Очистить',
    font=('Roboto',15),
    background='#780000',
    foreground='white',
    command=clean
)
button_clean.pack()

#Закрываем окно
window.wm_attributes('-topmost',True)
window.mainloop()





























