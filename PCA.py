import numpy as np

def PCA(A,t):
    m, n = A.shape
    
    if t > n :
        print("You Entered Higher Dimension")
        print("Returned Zero")
        return 0
    
    A_cen = A - A.mean(axis=0)

    U, D ,Vt = np.linalg.svd(A_cen)

    m, n = A_cen.shape

    PCV = np.zeros((n,t))

    PCV[:,:] = Vt.T[:,:t]

    return PCV
