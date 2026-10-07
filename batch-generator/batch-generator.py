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
    print(inds)
    for i in range(0,n,batch_size):
        if (i+ batch_size)>n:
            if drop_last: 
                pass
            else:
                x_batch = X[inds[i:n]]
                y_batch = y[inds[i:n]]
                yield (x_batch,y_batch)
        else :  
            x_batch = X[inds[i:i+batch_size]]
            y_batch = y[inds[i:i+batch_size]]
            yield(x_batch,y_batch)