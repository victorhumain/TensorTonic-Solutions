import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    var = np.sum((x-np.mean(x))*(x-np.mean(x)))/(len(x)-1)
    return {
        "variance":float(var),
        "standard_deviation":float(np.sqrt(var)),
    }