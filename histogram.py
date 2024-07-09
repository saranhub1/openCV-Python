import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load an image using PIL (Python Imaging Library)
image_path = "C:\\Users\saran\\Downloads\\moon300.jpg"
image = Image.open(image_path)

# Convert the image to grayscale (if it's a color image)
gray_image = image.convert("L")

# Convert the grayscale image to a NumPy array
image_array = np.array(gray_image)

# Calculate the histogram
histogram, bin_edges = np.histogram(image_array, bins=256, range=(0, 255))

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.title("Moon Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.bar(bin_edges[:-1], histogram, width=1)
plt.show()
