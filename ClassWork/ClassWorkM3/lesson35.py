import tkinter
from tkinter import ttk
from tkinter import messagebox
import random

class App(tkinter.Tk):
    
    #StringVar
    def __init__(self):
        super(App, self).__init__()
        self.title('FindColorApp')
        self.resizable(False, False)
        self.geometry('800x600')
        self.configure(bg='#073b4c')
        self.colorText = tkinter.StringVar()

        self.timeleft = 60
        self.score    = 0

        #Intro
        self.introTitle = ttk.Label(
            self,
            text='Enter color of the text',
            font='Helvetica 30',
            background='#073b4c',
            foreground='white'
        )
        self.introTitle.pack()
        
        #StartGameButton
        self.startButton = ttk.Button(
            self,
            text='START',
            command=self.startGame,
        )
        self.startButton.place(x=350, y=80)

        #Titles
        self.timeLabel = ttk.Label(
            self,
            text='TIME LEFT',
            font='Helvetica 30',
            background='#073b4c',
            foreground='white'
        )
        self.timeLabel.place(x=50, y=200)

        self.scoreLabel = ttk.Label(
            self,
            text='SCORE',
            font='Helvetica 30',
            background='#073b4c',
            foreground='white'
        )
        self.scoreLabel.place(x=500, y=200)

        #ColorGame

        self.gameLabel = ttk.Label(
            self,
            text='.',
            font='Helvetica 30',
            background='#073b4c'
        )
        self.gameLabel.place(x=325, y=300)

        #Color Game Entry
        self.AnswerGame = ttk.Entry(
            self,
            width=10,
            font=('Helvetica 30'),
            textvariable=self.colorText
        )
        self.AnswerGame.place(x=270, y=400)
        self.AnswerGame.focus()

    def startGame(self):
        
        if self.timeleft > 0:
            
            self.timeleft -= 1      #отнимаем каждый раз по 1 секунд
            
            #Displaying -> Отображать данные
            self.timeLabel.config(
                text='TIME LEFT: {}'.format(str(self.timeleft))
            )
            #Создаем список цветов
            self.randomColor = [
                'GREEN',
                'RED',
                'BLACK',
                'WHITE',
                'PINK',
                'VIOLET',
                'BROWN',
                'YELLOW'
            ]
            random.shuffle(self.randomColor)

            #Displaying colors in the gameLabel
            self.gameLabel.config(
                text=str(self.randomColor[0]),
                foreground=self.randomColor[1]
            )
            if self.colorText.get().lower() == self.randomColor[1].lower():
                #If yes increment the score value by 1
                self.score += 1
                #Displaying the score
                self.scoreLabel.config(
                    text='SCORE {}'.format(str(self.score))
                )
                self.AnswerGame.delete(0, tkinter.END)

            self.timeLabel.after(1000, self.startGame)

        else:
            messagebox.showinfo('TIME UP!', 'YOUR SCORE IS : {0}'.format(str(self.score)))

if __name__ == '__main__':
    app = App()
    app.mainloop()