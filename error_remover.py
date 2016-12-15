#!/usr/bin/python
#this program takes an binary image as input and gives an image completely free from errors
import sys
import numpy as np
import cv2
import sys
import easygui
import matplotlib.pyplot as plt
import math
def getcontour(binary):
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
        return cnt
    except:
        print "no skin region found"
        return None
def fitline(img,cnt):
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.cv.CV_DIST_L2,0,0.01,0.01)
    #[vx,vy,x,y] = cv2.fitLine(cnt,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
def approximate_contour(cnt):
    #lets approximate contour
    epsilon = 0.0004*cv2.arcLength(cnt,True)
    cnt = cv2.approxPolyDP(cnt,epsilon,True)
    return cnt
def reverse(img):
    return 255-img
path = easygui.fileopenbox("choose image to work on")
img = cv2.imread(path,1)
img=cv2.resize(img,(1200,700))
drawing = np.zeros(img.shape,np.uint8) # empty image for testing purposes
#img=cv2.medianBlur(img,7)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##thresh,binary = cv2.threshold(gray,110,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
binary = cv2.inRange(gray,65,255)
#find contour
cnt=getcontour(binary)
#cnt=approximate_contour(cnt)
"""
ellipse = cv2.fitEllipse(cnt)
fitline(drawing,cnt)
center, axis_length and orientation of ellipse
center,axes,orientation = ellipse

print orientation,center,axes
cv2.ellipse(drawing,ellipse,(0,255,0),2)
"""
#draw moment of this contour


M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

#find convex hull of contour
hull = cv2.convexHull(cnt,returnPoints = False)
#print hull
corners=[]
for i in hull:
    #print cnt[i[0]][0][0]
    corners.append((cnt[i[0]][0][0],cnt[i[0]][0][1]))
for i in corners:
    cv2.circle(drawing,i,8,[0,0,255],-1)
defects = cv2.convexityDefects(cnt,hull)
#convexityDefects is array of four values [start,end,far,approximate distance to farthest point]
far_points=[]
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    far_points.append(far)
    cv2.line(drawing,start,end,[255,255,255],3)
    cv2.circle(drawing,far,7,[255,0,0],-1)
distance  =[]
tips=[]
for (i,j) in corners:
    if j < cY:
        tips.append((i,j))
for (i,j) in corners:
    distance.append(math.sqrt((cX-i)**2+(cY-j)**2))
index=distance.index(max(distance))
top=tips[index]
cv2.line(drawing,tuple(top),(cX,cY),[255,255,255],3)
#draw moment
cv2.circle(drawing, (cX, cY), 5, (0, 255, 0), -1)
#draw contour
cv2.drawContours(drawing,[cnt],0,(255,255,255),2)
cv2.imshow("contour",drawing)
cv2.waitKey(0)
