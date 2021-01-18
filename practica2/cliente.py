import socket
from tkinter import *

 

msgFromClient = "Hello UDP Server"

bytesToSend=str.encode(msgFromClient)

host, port = sys.argv[1:3]

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

serverAddressPort=(host, int(port))

bufferSize = 1024

  

# Send to server using created UDP socket

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDPClientSocket:
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	window = Tk()
	window.title("Cliente")
	window.geometry('320x100')
	horas = Label(window, text='00')
	horas.grid(column=0, row=0)
	minutos = Label(window, text='00')
	minutos.grid(column=1, row=0)
	segundos = Label(window, text='00')
	segundos.grid(column=2, row=0)
	while True:
		msgFromServer = UDPClientSocket.recvfrom(bufferSize)	 
		msg = "{}".format(msgFromServer[0].decode())
		horas.configure(text=msg)
		minutos.configure(text="")
		segundos.configure(text="")
		window.update_idletasks()
		window.update()