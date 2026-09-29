import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    N = len(x)
    x = np.asarray(x,dtype="float")
    x_bar = np.mean(x)
    s = np.sqrt((1/(N-1))*np.sum((x-x_bar)**2))
    return float((x_bar - mu0)/(s/np.sqrt(N)))