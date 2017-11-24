from matcher import *
import os
import sys
import numpy as np
import cv2

def check(path,limit):
    total=0
    success=0
    folders=os.listdir(path)
    folderz=[path+"/"+i for i in folders]
    for i in folderz:
        images=os.listdir(i)
        images=[i+"/"+j for j in images]
        for j in images:
            #print j,
            person=j.split("/")[5]
            #print person
            if match(j,limit)==person:
                success+=1
            total+=1
    #print success," matched out of ",total,success*100/float(total),"%"
    return success*100/float(total)
path=easygui.diropenbox("select the folder you want to check your result on")
for i in range(2,11):
    print i,check(path,i)
#print check(path,5)
