import cv2
image_path = "C:/Users/GOKUL/Downloads/car.jpg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('RGB', rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
