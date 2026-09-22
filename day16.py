# colour detection
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ref,frame=cap.read()
    if not ref:
        break
    # BGR 2 HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # COLOR RANGE OF RED
    lowwer_red=np.array([0,100,100])
    uppper_red=np.array([30,255,255])
    # MASK OF RED COLOR
    mask=cv2.inRange(frame,lowwer_red,uppper_red)
    # RESULT
    result=cv2.bitwise_and(frame,frame,mask=mask)
    # SHOWING THE ALL IMAGE
    cv2.imshow("origanl",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("result",result)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()