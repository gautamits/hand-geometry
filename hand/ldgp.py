import cv2
import numpy as np


def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))                                #this function returns euclidean distance between two one dimensional arrays	
	
								    #this function returns histogram of image,
def hist(a):
	hist, bin_edges = np.histogram(a, bins = range(64))
	return hist
								    #this function returns ldgp of an image
def calcgrad(i):
	height,width=i.shape
								    #zero padding
	first=np.pad(i,((0,0),(1,0)),'constant')
	second=np.pad(i,((0,1),(1,0)),'constant')
	third=np.pad(i,((0,1),(0,0)),'constant')
	fourth=np.pad(i,((0,1),(0,1)),'constant')
	first=first[:,0:width]
	second=second[1:height+1,0:width]
	third=third[1:height+1,:]
	fourth=fourth[1:height+1,1:width+1]
	first=i-first                                               #gradient at 0 degree
	second=i-second                                             #gradient at 45 degree
	third=i-third                                               #gradient at 90 degree
	fourth=i-fourth                                             # gradient at 135 degree
	combo1=32*np.array( first >= second, dtype=int)             #binary arrays being converted to decimal
	combo2=16*np.array( first >= third, dtype=int)
	combo3=8*np.array( first >= fourth, dtype=int)
	combo4=4*np.array( second >= third, dtype=int)
	combo5=2*np.array( second >= fourth, dtype=int)
	combo6=np.array( third >= fourth, dtype=int)
	ldgp=combo1+combo2+combo3+combo4+combo5+combo6
	ldgp=np.array(ldgp,dtype='uint8')
	return ldgp                                                 #final ldgp returned



