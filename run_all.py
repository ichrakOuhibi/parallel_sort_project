import numpy as np
import time
import psutil
import os
import threading
from load_file import load_file_as_array
from sequential_sort import sequential_sort
from multiprocess_sort import multiprocess_sort
from multithread_sort import multithread_sort
from prod_cons_sort import prod_cons_sort

results = []

def track_memory(main_pid, result_dict):
    process = psutil.Process(main_pid)
    peak_mem = 0

    while result_dict["running"]:
        mem = process.memory_info().rss
        for child in process.children(recursive=True):
            try:
                mem += child.memory_info().rss
            except psutil.NoSuchProcess:
                continue
        peak_mem = max(peak_mem, mem)
        time.sleep(0.1)

    result_dict["peak"] = peak_mem / 1024 / 1024  # Convert to MB

def measure(method_name, func, data_copy):
    print(f"\n🎯 {method_name}")
    result_dict = {"running": True, "peak": 0}
    main_pid = os.getpid()

    tracker = threading.Thread(target=track_memory, args=(main_pid, result_dict))
    tracker.start()

    start = time.time()
    func(data_copy)
    end = time.time()

    result_dict["running"] = False
    tracker.join()

    exec_time = end - start
    cpu_used = psutil.cpu_percent(interval=1)
    ram_used = result_dict["peak"]

    print(f"⏱️ Temps d'exécution : {exec_time:.4f} sec")
    print(f"🧠 RAM utilisée (peak total) : {ram_used:.2f} MB")
    print(f"💻 CPU utilisé : {cpu_used:.2f} %")

    results.append((method_name, exec_time, ram_used, cpu_used))
# Chargement des données
data = load_file_as_array("large_input.txt")

# Exécution
measure("MonoProcess", sequential_sort, data.copy())
measure("MultiProcess + Pipe", multiprocess_sort, data.copy())
measure("MultiThread + Sémaphores", multithread_sort, data.copy())
measure("Producteur / Consommateur", lambda _: prod_cons_sort(), None)
#measure("Producteur / Consommateur", prod_cons_sort, None)

# Résumé
print("\n📊 Résumé Comparatif :")
print("Méthode\t\t\tTemps(s)\tRAM(MB)\t\tCPU(%)")
for name, t, ram, cpu in results:
    print(f"{name:<24}{t:.4f}\t\t{ram:.2f}\t\t{cpu:.2f}")
