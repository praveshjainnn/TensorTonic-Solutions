import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.array(x, dtype = float)
    result = np.where(
    x >= 0, x,
    alpha * x)
    return result

