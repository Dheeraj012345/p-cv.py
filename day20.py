#         COMPUTR VISION MINI PROJECT 
#               simple progarame 
import cv2
from ultralytics import YOLO
# YOLO MODEL
model=YOLO("yolo11n.pt")
# CEMARA OPEN
cap=cv2.VideoCapture(0)
while True:
    ref,frame=cap.read()
    if not ref:
        break
    # FOR THE YOLO PROPERTIES
    result=model(frame)
    # FOR THE DETAIL ON THE FRAME
    annotaed_frame=result[0].plot()
    # SHOWING THE FRAME
    cv2.imshow("DETECTION MODEL",annotaed_frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

#                    ADVANCE PROGRAME

import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    #  FOR THE COUNTING 
    count = 0
    #  FOR SAPARETE THE ALL ITEM WHO IS  SHOW IN THE FRAME
    for box in results[0].boxes:
        # CHECKING THE CONFIDENCE THE ITEM IN THE FRAME
        confidence = float(box.conf[0])
        # FOR THE CONFIDENCE LIMIT
        if confidence > 0.5:
        #   ADD THE DETECTED OBJECT 
            count = count + 1
            #  ITS USE FOR THE CLASS ID EX=person have one id and bottle has sencond id
            class_id = int(box.cls[0])
            # CONVERT THE CLASS ID INTO A ACTUAL NAME
            name = model.names[class_id]
            # FOR THE POSISAING
            x, y, w, h = map(int, box.xywh[0])
            # FOR THE RECTANGLE AROUND THE OBJECT
            cv2.rectangle(
                frame,
                (x-w//2, y-h//2),
                (x+w//2, y+h//2),
                (0,255,0),
                2
            )
            # FOR PUTING THE NAME AND CONFIDECE OF THE OBJECT
            cv2.putText(
                frame,
                f"{name} {confidence:.2f}",
                (x-w//2, y-h//2-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

    # FOR COUNT THE ALL OBJECT IN THE SCREEN
    cv2.putText(
        frame,
        f"Objects: {count}",
        (10,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )
#    SHOWING THE IMAGE
    cv2.imshow("Day 20", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindo