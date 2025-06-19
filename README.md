# 🧠 Tri Parallèle d’un Gros Fichier Texte

Projet Python illustrant plusieurs techniques de tri (séquentiel, multi-processus, multi-thread) avec mesures de performances et synchronisation.

---

## 🚀 Objectifs

- Lire un grand tableau (représentant un fichier texte).
- Le trier séquentiellement, puis parallèlement (processus, threads).
- Mesurer les temps d'exécution.
- Synchroniser via :
  - Sémaphores
  - Producteur / Consommateur
- Affichage visuel pour démonstration pédagogique 🎥

---

## 🏗️ Architecture

```bash
parallel_sort_project/
│
├── mono_sort.py               # Tri séquentiel + mesure de temps
├── multi_process_sort.py      # Tri avec multiprocessing + Pipe
├── multi_thread_sort.py       # Tri avec threads + sémaphores
├── producer_consumer.py       # Synchronisation Producteur/Consommateur
├── visual_sort.py             # Animation graphique matplotlib
├── utils/
│   ├── merge_sort.py          # Implémentation Merge Sort
│   ├── merge.py               # Fonction de fusion
│   └── helpers.py             # Fonctions auxiliaires (ex: timers)
├── input.txt                  # Fichier texte simulé
├── README.md
└── requirements.txt           # Dépendances
