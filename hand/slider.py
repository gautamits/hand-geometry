import Tkinter
import numpy as np
import cv2
import matplotlib.pyplot as plt
def echo():
	#print lr.get(),lg.get(),lb.get(),hr.get(),hg.get(),hb.get()
	lower=np.array([lr.get(),lg.get(),lb.get()],dtype="uint8")
	upper=np.array([hr.get(),hg.get(),hb.get()],dtype="uint8")
	print lower,upper
	mask = cv2.inRange(hsv,lower,upper)
	#cv2.imshow("masked",mask)
def print_value(val):
    echo()
lower = np.array([0,48,80],dtype="uint8")
upper = np.array([20,255,255],dtype="uint8")
i=cv2.imread("hand.JPG")
hsv=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
root = Tkinter.Tk()

lr = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)
lg = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)
lb = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)

lr.pack()
lg.pack()
lb.pack()
hr = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)
hg = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)
hb = Tkinter.Scale(orient='horizontal', from_=0, to=255, command=print_value)

hr.pack()
hg.pack()
hb.pack()






root.mainloop()
cv2.waitKey(0)



