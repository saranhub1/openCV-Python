import numpy as np
import cv2

# Read the input image in grayscale mode
img = cv2.imread("C:\\Users\\saran\\Downloads\\400x400-vector-36412455.jpg", cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the image
row, col = img.shape

# Function to convert pixel values to binary arrays
def intToBitArray(img):
    bit_list = []
    for i in range(row):
        for j in range(col):
            bit_list.append(np.binary_repr(img[i][j], width=8))
    return bit_list

# Convert the binary data to a 2D array
imgIn1D = intToBitArray(img)
imgIn2D = np.reshape(imgIn1D, (row, col))

# Function to extract a specific bit plane
def bitplane(bitImgVal, img1D):
    bit_list = [int(i[bitImgVal]) for i in img1D]
    return bit_list

# Create 8-bit and 7-bit planes
eightbitimg = np.array(bitplane(0, imgIn1D)) * 128
sevenbitimg = np.array(bitplane(1, imgIn1D)) * 64

# Combine bit planes
combine = eightbitimg + sevenbitimg

# Reshape the combined image to the original dimensions
comb = np.reshape(combine, (row, col))

# Save the combined image
cv2.imwrite("comb.jpeg", comb)
print("Combined image saved as 'comb.jpeg'.")

# Reshape the 8-bit and 7-bit planes to the original dimensions
eightbitimg = np.reshape(eightbitimg, (row, col))
sevenbitimg = np.reshape(sevenbitimg, (row, col))

# Save the individual bit planes
cv2.imwrite("8bitvalue.jpg", eightbitimg)
cv2.imwrite("7bitvalue.jpg", sevenbitimg)
print("8-bit and 7-bit planes saved as '8bitvalue.jpg' and '7bitvalue.jpg'.")

# Read another grayscale image (you should provide the correct path)
gray = cv2.imread("C:\\Users\\saran\\Downloads\\400x400-vector-36412455.jpg", cv2.IMREAD_GRAYSCALE)

# Save and display the grayscale image
cv2.imwrite("gray.jpeg", gray)
cv2.imshow("gray.jpeg", gray)
print("Grayscale image saved as 'gray.jpeg'. Press any key to close the window.")

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
