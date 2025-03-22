import threading
import time

# Eventos
ev = threading.Event()  
terminar_ev = threading.Event()  # Nueva señal para terminar el programa

def genera_eventos():
    for _ in range(5):
        time.sleep(2)
        ev.set()  # Activa la señal para escribir
    terminar_ev.set()  # Señal para terminar el programa

def escribe_algo():
    while not terminar_ev.is_set():  # Mientras no se active la señal de terminación
        ev.wait()  # Espera a que se active ev
        if terminar_ev.is_set():  # Si se activa la señal de terminación, salir
            break
        print("Hola")
        ev.clear()  # Resetea la señal para la siguiente iteración

# Crear e iniciar los hilos
T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()

# Esperar a que terminen los hilos
T1.join()
T2.join()

print("Programa finalizado")
