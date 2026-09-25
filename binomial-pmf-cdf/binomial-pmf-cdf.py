import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    cdf, pdf = 0,0
    for i in range(k+1):
        pdf = math.comb(n,i)*pow(p,i)*pow(1.0-p,n-i)
        cdf += pdf

    return {
        "pmf": pdf,
        "cdf":cdf
    }