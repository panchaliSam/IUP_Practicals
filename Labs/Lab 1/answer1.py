#1) Read and save an image
import cv2

# Read the image
img = cv2.imread(("sunflower.jpg"), -1)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")

# Display the image
cv2.imshow("Sunflower", img)
cv2.waitKey(0);
cv2.destroyAllWindows()

# Save the image
cv2.imwrite("sunflower_gray.jpg", img)