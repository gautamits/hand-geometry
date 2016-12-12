#!/usr/bin/python
#will take corrected binary image and rotate it
import sys
import numpy as np
import cv2
import sys
import easygui
import matplotlib.pyplot as plt

path = easygui.fileopenbox("choose image to work on")
img = cv2.imread(path,1)
img=cv2.resize(img,(1200,700))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# apply 3x3 media filter on image
medianFiltered = cv2.medianBlur(gray,3)

#apply binary threshold

#otsu's method
thresh,binary = cv2.threshold(medianFiltered,110,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print thresh
#normal thresholding
thresh=90
#binary = cv2.threshold(medianFiltered, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("gray image",binary)
cv2.waitKey(0)
