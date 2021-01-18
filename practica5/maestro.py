import socket
import sys
import random
import xmlrpc.client as RPC
from hiloServidor import hiloServidor
from hiloReloj import hiloReloj
from ventana import ventana
import threading
import time


def servirPorSiempre(socketTcp,reloj,servidorPeticiones):
    try:
        while True:
            client_conn, client_addr = socketTcp.accept()
            #Se crea un hilo para mantener el reloj del servidor de relojes          
            nuevoCliente = hiloServidor(client_conn,reloj,servidorPeticiones)
            nuevoCliente.start()
            #nuevoCliente.join()
    except KeyboardInterrupt:
        print("Deteniendo el servidor")
        #libros.close()
        #socketUDP.close()
        sys.exit(1)
    except Exception as e:
        socketTcp.close()
        print(e)




host, port = sys.argv[1:3]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)
serveraddr = (host, int(port))
horas=random.randint(0,23)
minutos=random.randint(0,59)
segundos=random.randint(0,59)
#TCPServerSocket2.close()
#TCPServerSocket1.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(1)
    #UDPServerSocket.listen()
    reloj = hiloReloj(horas,minutos,segundos)
    reloj.start()
    #reloj.join()
    servidorPeticiones = RPC.ServerProxy('http://localhost:8000')
    print("El servidor TCP está disponible y en espera de solicitudes")
    #window=ventana(reloj,servidorPeticiones)
    #window.start()
    #window.join()
    servirPorSiempre(TCPServerSocket,reloj,servidorPeticiones)
