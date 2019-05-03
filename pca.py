import numpy as np

def pca(a,t):
    """ Returns PCA result matrix

    When t is larger than original dimension,
    returns zero

    Parameters
    ---------
    a : numpy.ndarray (2D)
        matrix to be analyzed
    t : int
        reduced dimension

    Returns
    ---------
    pcv : numpy.ndarray (2D)
        result of PCA

    """
    m, n = a.shape    
    a_cen = a - a.mean(axis=0)
    u, s, vt = np.linalg.svd(a_cen)
    m, n = a_cen.shape
    pcv = np.zeros((n,t))
    try:
        pcv[:,:] = vt.T[:,:t]
    except:
        print('You Entered Wrong t Value')
        return 0
    else:
        return pcv
