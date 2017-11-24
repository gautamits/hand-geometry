from Tkinter import *
import cv2
#import Image, ImageTk
import PIL
from PIL import Image, ImageTk
import numpy as np
from ldgp import calcgrad
import easygui
import sys
lower=np.array([0,0,0],dtype="uint8")
upper=np.array([0,0,0],dtype="uint8")
def print_value(val):
	#print val
	#lower=np.array([lr.get(),lg.get(),lb.get()],dtype="uint8")
	#upper=np.array([hr.get(),hg.get(),hb.get()],dtype="uint8")
	lower[0]=lr.get()
	lower[1]=lg.get()
	lower[2]=lb.get()
	upper[0]=hr.get()
	upper[1]=hg.get()
	upper[2]=hb.get()
	#print lower,upper
	mask = cv2.inRange(img,lower,upper)
	#grad=calcgrad(mask)
	#grad=grad*4
	im = PIL.Image.fromarray(mask)
	imgtk = PIL.ImageTk.PhotoImage(image=im)
	l1.configure(image=imgtk)
	l1.image=imgtk
if len(sys.argv)==2:
	img = cv2.imread(sys.argv[1])
else:
	img=cv2.imread(easygui.fileopenbox())
height,width=img.shape[:2]
print height,width
ratio=float(700)/height
img=cv2.resize(img,(int(ratio*width),int(ratio*height)))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Rearrang the color channel
b,g,r = cv2.split(hsv)
img = cv2.merge((r,g,b))
	
	
tk=Tk()

page1 = Frame(tk,bg="blue",width=1200,height=100)
lr = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lg = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lb = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lr.set(40)
lg.set(0)
lb.set(0)
lr.pack(side=LEFT,expand=1,fill=BOTH)
lg.pack(side=LEFT,expand=1,fill=BOTH)
lb.pack(side=LEFT,expand=1,fill=BOTH)


page2 = Frame(tk,bg="blue",width=1200,height=100)
hr = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hg = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hb = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hr.set(255)
hg.set(40)
hb.set(255)
hr.pack(side=LEFT,expand=1,fill=BOTH)
hg.pack(side=LEFT,expand=1,fill=BOTH)
hb.pack(side=LEFT,expand=1,fill=BOTH)

page3 = Frame(tk,bg="blue",width=1200,height=700)
im = PIL.Image.fromarray(img)
imgtk = PIL.ImageTk.PhotoImage(image=im) 
# Put it in the display window
l1=Label(page3, image=imgtk)
l1.pack()


page1.pack(expand=1,fill=BOTH)
page2.pack(expand=1,fill=BOTH)
page3.pack(side = "bottom", fill = "both", expand = "yes")
tk.mainloop()
print lower,upper
cv2.imwrite("testing.jpg",cv2.inRange(img,lower,upper))
