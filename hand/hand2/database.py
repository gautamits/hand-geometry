import os
import cv2
import sys
import numpy as np
name=raw_input("enter name of person\n")
try:
    os.rmdir(name)
except:
    print "folder deleted"
os.mkdir(name)
os.chdir(name)
cap=cv2.VideoCapture(0)
i=1
while(cap.isOpened()):
    ret,img=cap.read()
    cv2.imshow(name,img)
    k=cv2.waitKey(5) & 0xFF
    print k
    if k==32:
        cv2.imwrite(name+"_"+str(i)+".jpg",img)
        i+=1
    elif k==27:
        cap.release()
        cv2.destroyAllWindows()
        os.chdir("..")
        break
