import cv2
import numpy as np

img = cv2.imread('Resources/cat.jpg')

roi = img[0:250,200:800]
cv2.imshow("roi",roi)
cv2.moveWindow('roi',800,50)

imgray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
imgray = cv2.cvtColor(imgray,cv2.COLOR_GRAY2BGR)
img[0:250,200:800] = imgray


cv2.imshow("img",img)
cv2.imshow("Gray",imgray)
cv2.waitKey(0)
