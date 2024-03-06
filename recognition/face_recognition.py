import numpy as np
import cv2  as cv

haar_cascade = cv.CascadeClassifier('recognition\haar_face.xml')

people = ['daili', 'gms', 'hpwink', 'simao']
# features = np.load('features.npy')
# labels = np.load('features.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('recognition\face_trained.yml')

img = cv.imread(r'C:\Users\HP\OneDrive\Máy tính\Processing\Validation\gms (11).png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#  Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a cofidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,225,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,0,225), thickness=2)
    
cv.imshow('Detectd Face', img)

cv.waitKey(0)