import time
from merge_utils import merge_sort

def sequential_sort(arr):
    A = arr.copy()
    start = time.time()
    merge_sort(A, 0, len(A) - 1)
    end = time.time()
    print(f"[MonoProcess] Temps d'exécution : {end - start:.4f} sec")
    return A
