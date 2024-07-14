import cv2
image=cv2.imread("C:\\Users\\saran\\Downloads\\superadobe PG1.png")
cv2.imshow('Orginal Image',image)
cv2.waitKey(0)
Gaussian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blurring',Gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
