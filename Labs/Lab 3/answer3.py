# BGR histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sunflower.jpg", 1)
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.title("BGR Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()