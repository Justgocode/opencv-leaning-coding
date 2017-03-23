#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.pyrDown(
    cv2.imread("./Opencv/Contours Detect/LED.gif", cv2.IMREAD_UNCHANGED))
img0 = img.copy()
ret, thresh = cv2.threshold(
    cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 80, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)
img1 = thresh.copy()
img2 = image.copy()
img3 = contours.copy()

print(contours)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rect = cv2.minAreaRect(c)  # 这里是求得轮廓信息的最小区域，opencv中并没有直接从轮廓信息得到最小句矩形坐标的方法。
    box = cv2.boxPoints(rect)  # 1 
    box = np.int0(box)  # 2 经过1,2步就可以由最小区域得到矩形的坐标，此时的坐标点事福点事，所以需要3的函数来进行转换
    cv2.drawContours(img, [box], 0, (255, 255, 255),
                     3)  # 第三个参数是绘制的轮廓数组的索引，如果是-1就绘出所有的轮廓，负责绘出指定的
    # 第四的参数是颜色，第五个参数是指定绘图的密度
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0, 255, 0), 1)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
cv2.imshow("img0", img0)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.detroyAllWindows()
