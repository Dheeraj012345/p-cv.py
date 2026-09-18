# #       ==============CODE IS ON THE ONLY WHERE THE 1 # their WHERE IS 2## THAT IS USE FOR THE IMFORMATION=====================
#  #                     EDGE DETECTION
# # Edge=where the object bountry is end and the other object boundry start in the image that is called edge
# # Canny eage detection=it is use for to detected or change the object boundary in the image
# import cv2
# image = cv2.imread("image/image.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 100, 200)#this is use for the canny
# edges1 = cv2.Canny(gray, 50, 100)
# edges2 = cv2.Canny(gray, 100, 200)
# edges3 = cv2.Canny(gray, 150, 250)
# edge4=cv2.Canny(gray,200,250)
# cv2.imshow("Original", image)
# cv2.imshow("Edges", edges)
# cv2.imshow("50-100", edges1)
# cv2.imshow("100-200", edges2)
# cv2.imshow("150-250", edges3)
# cv2.imshow("strong image",edge4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # gray
# #  ↓
# # Grayscale image

# # 100
# #  ↓
# # Lower threshold

# # 200
# #  ↓
# # Upper threshold

# #  ↓
# # Canny
# #  ↓
# # Edges
# # Edge strength

# # 0 ─────── 100 ───────── 200 ───────── 255
# #           ↑             ↑
# #         Lower         Upper

# # 200 se upar → Strong edge ✅
# # 100 se neeche → Edge nahi ❌
# # 100–200 ke beech → Weak edge; Canny dekhta hai ki woh kisi strong edge se connected hai ya nahi.
# # Original
# #     ↓
# # Canny
# #     ↓
# # Outer boundary + Object ke andar ke strong changes
