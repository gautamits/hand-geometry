from Tkinter import *
import cv2
import Image, ImageTk
import numpy as np
from ldgp import calcgrad

def print_value(val):
	print val
	lower=np.array([lr.get(),lg.get(),lb.get()],dtype="uint8")
	upper=np.array([hr.get(),hg.get(),hb.get()],dtype="uint8")
	print lower,upper
	_,img=cam.read()
	mask = cv2.inRange(img,lower,upper)
	#grad=calcgrad(mask)
	#grad=grad*4
	im = Image.fromarray(mask)
	imgtk = ImageTk.PhotoImage(image=im)
	l1.configure(image=imgtk)
	l1.image=imgtk

cam = cv2.VideoCapture(0)
	
	
tk=Tk()

page1 = Frame(tk,bg="blue",width=1200,height=100)
lr = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lg = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lb = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
lr.pack(side=LEFT,expand=1,fill=BOTH)
lg.pack(side=LEFT,expand=1,fill=BOTH)
lb.pack(side=LEFT,expand=1,fill=BOTH)


page2 = Frame(tk,bg="blue",width=1200,height=100)
hr = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hg = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hb = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
hr.pack(side=LEFT,expand=1,fill=BOTH)
hg.pack(side=LEFT,expand=1,fill=BOTH)
hb.pack(side=LEFT,expand=1,fill=BOTH)

page3 = Frame(tk,bg="blue",width=1200,height=700)
_,img=cam.read(0)
height,width=img.shape[:2]
print height,width
ratio=float(700)/height
img=cv2.resize(img,(int(ratio*width),int(ratio*height)))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Rearrang the color channel
b,g,r = cv2.split(hsv)
img = cv2.merge((r,g,b))
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)
l1=Label(page3, image=imgtk)
l1.pack()




page1.pack(expand=1,fill=BOTH)
page2.pack(expand=1,fill=BOTH)
page3.pack(side = "bottom", fill = "both", expand = "yes")


	
print_value(0)
tk.mainloop()
