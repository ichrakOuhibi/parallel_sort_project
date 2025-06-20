import numpy as np
import time
import threading
from merge_utils import merge_sort, merge

def multithread_sort(arr):
    size = len(arr)
    nb_parts = 4
    chunk_size = size // nb_parts

    semaphores = [threading.Semaphore(0) for _ in range(nb_parts)]
    sorted_parts = [None] * nb_parts

    def thread_sort(sub_array, index):
        print(f"➡️  Thread T{index} started for part {index}")
        merge_sort(sub_array, 0, len(sub_array) - 1)
        sorted_parts[index] = sub_array
        print(f"✅ Thread T{index} finished for part {index}")
        semaphores[index].release()

    threads = []
    start = time.time()

    for i in range(nb_parts):
        start_idx = i * chunk_size
        end_idx = size if i == nb_parts - 1 else (i + 1) * chunk_size
        sub_array = arr[start_idx:end_idx]
        t = threading.Thread(target=thread_sort, args=(sub_array, i))
        threads.append(t)
        t.start()

    for sem in semaphores:
        sem.acquire()

    part1 = np.concatenate((sorted_parts[0], sorted_parts[1]))
    merge(part1, 0, len(sorted_parts[0]) - 1, len(part1) - 1)

    part2 = np.concatenate((sorted_parts[2], sorted_parts[3]))
    merge(part2, 0, len(sorted_parts[2]) - 1, len(part2) - 1)

    final = np.concatenate((part1, part2))
    merge(final, 0, len(part1) - 1, len(final) - 1)

    end = time.time()
    print(f"[MultiThread + Sémaphores] Temps d'exécution : {end - start:.4f} sec")
    return final