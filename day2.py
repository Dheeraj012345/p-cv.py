
# #                 ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================import cv2
# image=cv2.imread("image1.jpg")#this is use for to read the image
# print(image)
# print(image.shape)#this is use for to get shape of the image like width ,hight and chenels
# cv2.imshow("my image",image)#this is use for the show the imaege in the window 
# cv2.waitKey(0)
# cv2.destroyAllWindows


#                    this is use for when image in anothe folder
# image=cv2.imread("image/image.jpg")#that is use for the read and show the image if image is another folder
# cv2.imshow("my image",image)
# print(image.shape)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#                         imwrite()
# write the image that is use for to save the image 
# image=cv2.imread("image/image.jpg")
# cv2.imshow("origanal image",image)
# cv2.imwrite("dheeraj.jpg",image)#that is use for to save the image in the folder with your any name 
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #                         imgae procesing
# # image procesing use for to covert the photo colour one format to anothe format
# image=cv2.imread("image/image.jpg")
# cv2.imshow("origanal image",image)
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#this line chage the colour of the photo 
# cv2.imshow("gray image",gray)
# cv2.imwrite("gray.jpg",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#                   final project
import cv2
image=cv2.imread("image/image.jpg")
cv2.imshow("origanel image",image)
cv2.imwrite("DHEERAJ.jpg",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("edite image",gray)
cv2.imwrite("dheerajgray.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


