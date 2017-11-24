import os
import easygui
import cv2
from error_remover import midfinger
path=easygui.diropenbox("select the folder you want to choose images from")
files=os.listdir(path)
files=sorted(files)
files=[path+'/'+i for i in files]
for i in files:
    output,distances,tips,valleys=midfinger(cv2.imread(i,1))
    if len(valleys)!=5 or len(tips) != 5:
        print i,len(valleys),len(tips)
        os.remove(i)
