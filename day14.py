# live video processing
import cv2

# Camera start
cap = cv2.VideoCapture(0)

while True:

    # Camera se frame lena
    ret, frame = cap.read()

    # Check frame mila ya nahi
    if not ret:
        print("Frame nahi mila")
        break

    # Color frame ko grayscale mein convert
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Grayscale se edges detect
    edges = cv2.Canny(gray, 100, 200)

    # Teen windows
    cv2.imshow("Original", frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("Edges", edges)

    # Q dabane par band
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Camera band
cap.release()
cv2.destroyAllWindows()
