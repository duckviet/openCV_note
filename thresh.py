import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('hpwink.png')
cv.imshow("puzzle", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grey",  gray)

# Simple thresholding
threshold, thresh  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

threshold, thresh_inv  = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold Inverse", thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 11)
cv.imshow("Adaptive thresholding", adaptive_thresh)

cv.waitKey(0)
