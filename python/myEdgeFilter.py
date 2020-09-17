import cv2
import numpy as np
import numpy.matlib as npm
import math

from GaussianKernel import Gauss2D
from myImageFilterX import myImageFilterX

def myEdgeFilter(img0, sigma):
	# smooth the image
    hfilt = Gauss2D((5,5),sigma)
    Im0X = myImageFilterX(img0, hfilt)

    return Img1,Io,Ix,Iy


