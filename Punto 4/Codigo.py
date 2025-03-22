import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s')

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)
condition = threading.Condition()

running = True  # Variable de control

class HiloProductor(threading.Thread):
    def __init__(self, name=None):
        super(HiloProductor, self).__init__()
        self.name = name

    def run(self):
        while running:  # Verifica si debe seguir corriendo
            item = random.randint(1, 10)
            with condition:
                while q.full() and running:
                    condition.wait()
                if not running:
                    break
                q.put(item)
                logging.debug(f'Insertando "{item}" : {q.qsize()} elementos en la cola')
                condition.notify()
            time.sleep(random.random())

class HiloConsumidor(threading.Thread):
    def __init__(self, name=None):
        super(HiloConsumidor, self).__init__()
        self.name = name

    def run(self):
        while running:
            with condition:
                while q.empty() and running:
                    condition.wait()
                if not running:
                    break
                item = q.get()
                logging.debug(f'Sacando "{item}" : {q.qsize()} elementos en la cola')
                condition.notify()
            time.sleep(random.random())

p = HiloProductor(name='Productor1')
p2 = HiloProductor(name='Productor2')
c = HiloConsumidor(name='Consumidor')

p.start()
p2.start()
c.start()

# Simulación: el programa se ejecuta por 5 segundos y luego termina
time.sleep(15)
running = False  # Detiene los hilos

# Desbloquear hilos en espera
with condition:
    condition.notify_all()

p.join()
p2.join()
c.join()

logging.debug("Programa finalizado.")
