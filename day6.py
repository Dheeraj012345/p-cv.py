
##        ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================#                             colour change
#    #              BGR TO GRAY
# import cv2
# image=cv2.imread("image/image.jpg")
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#this line use for to colour change
# cv2.imshow("orignal image",image)
# cv2.imshow("GRAY image",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #              BGR TO HSV
# # HSV hue satruation value this is use for the to find the colour detection because
# # they show the storng colour clerly
# # HSV ka full form hai:

# # H = Hue → color ka type
# # S = Saturation → color kitna strong/pure hai
# # # V = Value → color kitna bright/dark hai
# import cv2
# image = cv2.imread("image/image.jpg")
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("Original", image)
# cv2.imshow("HSV", hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #                              slipt the hsv
# import cv2
# image = cv2.imread("image/image.jpg")
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)#its splite the image  in three form 
# H, S, V = cv2.split(hsv)
# cv2.imshow("Hue", H)
# cv2.imshow("Saturation", S)
# cv2.imshow("Value", V)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #                             BGR TO RGB conversation 
# import cv2
# image=cv2.imread("image/image.jpg")
# rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# cv2.imshow("BGR IMAGE",image)
# cv2.imshow("RGB IMAGE",rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#                                 final project
import cv2

# Original image
image = cv2.imread("image/image.jpg")

# BGR → Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# BGR → HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# BGR → RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show images
cv2.imshow("Original BGR", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("RGB", rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()