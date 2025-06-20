import numpy as np

def load_file_as_array(filename):
    with open(filename, "r") as f:
        data = [int(line.strip()) for line in f]
    return np.array(data)