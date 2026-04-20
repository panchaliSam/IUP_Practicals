#7) Write text on image
import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

cv2.putText(img, "Hello, OpenCV!", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()