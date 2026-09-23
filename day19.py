#                         object detection
#                   YOLO=you only look once
# yolo is a one type of a object detection model family .its detected the object identify and locates in the frame

#                           CLASS
# class tell what kind of a object in the frame.ex person ,bottle ect
#                         CONFIDENCE
# confidece tells hwo mauch detector confident about the object identity .ex=person 0.97 ect
#                         BOUNDING BOX
# its crete a rectangle shape around the object

from ultralytics import YOLO
import cv2

# YOLO model load
model = YOLO("yolo11n.pt")

# Camera ON
cap = cv2.VideoCapture(0)

while True:

    # Camera frame
    ret, frame = cap.read()

    if not ret:
        break

    # Object detection
    results = model(frame)#this one is important because its found the what type of things i the frame ex=person bottle ,and also object x,y,,w,h,confidence

    # Detection  draw in the frame
    annotated_frame = results[0].plot()#this one is important becaue it use for the write all the in the in the object ex x,y,w,h confidence ,rectnagle

    # Screen  show
    cv2.imshow("YOLO Object Detection", annotated_frame)

    # exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
