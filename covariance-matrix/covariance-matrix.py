import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X_c = X - np.mean(X,axis=0)
    sigma = (X_c.T@X_c)*(1/(len(X)-1))
    
    return sigma
