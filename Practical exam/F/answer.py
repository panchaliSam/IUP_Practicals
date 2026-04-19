# #Gamma correction for dark image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("original.jpg", 0)

if img is None:
    print("Error: image not found")
    exit()

gamma = 0.3
img1 = np.array(255 * (img / 255) ** gamma, dtype='uint8')

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Input Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Output Image")
plt.imshow(img1, cmap='gray')
plt.axis('off')

plt.show()

#Logarithmic transformation for dark image
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread("original.jpg", 0)

# if img is None:
#     print("Error: image not found")
#     exit()

# # Convert to float for precision
# img_float = img.astype(np.float32)

# # Apply log transformation
# c = 255 / np.log(1 + np.max(img_float))
# img1 = c * np.log(1 + img_float)

# # Convert back to uint8
# img1 = np.array(img1, dtype=np.uint8)

# plt.figure(figsize=(10,4))

# plt.subplot(1,2,1)
# plt.title("Input Image")
# plt.imshow(img, cmap='gray')
# plt.axis('off')

# plt.subplot(1,2,2)
# plt.title("Log Transformed Image")
# plt.imshow(img1, cmap='gray')
# plt.axis('off')

# plt.show()