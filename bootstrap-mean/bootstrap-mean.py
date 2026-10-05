import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)
    x = np.asarray(x,dtype=float)
    means = np.zeros((n_bootstrap,1))
    for i in range(n_bootstrap):
        x_b = rng.choice(x,x.shape[0],replace=True)
        means[i]= np.mean(x_b)
    alpha  =(1-ci)/2
    lower = np.quantile(means,alpha)
    upper = np.quantile(means,1-alpha)

    return {
        "bootstrap_mean": np.mean(means),
        "lower":float(lower),
        "upper": float(upper)
    }