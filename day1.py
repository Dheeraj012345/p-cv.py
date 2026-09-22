# #              ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
#  import cv2
# image= cv2.imread("image1.jpg")#this is use for the read the image
# cv2.imshow("MY image",image)#that is use for show the image in the terminal
# print(image.shape)
# pixel=image[100,200]
# print(pixel)
# print("BGR value: ",pixel)
# if pixel[2]>200:
# print("RED value is high hai")
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#         SAPATARE THE SHAPE OF THE IMAGE
# import cv2
# image = cv2.imread("image.jpg")
# height, width, channels = image.shape
# red_pixels = 0
# for y in range(height):
#     for x in range(width):

#         pixel = image[y, x]

#         B = pixel[0]
#         G = pixel[1]
#         R = pixel[2]

#         if R > 200 and G < 100 and B < 100:
#             red_pixels = red_pixels + 1

# print("Red pixels:", red_pixels)


import cv2
import numpy as np

image = cv2.imread("image1.jpg")

lower = np.array([0, 0, 150])
upper = np.array([100, 100, 255])

mask = cv2.inRange(image, lower, upper)

cv2.imshow("Original Image", image)
cv2.imshow("Red Area", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
