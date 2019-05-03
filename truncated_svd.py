import numpy as np

def truncated_svd(a,t):
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
        return trunc_U, trunc_D, trunc_Vt
