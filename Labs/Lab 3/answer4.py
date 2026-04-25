import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("sunflower.jpg", 0)

# Create mask (black image)
mask = np.zeros(img.shape, dtype=np.uint8)
print("Height:", img.shape[0])
print("Width:", img.shape[1])

# Correct rectangle (matches lab figure)
mask[100:500, 600:1000] = 255
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply mask
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Compute histograms
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

# Display results
plt.figure(figsize=(10, 8))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(222)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.axis('off')

plt.subplot(223)
plt.imshow(masked_img, cmap='gray')
plt.title("Masked Image")
plt.axis('off')

plt.subplot(224)
plt.plot(hist_full, label='Full Image')
plt.plot(hist_mask, label='Masked Image')
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.legend()

plt.tight_layout()
plt.show()