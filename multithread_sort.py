import numpy as np
import time
import threading
from threading import Semaphore
from merge_utils import merge_sort

semaphore = Semaphore(0)
sorted_parts = []

def thread_sort(arr, idx):
    thread_name = threading.current_thread().name
    print(f"➡️  Thread {thread_name} started for part {idx}")
    merge_sort(arr, 0, len(arr) - 1)
    print(f"✅ Thread {thread_name} finished for part {idx}")
    sorted_parts.append((idx, arr))
    semaphore.release()

def multithread_sort(arr):
    global sorted_parts
    sorted_parts = []

    parts = np.array_split(arr, 2)
    threads = []

    start = time.time()
    for i, part in enumerate(parts):
        t = threading.Thread(target=thread_sort, args=(part, i), name=f"T{i}")
        threads.append(t)
        t.start()

    for _ in threads:
        semaphore.acquire()

    for t in threads:
        t.join()

    sorted_parts.sort()
    merged = np.concatenate([part for _, part in sorted_parts])
    merge_sort(merged, 0, len(merged) - 1)
    end = time.time()
    print(f"[MultiThread + Sémaphore] Temps d'exécution : {end - start:.4f} sec")
    return merged
