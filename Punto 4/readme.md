# Explicación del Punto 4
Este punto implementa el problema del Productor-Consumidor utilizando hilos y una cola (queue.Queue) en Python. El código implementa sincronización de hilos usando threading.Condition(), que protege la región crítica y evita condiciones de carrera.

## ¿Cómo funciona el código?

- Se crean dos señales (ev y terminar_ev) para coordinar la comunicación entre los hilos.

El primer hilo (genera_eventos):

- Espera 2 segundos.

- Activa la señal (ev.set()), indicando que el otro hilo puede continuar.

- Repite esto 5 veces y luego activa terminar_ev, indicando que el programa debe terminar.

El segundo hilo (escribe_algo):

- Espera a que ev se active.

- Cuando recibe la señal, imprime "Hola", luego borra la señal (ev.clear()) y espera otra vez.

- Si terminar_ev se activa, termina la ejecución.

Ambos hilos terminan y se imprime "Programa finalizado".

## ¿Dónde está la protección de la región crítica?
Uso de with condition:

condition es un objeto de threading.Condition(), que actúa como un candado (Lock) para garantizar que solo un hilo acceda a la cola (q) a la vez.

Se usa dentro de un bloque with, lo que garantiza que el bloqueo se adquiera y libere automáticamente.

El código protege la región crítica (acceso a la cola q) usando threading.Condition() y su sistema de espera y notificación, asegurando que los productores y consumidores se coordinen correctamente.
