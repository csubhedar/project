import cv2
import numpy as np

r_cascade=cv2.CascadeClassifier('rooafza10.xml')

cap=cv2.VideoCapture(0)

while(cap.isOpened):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ru=r_cascade.detectMultiScale(gray,1.2,6)
    for(x,y,w,h) in ru:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(25) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
