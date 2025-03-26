# Explicación del Punto 9

El código original tenía un problema de ejecución secuencial:

Procesaba 1,000 órdenes de manera una por una.
Cada orden tenía un time.sleep(random.uniform(0, 1)), lo que hacía que todo tardara demasiado (~9 min).

## ¿Cómo se optimizó?
1️⃣ Uso de ThreadPoolExecutor
📌 Se reemplazó el bucle for tradicional por un ThreadPoolExecutor con max_workers=10.

## Conclusión
Esta optimización transforma un proceso secuencial en uno concurrente usando ThreadPoolExecutor. La clave fue paralelizar las operaciones costosas, reduciendo el tiempo de espera innecesario. 🚀
