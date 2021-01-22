from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import sys
import random
import json
import sqlite3
from sqlite3 import Error

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.daemon=True
        self.localServer = SimpleXMLRPCServer(("localhost",8000),requestHandler=RequestHandler)
        self.localServer.register_introspection_functions()
        self.localServer.register_instance(pasoDeMensajes())
    def run(self):
         self.localServer.serve_forever()

class pasoDeMensajes:
    def __init__(self):
        self.libros = [{'titulo':'Pedro Paramo','isbn':'1234567','precio':250,'autor':'Autor 1'},
                       {'titulo':'El llano en llamas','isbn':'7654321','precio':400,'autor':'Autor 2'},
                       {'titulo':'Mujercitas','isbn':'4321567','precio':900,'autor':'Autor 3'}
                      ]
        self.usados=set()
    def reinicia(self):
        #Reinicia el status de todos los libros
        try:
            with sqlite3.connect('libros.db') as db:
                cursor = db.cursor()
                for i in range(4):
                    id=i+1
                    cursor.execute('UPDATE libros set status=\'disponible\' where id='+str(id))
                    db.commit()
        except Error:
            print(Error)
        return 'Listo'
    def pideLibro(self):
        result=-1
        try:
            with sqlite3.connect('libros.db') as db:
                cursor = db.cursor()
                cursor.execute('SELECT * from libros where status=\'disponible\'')
                resultados= cursor.fetchall()
                if len(resultados)==0:
                    result= -1
                else:
                    numero = random.randint(0,len(resultados)-1)
                    result = json.dumps(resultados[numero])
                    cursor.execute('UPDATE libros set status=\'usado\' where id='+str(resultados[numero][0]))
                    db.commit()
        except Error:
            print(Error)
        print(result)

        return result
        


try:

    server= ServerThread()
    server.start()
    
    print("Escuchando en la direccion localhost:8000")

except Exception as e:
    print(str(e))
except KeyboardInterrupt:
    print("\nKeyboard interrupt recibida, saliendo.")
    sys.exit(0)
