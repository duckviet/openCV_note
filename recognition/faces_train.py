import os
import cv2 as cv
import numpy as np

people = ['daili', 'gms', 'hpwink', 'simao']
DIR = r'C:\Users\HP\OneDrive\Máy tính\Processing\Training'

haar_cascade = cv.CascadeClassifier('recognition\haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path =os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('recognition\face_trained.yml')
np.save('recognition\features.npy', features)
np.save('recognition\labels.npy', labels)