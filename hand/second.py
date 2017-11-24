import numpy as np
import cv2
import matplotlib.pyplot as plt

i = cv2.imread("testing.jpg" , 0) 
im_bw = cv2.threshold( i , 128, 255 , cv2.THRESH_BINARY | cv2.THRESH_OTSU )[1]
plt.imshow(im_bw)
plt.show()
thresh = cv2.threshold( im_bw , 128 , 255 , 0 )[1]
contours = cv2.findContours ( thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
k = cv2.findContours ( thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE )
cv2.drawContours( im_bw , contours[2] , -1 , ( 0 , 255 , 0 ) , 3 )
plt.imshow(im_bw)
plt.show()