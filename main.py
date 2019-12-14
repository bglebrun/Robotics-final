#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2

# Initialize video capture
VIDEO_CAPTURE = cv2.VideoCapture(0)

# While video capture is running
while VIDEO_CAPTURE.isOpened():
    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    # Grayscale and invert
    GRAY_IMG = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    INV_GRAY = cv2.bitwise_not(GRAY_IMG)

    # HSV for yellow masking
    HSV = cv2.cvtColor(FRAME, cv2.COLOR_BGR2HSV)

    # Define Yellow-white mask
    LOWER_YELLOW = np.array([20, 100, 100], dtype="uint8")
    UPPER_YELLOW = np.array([30, 255, 255], dtype="uint8")

    # Apply masks for yellow-white detection
    MASK_YELLOW = cv2.inRange(HSV, LOWER_YELLOW, UPPER_YELLOW)
    MASK_WHITE = cv2.inRange(INV_GRAY, 200, 255)
    MASK_YW = cv2.bitwise_or(MASK_WHITE, MASK_YELLOW)
    MASK_YW_IMAGE = cv2.bitwise_and(INV_GRAY, MASK_YW)

    # Gaussian blur for filtering
    BLUR = cv2.GaussianBlur(MASK_YW_IMAGE, (5, 5), 0)

    # Canny edge detection threshold, try 1:2 or 1:3
    LOW_THRESH = 50
    HIGH_THRESH = 150

    CANNY_EDGE = cv2.Canny(BLUR, LOW_THRESH, HIGH_THRESH)

    LINES = cv2.HoughLines(CANNY_EDGE, 1, np.pi/180, 200)

    hough_calc = np.copy(FRAME) * 0

    for line in LINES:
        for x1, y1, x2, y2 in line:
            cv2.line(hough_calc, (x1, y1), (x2, y2), (255, 0, 0), 10)

    FINAL = cv2.addWeighted(FRAME, 0.8, hough_calc, 1, 0)

    # Display the resulting processed frame
    cv2.imshow('FRAME', FINAL)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
