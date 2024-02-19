import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imageBasic'
images = []  # List to store images in the folder
classNames = []

# Get the names of the files in the 'imageBasic' folder
myList = os.listdir(path)
print(myList)

for cl in myList:
    currImg = cv2.imread(f'{path}/{cl}')
    images.append(currImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        mydatalist = f.readlines()
        print(mydatalist)
        nameList = []
        for line in mydatalist:
            entry = line.split(',')
            nameList.append(entry[0].strip())  # Strip the whitespace from the name
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
x
# To find the encodings of the images in the 'imageBasic' folder
encodeListKnown = findEncodings(images)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    # Reduce the size of the image to increase processing speed
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the current frame
    facesCurrFrame = face_recognition.face_locations(imgS)
    encodesCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

    for encodeFace, faceLoc in zip(encodesCurrFrame, facesCurrFrame):
        # Compare faces and get the distances
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)

        # Find the index of the closest match
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            # Create rectangles around the recognized face and display the name
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the webcam feed
        break

cap.release()
cv2.destroyAllWindows()
