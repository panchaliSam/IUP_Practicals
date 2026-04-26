#Negative transformation for color images
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Complete the code
img = cv2.imread("apples.jpg", 1)

img_neg = 255 - img

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_neg_rgb = cv2.cvtColor(img_neg, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_neg_rgb)
plt.title("Negative Image")
plt.axis('off')

plt.show()