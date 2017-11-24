import os
from Tkinter import *
import cv2
#import Image, ImageTk
import PIL
from PIL import Image, ImageTk
import numpy as np
import easygui
import sys
from error_remover import *
from shutil import copyfile
index=0
files="data.jpg"
def accept():
    global index
    global saved
    #f=files[index].split("/")
    #name=f[len(f)-1]
    #copyfile(files[index],"/home/amit/"+saved+"/"+name)
    #index+=1
    tk.title(files[index])
    print index,files[index]
    output,distances,tips,valleys = midfinger(cv2.resize(cv2.imread(files[index],1),(1200,700)))
    output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    im = PIL.Image.fromarray(output)
    imgtk = PIL.ImageTk.PhotoImage(image=im)
    l1.configure(image = imgtk)
    l1.image=imgtk
    #panel.image = img2
    print "accepted"
    f=open("distances","r+w")
    f.write(str(distances))
    f.close()
def deny():
    global index
    #index+=1
    tk.title(files[index])
    print index,files[index]
    output,distances,tips,valleys = midfinger(cv2.resize(cv2.imread(files[index],1),(1200,700)))
    output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    im = PIL.Image.fromarray(output)
    imgtk = PIL.ImageTk.PhotoImage(image=im)
    l1.configure(image = imgtk)
    l1.image=imgtk
    print "denied"
    exit()


tk=Tk()
page1 = Frame(tk,bg="blue",width=1200,height=100)
ok = Button(page1,command=accept,text="ok")
cancel = Button(page1,command=deny,text="cancel")
ok.pack(side=LEFT,expand=1,fill=BOTH)
cancel.pack(side=RIGHT,expand=1,fill=BOTH)
page3 = Frame(tk,bg="blue",width=1200,height=700)
tk.title(files[index])
img=cv2.imread(files[index],1)
img=cv2.resize(img,(1200,700))
output,distances,tips,valleys=midfinger(img)
output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
im = PIL.Image.fromarray(output)
imgtk = PIL.ImageTk.PhotoImage(image=im)
l1=Label(page3, image=imgtk)
l1.pack()
page1.pack(expand=1,fill=BOTH)
page3.pack(side = "bottom", fill = "both", expand = "yes")
tk.mainloop()

#cv2.imwrite("testing.jpg",cv2.inRange(img,lower,upper))
