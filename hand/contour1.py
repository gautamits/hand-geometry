import numpy as np
import cv2
import matplotlib.pyplot as plt
im=cv2.imread("testing.jpg",0)
contours, hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
for i in contours:
	print i
cnt = contours[0]
cv2.drawContours(im,contours,0,(0,255,0),3)
plt.imshow(im)
plt.show()

