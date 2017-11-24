import cv2
import numpy as np
cam=cv2.VideoCapture(0)
try:
	while True:
		ret,img=cam.read()
		imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
		height,width,channel=img.shape
		#print width,height,channel
		image=np.zeros((height*2,width*2,channel),np.uint8)
		image[:height,:width]=img
		image[:height,width:width*2]=imgYCC
		cv2.imshow("image",image)
		#cv2.imshow("cam",imgYCC)

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
except KeyboardInterrupt:
	cam.release()
	cv2.destroyAllWindows()
