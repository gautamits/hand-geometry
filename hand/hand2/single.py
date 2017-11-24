import cv2
import numpy as np
import math
import scipy
import easygui
import sys
cap = cv2.VideoCapture(0)
def distance((a,b),c,d):
    return math.sqrt(((a-c)**2)+((b-d)**2))
def multidim_intersect(arr1, arr2):
    arr1_view = arr1.view([('',arr1.dtype)]*arr1.shape[1])
    arr2_view = arr2.view([('',arr2.dtype)]*arr2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return intersected.view(arr1.dtype).reshape(-1, arr1.shape[1])

img = cv2.imread(easygui.fileopenbox(),1)
crop_img = img[:]
grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
value = (35, 35)
#blurred = cv2.GaussianBlur(grey, value, 0)
#_, thresh1 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
_, thresh1 = cv2.threshold(grey, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#threshold image is binary image on which we are going to perform some operations
threshold = cv2.cvtColor(thresh1,cv2.COLOR_GRAY2RGB)
#cv2.imshow('Thresholded', thresh1)
#print img.shape
#print threshold.shape
#original image and threshold value
img2 = np.hstack((img,threshold))

version = cv2.__version__.split('.')[0]

if version is '3':
    image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
           cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
elif version is '2':
    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
           cv2.CHAIN_APPROX_NONE)

try:
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
except:
    print "no skin region found"
#find bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)
#crop the rectangle which contains the hand
#cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
#find out convex hull
hull = cv2.convexHull(cnt)
#create an empty array and draw hull and contour in it
drawing = np.zeros(crop_img.shape,np.uint8)
cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
#cv2.drawContours(drawing,[hull],0,(0,0,255),0)

########################################### time to derive moment and draw it
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
# draw the contour and center of the shape on the image
#cv2.drawContours(imag, [c], -1, (0, 255, 0), 2)
cv2.circle(crop_img, (cX, cY), 7, (255, 255, 255), -1)
cv2.line(crop_img,(0,cY),(crop_img.shape[1],cY),(255,255,255),2)

hull = cv2.convexHull(cnt,returnPoints = False)
#find out convexity defects
defects = cv2.convexityDefects(cnt,hull)
count_defects = 0
#draw contours in threshold1
#cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
interesting=[]
lower=[]
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
    """if angle <= 90:
        count_defects += 1
        cv2.circle(crop_img,far,4,[0,0,255],-1)
    """
    dist = cv2.pointPolygonTest(cnt,far,True)
    cv2.line(crop_img,start,end,[0,255,0],2)
    cv2.circle(crop_img,far,5,[0,0,255],-1)
    if far[1] < cY:
        interesting.append(far)
    else:
        lower.append(far)
distances = []
for i in lower:
    distances.append(distance(i,cX,cY))
#print distances
thumb=None
try:
    thumb = lower[distances.index(min(distances))]
except:
    print "thumb not found"
"""
if count_defects == 1:
    cv2.putText(img,"I am Vipul", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
elif count_defects == 2:
    str = "This is a basic hand gesture recognizer"
    cv2.putText(img, str, (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
elif count_defects == 3:
    cv2.putText(img,"This is 4 :P", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
elif count_defects == 4:
    cv2.putText(img,"Hi!!!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
else:
    cv2.putText(img,"Hello World!!!", (50,50),\
                cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
"""
#cv2.imshow('drawing', drawing)
#cv2.imshow('end', crop_img)
#cv2.imshow('Gesture', img)
#for i in interesting:
    #cv2.circle(drawing,i,5,[0,0,255],-1)
#cv2.circle(drawing,thumb,5,[0,0,255],-1)
all_img = np.hstack((drawing, crop_img))
all_img = np.vstack((img2,all_img))
all_img=cv2.resize(all_img,(1300,700))

#all_img=np.vstack((all_img,img))
cv2.imshow('Contours', all_img)
k = cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
