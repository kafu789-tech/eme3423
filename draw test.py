import cv2
import numpy as np

img =cv2.imread('Resources/cat.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'This is cat',(10,100),font,2,(100,100,100),2)

# img = np.zeros((500,500,3),np.uint8)
#
# img =  cv2.line(img,(0,0),(500,500),(255,0,255),5)
#
# img = cv2.circle(img,(300,200),50,(0,255,0),5)
#
# img = cv2.rectangle(img,(100,100),(200,150),(0,0,255),3)
#
# pts = np.array([[10,20],[20,30],[50,100],[100,200],[300,400],[350,450]],np.int32)
# img = cv2.polylines(img,[pts],True,(0,255,255))
#
# print(img)

cv2.imshow("img",img)

cv2.waitKey(0)