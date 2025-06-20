import numpy as np
import time
import multiprocessing
from merge_utils import merge_sort, merge

def sort_in_process(sub_array, conn, index):
    print(f"➡️  Processus PID={multiprocessing.current_process().pid} started for part {index}")
    merge_sort(sub_array, 0, len(sub_array) - 1)
    conn.send(sub_array)
    conn.close()
    print(f"✅ Processus PID={multiprocessing.current_process().pid} finished for part {index}")

def merge_two_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return np.array(result)

def multiprocess_sort(arr):
    size = len(arr)
    nb_parts = 4
    chunk_size = size // nb_parts

    processes = []
    pipes = []
    sorted_parts = []

    start = time.time()

    for i in range(nb_parts):
        start_index = i * chunk_size
        end_index = size if i == nb_parts - 1 else (i + 1) * chunk_size
        sub_array = arr[start_index:end_index]

        parent_conn, child_conn = multiprocessing.Pipe()
        p = multiprocessing.Process(target=sort_in_process, args=(sub_array, child_conn, i))
        processes.append(p)
        pipes.append(parent_conn)
        p.start()

    for i, conn in enumerate(pipes):
        try:
            part = conn.recv()
            print(f"✅ Données reçues du processus {i}")
            sorted_parts.append(part)
        except Exception as e:
            print(f"❌ Erreur réception pipe {i} : {e}")

    for p in processes:
        p.join()

    merged = sorted_parts[0]
    for i in range(1, len(sorted_parts)):
        merged = merge_two_sorted(merged, sorted_parts[i])

    end = time.time()
    print(f"[MultiProcess + Pipe] Temps d'exécution : {end - start:.4f} sec")
    return merged
