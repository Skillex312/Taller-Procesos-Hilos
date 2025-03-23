from datetime import datetime, timedelta
import time
import uuid
import random
from concurrent.futures import ThreadPoolExecutor

class OrdersManager:
    __orders = []
    __orders_processed = 0
    __last_printed_log = datetime.now()

    def __init__(self) -> None:
        self.__generate_fake_orders(quantity=1_000)

    def __generate_fake_orders(self, quantity):
        self.__log("Generating fake orders")
        self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__log(f"{len(self.__orders)} generated...")

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order
        time.sleep(random.uniform(0, 1))  # Simula el tiempo de guardado en DB
        return f"Order [{id}] {number} was successfully processed."

    def process_orders(self):
        with ThreadPoolExecutor(max_workers=10) as executor:  # Procesa 10 órdenes en paralelo
            results = executor.map(self.__fake_save_on_db, self.__orders)
            
            for idx, result in enumerate(results, 1):
                self.__orders_processed += 1
                if idx % 50 == 0:  # Imprimir log cada 50 órdenes
                    self.__log(f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}")

orders_manager = OrdersManager()

start_time = time.time()
orders_manager.process_orders()
delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecución optimizado: {delay:.2f} segundos...")
 
