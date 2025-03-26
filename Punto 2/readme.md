# Explicación del Punto 2
El segundo punto trata sobre la creación de una secuencia numérica compartida entre hilos en Python. (Se refiere a una lista de números generada y utilizada dentro de un hilo en Python, pero accesible para el flujo principal del programa.)

Explicación del Código (Codigo.py)

calcular_secuencia(n1, n2):

Si n1 < n2, genera una lista con los números en ese rango y la imprime.

Si n1 >= n2, muestra un mensaje de error.

main():

Crea un hilo para ejecutar calcular_secuencia(n1, n2).

Espera a que el hilo termine (.join()).

Calcula y muestra la resta n2 - n1.
