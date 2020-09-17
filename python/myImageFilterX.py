import cv2
import numpy as np

import math


def myImageFilterX(img0, hfilt):
    # Your implemention

    fSize = len(hfilt)
    img1 = np.zeros_like(img0) # 0 padding

    borderSize = math.floor(fSize / 2)

    for i in range(borderSize, len(img0) - borderSize):
        for j in range(borderSize, len(img0[0]) - borderSize):
            area = img0[i - borderSize : i + borderSize + 1, j - borderSize : j + borderSize + 1]
            #print(i, ", ", j, ", ", area.shape)
            img1[i][j] = np.sum(area * hfilt) # element-wise

    return img1
