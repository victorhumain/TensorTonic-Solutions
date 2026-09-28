import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    N = len(X)
    X = np.array(X)
    X_c = X - np.mean(X,axis=0)
    sigma  = (X_c.T@X_c)/(N-1)
    stds = np.sqrt(np.diag(sigma))
    stds_p = np.outer(stds,stds)
    stds_pr = stds_p.reshape(sigma.shape[0],sigma.shape[1])
    return sigma/stds_pr