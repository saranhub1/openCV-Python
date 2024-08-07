import cv2
import numpy as np
image=cv2.imread("C:\\Users\\saran\\Downloads\\superadobe PG1.png")
height, width = image.shape[:2]
quarter_height, quarter_width = height/4, height/4
T=np.float32([[1,0, quarter_width],[0,1, quarter_height]])
img_translation=cv2.warpAffine(image,T,(width,height))
cv2.imshow("Orginalimage", image)
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)
cv2.destryAllWindows()
