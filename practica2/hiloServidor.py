import threading
import time
from os import path

class hiloServidor(threading.Thread):
    def __init__(self,socket,cliente,reloj):
        super(hiloServidor,self).__init__()
        self.daemon=True
        self.socket=socket
        self.cliente=cliente
        self.reloj=reloj

    def run(self):
        try:
            while True:
                bytesToSend=str(self.reloj.reloj['horas']+':'+self.reloj.reloj['minutos']+':'+self.reloj.reloj['segundos'])
                self.socket.sendto(bytesToSend.encode(), self.cliente)
        except IOError as e:
            #print(e)
            pass