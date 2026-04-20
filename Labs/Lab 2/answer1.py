#Color Space Conversion (BGR ↔ Gray, HSV)
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sunflower.jpg")

#BGR to RGB
original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);

#BGR to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.title("Input Image")
plt.imshow(img)
plt.axis('off')

plt.subplot(1,4,2)
plt.title("RGB Image")
plt.imshow(original)
plt.axis('off')

plt.subplot(1,4,3)
plt.title("Gray Image")
plt.imshow(gray)
plt.axis('off')

plt.subplot(1,4,4)
plt.title("HSV Image")
plt.imshow(hsv)
plt.axis('off')

plt.show()