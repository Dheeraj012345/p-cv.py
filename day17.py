#                    object tracking
#                   RED OBJECT TRACKING
# centroid=it is a object center point .itd detected the center point of objectq

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # BGR → HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color range
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Red mask
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        # Contour area
        area = cv2.contourArea(contour)

        if area > 500:

            # Bounding box
            x, y, w, h = cv2.boundingRect(contour)

            # Center
            center_x = x + w // 2
            center_y = y + h // 2

            # Rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Coordinates
            cv2.putText(
                frame,
                f"Center: ({center_x}, {center_y})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("Object Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Camera
#   ↓
# Frame
#   ↓
# BGR → HSV
#   ↓
# Red ki range
#   ↓
# Mask
#   ↓
# Contours
#   ↓
# Area check
#   ↓
# Bounding Box
#   ↓
# Center Point
#   ↓
# Rectangle + Dot
#   ↓
# Final Frame