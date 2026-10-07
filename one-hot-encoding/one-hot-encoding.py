import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    Y = np.asarray(y,dtype="float")
    high_val = num_classes if num_classes is not None else int(Y.max()+1)
    W = np.asarray([[0.0]*high_val]*len(y),dtype="float")
    for i in range(len(y)):
        W[i,y[i]] = 1 
    return W