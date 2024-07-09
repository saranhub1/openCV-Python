import cv2
import numpy as np

# Load an image
image = cv2.imread("C:\\Users\\saran\\Downloads\\ip 5th sem\\moonnasa.jpeg", cv2.IMREAD_GRAYSCALE)

# Ensure the image size is a multiple of 8 for DCT/IDCT
rows, cols = image.shape
if rows % 8 != 0 or cols % 8 != 0:
    new_rows = rows + 8 - (rows % 8)
    new_cols = cols + 8 - (cols % 8)
    image = cv2.resize(image, (new_cols, new_rows))

# Perform DCT
dct = cv2.dct(np.float32(image))

# Perform IDCT
idct = cv2.idct(dct)

# Convert back to uint8 and display the images
dct_uint8 = np.uint8(dct)
idct_uint8 = np.uint8(idct)

cv2.imshow('Original Image', image)
cv2.imshow('DCT Image', dct_uint8)
cv2.imshow('IDCT Image', idct_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()
