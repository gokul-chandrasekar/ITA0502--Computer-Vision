import cv2
image_path =  "C:/Users/GOKUL/Downloads/car.jpg"
image = cv2.imread(image_path)
text = "Welcome!"
position = (50, 50)  
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_color = (255, 0, 0)  
thickness = 2
cv2.putText(image, text, position, font, font_scale, font_color, thickness)

cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
