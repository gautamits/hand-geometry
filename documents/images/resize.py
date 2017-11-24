import cv2
import sys
image=sys.argv[1]
directory="/".join(image.split("/")[::-1][1:][::-1])
path=image.split("/")[::-1][0]
width=int(sys.argv[2])
extension=path.split(".")[::-1][0]
print extension
name="".join(path.split(".")[::-1][1:][::-1])
print name

print "converting",image," to",width
i=cv2.imread(image)
image_height=i.shape[0]
image_width=i.shape[1]
image_height=int(image_height*(width/float(image_width)))
i=cv2.resize(i,(width,image_height))
print "saving to ",directory+"/"+name+"_modified."+extension
cv2.imwrite(directory+"/"+name+"."+extension,i)
