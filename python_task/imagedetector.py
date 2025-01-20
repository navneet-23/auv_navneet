import cv2 
import os
import matplotlib.pyplot as plt
import numpy as np
print('Hopefully no eror')
shape = cv2.imread('color.png')
greyshape = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(greyshape, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i = 0
for contour in contours:
    if i == 0:
        i = 1
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        print('triangle')
    elif len(approx) == 4:
        print('sqaure')
    elif len(approx) == 5:
        print('Pentagon')
    elif len(approx) == 6:
        print('Hexagon')
    elif len(approx) == 7:
        print('How many will you check dude')
    else:
        print('Circle')
hsv_image = cv2.cvtColor(shape, cv2.COLOR_BGR2HSV)
lred = np.array([0, 120, 70])
ured = np.array([10, 255, 255])
mask = cv2.inRange(hsv_image, lred, ured)
result = cv2.bitwise_and(shape, shape, mask=mask)
cv2.imshow('Original Image', shape)
cv2.imshow('Detected Color', result)
cv2.waitKey(0)
cv2.destroyAllWindows()