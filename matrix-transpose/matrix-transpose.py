import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here

    A = np.array(A)
    N,M = A.shape
    result = np.zeros((M,N), dtype = A.dtype)
    for i in range(N):
        for j in  range(M):
            result[j,i] = A[i,j] 
    return result



