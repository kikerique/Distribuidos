import threading
import time
import json
import random
import socket
from os import path

class hiloServidor(threading.Thread):
    def __init__(self,socket,reloj,servidorPeticiones):
        super(hiloServidor,self).__init__()
        self.daemon=True
        self.socket=socket
        self.hiloReloj=reloj
        self.peticiones=servidorPeticiones
    def dameLibro(self):
        #print(self.usados)
        return self.peticiones.pideLibro()


    def run(self):
        try:
            self.socket.send(json.dumps(self.hiloReloj.reloj).encode())
            time.sleep(0.5)
            while True:
                message = self.socket.recv(1024).decode()
                if(message=='Libro'):
                    libro = self.dameLibro()
                    if libro==-1:
                        #self.ventana.libro = 'Ya no hay libros'
                        bytesToSend= 'Ya no hay libros'+ str(';Horas')
                        self.socket.send(bytesToSend.encode())
                    else:
                        #print('guardado')
                        #self.ventana.libro = self.libros[numero]
                        bytesToSend=json.dumps(libro)+str(';Horas')
                        self.socket.send(bytesToSend.encode())
                    #Despacha el libro

        except IOError as e:
            #print(e)
            self.archivo.close()
            pass