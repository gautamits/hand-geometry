import easygui
import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *
import Tkinter,tkFileDialog
from error_remover import *
import math

root = Tkinter.Tk()
filez = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
root.destroy()
n=len(filez)
r=math.sqrt(n)
if r!=int(r):
    r=int(r+1)
else:
    r=int(r)
k=0
sample=np.zeros((1200,720),np.uint8)
h=[]
for i in range(r):
    j=0
    temp=[]
    for j in range(r):
        output,distances,tips,valleys=midfinger(cv2.resize(cv2.imread(filez[k],1),(1200,720)))
        temp.append(output)
    horizontal=temp[0]
    for l in xrange(1,len(temp)):
        horizontal=np.hstack((horizontal,temp[l]))
    h.append(horizontal)
    k+=1

output=h[0]
for i in xrange(1,len(h)):
    output=np.vstack((output,h[i]))
output=cv2.resize(output,(1200,720))
cv2.imshow("output",output)
cv2.waitKey(0)
