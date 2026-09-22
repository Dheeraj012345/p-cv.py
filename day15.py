# #                  motion detection

# #                     frame detection
# import cv2
# cap=cv2.VideoCapture(0)
# # while True:
# ref,frame1=cap.read()
# ref,frame2=cap.read()
# gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
# gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
# difference=cv2.absdiff(gray1,gray2)#its use for the defrrenciate the two frame
# cv2.imshow("frame1",gray1)
# cv2.imshow("frame2",gray2)
# cv2.imshow("defference",difference)
# cv2.waitKey(0)
# cap.release()
# cv2.destroyAllWindows()

# background detection

import cv2

cap = cv2.VideoCapture(0)

# first frame
ret, previous_frame = cap.read()

# first frame convert into gray
previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

while True:

    # new frame
    ret, current_frame = cap.read()

    if not ret:
        break

    # new frame convert into the gray
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # defference between first one and new one
    difference = cv2.absdiff(previous_gray, current_gray)

    #  convert the Difference into black white
    _, threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    # moment detection
    motion = cv2.countNonZero(threshold)

    if motion > 110:
        cv2.putText(
            current_frame,
            "Motion Detected!",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    else:
        cv2.putText(
            current_frame,
            "No Motion",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # showing  the current frame
    cv2.imshow("Motion Detector", current_frame)

    # that one is the one of the important line because 
    # its mean frame 1 for frame 2 and frame 2 for frame 3 ---------------
    previous_gray = current_gray

    # press q for them exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

# Frame 1
#    ↓
# Frame 2
#    ↓
# absdiff()
#    ↓
# Difference
#    ↓
# threshold()
#    ↓
# Black + White
#    ↓
# countNonZero()
#    ↓
# White pixels count
#    ↓
# if motion > 500
#    ↓
# Motion / No Motion
