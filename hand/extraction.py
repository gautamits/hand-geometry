#!/usr/bin/python2
import sys
import  cv2
import  numpy as np
import easygui
import Tkinter as tk
import matplotlib.pyplot as plt

img = cv2.imread("testing.jpg",0)
#ret,thresh = cv2.threshold(img,127,255,0)
(ret,thresh) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)
print M
cv2.drawContours(img,contours,-1,(0,255,0),1)
cv2.imshow("result",img)
cv2.waitKey(0)
#plt.imshow(thresh)
#plt.show()
