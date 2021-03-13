import cv2

image = cv2.imread(r"ImagenT2.png")
 
y=300
x=500
h=0
w=0
crop_image = image[x:w, y:h]
cv2.imshow("Cropped", crop_image)
cv2.waitKey(0)