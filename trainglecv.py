import cv2
import numpy as np
path="C:\\Users\\saran\\Downloads\\col.jpg"
image=cv2.imread(path)
window_name='image'
pts=np.array([[35,70],[35,100],[70,120]],np.int32)
pts=pts.reshape((-1,1,2))
isclosed=True
color=(255,0,0)
thickness=2
cv2.polylines(image,[pts],isclosed,color,thickness)
while(1):
               cv2.imshow('image',image)
               if cv2.waitKey(20)&0xFF==27:
                   break
cv2.destroyAllWindows() 
