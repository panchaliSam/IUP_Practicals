import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("DarkImage.jpg", 0)

if img is None:
    print("Error: image not found")
    exit()

# Calculate histogram of original image
hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])

# Apply Histogram Equalization
equalizedImg = cv2.equalizeHist(img)

# Histogram of equalized image
hist2 = cv2.calcHist([equalizedImg], [0], None, [256], [0, 256])

# Display images side by side
result = np.hstack((img, equalizedImg))

cv2.imshow("Original vs Equalized", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histograms
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])
plt.plot(hist1)

plt.subplot(1, 2, 2)
plt.title("Equalized Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])
plt.plot(hist2)

plt.tight_layout()
plt.show()