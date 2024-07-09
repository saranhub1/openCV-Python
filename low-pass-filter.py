import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
input_image = cv2.imread("C:\\Users\\saran\\Downloads\\ip 5th sem\\lowpass img.png", cv2.IMREAD_GRAYSCALE)

# Define different kernel sizes (3x3, 5x5, and 7x7)
kernel_sizes = [3, 5, 7]

# Apply low-pass filtering with different kernel sizes
filtered_images = []
for size in kernel_sizes:
    kernel = cv2.getGaussianKernel(size, 0)
    filtered_image = cv2.filter2D(input_image, -1, kernel)
    filtered_images.append(filtered_image)

# Plot the original and filtered images
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')

for i, size in enumerate(kernel_sizes):
    plt.subplot(1, 4, i + 2)
    plt.imshow(filtered_images[i], cmap='gray')
    plt.title(f'{size}x{size} Filtered')

plt.tight_layout()
plt.show()
