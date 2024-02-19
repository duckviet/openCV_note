import cv2 as cv

# Read image

# img = cv.imread("cs112-01.png")
# cv.imshow("Letter", img)
# cv.waitKey(0)

# Read videos

capture = cv.VideoCapture('IMG_1228.mp4')
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()