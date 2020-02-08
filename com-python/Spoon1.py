import cv2
import numpy as np
from skimage.color import rgb2gray
from skimage import io
img = cv2.imread("plastic_dark_background.jpg")
rows,cols = img.shape[0:2]
%matplotlib inline
io.imshow(img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = cv2.drawContours(img, img_contours, -1, (0, 255, 0))
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
img_contours = sorted(img_contours, key=cv2.contourArea)
 
for i in img_contours:
    if cv2.contourArea(i) > 100:
        break

mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [i],-1, 255, -1)

new_img = cv2.bitwise_and(img, img, mask=mask)
io.imshow(new_img)

grayscale = rgb2gray(new_img)
for x in range (1,rows):
        for y in range (1,cols):
            pixel = grayscale[x,y]
            print (pixel)

