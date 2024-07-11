import cv2
import numpy as np
image=cv2.imread("C:\\Users\\saran\\Downloads\\THANK YOU.jpg")
hav=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_red=np.array([178,179,0])
upper_red=np.array([255,255,155])
mask=cv2.inRange(hav,lower_red,upper_red)
cv2.imshow("Original Image",image)
cv2.imshow("HSV",mask)
cv2.waitKey(0)


