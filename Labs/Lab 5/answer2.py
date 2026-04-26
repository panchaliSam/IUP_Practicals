#Power-law transformation to improve the contrast of a dark image
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read gray scale image
img_gray = cv2.imread("gamma.jpg", 0)

img_norm = img_gray / 255.0
gamma = 0.5

img_gamma = np.power(img_norm, gamma)

#Scale back to [0, 255] range
img_gamma = np.uint8(img_gamma*255)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap="gray")
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_gamma, cmap="gray")
plt.title("Gamma Corrected Image")
plt.axis('off')

plt.show()