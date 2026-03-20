import numpy as np

def elu(x, alpha):
    # Convert input to NumPy array
    x = np.array(x, dtype=float)
    
    # Apply ELU element-wise
    result = np.where(x > 0, x, alpha * (np.exp(x) - 1))
    
    # Return list 
    return result.tolist()

