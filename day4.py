# #                   ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
# #                        resize
# # its means to change the image height and width
# import cv2
# image=cv2.imread("image/image.jpg")
# resize=cv2.resize(image,(200,300))#that is use for the resize
# cv2.imshow("orignal image:",image)
# cv2.imshow("resize image:",resize) 
# cv2.imwrite("Resize.jpg",resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #                        Crop
# # its means cut the image as your requirement
# import cv2
# image=cv2.imread("image/image.jpg")
# print(image.shape)
# cropped=image[500:678,342:452]#that is use for the crop
# cv2.imshow("origanal image",image)
# cv2.imshow("cropped image",cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# final programe
import cv2
print("==========TRANSPOT THE IMAGE========")
image=cv2.imread("image/image.jpg")
print("===========RESIZE the image=========")
resize=cv2.resize(image,(450,300))
print("===========CROP THE IMAGE===========")
crop=resize[0:300,0:200]
print("==========SHOW THE BOTH IMAGE========")
cv2.imshow("origanl image",image)
cv2.imshow("resize image",resize)
cv2.imshow("crop image",crop)
print("============SAVE THE IMAGE===========")
cv2.imwrite("orignal.jpg",image)
cv2.imwrite("resize.jpg",resize)
cv2.imwrite("crop.jpg",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
