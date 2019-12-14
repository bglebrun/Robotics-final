#!/usr/bin/env python
import numpy as np
import cv2

VIDEO_CAPTURE = cv2.VideoCapture(0)

while VIDEO_CAPTURE.isOpened():

    RET, FRAME = VIDEO_CAPTURE.read()

    GRAY_IMG = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    INV_GRAY = cv2.bitwise_not(GRAY_IMG)

    HSV = cv2.cvtColor(FRAME, cv2.COLOR_BGR2HSV)

    LOWER_YELLOW = np.array([20, 100, 100], dtype = "uint8")
    UPPER_YELLOW = np.array([30, 255, 255], dtype = "uint8")

    MASK_YELLOW = cv2.inRange(HSV, LOWER_YELLOW, UPPER_YELLOW)
    MASK_WHITE = cv2.inRange(INV_GRAY, 200, 255)
    MASK_YW = cv2.bitwise_or(MASK_WHITE, MASK_YELLOW)
    MASK_YW_IMAGE = cv2.bitwise_and(INV_GRAY, MASK_YW)

    BLUR_SEED = 5
    BLUR = cv2.GaussianBlur(MASK_YW_IMAGE, (5, 5) , 0)

    #Display the resulting FRAME
    cv2.imshow('FRAME', BLUR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

VIDEO_CAPTURE.release()
cv2.destroyAllWindows()