##Punto 1

Descripción General

Este ejercicio del taller trata sobre el cálculo del área de una figura compuesta utilizando hilos en Python. Se dividen los cálculos en diferentes hilos para ejecutarlos en paralelo y mejorar la eficiencia.

Estructura de la Carpeta

La carpeta contiene los siguientes archivos:

Algoritmo.md: Explica el algoritmo utilizado para el cálculo del área.

Codigo.py: Implementación en Python del algoritmo utilizando hilos.

Explicación del Algoritmo

Definición de variables para almacenar las áreas individuales y el área total.

Creación de cinco hilos para calcular áreas de diferentes secciones:

Triángulo Izquierdo (base=10, altura=12)

Rectángulo Central (base=8, altura=12)

Rectángulo Superior (base=6, altura=8)

Rectángulo Derecho (base=5, altura=6)

Triángulo Derecho (base=5, altura=6)

Ejecución en paralelo de los hilos para calcular las áreas.

Espera a que los hilos finalicen.

Suma de las áreas calculadas.

Impresión del resultado final.

Explicación del Código

El código en Codigo.py implementa el algoritmo utilizando la biblioteca threading en Python:

Variables globales: Un diccionario areas almacena las áreas calculadas.

Funciones para calcular áreas:

calcular_triangulo(nombre, base, altura): Calcula el área de un triángulo.

calcular_rectangulo(nombre, base, altura): Calcula el área de un rectángulo.

Creación y ejecución de hilos:

Se crean 5 hilos con threading.Thread().

Se inician con .start().

Se sincronizan con .join().

Cálculo final: Se suman las áreas y se muestran los resultados.

Ejecución del Programa

Para ejecutar el programa, usa el siguiente comando en la terminal:

python Codigo.py

Salida Esperada

Áreas calculadas: {'Triángulo Izquierdo': 60.0, 'Rectángulo Central': 96, 'Rectángulo Superior': 48, 'Rectángulo Derecho': 30, 'Triángulo Derecho': 15.0}
Área total de la figura: 249.0 m^2

Conclusión

Este ejercicio demuestra el uso de hilos en Python para paralelizar cálculos, lo que mejora la eficiencia en tareas que pueden dividirse en subprocesos independientes.

