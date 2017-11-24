import os
import sys
import numpy as np
import cv2
import easygui
from error_remover import *
naming=np.load("database/naming.npy")
database=np.load("database/data.npy")
locations=np.load("database/locations.npy")
labels=np.load("database/labels.npy")
def dist(x,y):
    x=np.array(x)
    y=np.array(y)
    #print len(x),len(y)
    return np.sqrt(np.sum((x-y)**2))
def match(path,limit):
    #print person
    img=cv2.imread(path,1)
    output,distances,tips,valleys=midfinger(img)
    d=[]

    for i in database:
        d.append(dist(distances,i))
    temp=np.copy(labels)
    d,temp=zip(*sorted(zip(d,temp)))

    temp=temp[1:limit]
    for i in temp:
        print naming[i]
    label=np.bincount(temp).argmax()
    return naming[label]

if __name__=='__main__':
    #name=raw_input("enter your name")
    name=easygui.enterbox("what is your name")
    path=easygui.fileopenbox("open the image you want to check on")
    if name==match(path,5):
        print "matched"
        easygui.msgbox("matched")
    else:
        print "not matched"
        easygui.msgbox("not matched")
