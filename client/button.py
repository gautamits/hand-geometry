
import Tkinter as tk
import Image, ImageTk

def callback(a):
    global string
    string=string+a
    var.set(string)
    print "callback",a
def okay():
    print "okay"
    global string
    return string
def deny():
    print "deny"
    return None
def clear():
    global string
    string=""
    var.set(string)
string=""

def get_pin():
    root=tk.Tk()
    var = tk.StringVar()
    var.set(string)

    pinFrame = tk.Frame(root,bg="blue",width=1200,height=100)

    l = tk.Label(pinFrame, textvariable = var)
    #l = Label(pinFrame)
    l.pack(expand=1,fill=tk.BOTH)
    pinFrame.pack(expand=1,fill=tk.BOTH)
    buttonFrame=tk.Frame(root,bg="blue",width=1200,height=100)
    tk.Grid.rowconfigure(buttonFrame, 0, weight=1)
    tk.Grid.columnconfigure(buttonFrame, 0, weight=1)
    tk.Grid.columnconfigure(buttonFrame, 1, weight=1)
    tk.Grid.columnconfigure(buttonFrame, 2, weight=1)
    tk.Grid.rowconfigure(buttonFrame, 1, weight=1)
    tk.Grid.rowconfigure(buttonFrame, 2, weight=1)
    tk.Grid.rowconfigure(buttonFrame, 3, weight=1)
    b1 = tk.Button(buttonFrame, text="1", command = lambda: callback("1"))
    b2 = tk.Button(buttonFrame, text="2", command = lambda: callback("2"))
    b3 = tk.Button(buttonFrame, text="3", command = lambda:callback("3"))
    b4 = tk.Button(buttonFrame, text="4", command = lambda: callback("4"))
    b5 = tk.Button(buttonFrame, text="5", command = lambda: callback("5"))
    b6 = tk.Button(buttonFrame, text="6", command = lambda: callback("6"))
    b7 = tk.Button(buttonFrame, text="7", command = lambda: callback("7"))
    b8 = tk.Button(buttonFrame, text="8", command = lambda: callback("8"))
    b9 = tk.Button(buttonFrame, text="9",command = lambda: callback("9"))
    b0 = tk.Button(buttonFrame, text="0",command = lambda: callback("0"))
    bstar = tk.Button(buttonFrame, text="*", command = lambda: callback("*"))
    bsharp = tk.Button(buttonFrame, text="#", command = lambda: callback("#"))
    b7.grid(row=0,column=0,sticky="nsew")
    b8.grid(row=0,column=1,sticky="nsew")
    b9.grid(row=0,column=2,sticky="nsew")
    b4.grid(row=1,column=0,sticky="nsew")
    b5.grid(row=1,column=1,sticky="nsew")
    b6.grid(row=1,column=2,sticky="nsew")
    b1.grid(row=2,column=0,sticky="nsew")
    b2.grid(row=2,column=1,sticky="nsew")
    b3.grid(row=2,column=2,sticky="nsew")
    b0.grid(row=3,column=0,sticky="nsew")
    bstar.grid(row=3,column=1,sticky="nsew")
    bsharp.grid(row=3,column=2,sticky="nsew")

    buttonFrame.pack(expand=1,fill=tk.BOTH)

    decisionFrame=tk.Frame(root,bg="blue",width=1200,height=100)
    ok = tk.Button(decisionFrame, text="OK", command=okay)
    ok.pack()
    cancel=tk.Button(decisionFrame,text="cancel",command=deny)
    cancel.pack()
    cleaner=tk.Button(decisionFrame,text="clear",command=clear)
    cleaner.pack()
    decisionFrame.pack()
    root.mainloop()
print get_pin()
