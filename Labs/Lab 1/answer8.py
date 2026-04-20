#8) Convert color image to grayscale, binary, and negative
import cv2

img = cv2.imread("sunflower.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary using threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Negative image
negative = 255 - img

cv2.imshow("Original Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow("Gray Image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow("Binary Image", binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow("Negative Image", negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
