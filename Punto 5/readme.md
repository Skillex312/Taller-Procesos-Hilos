# Explicación del Punto 5

Este ejercicio implementa tres hilos para trabajar con una lista compartida de números, con la siguiente lógica:

## Hilo Generador:

Crea números aleatorios entre 1 y 100.

Los inserta en una lista compartida (lista_numeros).

Se ejecuta en un bucle continuo hasta que el supervisor lo detenga.

## Hilo Sustituidor:

Recorre circularmente la lista y busca números que terminan en 0.

Cuando encuentra uno, lo sustituye por -1.

Continúa funcionando hasta que el supervisor lo detenga.

## Hilo Supervisor:

Monitorea la lista y calcula la suma total de los números.

Si la suma supera 20000, cambia la variable running = False para detener los otros hilos.

Imprime un mensaje indicando que el programa finalizó.
