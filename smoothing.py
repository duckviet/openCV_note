import cv2 as cv
import numpy as np

img = cv.imread("hpwink.png")
cv.imshow("Normal", img)

# Average
average = cv.blur(img, (7,7))
cv.imshow("Average", average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian", gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 25, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)