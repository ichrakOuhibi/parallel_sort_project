import numpy as np
import time

def print_bar_array(arr, max_height=50):
    scaled = [int((val / max(arr)) * max_height) for val in arr]
    for h in scaled:
        print("█" * h)
    print('-' * 40)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print_bar_array(arr)
                time.sleep(0.05)

if __name__ == "__main__":
    arr = np.random.randint(1, 20, 20)
    print("Avant le tri :")
    print_bar_array(arr)
    print("\nTri en cours...\n")
    bubble_sort(arr)
    print("\nAprès le tri :")
    print_bar_array(arr)
