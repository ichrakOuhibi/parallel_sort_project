import threading
import time
import random
from queue import Queue

buffer = Queue(maxsize=5)
N_PRODUCTIONS = 10

def producer(name):
    for i in range(N_PRODUCTIONS):
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"🟢 Producteur {name} ➜ produit {item}")
        time.sleep(random.uniform(0.1, 0.3))
    print(f"✅ Producteur {name} a terminé.")

def consumer(name):
    for i in range(N_PRODUCTIONS):
        item = buffer.get()
        print(f"🔵 Consommateur {name} ➜ consommé {item}")
        time.sleep(random.uniform(0.2, 0.4))
    print(f"✅ Consommateur {name} a terminé.")

def prod_cons_sort():
    p_thread = threading.Thread(target=producer, args=("P1",))
    c_thread = threading.Thread(target=consumer, args=("C1",))

    start = time.time()
    p_thread.start()
    c_thread.start()

    p_thread.join()
    c_thread.join()
    end = time.time()

    print(f"[Producteur/Consommateur] Temps d'exécution : {end - start:.4f} sec")
