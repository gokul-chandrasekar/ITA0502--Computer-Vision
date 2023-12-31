import cv2
img = cv2.imread("C:/Users/GOKUL/Downloads/eye.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("C:/Users/GOKUL/AppData/Local/Programs/Python/Python311/Scripts/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/GOKUL/AppData/Local/Programs/Python/Python311/Scripts/haarcascade_eye.xml")
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
print('Number of detected faces:', len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w] 
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
cv2.imshow('face Detected', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
