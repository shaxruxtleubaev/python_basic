import tkinter 
from tkinter import ttk 
from tkinter import messagebox 
import random

class App(tkinter.Tk):

    #StringVar 
    def __init__(self):
        super(App, self).__init__()
        self.title('FindColorApp')
        self.geometry('800x600')
        self.resizable(False, False)
        self.configure(bg='#273043')
        self.colorText = tkinter.StringVar()

        #Глобальная пере-я
        self.timeleft = 60
        self.score    = 0 

        #Intro 
        self.introTitle = ttk.Label(
            self,
            text='Enter color of the text',
            font=('Helvetica 30'),
            background='#273043',
            foreground='#ffffff'
        )
        self.introTitle.pack()

        #StartGameButton 
        self.startButton = ttk.Button(
            self,
            text='START',
            command=self.startGame
        )
        #self.startButton['text'] = 'START'
        self.startButton.place(x=350,y=80)

        #Titles 
        self.timeLabel = ttk.Label(
            self,
            text='TIME LEFT',
            font=('Helvetica 30'),
            background='#273043',
            foreground='#ffffff'
        )
        self.timeLabel.place(x=50, y=200)

        self.scoreLabel = ttk.Label(
            self,
            text='SCORE',
            font=('Helvetica 30'),
            background='#273043',
            foreground='#ffffff'
        )
        self.scoreLabel.place(x=500, y=200)

        #Color Game 
        self.gameLabel = ttk.Label(
            self,
            #text='jdksgjf',
            font=('Helvetica 30'),
            background='#273043',
        )
        self.gameLabel.place(x=325,y=300)

        #Color Game Entry
        self.answerGame = ttk.Entry(
            self,
            width=10,
            font=('Helvetica 30'),
            textvariable=self.colorText
        )
        self.answerGame.place(x=270, y=400)
        self.answerGame.focus()
    
    def startGame(self):

        if self.timeleft > 0:
            self.timeleft -= 1   # отнимаем каждый раз 1 секунд
            #Displaying -> Отображать данные 
            self.timeLabel.config(
                text='TIME LEFT {}'.format(str(self.timeleft))
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
                'ORANGE',
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
                self.answerGame.delete(0, tkinter.END)
            self.timeLabel.after(1000, self.startGame)
        else:
            messagebox.showinfo('TIME UP', 'YOUR SCORE IS : {0}'.format(str(self.score)))



if __name__ == '__main__':
    app = App()
    app.mainloop()