import threading
import time
import random
import sys
from tkinter import *
from tkinter import ttk
class ventana(threading.Thread):
	def __init__(self,reloj,servidorPeticiones):
		super(ventana,self).__init__()
		self.daemon = True # die when the main thread dies
		self.libro=''
		self.hora=reloj
		self.peticiones=servidorPeticiones
	def on_closing(self):
		self.window.destroy()
		raise KeyboardInterrupt
		sys.exit(1)
	def command(self):
		self.peticiones.reinicia()
	def run(self):
		self.window = Tk()
		self.window.title("Maestro")
		self.window.geometry('620x200')
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.horas = Label(self.window, text=self.hora)
		self.horas.grid(column=0, row=0)
		self.info = Label(self.window, text=self.libro)
		self.info.grid(column=1, row=0)
		self.btn1 = Button(self.window, text="Reiniciar",command=self.command)
		self.btn1.grid(column=2, row=1)
		while True:
			self.horas.configure(text=str(self.hora.reloj['horas'])+":"+str(self.hora.reloj['minutos'])+":"+str(self.hora.reloj['segundos']))
			self.window.update_idletasks()
			self.window.update()
		#self.window.mainloop()
