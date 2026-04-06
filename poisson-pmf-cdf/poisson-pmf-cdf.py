import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    
    # ----- log(k!) -----
    if k == 0:
        log_fact_k = 0.0
    else:
        log_fact_k = np.sum(np.log(np.arange(1, k + 1)))
    
    # ----- PMF -----
    log_pmf = -lam + k * np.log(lam) - log_fact_k
    pmf = np.exp(log_pmf)
    
    # ----- CDF -----
    cdf = 0.0
    
    for i in range(k + 1):
        
        if i == 0:
            log_fact_i = 0.0
        else:
            log_fact_i = np.sum(np.log(np.arange(1, i + 1)))
        
        log_pmf_i = -lam + i * np.log(lam) - log_fact_i
        cdf += np.exp(log_pmf_i)
    
    return float(pmf), float(cdf)