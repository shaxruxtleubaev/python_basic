import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title('Answer Finder')
        self.resizable(False, False)
        self.geometry('800x500')
        self.configure(bg='#073b4c')

        self.main = ttk.Label(
            self,
            text="Which figure's perimeter and area are to be found?",
            font='Bahnschrift 15',
            foreground='white',
            background='#073b4c'
        )
        self.main.pack()

        self.circle_button = ttk.Button(
            self,
            text='Circle'
        )
        self.circle_button.place(x=70, y=50)

        self.square_button = ttk.Button(
            self,
            text='Square'
        )
        self.square_button.place(x=360, y=50)

        self.triangle_button = ttk.Button(
            self,
            text='Triangle'
        )
        self.triangle_button.place(x=650, y=50)

        self.rectangle_button = ttk.Button(
            self,
            text='Rectangle'
        )
        self.rectangle_button.place(x=70, y=90)

        self.rhombus_button = ttk.Button(
            self,
            text='Rhombus'
        )
        self.rhombus_button.place(x=360, y=90)

        self.trapezoid_button = ttk.Button(
            self,
            text='Trapezoid'
        )
        self.trapezoid_button.place(x=650, y=90)

        self.cube_button = ttk.Button(
            self,
            text='Cube'
        )
        self.cube_button.place(x=70, y=130)

        self.pentagon_button = ttk.Button(
            self,
            text='Pentagon',
        )
        self.pentagon_button.place(x=360, y=130)

        self.hexagon_button = ttk.Button(
            self,
            text='Hexagon'
        )
        self.hexagon_button.place(x=650, y=130)

if __name__ == '__main__':
    app = App()
    app.mainloop()