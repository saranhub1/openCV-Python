import cv2
import numpy as np

# Function to generate the DCT matrix for a given size
def generate_dct_matrix(size):
    DCT_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i == 0:
                alpha_i = 1 / np.sqrt(size)
            else:
                alpha_i = np.sqrt(2) / np.sqrt(size)
            if j == 0:
                alpha_j = 1 / np.sqrt(size)
            else:
                alpha_j = np.sqrt(2) / np.sqrt(size)
            DCT_matrix[i, j] = alpha_i * alpha_j * np.cos(((2 * i + 1) * j * np.pi) / (2 * size))
    return DCT_matrix

# Load an image (replace 'input_image.jpg' with your image file)
image = cv2.imread("C:\\Users\\saran\\Downloads\\20230826_182947.jpg", cv2.IMREAD_GRAYSCALE)

# Convert the image to float32
image = np.float32(image)

# Apply 2D DCT
dct_image = cv2.dct(image)

# Specify the size of the DCT matrix (e.g., 4x4)
size = 4

# Generate and print the DCT matrix
DCT_matrix = generate_dct_matrix(size)
print("DCT Matrix ({}x{}):".format(size, size))
print(DCT_matrix)

# You can also normalize the DCT coefficients if desired
# dct_image /= np.max(np.abs(dct_image))

# Display the DCT image (optional)
cv2.imshow('DCT Image', dct_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the DCT coefficients to a file (optional)
np.save('dct_coefficients.npy', dct_image)
