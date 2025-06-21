import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# --- Algorithme de tri avec capture d'étapes ---
def bubble_sort(arr):
    frames = []
    colors = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            color_frame = ['skyblue'] * len(arr)
            color_frame[j] = 'red'
            color_frame[j+1] = 'red'
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            frames.append(arr.copy())
            colors.append(color_frame)
    return frames, colors

# --- Animation ---
def animate_sort(frames, colors):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0])), frames[0], color="skyblue")

    def update(i):
        for rect, val, col in zip(bar_rects, frames[i], colors[i]):
            rect.set_height(val)
            rect.set_color(col)
        return bar_rects

    anim = animation.FuncAnimation(fig, update, frames=len(frames), interval=50, repeat=False)
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    arr = np.random.randint(1, 100, 30)
    frames, colors = bubble_sort(arr.copy())
animate_sort(frames, colors)
