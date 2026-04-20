#6) Draw circle, rectangle, and line
import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")
# cv2.imshow("Original", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Draw a line
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)
# cv2.imshow("Line", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Draw a rectangle
cv2.rectangle(img, (50, 100), (450, 200), (0, 255, 0), 3)
# cv2.imshow("Rectangle", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Draw a circle)
cv2.circle(img, (250, 350), 50, (0, 0, 255), 3)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()