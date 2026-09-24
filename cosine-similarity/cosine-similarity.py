import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot_product = float(np.sum(np.array(a)*np.array(b)))
    norm_a= np.linalg.norm(a,2)
    norm_b= np.linalg.norm(b,2)
    if norm_a * norm_b == 0:
        return 0.0
    else :
        return float(dot_product/(norm_a*norm_b))