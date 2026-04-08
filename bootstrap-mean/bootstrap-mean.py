import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
 
    x = np.asarray(x)
    N = len(x)
    rng = rng or np.random.default_rng()

    # Collect bootstrap means
    boot_means = np.empty(n_bootstrap)
    for b in range(n_bootstrap):
        sample = rng.choice(x, size=N, replace=True)
        boot_means[b] = sample.mean()

    # Confidence interval
    alpha = 1 - ci
    lower = np.quantile(boot_means, alpha/2)
    upper = np.quantile(boot_means, 1 - alpha/2)

    return boot_means, lower, upper