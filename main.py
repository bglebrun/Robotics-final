#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2

# Some "Constants"
_THRESHOLD = 0
_DEADZONE = 0
_INV = False
SWITCH = '0 : NORM \n1 : INV'

def change_deadzone(pos):
    """ deadzone slider callback"""
    _DEADZONE = pos

def flip_thresh_type(pos):
    """ thresh type callback"""
    if pos == 0:
        _INV = False
    else:
        _INV = True

def change_threshold(pos):
    """threshold slider callback"""
    _THRESHOLD = pos

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

cv2.namedWindow('FRAME')

# Create trackbars for value editing
cv2.createTrackbar('threshold', 'FRAME', 175, 255, change_threshold)
cv2.createTrackbar(SWITCH, 'FRAME', 0, 1, flip_thresh_type)
cv2.createTrackbar('deadzone', 'FRAME', 6000, 100000, change_deadzone)

# While video capture is running
while VIDEO_CAPTURE.isOpened():

    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    if not RET:
        break

    # Logitech camera actual resolution: 960 x 544, 0 starts at top left
    ROI = FRAME[144:544, 0:960]

    PROCESSED = extract_keyframe(FRAME, _THRESHOLD, _INV)

    # Split frame into left and right
    FRAME_RIGHT = PROCESSED[144:544, 480:960]
    FRAME_LEFT = PROCESSED[144:544, 0:480]

    LHS_WHITE = np.sum(FRAME_LEFT == 255)
    print('Number of white pixels LHS:', LHS_WHITE)

    RHS_WHITE = np.sum(FRAME_RIGHT == 255)

    print("Number of white pixles RHS: ", RHS_WHITE)

    controller(LHS_WHITE, RHS_WHITE, _DEADZONE)

    _THRESHOLD = cv2.getTrackbarPos('threshold','FRAME')
    _DEADZONE = cv2.getTrackbarPos('deadzone', 'FRAME')
    _INV = cv2.getTrackbarPos(SWITCH, 'FRAME')

    # Display the resulting processed frame
    cv2.imshow('FRAME', PROCESSED)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
