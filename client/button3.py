import Tkinter
import cv2
import numpy as np
import Tkinter as tk
import Image, ImageTk
from error_remover import *
import time

class Values(Tkinter.Tk):
    """docstring for Values"""
    def __init__(self, parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        self.var = Tkinter.StringVar()
        self.string=""
        self.var.set(self.string)
        self.result=""

        self.pinFrame = Tkinter.Frame(self,bg="blue",width=1200,height=100)

        self.l = Tkinter.Label(self.pinFrame, textvariable = self.var)
        #l = Label(pinFrame)
        self.l.pack(expand=1,fill=Tkinter.BOTH)
        self.pinFrame.pack(expand=1,fill=Tkinter.BOTH)
        self.buttonFrame=Tkinter.Frame(self,bg="blue",width=1200,height=100)
        Tkinter.Grid.rowconfigure(self.buttonFrame, 0, weight=1)
        Tkinter.Grid.columnconfigure(self.buttonFrame, 0, weight=1)
        Tkinter.Grid.columnconfigure(self.buttonFrame, 1, weight=1)
        Tkinter.Grid.columnconfigure(self.buttonFrame, 2, weight=1)
        Tkinter.Grid.rowconfigure(self.buttonFrame, 1, weight=1)
        Tkinter.Grid.rowconfigure(self.buttonFrame, 2, weight=1)
        Tkinter.Grid.rowconfigure(self.buttonFrame, 3, weight=1)
        self.b1 = Tkinter.Button(self.buttonFrame, text="1", command = lambda: self.callback("1"))
        self.b2 = Tkinter.Button(self.buttonFrame, text="2", command = lambda: self.callback("2"))
        self.b3 = Tkinter.Button(self.buttonFrame, text="3", command = lambda:self.callback("3"))
        self.b4 = Tkinter.Button(self.buttonFrame, text="4", command = lambda: self.callback("4"))
        self.b5 = Tkinter.Button(self.buttonFrame, text="5", command = lambda: self.callback("5"))
        self.b6 = Tkinter.Button(self.buttonFrame, text="6", command = lambda: self.callback("6"))
        self.b7 = Tkinter.Button(self.buttonFrame, text="7", command = lambda: self.callback("7"))
        self.b8 = Tkinter.Button(self.buttonFrame, text="8", command = lambda: self.callback("8"))
        self.b9 = Tkinter.Button(self.buttonFrame, text="9",command = lambda: self.callback("9"))
        self.b0 = Tkinter.Button(self.buttonFrame, text="0",command = lambda: self.callback("0"))
        self.bstar = Tkinter.Button(self.buttonFrame, text="*", command = lambda: self.callback("*"))
        self.bsharp = Tkinter.Button(self.buttonFrame, text="#", command = lambda: self.callback("#"))
        self.b7.grid(row=0,column=0,sticky="nsew")
        self.b8.grid(row=0,column=1,sticky="nsew")
        self.b9.grid(row=0,column=2,sticky="nsew")
        self.b4.grid(row=1,column=0,sticky="nsew")
        self.b5.grid(row=1,column=1,sticky="nsew")
        self.b6.grid(row=1,column=2,sticky="nsew")
        self.b1.grid(row=2,column=0,sticky="nsew")
        self.b2.grid(row=2,column=1,sticky="nsew")
        self.b3.grid(row=2,column=2,sticky="nsew")
        self.b0.grid(row=3,column=0,sticky="nsew")
        self.bstar.grid(row=3,column=1,sticky="nsew")
        self.bsharp.grid(row=3,column=2,sticky="nsew")

        self.buttonFrame.pack(expand=1,fill=Tkinter.BOTH)

        self.decisionFrame=Tkinter.Frame(self,bg="blue",width=1200,height=100)
        self.ok = Tkinter.Button(self.decisionFrame, text="OK", command=self.okay)
        self.ok.pack()
        self.cancel=Tkinter.Button(self.decisionFrame,text="cancel",command=self.deny)
        self.cancel.pack()
        self.cleaner=Tkinter.Button(self.decisionFrame,text="clear",command=self.clear)
        self.cleaner.pack()
        self.decisionFrame.pack()

        """def submit(self):
        self.val1=self.Val1Txt.get()
        if self.val1=="":
            Win2=Tkinter.Tk()
            Win2.withdraw()

        self.val2=self.Val2Txt.get()
        if self.val2=="":
            Win2=Tkinter.Tk()
            Win2.withdraw()
        """


    def okay(self):
        print "okay"
        self.result=self.string
        self.quit()
    def deny(self):
        print "deny"
        self.result=None
        self.quit()
    def clear(self):
        self.string=""
        self.var.set(self.string)
    def callback(self,a):
        self.string=self.string+a
        self.var.set(self.string)
        print "callback",a

class snap(Tkinter.Tk):
    """docstring for Values"""
    def __init__(self, parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def show_frame(self):
        _, self.frame = self.cap.read()
        self.result=self.frame
        self.frame = cv2.flip(self.frame, 1)
        self.cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(self.cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)
    def initialize(self):
        self.result=None
        self.cap=cv2.VideoCapture(0)
        self.window = Tkinter.Tk()  #Makes main window
        self.window.wm_title("Digital Microscope")
        self.window.config(background="#FFFFFF")

        #Graphics window
        self.imageFrame = Tkinter.Frame(self.window, width=600, height=500)
        self.imageFrame.grid(row=0, column=0, padx=10, pady=2)

        #Capture video frames
        self.lmain = Tkinter.Label(self.imageFrame)
        self.lmain.grid(row=0, column=0)
        #Slider window (slider controls stage position)
        self.sliderFrame = Tkinter.Frame(self.window, width=600, height=100)
        self.sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


        self.show_frame()  #Display 2
        self.window.mainloop()  #Starts GUI




def accept(distances):
    print "accepted"
    send(distances)
def deny():
    print "denied"
    exit(1)
def send(distances):
    print distances

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    l1.imgtk = imgtk
    l1.configure(image=imgtk)
    l1.after(10, show_frame)

#cv2.imwrite("testing.jpg",cv2.inRange(i




app = Values(None)
app.title('Values')
app.mainloop() #this will run until it closes
app.quit()
#Print the stuff you want.
pin=app.result
print pin
if pin==None:
    exit(0)
cap=cv2.VideoCapture(0)
counter=0
#time.sleep(5)

#output,distances,tips,valleys=midfinger(frame)

root=tk.Tk()
page1 = tk.Frame(root,bg="blue",width=1200,height=100)
ok = tk.Button(page1,text="ok",command = lambda: accept(distances))
cancel = tk.Button(page1,command=deny,text="cancel")
ok.pack(side=tk.LEFT,expand=1,fill=tk.BOTH)
cancel.pack(side=tk.RIGHT,expand=1,fill=tk.BOTH)
page3 = tk.Frame(root,bg="blue",width=1200,height=700)
l1=tk.Label(page3)
l1.pack()
page1.pack(expand=1,fill=tk.BOTH)
page3.pack(side = "bottom", fill = "both", expand = "yes")
show_frame()
root.mainloop()

