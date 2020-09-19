import numpy as np



def myHoughLines(H, nLines):
    # Your implemention

    # perform NMS to all neighbors
    H_sup = np.copy(H)
    borderSize = 1 # 3*3 filter for NMS

    for i in range(borderSize, len(H) - borderSize):
        for j in range(borderSize, len(H[0]) - borderSize):
            pass

    # find top nLines
    rhos = np.zeros((nLines))
    thetas = np.zeros((nLines))

    return rhos,thetas