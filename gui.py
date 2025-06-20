import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from load_file import load_file_as_array
from sequential_sort import sequential_sort
from multiprocess_sort import multiprocess_sort
from multithread_sort import multithread_sort
from prod_cons_sort import prod_cons_sort
from generate_file import generate_large_file

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_gui():
    data = None

    def load_data():
        nonlocal data
        file = filedialog.askopenfilename(title="Choisir un fichier texte")
        if file:
            try:
                data = load_file_as_array(file)
                status_label.config(text=f"✅ Fichier chargé : {file}", fg="green")
                print(f"Fichier chargé : {file}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Chargement échoué : {e}")
                print(f"Erreur chargement fichier : {e}")

    def generate_file():
        try:
            generate_large_file("large_input.txt", 100_000)
            status_label.config(text="✅ Fichier large_input.txt généré", fg="green")
            print("Fichier large_input.txt généré")
        except Exception as e:
            messagebox.showerror("Erreur", f"Génération échouée : {e}")
            print(f"Erreur génération fichier : {e}")

    def show_chart(frame, times):
        methods = ["MonoProcess", "MultiProcess", "MultiThread", "Prod/Cons"]
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(methods, times, color=['blue', 'green', 'orange', 'purple'])
        ax.set_ylabel("Temps (sec)")
        ax.set_title("Comparaison des temps d'exécution")
        ax.grid(True, axis='y')

        # Supprimer ancien graphique
        for widget in frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        print("Graphique affiché")

    def run_all():
        if data is None:
            messagebox.showwarning("Données manquantes", "Veuillez charger un fichier d'abord")
            print("Données manquantes: pas de fichier chargé")
            return

        out.delete(1.0, tk.END)
        out.insert(tk.END, "🔁 Lancement des tris...\n")
        print("Lancement des tris...")

        seq_data = data.copy()
        mp_data = data.copy()
        mt_data = data.copy()

        try:
            _, t1 = sequential_sort(seq_data)
            print(f"MonoProcess tri fini en {t1:.4f} sec")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur MonoProcess: {e}")