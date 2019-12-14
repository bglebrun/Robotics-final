#!/usr/bin/env python
"""Primary CV code with image processing, inputs a webcam and then
returns a simplified lane detection algorithm"""

import numpy as np
import cv2

def EXTRACT_KEYFRAME(FRAME):
    LOWER_THRESH = 55
    UPPER_THRESH = 255
    RET, BINARY = cv2.threshold(FRAME, LOWER_THRESH, UPPER_THRESH, cv2.THRESH_BINARY_INV)
    # EDGES = cv2.Canny(BINARY, 100, 200)

    # Gaussian blur for filtering
    BLUR = cv2.GaussianBlur(BINARY, (5, 5), 0)

    return BLUR

def BUILD_BLOB_DETECTOR():
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 255
    
    # Filter by Area.
#    params.filterByArea = True
#    params.minArea = 1
#    params.maxArea = 100
    
    # Filter by Circularity
    # params.filterByCircularity = True
    # params.minCircularity = 0.1
    
    # Filter by Convexity
    # params.filterByConvexity = True
    # params.minConvexity = 0.87
    
    # Filter by Inertia
    #  params.filterByInertia = True
    # params.minInertiaRatio = 0.01
    
    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
    return detector


# Initialize video capture
VIDEO_CAPTURE = cv2.VideoCapture(0)


# While video capture is running
while VIDEO_CAPTURE.isOpened():

    # Get capture frame
    RET, FRAME = VIDEO_CAPTURE.read()

    if not RET:
        break

    # Split frame into left and right
    FRAME_RIGHT = FRAME[0:544, 480:960]
    FRAME_LEFT = FRAME[0:544, 0:480]

    # Logitech camera actual resolution: 960 x 544, 0 starts at top left
    ROI = FRAME[136:544, 0:960]

    # TODO: Old process code, change for left and right frames
    PROCESSED = EXTRACT_KEYFRAME(ROI)

    DETECTOR = BUILD_BLOB_DETECTOR()

    # Detect Blobs
    KEYPOINTS = DETECTOR.detect(PROCESSED)

    IMAGE_KEYPOINTS = cv2.drawKeypoints(PROCESSED, KEYPOINTS, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the resulting processed frame
    cv2.imshow('FRAME', IMAGE_KEYPOINTS)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy and cleanup
VIDEO_CAPTURE.release()
cv2.destroyAllWindows()
