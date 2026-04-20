#To split and merge channels
# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread("sunflower.jpg")

# # Split the image into its color channels
# b, g, r = cv2.split(img)

# cv2.imshow("Blue Channel", b)
# cv2.imshow("Green Channel", g)
# cv2.imshow("Red Channel", r)

# plt.figure(figsize=(10, 5))

# plt.subplot(1, 3, 1)
# plt.imshow(b, cmap='gray')
# plt.title("Blue Channel")
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(g, cmap='gray')
# plt.title("Green Channel")
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(r, cmap='gray')
# plt.title("Red Channel")
# plt.axis('off')

# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

img = cv2.imread("sunflower.jpg")

# Split into Blue, Green, Red channels
b, g, r = cv2.split(img)

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

# Merge back
merged = cv2.merge((b, g, r))
cv2.imshow("Merged Image", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()