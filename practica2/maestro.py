import socket
import sys
from hiloServidor import hiloServidor
from hiloReloj import hiloReloj
from ventana import ventana
import threading
import time


def servirPorSiempre(socketUDP,relojes):
    contador=0

    try:
        while True:
            message,address = socketUDP.recvfrom(1024)
            print(str('Cliente: '+str(address)+' dice: '+str(message)))
            if contador<3:
                nuevoCliente = hiloServidor(socketUDP,address,relojes[contador])
                nuevoCliente.start()
                contador+=1
            else:
                contador=0
                nuevoCliente = hiloServidor(address,relojes[contador])
                nuevoCliente.start()
                contador+=1
            #nuevoCliente = hiloServidor(client_conn,r1)
            #nuevoCliente.start()
            #time.sleep(1)
            #print(r1.reloj)
                    
                
    except KeyboardInterrupt:
        print("Deteniendo el servidor")
        #socketUDP.close()
        sys.exit(1)
    except Exception as e:
        socketUDP.close()
        print(e)




host, port = sys.argv[1:3]

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

serveraddr = (host, int(port))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    UDPServerSocket.bind(serveraddr)
    #UDPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")
    #Aquí se generan los tres relojes
    condition1 = threading.Condition()
    condition2 = threading.Condition()
    condition3 = threading.Condition()
    reloj1=hiloReloj(condition1)
    reloj2=hiloReloj(condition2)
    reloj3=hiloReloj(condition3)
    reloj1.start()
    reloj2.start()
    reloj3.start()
    window=ventana([reloj1,reloj2,reloj3],[condition1,condition2,condition3])
    window.start()
    servirPorSiempre(UDPServerSocket,[reloj1,reloj2,reloj3])
