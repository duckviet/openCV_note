import cv2 as cv
import numpy as np

img = cv.imread('hpwink.png')
cv.imshow("puzzle", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray img', gray)

# Blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur) 

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

# Resize 
resize = cv.resize(img, (400,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resize)

# Cropping
cropped = img[50:200, 200: 400]
cv.imshow("Crop", cropped)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left       x --> Right
# -y --> Up         y --> Down
translated = translate(img, 100, 100)
cv.imshow("Transfrom", translated)

# Rotation
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]
    
    if rotationPoint is None:
        rotationPoint = (width//2, width//2)
        
    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotate", rotated)

# Flipping
flip = cv.flip(img, 1)
cv.imshow("Flip", flip)
cv.waitKey(0)