import cv2
def diff(x,y,z):
    img1=cv2.absdiff(x,y)
    img2=cv2.absdiff(y,z)
    comm_diff=cv2.bitwise_and(img1,img2)
    return comm_diff
cam=cv2.VideoCapture(0)
status,frame1=cam.read()
status,frame2=cam.read()
status,frame3=cam.read()
#gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
#gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
#gray3=cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)
while cam.isOpened():
    img_diff=diff(frame1,frame2,frame3)
    cv2.imshow('diff_img',img_diff)
    status,frame=cam.read()
    frame1=frame2
    frame2=frame3
    frame3=frame                #cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()


