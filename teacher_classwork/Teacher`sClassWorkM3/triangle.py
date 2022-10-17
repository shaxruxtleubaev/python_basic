import tkinter as tk
from tkinter import ttk
import math 
from tkinter import Menu
import sys
from tkinter import messagebox


class App(tk.Tk):
	
	def __init__(self):
		super(App, self).__init__()
		self.title('Triangle')
		self.geometry('640x480')
		self.resizable(False,False)
		self.configure(bg='#b7d5d4')
		self.menubar = Menu(self)
		self.config(menu=self.menubar)
		self.createMenu()



		self.title = ttk.Label(
			self,
			text='ТРЕУГОЛЬНИК',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.title.pack()

		self.a_label = ttk.Label(
			self,
			text='A:',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.a_label.place(x=40,y=60)

		self.b_label = ttk.Label(
			self,
			text='B:',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.b_label.place(x=40,y=120)

		self.c_label = ttk.Label(
			self,
			text='C:',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.c_label.place(x=40, y=180)

		self.entry_a = ttk.Entry(
			self,
			width=5,
			font=('Roboto 20')
		)
		self.entry_a.place(x=100, y=65)

		self.entry_b = ttk.Entry(
			self,
			width=5,
			font=('Roboto 20')
		)
		self.entry_b.place(x=100, y=125)

		self.entry_c = ttk.Entry(
			self,
			width=5,
			font=('Roboto 20')
		)
		self.entry_c.place(x=100, y=185)

		self.p_label = ttk.Label(
			self,
			text='P:',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.p_label.place(x=400,y=60)

		self.s_label = ttk.Label(
			self,
			text='S:',
			font=('Roboto 30'),
			background='#b7d5d4',
			foreground='#ffffff'
		)
		self.s_label.place(x=400,y=120)

		self.entry_p = ttk.Entry(
			self,
			width=5,
			font=('Roboto 20')
		)
		self.entry_p.place(x=460, y=65)

		self.entry_s = ttk.Entry(
			self,
			width=5,
			font=('Roboto 20')
		)
		self.entry_s.place(x=460, y=125)

		self.operation_button = ttk.Button(
			self,
			text='Вычислить',
		)
		self.operation_button['command'] = self.operation
		self.operation_button.place(x=460,y=185)



	def operation(self):
		
		self.a = self.entry_a.get() #str
		self.b = self.entry_b.get()	#str
		self.c = self.entry_c.get() #str

		self.p = int(self.a) + int(self.b) + int(self.c)
		self.entry_p.insert(0, self.p)

		try:
			#Равносторонний треугольник
			if self.a == self.b and self.b == self.c and self.a == self.c:
				self.s = (pow(int(self.a),2)*math.sqrt(3))/4
				self.entry_s.insert(0, self.s)

			#Разносторонний треугольник
			if self.a != self.b and self.a != self.c and self.b != self.c:
				self.s = math.sqrt((self.p/2)*((self.p/2)-int(self.a))\
					*((self.p/2)-int(self.b))*((self.p/2)-int(self.c)))
				self.entry_s.insert(0, self.s)

			#Равнобедренный треугольник
			if self.a == self.b != self.c or self.a == self.c != self.b or \
			self.b == self.c != self.a:
				self.s = math.sqrt((self.p/2)*((self.p/2)-int(self.a))\
					*((self.p/2)-int(self.b))*((self.p/2)-int(self.c)))
				self.entry_s.insert(0, self.s)

		except ValueError:	
			print('ОШИБКА')
		

	def createMenu(self):

		menuBar = Menu(self)
		self.config(menu = menuBar)

		file_menu = Menu(menuBar, tearoff = 0)
		menuBar.add_cascade(label="File", menu=file_menu)
		file_menu.add_command(label='New')
		file_menu.add_command(label='Exit', command=self.quit)
		file_menu.add_separator()
		file_menu.add_command(label='Open')

	def quit(self):
		sys.exit(0)

        
if __name__ == '__main__':
	window = App()
	window.iconphoto(False, window.icon)
	window.mainloop()


