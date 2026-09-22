#   #            ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
# #                              thersholding
# # this use for convert the image white and black .
# # acordibg to the pixel rule(line) its convert the image in the white and black
k
# and its use for fixed threshold and this is use for object and back ground sparation
# #                           binary thersholding
# import cv2
# image=cv2.imread("image/image.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# _,thershold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# cv2.imshow("real image",image)
# cv2.imshow("gray image",gray)
# cv2.imshow("threshol image",thershold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #                  SIMPLE EXAMPLE
# # Pixel values:

# #   30    80    120    150    200    240
# #    │     │      │      │      │      │
# #    ↓     ↓      ↓      ↓      ↓      ↓
# #    0     0      0     255    255    255
# #    │────────────────│──────────────────
# #         BLACK              WHITE
# #                   ↑
# #              Threshold=127
# # Pixel ≤ 127  →  0   → Black
# # Pixel > 127  → 255 → White


# #                       ADAPTIVE THRESHOLDING
# # its use for acording to the area thresloding
# # its convert the image in the small small part each part has its threshold
# import cv2
# image=cv2.imread("image/image.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)#this line use for adaptethreshold
# cv2.imshow("real image",image)
# cv2.imshow("gray image",gray)
# cv2.imshow("adaptive image",adaptive)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #                   simple example
# #         POORI IMAGE
# #              ↓
# #     ┌────┬────┬────┐
# #     │11×11│11×11│11×11│
# #     ├────┼────┼────┤
# #     │11×11│11×11│11×11│
# #     └────┴────┴────┘
# #        ↓
# # Har area ka local threshold
# #        ↓
# #    Black / White
# # ADAPTIVE THRESHOLD

# # Image ko chhote areas mein dekho
# #      ↓
# # Area 1 → local threshold
# # Area 2 → local threshold
# # Area 3 → local threshold
# #      ↓
# # Black / White


#                OBJECT NAD BACKGROUND SAPARATION
import cv2

# Image read
image = cv2.imread("image/image.jpg")

# Color image → Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding
_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Images show
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Object Background", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()

# #                   FINAL PROJECT
# import cv2
# image=cv2.imread("image/image.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# _,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imshow("real image",image)
# cv2.imshow("gray image",gray)
# cv2.imshow("threshold image",threshold)
# cv2.imshow("adaptive image",adaptive)
# cv2.waitKey(0)
# cv2.destroyAllWindows
