import threading

def calcular_secuencia(n1, n2):
    if n1 < n2:
        secuencia = list(range(n1, n2 + 1))
        print(f"Secuencia compartida: {secuencia}")
    else:
        print("n1 no es menor que n2, no se puede calcular la secuencia.")

def main():
    n1 = int(input("Ingrese el primer número (n1): "))
    n2 = int(input("Ingrese el segundo número (n2): "))

    hilo = threading.Thread(target=calcular_secuencia, args=(n1, n2))
    hilo.start()
    hilo.join()

    resultado_resta = n2 - n1
    print(f"Resultado de la resta (n2 - n1): {resultado_resta}")

if __name__ == "__main__":
    main()
