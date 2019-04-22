import numpy as np

def PCA(A,t):
    A_cen = A - A.mean(axis=0)

    U, D ,Vt = np.linalg.svd(A_cen)

    m, n = A_cen.shape

    PCV = np.zeros((n,t))

    PCV[:,:] = Vt.T[:,:t]

    return PCV
