import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x, dtype=float)
    n = len(x)
    
    # Sample mean
    xbar = np.mean(x)
    
    # Sample standard deviation (Bessel correction)
    s = np.sqrt(np.sum((x - xbar)**2) / (n - 1))
    
    # Standard error
    se = s / np.sqrt(n)
    
    # t-statistic
    t_stat = (xbar - mu0) / se
    return float(t_stat)