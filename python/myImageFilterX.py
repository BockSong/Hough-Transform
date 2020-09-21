import cv2
import numpy as np

import math


def myImageFilterX(img0, hfilt):
    hs = len(hfilt)

    # zero padding
    pSize = hs // 2
    imgp = np.pad(img0, ((pSize, pSize), (pSize, pSize)), 'constant')

    # im2col
    ih, iw = (imgp.shape[0] - hs) + 1, (imgp.shape[1] - hs) + 1
    strides = (*imgp.strides[:-2], imgp.strides[-2], imgp.strides[-1], *imgp.strides[-2:])
    col = np.lib.stride_tricks.as_strided(imgp, shape=(ih,iw,hs,hs), strides=strides)

    img1 = np.tensordot(col, hfilt)

    return img1
