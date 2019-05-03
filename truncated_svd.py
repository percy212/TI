import numpy as np

def truncated_svd(a,t):
    """ Returns truncatedSVD result matrices


    When t is larger than original dimension,
    return zeros

    
    Parameters
    ---------
    a : numpy.ndarray (2D)
        matrix to be decomposed
    t : int
        dimension to reduce

    Returns
    ---------
    trunc_u : numpy.ndarray (2D)
        truncated u matrix
    trunc_s : numpy.ndarray (2D)
        truncated s matrix
    trunc_vt : numpy.ndarray (2D)
        truncated vt matrix
    """
    m, n = a.shape
    u, s, vt = np.linalg.svd(a)
    trunc_u = np.zeros((m,t))
    trunc_s = np.zeros((t,t))
    trunc_vt = np.zeros((t,n))
    try:
        trunc_u[:,:] = u[:,:t]
        for i in range(t):
           trunc_s[i][i] = s[i]
        trunc_vt[:,:] = vt[:t,:]
    except:
        print('You Entered Wrong t Value')
        return 0, 0, 0
    else:
        return trunc_u, trunc_s, trunc_vt
