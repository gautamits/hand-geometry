#creates databse of a folder
import os
import sys
import numpy as np
import cv2
from error_remover import *
path=easygui.diropenbox("select the folder you want to create database from")
naming=[]
labels=[]
locations=[]
data=[]
try:
	os.mkdir("database")
except:
	easygui.msgbox("databse folder already existing")
k=0
for folders in os.listdir(path):
	folder=path+'/'+folders
	naming.append(folders)
	for images in os.listdir(folder):
		image=folder+'/'+images
		print image
		locations.append(image)
		labels.append(k)
		output,distances,tips,valleys=midfinger(cv2.imread(image,1))
		data.append(distances)
	k+=1
os.chdir("database")
np.save("naming",np.array(naming))
#np.savetxt("naming", np.array(naming), delimiter="\t")
np.save("labels",np.array(labels))
np.savetxt("labels", np.array(labels), delimiter=",")
np.save("locations",np.array(locations))
#np.savetxt("locations", np.array(locations), delimiter="\t")
np.save("data",np.array(data))
np.savetxt("data", np.array(data), delimiter=",")
