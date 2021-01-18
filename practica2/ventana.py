import threading
import _thread
import time
import random
import sys
from tkinter import *
from tkinter import ttk
class ventana(threading.Thread):
	def __init__(self,relojes,condiciones):
		super(ventana,self).__init__()
		self.daemon = True # die when the main thread dies
		self.relojes=relojes
		self.condiciones=condiciones
	def pausa1(self):
		self.estatus1.configure(text="Modifcando")
		self.horas1.grid_remove()
		self.minutos1.grid_remove()
		self.segundos1.grid_remove()
		self.comboHoras1.grid()
		self.comboMinutos1.grid()
		self.comboSegundos1.grid()
		self.relojes[0].pausa=True
	def continuar1(self):
		horas=self.comboHoras1.get()
		minutos=self.comboMinutos1.get()
		segundos=self.comboSegundos1.get()
		self.comboHoras1.grid_remove()
		self.comboMinutos1.grid_remove()
		self.comboSegundos1.grid_remove()
		self.horas1.grid()
		self.minutos1.grid()
		self.segundos1.grid()
		self.relojes[0].reloj['horas']=horas.zfill(2)
		self.relojes[0].reloj['minutos']=minutos.zfill(2)
		self.relojes[0].reloj['segundos']=segundos.zfill(2)
		with self.condiciones[0]:
			self.condiciones[0].notify()
		self.estatus1.configure(text="Continuando")
	def pausa2(self):
		self.estatus2.configure(text="Modifcando")
		self.horas2.grid_remove()
		self.minutos2.grid_remove()
		self.segundos2.grid_remove()
		self.comboHoras2.grid()
		self.comboMinutos2.grid()
		self.comboSegundos2.grid()
		self.relojes[1].pausa=True
	def continuar2(self):
		horas=self.comboHoras2.get()
		minutos=self.comboMinutos2.get()
		segundos=self.comboSegundos2.get()
		self.comboHoras2.grid_remove()
		self.comboMinutos2.grid_remove()
		self.comboSegundos2.grid_remove()
		self.horas2.grid()
		self.minutos2.grid()
		self.segundos2.grid()
		self.relojes[1].reloj['horas']=horas.zfill(2)
		self.relojes[1].reloj['minutos']=minutos.zfill(2)
		self.relojes[1].reloj['segundos']=segundos.zfill(2)
		with self.condiciones[1]:
			self.condiciones[1].notify()
		self.estatus2.configure(text="Continuando")
	def pausa3(self):
		self.estatus3.configure(text="Modifcando")
		self.horas3.grid_remove()
		self.minutos3.grid_remove()
		self.segundos3.grid_remove()
		self.comboHoras3.grid()
		self.comboMinutos3.grid()
		self.comboSegundos3.grid()
		self.relojes[2].pausa=True
	def continuar3(self):
		horas=self.comboHoras3.get()
		minutos=self.comboMinutos3.get()
		segundos=self.comboSegundos3.get()
		self.comboHoras3.grid_remove()
		self.comboMinutos3.grid_remove()
		self.comboSegundos3.grid_remove()
		self.horas3.grid()
		self.minutos3.grid()
		self.segundos3.grid()
		self.relojes[2].reloj['horas']=horas.zfill(2)
		self.relojes[2].reloj['minutos']=minutos.zfill(2)
		self.relojes[2].reloj['segundos']=segundos.zfill(2)
		with self.condiciones[2]:
			self.condiciones[2].notify()
		self.estatus3.configure(text="Continuando")
	def on_closing(self):
		self.window.destroy()
		raise KeyboardInterrupt
		sys.exit(1)
	def run(self):
		self.window = Tk()
		self.window.title("Maestro")
		self.window.geometry('620x200')
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		#Reloj1
		self.horas1 = Label(self.window, text='00')
		self.horas1.grid(column=0, row=0)
		self.minutos1 = Label(self.window, text='00')
		self.minutos1.grid(column=1, row=0)
		self.segundos1 = Label(self.window, text='00')
		self.segundos1.grid(column=2, row=0)
		self.estatus1 = Label(self.window, text='Reloj 1')
		self.estatus1.grid(column=3, row=0)
		self.btn1 = Button(self.window, text="Modificar",command=self.pausa1)
		self.btn1.grid(column=0, row=1)
		self.btn2 = Button(self.window, text="Enviar",command=self.continuar1)
		self.btn2.grid(column=1, row=1)

		#Modificaciones
		self.comboHoras1 = ttk.Combobox(self.window)
		self.comboHoras1['values']= [x for x in range(24)]
		self.comboHoras1.current(1) #set the selected item
		self.comboHoras1.grid(column=0, row=0)
		self.comboHoras1.grid_remove()
		self.comboMinutos1 = ttk.Combobox(self.window)
		self.comboMinutos1['values']= [x for x in range(60)]
		self.comboMinutos1.current(0) #set the selected item
		self.comboMinutos1.grid(column=1, row=0)
		self.comboMinutos1.grid_remove()
		self.comboSegundos1 = ttk.Combobox(self.window)
		self.comboSegundos1['values']= [x for x in range(60)]
		self.comboSegundos1.current(0) #set the selected item
		self.comboSegundos1.grid(column=2, row=0)
		self.comboSegundos1.grid_remove()
		#Fin modificaciones
		#Fin Reloj1
		#Reloj 2
		self.horas2 = Label(self.window, text='00')
		self.horas2.grid(column=0, row=2)
		self.minutos2 = Label(self.window, text='00')
		self.minutos2.grid(column=1, row=2)
		self.segundos2 = Label(self.window, text='00')
		self.segundos2.grid(column=2, row=2)
		self.estatus2 = Label(self.window, text='Reloj 2')
		self.estatus2.grid(column=3, row=2)
		self.btn3 = Button(self.window, text="Modificar",command=self.pausa2)
		self.btn3.grid(column=0, row=3)
		self.btn4 = Button(self.window, text="Enviar",command=self.continuar2)
		self.btn4.grid(column=1, row=3)

		#Modificaciones
		self.comboHoras2 = ttk.Combobox(self.window)
		self.comboHoras2['values']= [x for x in range(24)]
		self.comboHoras2.current(0) #set the selected item
		self.comboHoras2.grid(column=0, row=2)
		self.comboHoras2.grid_remove()
		self.comboMinutos2 = ttk.Combobox(self.window)
		self.comboMinutos2['values']= [x for x in range(60)]
		self.comboMinutos2.current(0) #set the selected item
		self.comboMinutos2.grid(column=1, row=2)
		self.comboMinutos2.grid_remove()
		self.comboSegundos2 = ttk.Combobox(self.window)
		self.comboSegundos2['values']= [x for x in range(60)]
		self.comboSegundos2.current(0) #set the selected item
		self.comboSegundos2.grid(column=2, row=2)
		self.comboSegundos2.grid_remove()
		#Fin modificaciones
		#Fin Reloj 2

		#Reloj 3
		self.horas3 = Label(self.window, text='00')
		self.horas3.grid(column=0, row=4)
		self.minutos3 = Label(self.window, text='00')
		self.minutos3.grid(column=1, row=4)
		self.segundos3 = Label(self.window, text='00')
		self.segundos3.grid(column=2, row=4)
		self.estatus3 = Label(self.window, text='Reloj 2')
		self.estatus3.grid(column=3, row=4)
		self.btn5 = Button(self.window, text="Modificar",command=self.pausa3)
		self.btn5.grid(column=0, row=5)
		self.btn6 = Button(self.window, text="Enviar",command=self.continuar3)
		self.btn6.grid(column=1, row=5)

		#Modificaciones
		self.comboHoras3 = ttk.Combobox(self.window)
		self.comboHoras3['values']= [x for x in range(24)]
		self.comboHoras3.current(0) #set the selected item
		self.comboHoras3.grid(column=0, row=4)
		self.comboHoras3.grid_remove()
		self.comboMinutos3 = ttk.Combobox(self.window)
		self.comboMinutos3['values']= [x for x in range(60)]
		self.comboMinutos3.current(0) #set the selected item
		self.comboMinutos3.grid(column=1, row=4)
		self.comboMinutos3.grid_remove()
		self.comboSegundos3 = ttk.Combobox(self.window)
		self.comboSegundos3['values']= [x for x in range(60)]
		self.comboSegundos3.current(0) #set the selected item
		self.comboSegundos3.grid(column=2, row=4)
		self.comboSegundos3.grid_remove()
		#Fin modificaciones
		#Fin Reloj 2
		while True:
			self.horas1.configure(text=self.relojes[0].reloj['horas'])
			self.minutos1.configure(text=self.relojes[0].reloj['minutos'])
			self.segundos1.configure(text=self.relojes[0].reloj['segundos'])
			self.horas2.configure(text=self.relojes[1].reloj['horas'])
			self.minutos2.configure(text=self.relojes[1].reloj['minutos'])
			self.segundos2.configure(text=self.relojes[1].reloj['segundos'])
			self.horas3.configure(text=self.relojes[2].reloj['horas'])
			self.minutos3.configure(text=self.relojes[2].reloj['minutos'])
			self.segundos3.configure(text=self.relojes[2].reloj['segundos'])
			self.window.update_idletasks()
			self.window.update()
		#self.window.mainloop()
