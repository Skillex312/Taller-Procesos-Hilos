import threading
import time
'''
Se debe pensar en estas señales como elementos booleanos que pueden estar activos 
o innactivos, al tiempo que tenemos bloqueos o cerrduras que solo pueden pasar
si la señal está activa. 
'''
    
def genera_eventos():
  for x in range (5):
    time.sleep(2)
    ev.set()         
  
def escribe_algo():     
  while (True):
    ev.wait()
    print ("hola")
    ev.clear()     
    
ev =  threading.Event()
T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()