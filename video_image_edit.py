import cv2
import random

cam=cv2.VideoCapture(0)
img=cv2.imread('dog.png')
print(img.size)
while cam.isOpened():
    #print('camera is ready')
    status,frame=cam.read()
    cv2.rectangle(frame,(20,20),(100,100),(0,0,255),2)
    cv2.rectangle(frame,(480,20),(560,100),(0,0,255),2)
    cv2.rectangle(frame,(20,380),(100,460),(0,0,255),2)
    cv2.rectangle(frame,(480,380),(560,460),(0,0,255),2)
    crop_img = frame[20:100, 20:100]
    crop_img1 = frame[20:100, 480:560]
    crop_img2 = frame[380:460, 20:100]
    crop_img3 = frame[380:460, 480:560]
    cv2.imshow('capture', frame)
    #cv2.imshow('crop',crop_img)
    #cv2.imshow('crop1',crop_img1)
    #cv2.imshow('crop2',crop_img2)
    #cv2.imshow('crop3',crop_img3)
    img[200:280, 20:100]=crop_img1
    cv2.imshow('crop4',img)
    #x=random.random()
    #y=str(x)[3:6]
    #cv2.imwrite('/home/inferni/Desktop/mypython/ppp/adhoc'+y+'.jpg',frame)
    if cv2.waitKey(1) & 0xFF==ord('q') :
        break
cv2.destroyAllWindows()
cam.release()


