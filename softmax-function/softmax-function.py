import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here

    x = np.array(x, dtype=float)

    if x.ndim == 1:
        x = x - np.max(x)                 # numerical stability
        exp_x = np.exp(x)
        return exp_x / np.sum(exp_x)

    elif x.ndim == 2:
        x = x - np.max(x, axis=1, keepdims=True)   # FIXED LINE
        exp_x = np.exp(x)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)



