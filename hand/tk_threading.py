import multiprocessing
import Tkinter as tk
import cv2

e = multiprocessing.Event()
p = None

# -------begin capturing and saving video
def startrecording(e):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc,  20.0, (640,480))

    while(cap.isOpened()):
        if e.is_set():
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            e.clear()
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
        else:
            break

def start_recording_proc():
    global p
    p = multiprocessing.Process(target=startrecording, args=(e,))
    p.start()

# -------end video capture and stop tk
def stoprecording():
    e.set()
    p.join()

    root.quit()
    root.destroy()

if __name__ == "__main__":
    # -------configure window
    root = tk.Tk()
    root.geometry("%dx%d+0+0" % (100, 100))
    startbutton=tk.Button(root,width=10,height=1,text='START',command=start_recording_proc)
    stopbutton=tk.Button(root,width=10,height=1,text='STOP', command=stoprecording)
    startbutton.pack()
    stopbutton.pack()

    # -------begin
    root.mainloop()
