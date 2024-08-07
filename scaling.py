import cv2
import numpy as np
file_name="C:\\Users\\saran\\Downloads\\superadobe PG1.png"
try:
    img=cv2.imread(file_name)
    (height,width) = img.shape[:2]
    res=cv2.resize(img,(int(width/2), int(height/2)),interpolation=cv2.INTER_LINEAR)
    cv2.imshow('result.png',res)
except IOError:
    print('Error while reading files!!!')
