#!/usr/bin/python
import matplotlib.pyplot as plt
import cv2
import numpy as np
i=cv2.imread("hand.JPG")
hsv=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
lower = np.array([0,48,80],dtype="uint8")
upper = np.array([20,255,255],dtype="uint8")
mask = cv2.inRange(hsv,lower,upper)
plt.imshow(mask)
plt.show()
