import cv2
import numpy as np
import numpy.matlib as npm
import math

from GaussianKernel import Gauss2D
from myImageFilterX import myImageFilterX

from matplotlib import pyplot as plt
import matplotlib

def myEdgeFilter(img0, sigma):
	# smooth out the image with the Gaussian kernel
    hsize = 2 * math.ceil(3 * sigma) + 1
    hfilt = Gauss2D((hsize, hsize), sigma)
    img0X = myImageFilterX(img0, hfilt)

    # find image gradient in the x and y directions
    sobel_x = np.array([(1, 0, -1), (2, 0, -2), (1, 0, -1)])
    sobel_y = np.transpose(sobel_x)

    Ix = myImageFilterX(img0X, sobel_x)
    Iy = myImageFilterX(img0X, sobel_y)

    # compute edge magnitude image and edge orientation image
    Im = np.sqrt(np.square(Ix) + np.square(Iy))
    Io = np.arctan(Iy / Ix)

    # perform NMS
    Img1 = Im

    '''
    plt.imshow(Ix,cmap="gray")
    plt.show()
    plt.imshow(Iy,cmap="gray")
    plt.show()
    '''
    
    return Img1,Io,Ix,Iy


