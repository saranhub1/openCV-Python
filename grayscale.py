import cv2
image=cv2.imread("C:\\Users\\saran\\Downloads\\superadobe PG1.png")
window_name='image'
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow(window_name, image)
