import os
import psutil

def listar_procesos():
    """Lista los procesos en ejecución con su PID y nombre."""
    print(f"{'PID':<10}{'Nombre del Proceso'}")
    print("="*30)
    
    for proceso in psutil.process_iter(['pid', 'name']):
        print(f"{proceso.info['pid']:<10}{proceso.info['name']}")

def eliminar_proceso(pid):
    """Elimina un proceso por su PID."""
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()  # Intentar cerrar el proceso de forma segura
        print(f"✅ Proceso con PID {pid} terminado.")
    except psutil.NoSuchProcess:
        print("❌ Error: No existe un proceso con ese PID.")
    except psutil.AccessDenied:
        print("❌ Error: No tienes permisos para eliminar este proceso.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

if __name__ == "__main__":
    listar_procesos()
    
    try:
        pid_a_eliminar = int(input("\n🔴 Ingresa el PID del proceso que deseas eliminar: "))
        eliminar_proceso(pid_a_eliminar)
    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
