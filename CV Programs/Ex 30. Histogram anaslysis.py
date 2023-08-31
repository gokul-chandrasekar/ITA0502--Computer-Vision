import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C:/Users/GOKUL/Downloads/istockphoto-1368965646-612x612.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title('Histogram')                                                                                                                                                    
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

equalized_image = cv2.equalizeHist(image)
equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

plt.plot(equalized_hist)
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
