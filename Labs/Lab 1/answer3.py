#3) Access image properties
import cv2

img = cv2.imread("sunflower.jpg")

print("Image shape:", img.shape) # (height, width, channels)
print("Image size:", img.size) # total number of pixels
print("Image data type:", img.dtype) # data type of pixel values