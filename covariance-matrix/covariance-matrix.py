import numpy as np

def covariance_matrix(X):
    # Convert input to numpy array
    X = np.asarray(X, dtype=float)
    
    # Check validity: must be 2D and have at least 2 samples
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    
    N, D = X.shape
    
    # Step 1: Center the data
    mu = np.mean(X, axis=0)        # shape (D,)
    X_centered = X - mu            # shape (N, D)
    
    # Step 2: Compute covariance matrix
    Sigma = (X_centered.T @ X_centered) / (N - 1)  # shape (D, D)
    
    return Sigma
