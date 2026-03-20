import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.array(x, dtype = float)
    result = np.maximum(0,x)
    return result


