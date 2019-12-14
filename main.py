#!/usr/bin/env python
import cv2

VIDEO_CAPTURE = cv2.VideoCapture(-1)
VIDEO_CAPTURE.set(3, 160)
VIDEO_CAPTURE.set(4, 120)

while True:

    RET, FRAME = VIDEO_CAPTURE.read()

    # FRAME = FRAME[60:120, 0:160]

    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(GRAY,(5,5),0)

    RET, THRESH = cv2.threshold(GRAY, 60, 255, cv2.THRESH_BINARY_INV)

    CONTOURS, HIERARCHY = cv2.findContours(THRESH.copy(), 1, cv2.CHAIN_APPROX_NONE)

    if len(CONTOURS) > 0:
        C = max(CONTOURS, key=cv2.contourArea)
        M = cv2.moments(C)

        C_X = int(M['m10']/M['m00'])
        C_Y = int(M['m01']/M['m00'])

        cv2.line(FRAME, (C_X, 0), (C_X, 720), (200, 0, 0), 1)
        cv2.line(FRAME, (0, C_Y), (1280, C_Y), (255, 0, 0), 1)

        cv2.drawContours(FRAME, CONTOURS, -1, (0, 255, 0), 1)

        if C_X >= 120:
            print("Turn Left!")

        if C_X < 120 and C_X > 50:
            print("On Track!")

        if C_X <= 50:
            print("Turn Right")

    else:
        print("I don't see the line")

    #Display the resulting FRAME
    cv2.imshow('FRAME', FRAME)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
