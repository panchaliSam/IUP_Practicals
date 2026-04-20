#5) Resize and rotate image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sunflower.jpg")

#Resize image to 300x300
resized = cv2.resize(img, (300,300))
# cv2.imshow("Resized", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Rotate image by 90 degrees
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Change the color - OpenCV uses: BGR, Matplotlib uses: RGB
resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Resized Image")
plt.imshow(resized_rgb)
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Rotated Image")
plt.imshow(rotated_rgb)
plt.axis('off')

plt.show()
