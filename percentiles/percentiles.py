import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    
    x = np.sort(np.array(x))
    q = np.array(q)

    # Use NumPy's built-in interpolation method
    return np.percentile(x, q, method='linear')

