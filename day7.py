
#        # ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================/
#                       #   revision day1--- day6

import cv2

# Image read
image = cv2.imread("image/image.jpg")

# Image information
height, width, channels = image.shape

print("===== IMAGE INFORMATION =====")
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Resize
resized = cv2.resize(image, (400, 300))

# Crop
cropped = image[100:400, 50:300]

# Rotate 90° clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Horizontal Flip
flipped = cv2.flip(image, 1)

# Show all
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("Resized", resized)
cv2.imshow("Cropped", cropped)
cv2.imshow("Rotated", rotated)
cv2.imshow("Flipped", flipped)
# save all
cv2.imwrite("gray.jpg", gray)
cv2.imwrite("hsv.jpg", hsv)
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("flipped.jpg", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
