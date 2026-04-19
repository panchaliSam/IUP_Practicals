import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image here
img = cv2.imread("lady.png", 0);

# create the kernal
kernel = np.ones((5,5), np.float32) / 25

# smooth the imag
smooth = cv2.filter2D(img, -1, kernel)

# subtract the smoothed image from the original image
output = cv2.subtract(img, smooth)

# Display the input and output images
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Input Image (A)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Output Image (B)")
plt.imshow(smooth, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Output Image (C)")
plt.imshow(output, cmap='gray')
plt.axis('off')

plt.show()

cv2.waitKey(0)