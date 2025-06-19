import numpy as np
from sequential_sort import sequential_sort
from multiprocess_sort import multiprocess_sort
from multithread_sort import multithread_sort
from prod_cons_sort import prod_cons_sort

if __name__ == "__main__":
   # N = 100_000   ou un nombre plus petit pour tester
    N = 1_000_000
    data = np.random.randint(0, 1_000_000, size=N)

    sequential_sort(data)
    multiprocess_sort(data)
    multithread_sort(data)
    prod_cons_sort(data)
