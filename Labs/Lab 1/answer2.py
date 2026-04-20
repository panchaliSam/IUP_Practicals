#2) Access pixel values and modify them
import cv2

img = cv2.imread("sunflower.jpg")

# Access pixel value at (100, 100)
pixel = img[100, 100]
print("Pixel value at (100, 100):", pixel)

img[100, 100] = [0, 0, 255] # Change the pixel to green

# Display modified image
cv2.imshow("Modified Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()