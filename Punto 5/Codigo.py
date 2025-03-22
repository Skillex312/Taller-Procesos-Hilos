import threading
import random
import time

# Lista compartida y variable de control
lista_numeros = []
lock = threading.Lock()
running = True  # Controla la ejecución de los hilos

# Hilo 1: Generador de números aleatorios
def generador():
    global running
    while running:
        num = random.randint(1, 100)
        with lock:
            lista_numeros.append(num)
        time.sleep(0.01)  # Pequeña pausa para simular trabajo

# Hilo 2: Sustituidor de números terminados en 0
def sustituidor():
    global running
    while running:
        with lock:
            for i in range(len(lista_numeros)):
                if lista_numeros[i] % 10 == 0:  # Si termina en 0
                    lista_numeros[i] = -1
        time.sleep(0.05)

# Hilo 3: Supervisor (detiene todo cuando suma > 20000)
def supervisor():
    global running
    while running:
        with lock:
            if sum(lista_numeros) > 20000:
                running = False  # Señal para detener los hilos
                print("🔴 Límite alcanzado. Terminando hilos...")
        time.sleep(0.1)

# Crear e iniciar hilos
h1 = threading.Thread(target=generador)
h2 = threading.Thread(target=sustituidor)
h3 = threading.Thread(target=supervisor)

h1.start()
h2.start()
h3.start()

# Esperar a que terminen
h1.join()
h2.join()
h3.join()

# Mostrar resultado final
print("Lista final:", lista_numeros)
print("Suma total:", sum(lista_numeros))
