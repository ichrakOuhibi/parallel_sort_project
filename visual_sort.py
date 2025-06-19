import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Algorithme de tri avec capture d'étapes ---
def bubble_sort(arr):
    frames = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                frames.append(arr.copy())  # Capture après échange
    return frames

# --- Animation ---
def animate_sort(frames):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0])), frames[0], color="skyblue")

    ax.set_title("Tri à bulles - Animation")
    ax.set_xlabel("Index")
    ax.set_ylabel("Valeur")

    def update(frame):
        for rect, val in zip(bar_rects, frame):
            rect.set_height(val)
        return bar_rects

    anim = animation.FuncAnimation(fig, update, frames=frames, interval=50, repeat=False)
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    arr = np.random.randint(1, 100, 30)
    frames = bubble_sort(arr.copy())
    animate_sort(frames)
