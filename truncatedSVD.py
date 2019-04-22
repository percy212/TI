import numpy as np

def truncatedSVD(A,t):
    U,D,Vt = np.linalg.svd(A)
    m, n = A.shape

    trunc_U = np.zeros((m,t))
    trunc_D = np.zeros((t,t))
    trunc_V = np.zeros((n,t))

    trunc_U[:,:] = U[:,:t]

    for i in range(t):
        trunc_D[i][i] = D[i]

    trunc_V[:,:] = Vt.T[:,:t]

    return trunc_U, trunc_D, trunc_V
