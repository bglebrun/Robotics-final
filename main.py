#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2

def EXTRACT_KEYFRAME(FRAME, LOWER_THRESH=175, inverted=False):
    UPPER_THRESH = 255
    if inverted:
        TYPE = cv2.THRESH_BINARY_INV
    else:
        TYPE = cv2.THRESH_BINARY
    GREY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    RET, BINARY = cv2.threshold(GREY, LOWER_THRESH, UPPER_THRESH, TYPE)
    # EDGES = cv2.Canny(BINARY, 100, 200)

    # Gaussian blur for filtering
    BLUR = cv2.GaussianBlur(BINARY, (5, 5), 0)

    return BLUR

def CONTROLLER(LHS, RHS):
    DEADZONE = 6000
    pos = RHS - LHS
    # TODO Update comments
    #if the pos is positive we are too far right, turn left
    if pos < -1*DEADZONE:
        print("turn left")

    #if the pos is negative we are too far left, turn right
    elif pos > DEADZONE :
        print("turn right")

    #if pos == 0 we are dead center drive straight
    else:
        print("go straight")

    return

# Initialize video capture
VIDEO_CAPTURE = cv2.VideoCapture(0)


# While video capture is running
while VIDEO_CAPTURE.isOpened():

    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    if not RET:
        break

    # Logitech camera actual resolution: 960 x 544, 0 starts at top left
    ROI = FRAME[144:544, 0:960]

    PROCESSED = EXTRACT_KEYFRAME(FRAME)

    # Split frame into left and right
    FRAME_RIGHT = PROCESSED[144:544, 480:960]
    FRAME_LEFT = PROCESSED[144:544, 0:480]

    whiteLHS = np.sum(FRAME_LEFT == 255)
    print('Number of white pixels LHS:', whiteLHS)

    whiteRHS = np.sum(FRAME_RIGHT == 255)

    print("Number of white pixles RHS: ", whiteRHS)

    CONTROLLER(whiteLHS, whiteRHS)

    # Display the resulting processed frame
    cv2.imshow('FRAME', PROCESSED)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
