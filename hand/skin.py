import sys
import numpy as np
import cv2
converted=cv2.imread(sys.argv[1],1)
min_YCrCb = np.array([0,0,0],np.uint8) # Create a lower bound HSV
max_YCrCb = np.array([179,255,255],np.uint8) # Create an upper bound HSV

hsv = cv2.cvtColor(converted, cv2.COLOR_BGR2HSV) # assuming converted is your original stream...

skinRegion = cv2.inRange(hsv,min_YCrCb,max_YCrCb) # Create a mask with boundaries
contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find the contour on the skin detection
for i, c in enumerate(contours): # Draw the contour on the source frame
	area = cv2.contourArea(c)
	if area > 10000:
		cv2.drawContours(converted, contours, i, (255, 255, 0), 2) 
cv2.imshow("contour",converted);
cv2.waitKey(0)