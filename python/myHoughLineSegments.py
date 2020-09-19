import glob
import os.path as osp
import numpy as np
import cv2


def myHoughLineSegments(img_in, edgeimage, peakRho, peakTheta, rhosscale, thetasscale):
	# Your implemention
    nLines = len(peakRho)
    img_output = np.copy(img_in)

    img_output[:, :, 1] = cv2.add(img_output[:, :, 1], edgeimage * 255)

    '''
    for k in range(nLines):
        # retrive rho and theta values
        rho = rhosscale[peakRho[k]]
        theta = thetasscale[peakTheta[k]]

        # TODO: get the line segment

        # draw lines
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img_output, (x1,y1), (x2,y2), (0,255,0), 1)
    '''

    return img_output