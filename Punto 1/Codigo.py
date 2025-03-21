import threading

# Variables globales para almacenar las áreas
areas = {}

# Función para calcular el área de un triángulo
def calcular_triangulo(nombre, base, altura):
    areas[nombre] = 0.5 * base * altura

# Función para calcular el área de un rectángulo
def calcular_rectangulo(nombre, base, altura):
    areas[nombre] = base * altura

# Creación de hilos para cada figura
hilos = [
    threading.Thread(target=calcular_triangulo, args=("Triángulo Izquierdo", 10, 12)),
    threading.Thread(target=calcular_rectangulo, args=("Rectángulo Central", 8, 12)),
    threading.Thread(target=calcular_rectangulo, args=("Rectángulo Superior", 6, 8)),
    threading.Thread(target=calcular_rectangulo, args=("Rectángulo Derecho", 5, 6)),
    threading.Thread(target=calcular_triangulo, args=("Triángulo Derecho", 5, 6))
]

# Iniciar los hilos
for hilo in hilos:
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Calcular área total
area_total = sum(areas.values())

# Mostrar resultados
print("Áreas calculadas:", areas)
print("Área total de la figura:", area_total, "m^2")
