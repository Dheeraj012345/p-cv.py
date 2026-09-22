# #              ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION===================== 
#               # DRAWING IN OPEN CV
# #                          LINE
# import cv2
# image=cv2.imread("image/image.jpg")
# # cv2.line(image, start_point, end_point, color, thickness)#that is example how the lower line work
# line1=cv2.line(image,(50,50),(300,200),(0,0,225),3)#this line use for to line
# cv2.line(image, (100, 100), (400, 300), (0, 255, 0), 5)
# cv2.imshow("line image" ,image)
# cv2.imshow("line image" ,image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #                  RECTANGLE
# import cv2
# image=cv2.imread("image/image.jpg")
# cv2.rectangle(image,(50,50),(300,440),(0,0,255),4)#this onr use for the rectangle
# cv2.imshow("rectangle image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #                            CRICLE
# import cv2 
# image=cv2.imread("image/image.jpg")
# # cv2.circle(image, center, radius, color, thickness)#that is example how the lower line work
# cv2.circle(image,(200,300),80,(0,0,255),6)#this is for the circle
# cv2.imshow("imgae",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #                                       TEXT AND LABEL
# import cv2
# image=cv2.imread("image/image.jpg")
# # cv2.putText(image, text, position, font, scale, color, thickness)#that is example how the lower line work
# cv2.putText(image,"parat",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),5)#this is for the text and label
# cv2.imshow("image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#                    FINAL PROJECT
import cv2
image=cv2.imread("image/image.jpg")
# line
cv2.line(image,(100,200),(300,400),(0,0,255),5)
# rectangle
cv2.rectangle(image,(200,300),(300,400),(0,0,255),5)
# circle
cv2.circle(image,(200,300),100,(0,0,255),5)
# label and text
cv2.putText(image,"DHEERAJ",(50,50),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255),5)
cv2.imshow("image",image)
cv2.imwrite("label.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
