from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class pasoDeMensajes:
    def __init__(self):
        self.libros = [{'titulo':'Pedro Paramo','isbn':'1234567','precio':250,'autor':'Autor 1'},
                       {'titulo':'El llano en llamas','isbn':'7654321','precio':400,'autor':'Autor 2'},
                       {'titulo':'Mujercitas','isbn':'4321567','precio':900,'autor':'Autor 3'}
                      ]
        self.usados=set()
    def reinicia(self):
        #Reinicia el status de todos los libros
        self.usados.clear()
    def pideLibro(self):
        while True:
            if len(self.usados)==3:
                return -1
            numero = random.randint(0,2)
            if not(numero in self.usados):
                self.usados.add(numero)
                return self.libros[numero]
        


try:
    server= SimpleXMLRPCServer(('localhost',8000),requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(pasoDeMensajes())
    print("Escuchando en la direccion localhost:8000")
    # Run the server's main loop
    server.serve_forever()
except Exception as e:
    print(str(e))
except KeyboardInterrupt:
    print("\nKeyboard interrupt recibida, saliendo.")
    sys.exit(0)
