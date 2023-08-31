import cv2
import numpy as np
image_path = "C:/Users/GOKUL/Downloads/istockphoto-1368965646-612x612.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corner_image = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
corner_image = cv2.dilate(corner_image, None)
threshold = 0.01 * corner_image.max()
corner_coordinates = np.where(corner_image > threshold)
for y, x in zip(*corner_coordinates):
    cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  
cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
e
