#           contours,area,bounding box
# contours=basicly it use for the deteced the boundry nad outline of the object
# area=its use for to knwoing the object area in the image
# bounding box=it is use for the to create the rectangle/box around the object

#                         CONTOURS
# import cv2
# image=cv2.imread("image/image.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# _,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours,hierachy=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#this onr use for the to detected the boundry of the object
# print("Total contorus",len(contours))
# cv2.imshow("Threshold",threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # CONTORUS AREA=its use for the knowing the area of the object to paralle to the contorus
# import cv2

# # Image read
# image = cv2.imread("shape.jpg")

# # Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold
# _, threshold = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY_INV
# )

# # Contours find
# contours, hierarchy = cv2.findContours(
   # threshold,
#     cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE
# )

# # Har contour ka area
# for contour in contours:
#     area = cv2.contourArea(contour)
#     print("Area:", area)

# cv2.imshow("Image", image)
# cv2.imshow("Threshold", threshold)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # BONUDING BOXING=its use for the create the box around the object
# import cv2
# image=cv2.imread("shape.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# _,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
# contours,hiearchy=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# for contour in contours:
#  x,y,w,h=cv2.boundingRect(contour)#that one
#  cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)#that one line use for the boundring box
#  print("X:",x)
#  print("y:",y)
#  print("w:",w)
#  print("h:",h)
# cv2.imshow("bounding boxes",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#         GETING THE CENTER OF THE OBJECT

import cv2

image = cv2.imread("shape.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY_INV
)

contours, hierarchy = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:

    x, y, w, h = cv2.boundingRect(contour)

    center_x = x + w // 2
    center_y = y + h // 2

    print("Center:", center_x, center_y)

    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.circle(
        image,
        (center_x, center_y),
        5,
        (0, 0, 255),
        -1
    )

cv2.imshow("Object Center", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
