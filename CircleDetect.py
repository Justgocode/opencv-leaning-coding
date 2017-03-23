#!/usr/bin/env python

import cv2
import numpy as np
led = cv2.imread('./Opencv/Contours Detect/LED.gif')
gray_imgae = cv2.cvtColor(led, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_imgae, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    50,
    param1=100,
    param2=30,
    minRadius=0,
    maxRadius=50)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(led, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(led, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imwrite('LED_Circle.jpg', led)
cv2.imshow('HoughCircle', led)
cv2.waitKey()
cv2.detroyAllWindows()
