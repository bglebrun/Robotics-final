#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2

def extract_keyframe(image, lower_thresh=175, inverted=False):
    """Processes and returns frames for white space counting"""
    upper_thresh = 255
    if inverted:
        thresh_type = cv2.THRESH_BINARY_INV
    else:
        thresh_type = cv2.THRESH_BINARY
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grey, lower_thresh, upper_thresh, thresh_type)
    # EDGES = cv2.Canny(binary, 100, 200)

    # Gaussian blur for "filtering"
    blur = cv2.GaussianBlur(binary, (5, 5), 0)

    return blur

def controller(lhs, rhs, deadzone_val=6000):
    """Processes correct turn direction based on white values"""
    pos = rhs - lhs

    #if the pos is positive we are too far right, turn left
    if pos < -1*deadzone_val:
        print("turn left")

    #if the pos is negative we are too far left, turn right
    elif pos > deadzone_val:
        print("turn right")

    #if pos == 0 we are dead center drive straight
    else:
        print("go straight")

# Initialize video capture
VIDEO_CAPTURE = cv2.VideoCapture(0)

SWITCH = '0 : NORM \n1 : INV'
INV = False

# Create trackbars for value editing
cv2.createTrackbar('threshold', 'FRAME', 175, 255)
cv2.createTrackbar(SWITCH, 'FRAME', 0, 1)
cv2.createTrackbar('deadzone', 'FRAME', 6000, 100000)

THRESHOLD = 0
DEADZONE = 0

# While video capture is running
while VIDEO_CAPTURE.isOpened():

    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    if not RET:
        break

    # Logitech camera actual resolution: 960 x 544, 0 starts at top left
    ROI = FRAME[144:544, 0:960]

    PROCESSED = extract_keyframe(FRAME, THRESHOLD, INV)

    # Split frame into left and right
    FRAME_RIGHT = PROCESSED[144:544, 480:960]
    FRAME_LEFT = PROCESSED[144:544, 0:480]

    LHS_WHITE = np.sum(FRAME_LEFT == 255)
    print('Number of white pixels LHS:', LHS_WHITE)

    RHS_WHITE = np.sum(FRAME_RIGHT == 255)

    print("Number of white pixles RHS: ", RHS_WHITE)

    controller(LHS_WHITE, RHS_WHITE, DEADZONE)

    THRESHOLD = cv2.getTrackbarPos('threshold', 'FRAME')
    S_VAL = cv2.getTrackbarPos(SWITCH, 'FRAME')
    DEADZONE = cv2.getTrackbarPos('deadzone', 'FRAME')

    if S_VAL == 0:
        INV = False
    else:
        INV = True


    # Display the resulting processed frame
    cv2.imshow('FRAME', PROCESSED)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
