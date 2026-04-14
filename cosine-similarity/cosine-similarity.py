import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    
    # Compute norms
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    # Handle zero vectors gracefully
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    # Compute dot product and similarity
    similarity = np.dot(a, b) / (norm_a * norm_b)
    return float(similarity)