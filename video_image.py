import cv2
import random
import os

cam=cv2.VideoCapture(0)
while cam.isOpened():
    #print('camera is ready')
    status,frame=cam.read()
    bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.rectangle(frame,(200,100),(400,300),(0,0,255),2)
    cv2.putText(frame,'Solomon',(250,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow('capture', frame)
    #cv2.imshow('capture1', bwimg)
    k=cv2.waitKey(1)
    print(k)
    if  k%256 == 27:
        break
    elif k%256 == 32:
        # SPACE pressed
        x=random.random()
        y=str(x)[3:6]
        cv2.imwrite('capture'+y+'.jpg',frame)
        print('capture')
        os.system('sshpass -p (password)  scp /home/inferni/Desktop/mypython/capture'+y+'.jpg user@IP:/var/www/html/images')
cv2.destroyAllWindows()
cam.release()


