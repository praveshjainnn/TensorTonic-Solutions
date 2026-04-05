import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    arr  = np.array(x)
    mean = float(np.mean(arr))
    median = float(np.median(arr))
    
    # Mode (most frequent, smallest if tie)
    counts = Counter(arr)
    max_freq = max(counts.values())
    mode_candidates = [val for val, freq in counts.items() if     freq == max_freq]
    mode = float(min(mode_candidates))
    
    return mean, median, mode

    
    return mean, median, mode
 



