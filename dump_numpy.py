import os
import sys
import numpy as np
import cv2
import easygui
path=easygui.fileopenbox("select the folder you want to create database from")
a=np.load(path)
print a
