import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x, dtype = float)
    y = np.array(y, dtype = float)
    diff = x - y
    dis = np.sqrt(np.sum(diff ** 2))
    return float(dis)

