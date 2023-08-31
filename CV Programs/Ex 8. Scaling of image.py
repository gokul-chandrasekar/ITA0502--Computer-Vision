import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:/Users/GOKUL/Downloads/fall-autumn-red-season.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(400,500))
cv2.imshow("image",img)
cv2.waitKey(0)

    
