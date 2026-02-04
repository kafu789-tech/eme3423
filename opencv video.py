import cv2

capture = cv2.VideoCapture("Resources/kitten.mp4")

while True:
    success, img = capture.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'This is kitten', (10, 100), font, 2, (100, 100, 100), 2)
    
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("img",img)

    if cv2.waitKey(20) & 0xff ==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()