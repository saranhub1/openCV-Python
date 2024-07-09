import numpy as np
import cv2  # OpenCV for loading and displaying images

# Load the input image
input_image = cv2.imread("C:\\Users\\saran\\Downloads\\ip 5th sem\\lowpass img.png", cv2.IMREAD_GRAYSCALE)

# Create a copy of the input image
filtered_image = input_image.copy()

# Define the Laplacian kernel
h = np.array([[1, 1, 1],
              [1, -8, 1],
              [1, 1, 1]])

# Get the dimensions of the image
height, width = input_image.shape

# Iterate through each pixel (excluding border pixels)
for m in range(1, height - 1):
    for n in range(1, width - 1):
        # Apply convolution with the Laplacian kernel
        convolution_result = np.sum(input_image[m-1:m+2, n-1:n+2] * h)
        filtered_image[m, n] = convolution_result

# Display the filtered image
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
