#NumPy histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read the image
img = cv2.imread("sunflower.jpg", 0)

hist, bins = np.histogram(img.ravel(), 256, [0, 256])

plt.plot(hist)
plt.title("Histogram using NumPy")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()