from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.sum(x)/len(x)
    cpt = Counter(x)
    mode = np.array(cpt.most_common(1))[:,0].min()
    sorted_x = sorted(x)
    if len(x)%2:
        median = sorted_x[int((len(x))/2)]
    else:
        median = (sorted_x[int(len(x)/2)-1]+sorted_x[int(len(x)/2)])*0.5
    return {"mean":float(mean), "median":float(median), "mode":float(mode)}