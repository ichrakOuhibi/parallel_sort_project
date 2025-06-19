import numpy as np
import time

from sequential_sort import sequential_sort
from multiprocess_sort import multiprocess_sort
from multithread_sort import multithread_sort
from prod_cons_sort import prod_cons_sort

N = 50_000  # Ajuste selon ta machine (gros fichier ≈ 1 million lignes)

print("🔁 Génération du tableau de test...")
data = np.random.randint(0, 1_000_000, size=N)

print("\n🎯 Méthode 1 : MonoProcess (Tri séquentiel)")
seq_data = data.copy()
start = time.time()
sequential_sort(seq_data)
end = time.time()
print(f"[MonoProcess] Temps d'exécution : {end - start:.4f} sec")

print("\n🎯 Méthode 2 : MultiProcess + Pipe")
mp_data = data.copy()
multiprocess_sort(mp_data)

print("\n🎯 Méthode 3 : MultiThread + Sémaphores")
mt_data = data.copy()
multithread_sort(mt_data)

print("\n🎯 Méthode 4 : Producteur / Consommateur")
prod_cons_sort()
