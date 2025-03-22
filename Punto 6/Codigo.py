import threading
import random

# Diccionario compartido para almacenar resultados
resultados = {}
lock = threading.Lock()  # Para evitar problemas de concurrencia

def suma_numeros(hilo_id):
    """Función que genera 100 números aleatorios y suma sus valores"""
    suma = sum(random.randint(1, 1000) for _ in range(100))
    
    with lock:  # Sincronización para evitar problemas al escribir en el diccionario
        resultados[hilo_id] = suma

    print(f"Hilo {hilo_id}: suma = {suma}")

# Crear e iniciar 10 hilos
hilos = []
for i in range(1, 11):  # De 1 a 10
    hilo = threading.Thread(target=suma_numeros, args=(i,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Determinar el ganador
hilo_ganador = max(resultados, key=resultados.get)
suma_maxima = resultados[hilo_ganador]

print(f"\n🏆 El Hilo {hilo_ganador} gana con una suma de {suma_maxima}!")
