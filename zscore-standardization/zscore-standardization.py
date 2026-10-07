import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    X = np.asarray(X,dtype="float")
    stds = np.std(X, axis = axis,keepdims=True)
    stds = np.where(stds>eps,stds, np.inf)
    return (X - np.mean(X, axis=axis,keepdims=True))/stds