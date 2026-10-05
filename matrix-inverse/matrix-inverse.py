import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    A =np.asarray(A,dtype=float)
    n = A.shape[0]
    I = np.identity(n)
    A_aug = np.concatenate((A,I), axis=1)
    for i in range(n):
        #trouver le pivot
        pivot_row = i + np.argmax(np.abs(A_aug[i:,i]))
        if A_aug[pivot_row, i] == 0.0:
            print(A_aug)
            print(i)
            return None
        #swapper les lignes 
        A_aug[[i, pivot_row]] = A_aug[[i, pivot_row]]
        A_aug[i]  = A_aug[i]/A_aug[i][i]
        for j in range(n):
            if(j!=i):
                A_aug[j] = A_aug[j] - A_aug[j,i]*A_aug[i]  
    return A_aug[:,n:]