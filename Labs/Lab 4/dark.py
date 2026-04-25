import cv2
import numpy as np

# Read color image
img = cv2.imread("sunflower.jpg")

# Convert to float to avoid overflow
img_float = img.astype(np.float32)

# Reduce brightness (0.5 = darker)
dark = img_float * 0.2

# Clip values to [0,255]
dark = np.clip(dark, 0, 255).astype(np.uint8)

# Display
cv2.imshow("Original", img)
cv2.imshow("Dark Image", dark)

cv2.imwrite("DarkImage.jpg", dark)

cv2.waitKey(0)
cv2.destroyAllWindows()