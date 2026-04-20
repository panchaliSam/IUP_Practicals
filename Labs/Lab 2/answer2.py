#Object Tracking (Extract Blue Object from Video)
import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture("small_laptop_connections.mov")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for BLUE color
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Threshold the HSV image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Extract the blue object
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display outputs
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Extracted Object", result)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()