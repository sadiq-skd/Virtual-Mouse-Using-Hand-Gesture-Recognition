import cv2
import numpy as np
import HandTracking as Ht
import autopy
import pyautogui
import sys
from HandTracking import HandDetector
try:
    width = 640
    height = 480
    frameR = 100
    smoothening = 8
    prev_x, prev_y = 0, 0
    curr_x, curr_y = 0, 0
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    detector: HandDetector = Ht.HandDetector(maxHands=1)
    screen_width, screen_height = autopy.screen.size()
    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=False)
        lmlist, bbox = detector.findPosition(img, draw=False)
        if len(lmlist)!= 0:
            x1, y1 = lmlist[8][1:]
            x2, y2 = lmlist[12][1:]
            x4, y4 = lmlist[4][1:]
            x5, y5 = lmlist[20][1:]
            fingers = detector.fingersUp()
            cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)
            if fingers[1] == 1 and fingers[2] == 0:
                x3 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
                y3 = np.interp(y1, (frameR, height-frameR), (0, screen_height))
                curr_x = prev_x + (x3 - prev_x)/smoothening
                curr_y = prev_y + (y3 - prev_y) / smoothening
                autopy.mouse.move(screen_width - curr_x, curr_y)
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y
            if fingers[1] == 1 and fingers[2] == 1:
                length, img, lineInfo = detector.findDistance(8, 12, img)
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.leftClick()
            if fingers[1] == 1 and fingers[3] == 1:
                length, img, lineInfo = detector.findDistance(8, 4, img)
                if length < 20:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.rightClick()
            if fingers[1] == 1 and fingers[4] == 1:
                length, img, lineInfo = detector.findDistance(8, 20, img)
                if length < 80:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.mouseDown()
        cv2.imshow("Mouse", img)
        cv2.waitKey(1)
except KeyboardInterrupt:
    sys.exit()
