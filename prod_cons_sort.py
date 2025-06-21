import threading
import time
import numpy as np
from queue import Queue

buffer = Queue(maxsize=4)
sorted_parts = []            # Liste globale pour les morceaux triés
sorted_parts_lock = threading.Lock()
N_PARTS = 4                  # Nombre de blocs à trier

def producer(name, data_parts):
    for part in data_parts:
        buffer.put(part)
        print(f"🟢 Producteur {name} ➜ bloc produit de taille {len(part)}")
        time.sleep(0.1)
    print(f"✅ Producteur {name} a terminé.")

def consumer(name):
    for _ in range(N_PARTS):
        block = buffer.get()
        sorted_block = np.sort(block)  # Le tri réel ici ✅
        with sorted_parts_lock:
            sorted_parts.append(sorted_block)
        print(f"🔵 Consommateur {name} ➜ a trié un bloc de taille {len(block)}")
        time.sleep(0.2)
    print(f"✅ Consommateur {name} a terminé.")

def prod_cons_sort(data):
    global sorted_parts
    sorted_parts = []  # Réinitialiser
    # Découpage du tableau en N blocs
    data_parts = np.array_split(data, N_PARTS)

    p_thread = threading.Thread(target=producer, args=("P1", data_parts))
    c_thread = threading.Thread(target=consumer, args=("C1",))

    start = time.time()
    p_thread.start()
    c_thread.start()

    p_thread.join()
    c_thread.join()

        # Fusion finale des blocs triés
    result = np.concatenate(sorted_parts)
    result = np.sort(result)  # Trie final après concaténation

    end = time.time()
    print(f"[Producteur/Consommateur] Temps d'exécution : {end - start:.4f} sec")

    # ✅ Affichage du résultat trié (partiel ou total selon besoin)
    print("🔢 Extrait du résultat trié :", result[:20])  # afficher les 20 premiers éléments triés

    return result
