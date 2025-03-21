## Algoritmo para calcular el área de la figura

```pseudo
Inicio
    Definir variables: area_total, areas[]
    
    Iniciar Hilos:
        Hilo_1: Calcular área de Triángulo Izquierdo (base=10, altura=12)
        Hilo_2: Calcular área de Rectángulo Central (base=8, altura=12)
        Hilo_3: Calcular área de Rectángulo Superior (base=6, altura=8)
        Hilo_4: Calcular área de Rectángulo Derecho (base=5, altura=6)
        Hilo_5: Calcular área de Triángulo Derecho (base=5, altura=6)

    Esperar a que todos los hilos finalicen

    Calcular área total:
        area_total = Suma de todas las áreas

    Mostrar area_total
Fin

