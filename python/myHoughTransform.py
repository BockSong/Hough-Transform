import cv2
import numpy as np


def myHoughTransform(InnputImage, rho_resolution, theta_resolution):
    '''
    theta_resolution: assume in degree
    '''
	# Your implemention

    # init
    rhob = np.sqrt(np.square(InnputImage.shape[0]) + np.square(InnputImage.shape[1]))
    rhos = np.arange(-rhob, rhob, rho_resolution)
    thetas = np.deg2rad(np.arange(-90, 90, theta_resolution))

    H = np.zeros((len(rhos), len(thetas)))

    # hough vote
    edges = np.argwhere(InnputImage > 0)
    '''
    for i in range(len(edges)):
        x, y = edges[i][0], edges[i][1]
        for j in range(len(thetas)):
            theta = thetas[j]
            rho = x * np.cos(theta) + y * np.sin(theta)
            r_idx = np.argmin(np.abs(rhos - rho))

            H[r_idx][j] += 1
        
        if i % 1000 == 0:
            print(i * 1.0 / len(edges))
    '''
    return H, rhos, thetas