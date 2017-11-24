import Tkinter as tk
from threading import Thread,Event
from multiprocessing import Array
from ctypes import c_int32

class CaptureController(tk.Frame):
    NSLIDERS = 6
    def __init__(self,parent):
        tk.Frame.__init__(self)
        self.parent = parent

        # create a synchronised array that other threads will read from
        self.ar = Array(c_int32,self.NSLIDERS)

        # create NSLIDERS Scale widgets
        self.sliders = []
        for ii in range(self.NSLIDERS):
            # through the command parameter we ensure that the widget updates the sync'd array
            s = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL,
                         command=lambda pos,ii=ii:self.update_slider(ii,pos))
            s.pack()
            self.sliders.append(s)

        # Define a quit button and quit event to help gracefully shut down threads 
        tk.Button(self,text="Quit",command=self.quit).pack()
        self._quit = Event()
        self.capture_thread = None

    # This function is called when each Scale widget is moved
    def update_slider(self,idx,pos):
        self.ar[idx] = c_int32(int(pos))

    # This function launches a thread to do video capture
    def start_capture(self):
        self._quit.clear()
        # Create and launch a thread that will run the video_capture function 
        self.capture_thread = Thread(target=video_capture, args=(self.ar,self._quit))
        self.capture_thread.daemon = True
        self.capture_thread.start()

    def quit(self):
        self._quit.set()
        try:
            self.capture_thread.join()
        except TypeError:
            pass
        self.parent.destroy()

# This function simply loops over and over, printing the contents of the array to screen
def video_capture(ar,quit):

    # This while loop would be replaced by the while loop in your original code
    while not quit.is_set():
        print ar[:]
        # the slider values are all readily available through the indexes of ar
        # i.e. w1 = ar[0]
        # w2 = ar[1]
        # etc. 


if __name__ == "__main__":
    root = tk.Tk()
    selectors = CaptureController(root)
    selectors.pack()
    selectors.start_capture()
    root.mainloop()
