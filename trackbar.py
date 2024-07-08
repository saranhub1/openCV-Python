# Python program to create RGB color palette with trackbars importing libraries
import cv2 
import numpy as np 
   
# empty function called when any trackbar moves 
def emptyFunction(self): 
    pass
  
# blackwindow having 3 color chanels 
image = np.zeros((512, 512, 1), np.uint8)  
windowName ="Open CV Color Palette"
      
# window name
#create a window control to contain the trackbar
cv2.namedWindow(windowName)  
       
# there trackbars which have the name 
    # of trackbars min and max value  

cv2.createTrackbar('my track bar 1', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('my track bar 2', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('my track bar 3'. windowName, 0, 255, emptyFunction)
       
# Used to open the window 
# till press the ESC key 
while(True):
    gs = cv2.getTrackbarPos('my track bar', windowName) 
    cv2.imshow(windowName, image) 
    if cv2.waitKey(1) == 27:
        break
         
        # values of blue, green, red
    image[0:255] = [gs]
  
 
           
cv2.destroyAllWindows()
