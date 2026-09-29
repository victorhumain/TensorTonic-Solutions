import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    pmf,cdf=0,0
    for i in range(k+1):
        pmf = (math.exp(-lam)*math.pow(lam,i))/math.factorial(i)
        cdf= cdf+pmf
    return {
        "pmf": float(pmf),
        "cdf":float(cdf),
    }