import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X = np.asarray(X,dtype="float")
    n,d = X.shape

    X_c = X - np.mean(X,axis=0)
    C = (X_c.T@X_c)/(n-1)
    eigval, eigvec = np.linalg.eigh(C)
    ind = np.argpartition(eigval, -k)[-k:]
    ind = ind[np.argsort(eigval[ind])[::-1]]
    k_eigval = eigval[ind]
    W = eigvec[:,ind]
    return X_c@W