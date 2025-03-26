# Explicación del Punto 3

Imagina que tienes dos personas trabajando juntas en una tarea:

Persona 1 (hilo T1) tiene un temporizador y cada cierto tiempo da una señal para que la otra persona haga algo.

Persona 2 (hilo T2) espera la señal antes de hacer su parte del trabajo.

## 💡 ¿Cómo funciona el código?

Se crean dos señales (ev y terminar_ev) para coordinar la comunicación entre los hilos.

El primer hilo (genera_eventos):

Espera 2 segundos.

Activa la señal (ev.set()), indicando que el otro hilo puede continuar.

Repite esto 5 veces y luego activa terminar_ev, indicando que el programa debe terminar.

El segundo hilo (escribe_algo):

Espera a que ev se active.

Cuando recibe la señal, imprime "Hola", luego borra la señal (ev.clear()) y espera otra vez.

Si terminar_ev se activa, termina la ejecución.

Ambos hilos terminan y se imprime "Programa finalizado".
