import cv2
import numpy as np
from Tkinter import *

master = Tk()
w1 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w1.pack()
w2 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w2.pack()
w3 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w3.pack()
w4 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w4.pack()
w5 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w5.pack()
w6 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w6.pack()

lr = w1.get()
lg = w2.get()
lb = w3.get()
ur = w4.get()
ug = w5.get()
ub = w6.get()

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([lr,lg,lb])
    upper_blue = np.array([ur,ug,ub])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
window.mainLoop()
