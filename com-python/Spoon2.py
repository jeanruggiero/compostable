import cv2

img = cv2.imread("plastic_dark_background.jpg")
print(type(img))
height, width = img.shape[0:2]
print(img.shape[0:2])
cv2.imshow('Original Image', img)
cv2.waitKey(0)
