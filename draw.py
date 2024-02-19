import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# # Bases RGB color
# blank[:] = 0,0,255
# cv.imshow("Green", blank)

#1. Paint the image
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Green", blank)

#2. Draw a Rectangle
#           ...      start position    end position        color      border
cv.rectangle(blank, (100,100),         (250,250),         (0,250,0), thickness=-1)
cv.imshow("Rectangle", blank)


#3. Draw a circle
cv.circle(blank, (100,100), 50, (180, 0,  0), thickness=-1)
cv.imshow("Circle", blank)

# 4. Draw a line 
cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),thickness=3 )
cv.imshow("Line", blank)


#5. Write text
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (225, 255, 255), 2)
cv.imshow("Text", blank)

cv.waitKey(0)