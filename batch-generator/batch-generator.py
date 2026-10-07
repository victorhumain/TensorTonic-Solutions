import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    rng  = np.random.default_rng(seed)
    X,y = np.asarray(X,dtype="float"),np.asarray(y,dtype="float"),
    n = len(X)
    inds = np.arange(n)
    rng.shuffle(inds)
    for i in range(0,n,batch_size):
        batchs_inds = inds[i:i+batch_size]
        if drop_last and batchs_inds.size <batch_size:
            break
        x_batch = X[batchs_inds]
        y_batch = y[batchs_inds]
        yield(x_batch,y_batch)