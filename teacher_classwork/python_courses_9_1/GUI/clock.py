import tkinter 
from tkinter import ttk 
from time import strftime

class App(tkinter.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title('Clock')
        self.resizable(False, False)
        #self.geometry('800x100')
        self.configure(background='#151316')

        self.clock_label = ttk.Label(
            self,
            font=('Technology 50'),
            background='#151316',
            foreground='#C93535'
        )
        self.clock_label.pack()
        self.timer()
    
    def timer(self):

        time = strftime('%H:%M:%S-%Y-%B-%d')
        self.clock_label.configure(text=time)
        self.clock_label.after(True, self.timer)
    

if __name__ == '__main__':

    app = App()
    app.wm_attributes('-topmost',True)
    app.mainloop()