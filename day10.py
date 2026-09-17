#             #==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
# #                               BLUE AND NOISE
# import cv2
# # NOISE=In the pictrue some kind of random pixel/doit come . that is called noise
# # BLru=its use for to smoth and clean the image 
# # Noisy Image
# #      ↓
# #     Blur
# #      ↓
# # Smoother/Cleaner Image
# #                              GAUSSIANBLUR
# # 🔵 Gaussian Blur = image ko clear nahi karta, noise ko smooth karke kam karta hai
#its use for general smoothing
# import cv2
# image=cv2.imread("image/image.jpg")
# blur=cv2.GaussianBlur(image,(9,9),0)
# cv2.imshow("real image",image)
# cv2.imshow("blru image",blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#                       MEDIAN BLRU
# # MEDIAN BLRU=this is also use for noise free image but special dost /noise 
# # its use for random/salt nad pepper noise removall
# import cv2

# image = cv2.imread("image/image.jpg")

# median = cv2.medianBlur(image, 5)

# cv2.imshow("Original", image)
# cv2.imshow("Median Blur", median)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # | Gaussian Blur             | Median Blur                      |
# # | ------------------------- | -------------------------------- |
# # | Image ko smooth karta hai | Image ko smooth karta hai        |
# # | General noise reduction   | Random dots/noise ke liye useful |
# # | `cv2.GaussianBlur()`      | `cv2.medianBlur()`               |
# # | `(5,5)` kernel            | `5` kernel                       |


#                          final practical
import cv2
image=cv2.imread("image/image.jpg")
blru1=cv2.GaussianBlur(image,(5,5),0)
blru2=cv2.medianBlur(image,5)
cv2.imshow("real image",image)
cv2.imshow("gaussian image",blru1)
cv2.imshow("median image",blru2)
cv2.waitKey()
cv2.destroyAllWindows



# Gaussian Blur
# → general smoothing / noise reduction

# Median Blur
# → random dots (salt-and-pepper noise)
#    ko remove karne mein especially useful