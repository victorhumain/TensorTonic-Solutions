import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.array(A)
    A_prime = np.zeros((A.shape[1],A.shape[0]))
    for i in range(A.shape[1]):
        A_prime[i,:] = A [:,i]
    return A_prime