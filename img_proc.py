import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

orig = cv.imread('sample_test.png')
img1 = cv.cvtColor(orig, cv.COLOR_BGR2GRAY)
ret,thresh4 = cv.threshold(img1,45,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img1,45,255,cv.THRESH_TOZERO_INV)

plt.subplot(2,1,1), plt.imshow(thresh4,'gray')
plt.subplot(2,1,2), plt.imshow(thresh5, 'gray')
plt.show()