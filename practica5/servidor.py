import threading
from hiloServidor import hiloServidor
import time
import json
import random
from os import path

class servidor(threading.Thread):
    def __init__(self,socketTcp,usados):
        super(servidor,self).__init__()
        #self.daemon=True
        self.socketTcp=socketTcp
        self.usados = usados
        #self.hiloReloj=reloj
    def run(self):
        try:
            while True:
                client_conn, client_addr = self.socketTcp.accept()
	            #Se crea un hilo para mantener el reloj del servidor de relojes          
                nuevoCliente = hiloServidor(client_conn,self.usados)
                nuevoCliente.start()
        except KeyboardInterrupt:
            print("Deteniendo el servidor")
	        #socketUDP.close()
            sys.exit(1)
        except Exception as e:
            socketTcp.close()
            print(e)
        except IOError as e:
            #print(e)
            pass