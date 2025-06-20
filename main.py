import numpy as np
import time
from load_file import load_file_as_array
from sequential_sort import sequential_sort
from multiprocess_sort import multiprocess_sort
from multithread_sort import multithread_sort
from prod_cons_sort import prod_cons_sort


        # Version ligne de commande
        N = 50_000
        print("\n🔁 Chargement du tableau de test...")
        data = load_file_as_array("large_input.txt")

        print("\n🎯 Méthode 1 : MonoProcess (Tri séquentiel)")
        seq_data = data.copy()
        sequential_sort(seq_data)

        print("\n🎯 Méthode 2 : MultiProcess + Pipe")
        mp_data = data.copy()
        multiprocess_sort(mp_data)

        print("\n🎯 Méthode 3 : MultiThread + Sémaphores")
        mt_data = data.copy()
        multithread_sort(mt_data)

        print("\n🎯 Méthode 4 : Producteur / Consommateur")
        prod_cons_sort()
