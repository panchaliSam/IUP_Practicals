import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image here
img = cv2.imread("rectangle.png", 0);

# Find width and height of image
row, col = img.shape
print("Width: ", col);
print("Height: ", row);
print("Width and Height: ", img.shape);

# Create an zeros array to store the output image
img1 = np.zeros((img.shape), dtype='uint8');
print("Output image shape: ", img1.shape);
cv2.imwrite('output.jpg', img1);

# Specify the min and max range
min = 70;
max = 90;

# Loop over the input image and if pixel value lies in desired range keep it highlighted
# otherwise keep the image gray level unchanged
for i in range(row):
    for j in range(col):
        if (img[i,j] >= min and img[i,j] <= max):
            # keep gray level highlighted
            img1[i,j] = 255;
        else:
            img1[i,j] = img[i,j];

# Display the input and out images
cv2.imshow("Input Image", img);
cv2.imshow("Output Image", img1);
cv2.waitKey(0)
cv2.destroyAllWindows();

#Export the output image
cv2.imwrite('output.jpg', img1);