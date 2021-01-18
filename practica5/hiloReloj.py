import threading
import time
import random

class hiloReloj(threading.Thread):
    def __init__(self,horas,minutos,segundos):
        super(hiloReloj,self).__init__()
        self.daemon = True # die when the main thread dies
        #self.ventana=condition
        self.pausa= False
        self.reloj={'horas':horas,'minutos':minutos,'segundos':segundos}

    def run(self):
        try:
            #Simula el comportamiento de un reloj
            horas=int(self.reloj['horas'])
            minutos=int(self.reloj['minutos'])
            segundos=int(self.reloj['segundos'])
            while True:
                """if(self.pausa):
                    with self.ventana:
                        self.ventana.wait()
                        self.pausa=False
                        horas=int(self.reloj['horas'])
                        minutos=int(self.reloj['minutos'])
                        segundos=int(self.reloj['segundos'])"""
                time.sleep(1)
                segundos+=1
                if(segundos==60):
                    segundos=0
                    minutos+=1
                    if(minutos==60):
                        minutos=0
                        horas+=1
                        if(horas==24):
                            horas=0
                self.reloj['horas']=str(horas).zfill(2)
                self.reloj['minutos']=str(minutos).zfill(2)
                self.reloj['segundos']=str(segundos).zfill(2)
                    
                    
        except KeyboardInterrupt:
            print("Deteniendo el reloj")
            #socketUDP.close()
            sys.exit(1)
        except IOError as e:
            #print(e)
            pass