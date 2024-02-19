import cv2 as cv
import matplotlib.pyplot as plt 


img = cv.imread("hpwink.png")

# plt.imshow(img)
# plt.show()

cv.imshow("g", img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to L a b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# plt.show()
cv.imshow("RGB", rgb)

cv.waitKey(0)