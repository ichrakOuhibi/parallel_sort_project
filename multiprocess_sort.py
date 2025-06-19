import numpy as np
import time
from multiprocessing import Process, Pipe
import os
from merge_utils import merge_sort

def sort_in_process(arr, conn, idx):
    pid = os.getpid()
    print(f"➡️  Processus PID={pid} started for part {idx}")
    merge_sort(arr, 0, len(arr) - 1)
    print(f"✅ Processus PID={pid} finished for part {idx}")
    conn.send(arr)
    conn.close()

def multiprocess_sort(arr):
    half = len(arr) // 2
    A1, A2 = arr[:half], arr[half:]

    parent_conn1, child_conn1 = Pipe()
    parent_conn2, child_conn2 = Pipe()

    p1 = Process(target=sort_in_process, args=(A1, child_conn1, 1))
    p2 = Process(target=sort_in_process, args=(A2, child_conn2, 2))

    start = time.time()
    p1.start()
    p2.start()

    sorted1 = parent_conn1.recv()
    sorted2 = parent_conn2.recv()

    p1.join()
    p2.join()

    merged = np.concatenate((sorted1, sorted2))
    merge_sort(merged, 0, len(merged) - 1)

    end = time.time()
    print(f"[MultiProcess + Pipe] Temps d'exécution : {end - start:.4f} sec")
    return merged
