#!/usr/bin/python
#this program takes an binary image as input and gives an image completely free from errors
import sys
import numpy as np
import cv2
import sys
import easygui
import matplotlib.pyplot as plt

path = easygui.fileopenbox("choose image to work on")
img = cv2.imread(path,1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh,binary = cv2.threshold(gray,110,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#binary=255-binary
#find contour
version = cv2.__version__.split('.')[0]

if version is '3':
    image, contours, hierarchy = cv2.findContours(binary.copy(), \
           cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
elif version is '2':
    contours, hierarchy = cv2.findContours(binary.copy(),cv2.RETR_TREE, \
           cv2.CHAIN_APPROX_NONE)

try:
    #find contour with maximum area
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
except:
    print "no skin region found"
#draw moment of this contour
drawing = np.zeros(img.shape,np.uint8)
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

#find convex hull of contour
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
#convexityDefects is array of four values [start,end,far,approximate distance to farthest point]
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(drawing,start,end,[255,255,255],3)
    cv2.circle(drawing,far,7,[255,0,0],-1)

#draw moment
cv2.circle(drawing, (cX, cY), 5, (0, 255, 0), -1)
#draw contour
cv2.drawContours(drawing,[cnt],0,(255,255,255),2)
cv2.imshow("contour",drawing)
cv2.waitKey(0)
