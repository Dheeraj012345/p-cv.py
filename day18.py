#                       FACE DETECTION
# Haar cascade=it is a trained detector .its find the face with the help of face  pattrens


import cv2

# YuNet face detection model
model = "face_detection_yunet_2026may.onnx"

# Face detector create
face_detector = cv2.FaceDetectorYN.create(
    model,
    "",
    (320, 320)
)

# Camera ON
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Frame hight and width
    height, width = frame.shape[:2]

    # current frmae size for detector
    face_detector.setInputSize((width, height))

    # Face detect 
    _, faces = face_detector.detect(frame)

    # i face not found
    if faces is not None:

        for face in faces:

            # Face  position
            x = int(face[0])
            y = int(face[1])
            w = int(face[2])
            h = int(face[3])

            #  rectangle around the face
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Face  center
            center_x = x + w // 2
            center_y = y + h // 2

            # Center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Text
            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Final frame show
    cv2.imshow("Face Detection", frame)

    #  exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Camera close
cap.release()
cv2.destroyAllWindows()