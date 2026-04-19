import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image here
img = cv2.imread("input.png",0);
# cv2.imshow("Input Image", img);
# cv2.waitKey(0);
# cv2.destroyAllWindows();

# Find width and height of image
row, col = img.shape;
print("Width and Height of image is: ", row, col);

# Create an zeros array to store the output image
img1 = np.zeros((img.shape), dtype="uint8");
# cv2.imshow("Output Image", img1);
# cv2.waitKey(0);
# cv2.destroyAllWindows();

# Specify the min and max range
min = 100;
max = 200;

# Loop over the input image and if pixel value lies in desired range keep it highlighted
# otherwise keep the image gray level unchanged
for i in range(row):
    for j in range(col):
        r = int(img[i, j])
        if (r >= min and r <= max):
            s = ((255 * r) - 25500) / 100   
            img1[i, j] = np.clip(s, 0, 255) 
        elif (r < min):
            img1[i, j] = 0
        else:
            img1[i, j] = 255

# Display the input and out images
cv2.imshow("Input Image", img);
cv2.imshow("Output Image", img1);
cv2.waitKey(0);
cv2.destroyAllWindows();

cv2.imwrite("output.png", img1);