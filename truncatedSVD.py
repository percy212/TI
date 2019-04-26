import numpy as np

def truncatedSVD(A,t):
    m, n = A.shape

    if t > n :
        print("You Entered Higher Dimension")
        print("Returned Zeros")
        return 0, 0, 0
        
    U,D,Vt = np.linalg.svd(A)

    trunc_U = np.zeros((m,t))
    trunc_D = np.zeros((t,t))
    trunc_V = np.zeros((n,t))

    trunc_U[:,:] = U[:,:t]

    for i in range(t):
        trunc_D[i][i] = D[i]

    trunc_V[:,:] = Vt.T[:,:t]

    return trunc_U, trunc_D, trunc_V
