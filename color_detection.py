import cv2
import time
import numpy as np
img=cv2.imread('images.png')
print(img.shape)
time.sleep(1)
img1=cv2.inRange(img,(0,0,0),(100,100,255))
img2=cv2.bitwise_and(img,img,mask=img1)
#cv2.bitwise_and(img,img,mask=img1)
cv2.imshow('img.png',img)
cv2.imshow('mask.png',img1)
cv2.imshow('red.png',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
