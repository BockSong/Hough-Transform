import cv2
import numpy as np

import math

def myImageFilter(img0, hfilt):
    '''
    img0: numpy array
    hfilt: numpy array
    '''
    # Your implemention
    #print(type(hfilt))

    fSize = len(hfilt)
    img1 = np.zeros_like(img0) # 0 padding

    borderSize = math.floor(fSize / 2)

    for i in range(borderSize, len(img0) - borderSize):
        for j in range(borderSize, len(img0[0]) - borderSize):
            area = img0[i - borderSize : i + borderSize + 1, j - borderSize : j + borderSize + 1]
            #print(i, ", ", j, ", ", area.shape)
            img1[i][j] = np.sum(area * hfilt) # element-wise

    return img1
