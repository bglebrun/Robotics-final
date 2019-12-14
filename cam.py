import cv2
import numpy as np
from matplotlib import pyplot as plt

def PController( LHS, RHS ):
    pos = RHS - LHS
    #if the pos is positive we are too far right, turn left
    if( pos > 0 ):
        print("turn left")

    #if the pos is negative we are too far left, turn right
    if( pos < 0 ):
        print("turn right")

    #if pos == 0 we are dead center drive straight
    if( pos == 0 ):
        print("go straight")

    return

img = cv2.imread('tooRight.jpg', cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)

# Split frame into left and right
RHS = thresh1[144:544, 480:960]
LHS = thresh1[144:544, 0:480]

plt.imshow(RHS, cmap='gray')
plt.show()
plt.imshow(LHS, cmap='gray')
plt.show()


whiteLHS = np.sum(LHS == 255)
print('Number of white pixels LHS:', whiteLHS)

whiteRHS = np.sum(RHS == 255)

print("Number of white pixles RHS: ", whiteRHS)

PController( whiteLHS, whiteRHS )