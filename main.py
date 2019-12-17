#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2
import atomicpi
import gpio as GPIO

# Initializing our GPIO pins for the atomic pi H bridge controller
# Control by signal ID
GPIO_0 = atomicpi.signals.ISH_GPIO_0.global_idx # Enable A
GPIO.setup(GPIO_0, GPIO.OUT)
GPIO_1 = atomicpi.signals.ISH_GPIO_1.global_idx # Enable B
GPIO.setup(GPIO_1, GPIO.OUT)
GPIO_2 = atomicpi.signals.ISH_GPIO_2.global_idx # INPUT 1
GPIO.setup(GPIO_2, GPIO.OUT)
GPIO_3 = atomicpi.signals.ISH_GPIO_3.global_idx # INPUT 2
GPIO.setup(GPIO_3, GPIO.OUT)
GPIO_4 = atomicpi.signals.ISH_GPIO_4.global_idx # INPUT 3
GPIO.setup(GPIO_4, GPIO.OUT)
GPIO_7 = atomicpi.signals.ISH_GPIO_7.global_idx # INPUT 4
GPIO.setup(GPIO_7, GPIO.OUT)

INPUT_1 = GPIO_2
INPUT_2 = GPIO_3
INPUT_3 = GPIO_4
INPUT_4 = GPIO_7
ENABLE_A = GPIO_0
ENABLE_B = GPIO_1

# Some "Constants"
_THRESHOLD = 0
_DEADZONE = 0
_INV = False
_ROI = 0
SWITCH = '0 : NORM \n1 : INV'

# Right Side
def motor_a_fwd(motor_fwd=True):
    """ Turns on rights side forward """
    if motor_fwd:
        GPIO.output(INPUT_1, True)
        GPIO.output(INPUT_2, False)
    else:
        GPIO.output(INPUT_1, False)
        GPIO.output(INPUT_2, True)

# Left Side
def motor_b_fwd(motor_fwd=True):
    """ Turns on left side forward """
    if motor_fwd:
        GPIO.output(INPUT_3, False)
        GPIO.output(INPUT_4, True)
    else:
        GPIO.output(INPUT_3, True)
        GPIO.output(INPUT_4, False)

# Right Side
def motor_a_on(motor_on=True):
    """ Turns on right side motors """
    if motor_on:
        GPIO.output(ENABLE_A, True)
    else:
        GPIO.output(ENABLE_A, False)

# Left Side
def motor_b_on(motor_on=True):
    """ Turns on left side motors """
    if motor_on:
        GPIO.output(ENABLE_B, True)
    else:
        GPIO.output(ENABLE_B, False)

def change_deadzone(pos):
    global _DEADZONE
    """ deadzone slider callback"""
    _DEADZONE = pos

def flip_thresh_type(pos):
    """ thresh type callback"""
    global _INV
    if pos == 0:
        _INV = False
    else:
        _INV = True

def change_threshold(pos):
    """threshold slider callback"""
    global _THRESHOLD
    _THRESHOLD = pos

def change_roi(pos):
    """roi slider callback"""
    global _ROI
    _ROI = pos

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

def turn_left():
    """ Turns robot left """
    print("Turn left")
    motor_b_on(False)
    motor_a_on(True)

def turn_right():
    """ Turns robot right """
    print("Turn right")
    motor_b_on(True)
    motor_a_on(False)

def straight():
    """ Robot goes straight """
    print("Turn straight")
    motor_a_on(True)
    motor_b_on(True)

def controller(lhs, rhs, deadzone_val=6000):
    """Processes correct turn direction based on white values"""
    pos = rhs - lhs
    print("pos: ", pos)

    #if the pos is positive we are too far right, turn left
    if pos < -1*deadzone_val:
        turn_right()

    #if the pos is negative we are too far left, turn right
    elif pos > deadzone_val:
        turn_left()

    #if pos == 0 we are dead center drive straight
    else:
        straight()

# Initialize video capture and playback
VIDEO_CAPTURE = cv2.VideoCapture(0)
VIDEO_CAPTURE.set(3, 800)
VIDEO_CAPTURE.set(4, 600)
cv2.namedWindow('FRAME')

# Create trackbars for value editing
cv2.createTrackbar('threshold', 'FRAME', 175, 255, change_threshold)
cv2.createTrackbar(SWITCH, 'FRAME', 0, 1, flip_thresh_type)
cv2.createTrackbar('ROI', 'FRAME', 0, 450, change_roi)
cv2.createTrackbar('deadzone', 'FRAME', 6000, 100000, change_deadzone)

# Robot full speed ahead
motor_a_fwd()
motor_b_fwd()

# While video capture is running
while VIDEO_CAPTURE.isOpened():

    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    if not RET:
        break

    # Logitech camera actual resolution: 960 x 544, 0 starts at top left
    # Scaled to 800*600

    PROCESSED = extract_keyframe(FRAME, _THRESHOLD, _INV)

    # Split frame into left and right
    # FRAME_RIGHT = PROCESSED[272:544, 480:960]
    # FRAME_LEFT = PROCESSED[272:544, 0:480]
    FRAME_RIGHT = PROCESSED[_ROI:600, 400:800]
    FRAME_LEFT = PROCESSED[_ROI:600, 0:400]

    LHS_WHITE = np.sum(FRAME_LEFT == 255)
    print('Number of white pixels LHS:', LHS_WHITE)

    RHS_WHITE = np.sum(FRAME_RIGHT == 255)

    print("Number of white pixles RHS: ", RHS_WHITE)

    controller(LHS_WHITE, RHS_WHITE, _DEADZONE)

    COLOR_DBG = cv2.cvtColor(PROCESSED, cv2.COLOR_GRAY2BGR)

    # Draw debug lines
    # X split line
    cv2.line(COLOR_DBG, (400, 0), (400, 800), (0, 255, 0), 1)
    # Y ROI line
    cv2.line(COLOR_DBG, (0, _ROI), (800, _ROI), (0, 255, 0), 1)

    # Display the resulting processed frame
    cv2.imshow('FRAME', COLOR_DBG)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
