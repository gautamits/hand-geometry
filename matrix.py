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


k=1

fig = plt.figure()
plt.axis('off')
plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
for i in filez:
    output,distances,peaks,valleys=midfinger(cv2.imread(i,1))
    #print i,"valleys=",len(valleys),"peaks=",len(peaks)
    print distances
    #if len(valleys) != 5:
        #print valleys
    #cv2.imshow(i,output).
    #output=cv2.cvtColor(output,cv2.GRAY2RGB)
    output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    a=fig.add_subplot(r,r,k)
    a.axis('off')
    #img = mpimg.imread('../_static/stinkbug.png')
    #lum_img = img[:,:,0]
    imgplot = a.imshow(output)
    title=i.split("/")
    a.set_title(title[len(title)-1])
    k+=1
    #plt.colorbar(ticks=[0.1,0.3,0.5,0.7], orientation ='horizontal')
#plt.subplots_adjust(wspace=0, hspace=0)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.show()
