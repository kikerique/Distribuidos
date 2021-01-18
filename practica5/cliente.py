import socket
import time
import json
from tkinter import *
from hiloReloj import hiloReloj
 

msgFromClient = "Hello UDP Server"

bytesToSend=str.encode(msgFromClient)

host, port = sys.argv[1:3]

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

serverAddressPort=(host, int(port))
pedirLibro = False
buffer_size = 1024
window = Tk()
def command():
	global pedirLibro
	pedirLibro = True
	print('Pedir libro' + str(pedirLibro))

def on_closing():
	try:
		window.destroy()
		raise KeyboardInterrupt
	except KeyboardInterrupt:
		print("Deteniendo el cliente")
		sys.exit(1)

# Send to server using created UDP socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
	TCPClientSocket.connect(serverAddressPort)
	data = TCPClientSocket.recv(buffer_size)
	data = json.loads(data.decode())
	reloj = hiloReloj(data['horas'],data['minutos'],data['segundos'])
	reloj.start()
	#print(data.decode())
	window.title("Cliente")
	window.geometry('500x100')
	window.protocol("WM_DELETE_WINDOW", on_closing)
	horas = Label(window, text='Horas')
	horas.grid(column=0, row=0)
	info = Label(window, text='')
	info.grid(column=1, row=0)
	btn1 = Button(window, text="Pedir Libro",command=command)
	btn1.grid(column=1, row=1)
	while True:
		if pedirLibro:
			TCPClientSocket.send(str.encode('Libro'))
			time.sleep(1)
			pedirLibro = False
			msg = TCPClientSocket.recv(buffer_size).decode()
			msg = msg.split(';')
			info.configure(text=msg[0])
			horas.configure(text=msg[1])
		horas.configure(text=str(reloj.reloj['horas'])+":"+str(reloj.reloj['minutos'])+":"+str(reloj.reloj['segundos']))
		window.update_idletasks()
		window.update()

		