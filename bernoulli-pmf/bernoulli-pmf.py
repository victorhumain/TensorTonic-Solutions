import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    a = np.full(len(x),p)
    return {"pmf": np.where(np.array(x)==1,a,1.0-a),
    "mean":float(p),
    "variance":float(p*(1-p))}