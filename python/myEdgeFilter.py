import cv2
import numpy as np
import numpy.matlib as npm
import math

from GaussianKernel import Gauss2D
from myImageFilterX import myImageFilterX

from matplotlib import pyplot as plt
import matplotlib

def myEdgeFilter(img0, sigma):
    img0 = img0.astype('float32')

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
    Io = np.arctan(Iy / Ix) # gradient directions

    '''
    plt.imshow(Ix,cmap="gray")
    plt.show()
    plt.imshow(Iy,cmap="gray")
    plt.show()
    '''
    
    Img1 = np.copy(Im)

    # perform NMS in the gradient directions
    dgroups = np.array([0, np.pi / 4, np.pi / 2, (3 / 4) * np.pi, np.pi, - np.pi / 4, - np.pi / 2, - (3 / 4) * np.pi, - np.pi])
    borderSize = 1 # assume a 3*3 filter for NMS

    for i in range(borderSize, len(Im) - borderSize):
        for j in range(borderSize, len(Im[0]) - borderSize):
            idx = np.argmin(np.abs(dgroups - Io[i][j]))

            if idx == 0 or idx == 4 or idx == 9:
                if (Im[i][j] < Im[i][j - 1] or Im[i][j] < Im[i][j + 1]):
                    Img1[i][j] = 0
            elif idx == 2 or idx == 6:
                if (Im[i][j] < Im[i - 1][j] or Im[i][j] < Im[i + 1][j]):
                    Img1[i][j] = 0
            elif idx == 1 or idx == 8:
                if (Im[i][j] < Im[i - 1][j - 1] or Im[i][j] < Im[i + 1][j + 1]):
                    Img1[i][j] = 0
            elif idx == 3 or idx == 5:
                if (Im[i][j] < Im[i - 1][j + 1] or Im[i][j] < Im[i + 1][j - 1]):
                    Img1[i][j] = 0

    return Img1,Io,Ix,Iy


