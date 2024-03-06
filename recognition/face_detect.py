import cv2 as cv

img = cv.imread("Pic/hpwink (1).png")
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


haar_cascade = cv.CascadeClassifier("recognition\haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255,0), thickness=2)
    
cv.imshow("Face detect", img)
cv.waitKey(0)
