                    #    #==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================              WEBCAMP
# import cv2
# cap=cv2.VideoCapture(0)#its use for the on the cemera
# while True:
#     reft,frame=cap.read()#its use for the make the new frame for the cemara
#     cv2.imshow("WEBCAM:",frame)
#     if cv2.waitKey(1) & 0xFF==ord("q"):#its use for the stop the cremara
#         break
# cap.release()
# cv2.destroyAllWindows()


#       FPS(frame par second)

import cv2
import time


# Camera start
cap = cv2.VideoCapture(0)

# Previous time
prev_time = 0


while True:

    # get frame on the cemara
    ret, frame = cap.read()

    # calculate the fps
    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time


    # showing the fps on the screen
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    # Webcam on the screen
    cv2.imshow("Webcam", frame)


    # press the q cemera off
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Camera release
cap.release()

# Window close
cv2.destroyAllWindows()
