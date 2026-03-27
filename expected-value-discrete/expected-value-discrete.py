import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x, dtype = float)
    p = np.array(p, dtype = float)
    
    if x.shape != p.shape:
        raise ValueError("x and p must be of same shape")

    if not np.isclose(np.sum(p),1, atol=1e-6):
        raise ValueError("Probailities must sum to 1")

    return float(np.sum(x*p))






    


