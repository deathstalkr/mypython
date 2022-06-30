import cv2
import numpy as ny

# img= cv2.imread('w.jpg')
img1 = cv2.imread('dog.png', 0)
img2 = cv2.imread('dog.png')
img3=cv2.imread('hearts2.jpg')

# x=img.shape
#y = img1.shape
# print(x)
#print(y)
points = ny.array([[80, 182], [94, 182], [87, 176]])
points1=ny.array([[194,241],[222,211],[282,211],[310,241],[282,271],[222,271]])
points2=ny.array([[251,205],[258,199],[265,205]])
cv2.putText(img2, 'DOG', (52, 248),cv2.FONT_HERSHEY_COMPLEX,1.3, (180, 180,0), 5)
cv2.putText(img2, 'puppy', (212, 250),cv2.FONT_HERSHEY_SIMPLEX,0.95, (180, 0, 180), 3)
cv2.polylines(img2,ny.int32([points1]),1,(255,255,0),3)
cv2.line(img2, (87, 207), (87, 176), (0, 0, 255), 3)
cv2.rectangle(img2, (27, 49), (171, 176), (255, 0, 0), 2)
cv2.circle(img2, (256, 133), 59, (0, 0, 0), 2)
cv2.ellipse(img2, (87, 237), (60, 30), 0, 0, 360, (0, 255, 0), 3)
cv2.polylines(img2, ny.int32([points]), 1, (0, 0, 255), 2)
cv2.polylines(img2, ny.int32([points2]), 1, (0, 0, 255), 3)
# img[1000:2000][2000:3000]=[0,0,0]
# img1[250:300,300:450]=[0,0,0]

# cv2.imshow('woman',img)
# cv2.imshow('doggy',img1)
cv2.imshow('doggy2', img2)
cv2.imwrite('doggy2.jpg',img2)
added_image=cv2.addWeighted(img3,0.1,img2,0.9,1)
cv2.imshow('love.jpg',added_image)
cv2.imwrite('doggy_love.jpg',added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
