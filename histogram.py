import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('hpwink.png')
cv.imshow("puzzle", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# circle = cv.circle(blank, (img.shape[1]//2+50, img.shape[0]//2), 200, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow("Masked", mask)
# # Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
