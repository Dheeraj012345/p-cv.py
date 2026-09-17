# #              ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
# #                         rotating and flip th image
# rotation =this is use for to chage the angle of image 90,180 ect
# import cv2
# image=cv2.imread("image/image.jpg")
# rotate=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)# this line use for to rotate the image 
# cv2.imshow("origanal image",image)
# cv2.imshow("rotate image",rotate)
# cv2.imwrite("ROTATE.jpg" ,rotate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #                        Different type of rotation
# import cv2
# image=cv2.imread("image/image.jpg")
# rotate=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)# this line use for to rotate the image 
# rotate1=cv2.rotate(image,cv2.ROTATE_180)
# rotate2=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow("origanal image",image)
# cv2.imshow("rotate image",rotate)
# cv2.imshow("rotate1 image",rotate1)
# cv2.imshow("rotate2 image",rotate2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#                                                            FLIP
# # FLIP=this is use for to change the image coodinat ex=if i see on your self in the  mirror i see my left ear in right and right to left
# # the same things happening with image i change the its codnate its right show in left and left in right
# import cv2
# image=cv2.imread("image/image.jpg")
# flipeed=cv2.flip(image,1)#this line use for flping its flip HORIZONTAL FLIP
# cv2.imshow("origanl image" ,image)
# cv2.imshow("FLIPPED image", flipeed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #                        difrent types of fliping
# import cv2

# image = cv2.imread("image/image.jpg")

# horizontal = cv2.flip(image, 1)
# vertical = cv2.flip(image, 0)
# both = cv2.flip(image, -1)

# cv2.imshow("Original", image)
# cv2.imshow("Horizontal Flip", horizontal)#)#this is use for LEFT <--->RIGHT
# cv2.imshow("Vertical Flip", vertical)#this is use for LEFT <--->RIGHT
# cv2.imshow("Both Flip", both)#this is use for <--->BOTH
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#                    final project

import cv2
# ORIGINAL IMAGE
image=cv2.imread("image/image.jpg")
# 1 ROTATE THE IMAGE
rotated=cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
# 2 HORIZANTAL FLIP
flip=cv2.flip(image,1)
# 3 ROTATE AND FLIP
rotate1=cv2.rotate(image,cv2.ROTATE_180)
flip1=cv2.flip(rotate1,0)
# 4 SHOWING THE ALL IMAGE
cv2.imshow("rotate image" ,rotated)
cv2.imshow("flip image" ,flip)
cv2.imshow("rotate1 image" ,rotate1)
cv2.imshow("flip 1 image" ,flip1)
cv2.waitKey(0)
cv2.destroyAllWindows()