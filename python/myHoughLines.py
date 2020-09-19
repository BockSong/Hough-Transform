import numpy as np



def myHoughLines(H, nLines):
    # Your implemention

    H_sup = np.copy(H)
    borderSize = 1 # 3*3 filter used for NMS

    # perform NMS to all neighbors
    for i in range(borderSize, len(H) - borderSize):
        for j in range(borderSize, len(H[0]) - borderSize):
            if (H[i][j] != np.amax(H[i - 1:i + 2, j - 1:j + 2])):
                H_sup[i][j] = 0

    # find top nLines
    rhos = (-np.sum(H_sup, axis=1)).argsort()[:nLines]
    thetas = (-np.sum(H_sup, axis=0)).argsort()[:nLines]

    return rhos,thetas