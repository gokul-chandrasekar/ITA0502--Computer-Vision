import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
cv2.imshow(frame)
cv2.waitkey(0)
