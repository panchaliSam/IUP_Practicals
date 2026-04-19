# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the image here
# img = cv2.imread("cameraman.jpg", 0);
# # cv2.imshow("Input Image", img);
# # cv2.waitKey(0);
# # cv2.destroyAllWindows();

# # create the kernal
# kernel = np.ones((5, 5), np.float32) / 25;

# # smooth the image
# smooth = cv2.filter2D(img, -1, kernel);
# cv2.imshow("Smoothed Image", smooth);
# cv2.waitKey(0);
# cv2.destroyAllWindows();

# # subtract the smoothed image from the original image
# mask = cv2.subtract(img, smooth);
# output = cv2.add(img, mask);

# # Display the input and output images
# plt.figure(figsize=(12,4))

# plt.subplot(1,3,1)
# plt.title("Input Image")
# plt.imshow(img, cmap='gray')
# plt.axis('off')

# plt.subplot(1,3,2)
# plt.title("Smoothed Image")
# plt.imshow(smooth, cmap='gray')
# plt.axis('off')

# plt.subplot(1,3,3)
# plt.title("Unsharp Masking Output")
# plt.imshow(output, cmap='gray')
# plt.axis('off')

# plt.show()

# cv2.waitKey(0)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image here
img = cv2.imread("cameraman.jpg", 0);

# create the kernal
kernel = np.ones((5,5), np.float32) / 25

# smooth the image
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