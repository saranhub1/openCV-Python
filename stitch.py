import cv2
image_paths=("C:\\Users\\saran\\Downloads\\superadobe PG1.png","C:\\Users\\saran\\Downloads\\noi.jpg")
image=[]
for i in range(len(image_paths)):
    image.append(cv2.imread(image_paths[i]))
    image[i]=cv2.resize(image[i],(0,0),fx=0.8,fy=0.8)
cv2.imshow('1',image[0])
cv2.imshow('2',image[1])

stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(image)

cv2.imshow('final result',output)

if dummy !=cv2.STITCHER_OK:
    print("atitching ain't successful")
else:
    print("Your panorama is ready!!")

cv2.waitKey(0)
