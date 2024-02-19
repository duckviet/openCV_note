import cv2 as cv
import numpy as np

img = cv.imread("hpwink.png")
cv.imshow("g", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# split 
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# merge
merged = cv.merge([b,g,r])
cv.imshow("Merge", merged)

cv.waitKey(0)