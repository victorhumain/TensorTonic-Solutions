import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrice = np.array(matrix)
    norm = {"l2":2,"l1":1,"max":np.inf}
    if (axis==None):
        normes = np.linalg.norm(matrice.ravel(), ord=norm[norm_type],keepdims=True)
    else :
        normes = np.linalg.norm(matrice,axis=axis,ord=norm[norm_type],keepdims=True)
    normes = np.where(normes!=0,normes,1.0)

    return matrice/normes