import cv2
import numpy as np
import math
import scipy
cap = cv2.VideoCapture(1)
def distance(a,b,c,d):
    return math.sqrt(((a-c)**2)+((b-d)**2))
def multidim_intersect(arr1, arr2):
    arr1_view = arr1.view([('',arr1.dtype)]*arr1.shape[1])
    arr2_view = arr2.view([('',arr2.dtype)]*arr2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return intersected.view(arr1.dtype).reshape(-1, arr1.shape[1])

ret, img = cap.read()
#cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
#crop_img = img[100:300, 100:300]
crop_img = img[:]
grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
value = (35, 35)
#grey = cv2.GaussianBlur(grey, (1,1),0)
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
    distances.append(distance(i[0],i[1],cX,cY))
#print distances
thumb=None
try:
    thumb = lower[distances.index(min(distances))]
    interesting.append(thumb)
except:
    continue

xsorted = sorted(interesting)
reverse = [(y,x) for (x,y) in interesting]
ysorted = sorted(reverse)
try:
    for i in range(1,len(xsorted)):
        if distance(xsorted[i-1][0],xsorted[i-1][1],xsorted[i][0],xsorted[i][1])<20:
            del xsorted[i]
    for i in range(1,len(ysorted)):
        if distance(ysorted[i-1][1],ysorted[i-1][0],ysorted[i][1],ysorted[i][0])<20:
            del ysorted[i]
except:
    "print multiple values not deleted"
ysorted = [(y,x) for (x,y) in ysorted]

aset = set([tuple(x) for x in xsorted])
bset = set([tuple(x) for x in ysorted])
final=np.array([x for x in aset & bset])
#for i,j in yx:
    #cv2.circle(drawing,j,5,[0,0,255],-1)
if len(final) !=10:
    continue
distances=[]
for i in final:
	distances.append(distance(i[0],i[1],cX,cY))
#print distances
try:
    yx = zip(distances,final)
    yx=sorted(yx)
except:
    continue

lower=[]
upper=[]
for i in range(5):
    lower.append(yx[i][1])
for i in range(5,10):
    upper.append(yx[i][1])
"""for i in xsorted:
    cv2.circle(drawing,i,5,[0,0,255],-1)
"""
l=[(a,b) for (a,b) in lower]
lower=np.array(sorted(l))
for i in lower:
    cv2.circle(drawing,tuple(i),5,[0,0,255],-1)
for i in range(1,len(lower)):
    cv2.circle(drawing,((lower[i-1][0]+lower[i][0])/2,(lower[i-1][1]+lower[i][1])/2),5,[0,255,0],-1)
for i in upper:
    cv2.circle(drawing,tuple(i),5,[255,0,0],-1)
all_img = np.hstack((drawing, crop_img))
all_img = np.vstack((img2,all_img))
all_img=cv2.resize(all_img,(1300,700))

#all_img=np.vstack((all_img,img))
cv2.imshow('Contours', all_img)
k = cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
