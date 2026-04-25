#OpenCV histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read the image
img = cv2.imread("sunflower.jpg", 0)

#cv2.calcHist(images, channels, mask, histSize, ranges)
histr = cv2.calcHist(img, [0], None, [256], [0, 256])

plt.plot(histr)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()