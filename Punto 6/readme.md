# Explicación del Punto 6

Este código implementa un programa que ejecuta 10 hilos, cada uno realizando la suma de 100 números aleatorios entre 1 y 1000. Al final, se determina qué hilo obtuvo la suma más alta y se muestra el ganador.

## 🔹 Explicación Paso a Paso

### Diccionario compartido resultados

Se usa para almacenar la suma total de cada hilo, con su identificador como clave.

Se protege con un candado (lock) para evitar problemas de concurrencia.

### Función suma_numeros(hilo_id)

Genera 100 números aleatorios entre 1 y 1000.

Calcula su suma total.

Usa with lock: para evitar accesos simultáneos al diccionario resultados.

Guarda la suma en el diccionario y muestra el resultado del hilo en consola.

### Creación y ejecución de los hilos

Se crean 10 hilos con threading.Thread().

Cada hilo ejecuta la función suma_numeros(), pasando su identificador como argumento.

Se almacenan en una lista hilos y se inician con .start().

### Sincronización con .join()

Se espera a que todos los hilos terminen antes de continuar con el análisis de los resultados.

### Determinación del hilo ganador

Se usa max(resultados, key=resultados.get) para encontrar el hilo con la suma más alta.

Se imprime el hilo ganador y su suma máxima.

