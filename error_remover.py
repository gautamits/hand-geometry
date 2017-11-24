#!/usr/bin/python
#this program takes an binary image as input and gives an image completely free from errors
from __future__ import division
import sys
import numpy as np
import cv2
import sys
import easygui
import matplotlib.pyplot as plt
import math
colors=[[ 0 , 43 , 54 ] , [ 7 , 54 , 66 ] , [ 88 , 110 , 117 ] , [ 101 , 123 , 131 ] , [ 131 , 148 , 150 ] , [ 147 , 161 , 161 ] , [ 238 , 232 , 213 ] , [ 253 , 246 , 227 ] , [ 181 , 137 , 0 ] , [ 203 , 75 , 22 ] , [ 220 , 50 , 47 ] , [ 211 , 54 , 130 ] , [ 108 , 113 , 196 ] , [ 38 , 139 , 210 ] , [ 42 , 161 , 152 ] , [ 133 , 153 , 0 ] ]
def drawline(img,pt1,pt2,color,thickness=1,style='dotted',gap=20):
    dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
    pts= []
    for i in  np.arange(0,dist,gap):
        r=i/dist
        x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
        y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
        p = (x,y)
        pts.append(p)

    if style=='dotted':
        for p in pts:
            cv2.circle(img,p,thickness,color,-1)
    else:
        s=pts[0]
        e=pts[0]
        i=0
        for p in pts:
            s=e
            e=p
            if i%2==1:
                cv2.line(img,s,e,color,thickness)
            i+=1

def midpoint(a,b):
    return tuple(map(int,((a[0]+b[0])/2,(a[1]+b[1])/2)))
def distance2(a,b):
    dist = math.hypot(b[0] - a[0], b[1] - a[1])
    return dist
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return map(int,(x,y))
    else:
        return False
def plot_distances(tips,valleys,drawing,cX):
    tips=sorted(tips)
    valleys=sorted(valleys)
    thumb_point=tips[0]
    base=(cX,drawing.shape[0])
    valley1=valleys[1]
    valley0=valleys[0]
    #cv2.line(drawing,valley1,valley0,[255,255,255],3)
    knuckles=[]
    dist=[]
    line1=line(thumb_point,base)
    line2=line(valley1,valley0)
    thumb_base=intersection(line1,line2)
    knuckles.append(tuple(thumb_base))
    #cv2.line(drawing,thumb_point,tuple(thumb_base),[255,255,255],3)
    #print thumb_base
    #cv2.circle(drawing,tuple(thumb_base),7,[255,0,0],-1)
    #knuckles=[]
    for i in xrange(1,len(valleys)):
        knuckles.append(midpoint(valleys[i],valleys[i-1]))
    #print knuckles
    for i in knuckles:
        cv2.circle(drawing,i,7,[255,0,0],-1)
    for i,j in zip(tips,knuckles):
        drawline(drawing,i,j,[255,0,0],3)
        dist.append(distance2(i,j))
    #sixth distance
    try:
        drawline(drawing,knuckles[0],knuckles[1],[255,0,0],3)
        dist.append(distance2(knuckles[0],knuckles[1]))
    except:
        print "all knuckles not detected"
        return drawing,dist
    #seventh distance
    try:
        drawline(drawing,knuckles[1],knuckles[4],[255,0,0],3)
        dist.append(distance2(knuckles[1],knuckles[4]))
    except:
        print "all knuckles not detected"
        return drawing,dist
    #print dist
    return (drawing,dist)


def cluster(xaxis):
    #print xaxis
    result=[]
    temp=[]
    temp.append(xaxis[0])
    d=50
    for i in xrange(1,len(xaxis)):
        if xaxis[i]-xaxis[i-1] < d:
            temp.append(xaxis[i])
        else:
            result.append(temp)
            temp=[]
            temp.append(xaxis[i])
    result.append(temp)
    return result
def unique(arr):
    arr=sorted(arr)
    #print arr
    xaxis=[i for (i,j) in arr]
    result=cluster(xaxis)
    #print result
    mapx = {}
    for (i,j) in arr:
        mapx[i] = j
    mapy={}
    for (i,j) in arr:
        mapy[j]=i
    for i in xrange(0,len(result)):
        for j in xrange(0,len(result[i])):
            result[i][j]=mapx[result[i][j]]
    minimum=[]
    for i in result:
        minimum.append(min(i))
    #print minimum
    ret=[]
    for i in minimum:
        ret.append((mapy[i],i))
    return ret
def distance(a,b):
    if len(a)!=(len(b)):
        print "a and b are not equal size"
    total=0
    for i in xrange(len(a)):
        total+=(a[i][0]-b[i][0])**2+(a[i][1]-b[i][1])**2
    return math.sqrt(total)
def get_tips(cnt,hull,average):
    corners=[]
    tips=[]
    for i in hull:
        #print cnt[i[0]][0][0]
        corners.append((cnt[i[0]][0][0],cnt[i[0]][0][1]))
    for (i,j) in corners:
        if j < average:
            tips.append((i,j))
    arr=[j for (i,j) in tips]
    average2=sum(arr)/len(arr)
    average=(average+average2)/2
    tips=[]
    for (i,j) in corners:
        if j < average:
            tips.append((i,j))
    corners=sorted(corners)
    tips.append(corners[0])
    tips=sorted(tips)
    tips=unique(tips)
    return tips

def reference(binary,y):
    j=0
    temp=[]
    s1,s2=binary.shape[:2]
    for i in xrange(s1):
        if binary[i][y]==255:
            temp.append(i)
    return max(temp)
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
def get_valleys(cnt,hull,cX,cY):
    defects = cv2.convexityDefects(cnt,hull)
    #convexityDefects is array of four values [start,end,far,approximate distance to farthest point]
    far_points=[]
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        far_points.append(far)
        #cv2.line(drawing,start,end,[255,255,255],3)
    #obtain four valleys
    # far_points contains all convexity defects
    #return far_points
    centroid=[(cX,cY) for i in xrange(len(far_points))]
    dist=[]
    for i in far_points:
        dist.append(distance([i],[(cX,cY)]))
    z=zip(dist,far_points)
    z=sorted(z)
    z=z[:5]
    valleys=[]
    for i,j in z:
        valleys.append(j)
    return valleys

def fitline(img,cnt):
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.cv.CV_DIST_L2,0,0.01,0.01)
    #[vx,vy,x,y] = cv2.fitLine(cnt,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
def approximate_contour(cnt):
    #lets approximate contour
    epsilon = 0.0005*cv2.arcLength(cnt,True)
    cnt = cv2.approxPolyDP(cnt,epsilon,True)
    return cnt
def reverse(img):
    return 255-img
def midfinger(img):
    img=cv2.resize(img,(1200,700))
    drawing = np.zeros(img.shape,np.uint8) # empty image for testing purposes
    drawing[np.where((drawing==[0,0,0]).all(axis=2))] = [colors[15]]
    #drawing = reverse(drawing)
    #img=cv2.medianBlur(img,7)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #return (gray,None,None,None)
    ##thresh,binary = cv2.threshold(gray,110,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    binary = cv2.inRange(gray,65,255)
    #find contour
    cnt=getcontour(binary)
    cnt=approximate_contour(cnt)
    #draw moment of this contour
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    #xr=reference(binary,cY)
    #cv2.circle(drawing,(xr,cY),7,(255,0,0),-1)
    #draw contour
    cv2.drawContours(drawing,[cnt],0,(255,255,255),2)
    cv2.circle(drawing,(cX,cY),7,(0,255,0),-1)

    hull = cv2.convexHull(cnt,returnPoints = False)
    valleys=get_valleys(cnt,hull,cX,cY)
    for (i,j) in valleys:
        cv2.circle(drawing,(i,j),15,[0,0,255],-1)
    arr=[]

    for (i,j) in valleys:
        arr.append(j)
    average=sum(arr)/len(arr)
    tips=get_tips(cnt,hull,average)
    for (i,j) in tips:
        cv2.circle(drawing,(i,j),7,[0,255,0],-1)


    drawing,distances=plot_distances(tips,valleys,drawing,cX)
    fore_finger=distances[1]
    distances=[i/fore_finger for i in distances]
    return (drawing,distances,tips,valleys)
