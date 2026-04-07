import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    
    n = len(x)
    if n < 2:
        raise ValueError("Sample size must be at least 2")
    mean = sum(x) / n
    sq_dev = sum((xi - mean) ** 2 for xi in x)
    var = sq_dev / (n - 1)   # Bessel's correction
    std = var ** 0.5
    return var, std