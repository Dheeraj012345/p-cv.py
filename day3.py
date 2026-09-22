# #               ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================          
## reading the imformation on the image shape,height,width,chaneles,pixel indexing 
#     #              shape 
import cv2
# image=cv2.imread("image/image.jpg")
# print("image shape: ",image.shape)#this line use for to the print the shape of the image 


# #              acees the height and width and channels in deffrent contener
# image=cv2.imread("image/image.jpg")
# height,width,channels=image.shape #this line use for to store the value in the deffrent contener 
# print("HEIGHT: " ,height)
# print("WIDTH: ", width)
# print("CHANNELS: " ,channels)

# #                       channels

# image=cv2.imread("image/image.jpg")
# blue=image[:,:,:0]
# green=image[:,:,1]
# red=image[:,:,:3]
# print("Blue channel shape: ",blue.shape)
# # print("Green channel shape: ",green.shape)
# # print("Red channel shape: ",red.shape)



# #                         indexing=x
# #                                   (y=row/height direction)
# #                                  (x=coloum/width direction)
# image=cv2.imread("image/image.jpg")
# pixel=image[100,200]
# print(pixel)
# print("blue:",pixel[0])
# print("Green: ",pixel[1])
# print("Red: ",pixel[2])


# #                             multiple pixel
# this is use for the to get he pixel inforamtion of deffrent location
# image=cv2.imread("image/image.jpg")
# pixel1=image[100,200]
# pixel2=image[100,201]
# pixel3=image[101,200]
# pixel4=image[50,50]
# pixel5=image[300,200]
# pixel6=image[600,400]

# print("pixel 1: ",pixel1)
# print("pixel 2: ",pixel2)
# print("pixel 3: ",pixel3)
# print("pixel 4: ",pixel4)
# print("pixel 5: ",pixel5)
# print("pixel 6: ",pixel6)

#                   final porject=all the item come on the one programe
import cv2
# Image read
image=cv2.imread("image/image.jpg")
# Image properties
height,width,channels=image.shape
print("================ IMAGE INFORMATION===============")
print("Height: ", height)
print("Width: ",width)
print("Channels:",channels)
# reading the pixel
pixel1=image[100,200]
pixel2=image[100,300]
pixel3=image[400,200]
pixel4=image[101,340]   
print("\n============== PIXEL INFORMATION=============")
print("pixel 1 BGR : ", pixel1)
print("pixel 2 BGR : ",pixel2)
print("pixel 3 BGR : ",pixel3)
print("pixel 4 BGR : ",pixel4)
